/*
*	Author: Jack Strickland
*	
*	Description: A BASH-style shell that uses 3 built in functions (cd,pwd,exit),
*				and farms the rest of the commands to the system using exec calls. 
*				Supports I/O redirection, BUT ONLY ONE AT A TIME. 
*
*/


#include <unistd.h>
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <errno.h>

void prompt();
char* parse();
char** tokenize(char* commands);
int execute(char** args, int in, int out);


int shell_exit();
int shell_cd(char* dir);
int shell_pwd();

int main(int argc, char **argv)
{	
	char *cmd;
	char **args;	
	int shell_status=1, in=0, out=0;

	// start shell instance from $HOME
	chdir(getenv("HOME"));	

	// the loop that runs everything, depends on return of execute()
	do {	
		prompt();
		cmd = parse();
	
		if (strpbrk (cmd, ">"))			// when the command input redirects stdout
			out = 1;
		else if (strpbrk (cmd, "<"))	// when the command input redirects stdin
			in = 1;
		
		args = tokenize(cmd);			
		shell_status = execute(args,in,out);


		// free the malloc memory, and reset the redirection statuses
		free(cmd);
		free(args);
		in=out=0;

	} while (shell_status);
	return 0;
}

// called every iteration of loop, updates cwd$
void prompt()
{
	char cwd[128];

	getcwd(cwd, sizeof(cwd));
	printf("%s$ ", cwd);	
	fflush(stdout);	
}

// takes user input and returns it as a char* ending in \n\0
char* parse()
{	
	// where we are going to store the commands, buffer is 1024 to be safe
	int bufferSize = 1024;
	char *line = malloc (sizeof(char) * bufferSize);
	fgets(line, bufferSize, stdin);
	return line;
}

// takes char* returned by parse(), to tokenize based on redirection or not
char** tokenize(char* commands)
{
	int bufferSize = 128, token_count = 0;
	char **tokens = malloc (sizeof(char*) * bufferSize);
	char *token, *delim;

	// if the commands contain a redirection symbol
		// splits into arg[0] <||> arg[1]
		// note: arg[1] will contain leading whitespace
	if (strpbrk (commands,"<>"))
		delim = "<>\n";
	else
		delim = " \n";

	// start splitting, end with NULL
	token = strtok(commands, delim);
	while (token!=NULL) {
		tokens[token_count] = token;
		token_count +=1;
		token = strtok(NULL, delim);
	}

	tokens[token_count] = NULL;
	return tokens;
}

int execute(char** args, int in, int out)
{
	// check for built-in functions: exit, cd, pwd
	if (strcmp(args[0], "exit") == 0) {
		return shell_exit();

	} else if (strcmp(args[0], "cd") == 0) {
		return shell_cd(args[1]);

	} else if (strcmp(args[0], "pwd") == 0) {
		return shell_pwd();

	} else {
		
		// If not a built in function
		pid_t parent, child;
		int child_status;

		child = fork();
		if (child < 0){
			printf("Fork Failed\n");
			exit(-1);
		}
		else if (child == 0){
			//CHILD PROCESS
			// if redirection is happening, open correct stream
			if (in + out){
				char **cmd_t = tokenize(args[0]);
				if (in) {		
					FILE* infile = fopen(args[1]+1, "r");
		          	dup2(fileno(infile), 0);
		          	fclose(infile);
				} else if (out) {
					FILE* outfile = fopen(args[1]+1, "w"); 
					dup2(fileno(outfile), 1);
					fclose(outfile);
				}
				// will exectute only if in || out == 1
				execvp(cmd_t[0], cmd_t);
			} else { 
				// normal execution of a command with arguments (NO REDIRECTION)
				execvp(args[0],args);
			}
			// if unsuccessful execution, print error
			printf("Error %d (%s)\n", errno, strerror(errno));
			exit(1);
		} else {
			// this is parent process
			parent = wait(&child_status);
			fflush(stdout);
			return 1;
		}
	}
}


// BUILT-IN SHELL FUNCTIONS

int shell_exit()
{
	printf("EXITING SHELL\n");
	//printf("Script done, file is typescript\n");
	return 0;
}

int shell_cd(char* dir)
{
	int cd_status;
	cd_status = chdir(dir);

	if (cd_status == -1){	
		// when the directory cannot be changed to
		printf("Error %d (%s)\n", errno, strerror(errno));
	}
	return 1;
}

int shell_pwd()
{
	char cwd[128];	
	getcwd(cwd, sizeof(cwd));
	printf("%s\n", cwd);
	fflush(stdout);

	return 1;
}

