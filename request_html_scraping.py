# the HTML import from requests_html will parse a html content.
# the HTMLSession import from requests_html will parse a HTML content from a website online. 
from requests_html import HTML, HTMLSession

# using context manager to open a html file in a local repo. 
with open('simple2.html') as html_file:
    # to grab the contents of the source html file, use the read method. 
    source = html_file.read() 
    # now passing the content of the html file to an instance of HTML. 
    html = HTML(html=source)

# accessing the html content in html format. 
print('HTML Format:')
print(html.html)
print() # one line spacing

# accessing the html content in text format. 
print('Text Format:')
print(html.text)
print() # one line spacing

# access the title tag inside the html. 
# it returns a list of all title tags inside the html file. 
title = html.find('title')
print('Title List Format:')
print(title)
print() # one line spacing
print('Title Text Format of first index:')
print(title[0].text)
print() # one line spacing

# another way of getting the very first occurence of the matching tag finding. 
# use the first argument. 
match = html.find('#footer', first=True)
print(match.text)
print() # one line spacing

# find the list of containers. 
# to locate a specific container, you can use the dot method after a tag. 
# for instance, div.[class_name]
container = html.find('div.article', first=True) 
print('Container Text Form:')
print(container.text)
print() # one line spacing

# to find a specific element inside a container, you can just 
# call find method again and find the specific elemement. 
headline = container.find('h2', first=True)
print('Headline in Container Text Form:')
print(headline.text)
print() # one line spacing
content = container.find('a', first=True)
print('Content in Container Text Form:')
print(content.text)
print() # one line spacing

# to print/get every container inside a html file, considering that they have the same class name
# we can loop this. 
print('Print all data in all containers:')
for article in html.find('div.article'): 
    headline = container.find('h2', first=True)
    print('Headline in Container Text Form:')
    print(headline.text)
    print() # one line spacing
    content = container.find('a', first=True)
    print('Content in Container Text Form:')
    print(content.text)
    print() # one line spacing




