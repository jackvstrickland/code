# I made a script that automatically takes the address in a clipboard
# and opens a googlemap search of it. can use command line arg also

import webbrowser, sys, pyperclip

# print(sys.argv)

if len(sys.argv) > 1:

	# get address from command line if there are arguments passed

	# The address does not need spaces so those are removed and
	# the address becomes a single string. the [1:] removes the first 
	# command line arg which would be the name of the program.

	address = ' '.join(sys.argv[1:])

else:

	#get address from clipboard

	address = pyperclip.paste()


# now open the google maps page with address already provided

webbrowser.open('https://www.google.com/maps/place/' + address)


