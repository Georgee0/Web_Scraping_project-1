# Program to open several site result

import requests, sys, bs4, webbrowser

print('Searching................')      # displays text while downloading web page
res = requests.get('http://google.com/search?q=' 'http://pypi.org/search?q=' + ' '.join(sys.argv[1:]))
res.raise_for_status()

# Retrieve top search results
soup = bs4.BeautifulSoup(res.text, 'html.parser')

# Open tab for each new result
linkElems = soup.select('.package-snippet')
numOPen = min(5,len(linkElems))
for i in range (numOPen):
    urlToOPen = 'http://pypi.org' + linkElems[i].get('href')
    print('OPening...', urlToOPen)
    webbrowser.open(urlToOPen)