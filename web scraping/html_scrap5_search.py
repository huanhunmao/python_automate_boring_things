# Opens several search results.

import requests, sys, webbrowser, bs4
print('Searching...')
res = requests.get('https://google.com/search?q=' 'https://pypi.org/search/?q='
+ ' '.join(sys.argv[1:]))
res.raise_for_status()

# TODO: Retrieve top search result links.

# TODO: Open a browser tab for each result.