# This opens all my most visited websites on my browser at once.



import webbrowser, sys


url_list = ['https://www.reddit.com',
			'https://webmail.latech.edu',
			'https://mail.google.com',
			'https://cas.latech.edu/',
			]

for url in url_list:
	webbrowser.open(url)

