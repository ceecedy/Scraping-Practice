from bs4 import BeautifulSoup 
import requests

# opening the html file with beautiful soup 
# we don't need to specify the path since the html file is within the same directory. 
with open('simple.html') as html_file:
    # officially passing the html file to the beautifulsoup. 
    # parser is needed for this to let the beautifulsoup how to scrape the content. 
    soup = BeautifulSoup(html_file, 'lxml')
    
# if we print this scraped html file using lxml parser, it will become string 
# so tags of the html are also included to the output.
# using prettify from bs4 will make the output of the scraped content in a html file 
#   in good format just like how it is formatted in its own html file. 
print(soup.prettify())

# to output specific tag, you can call its tag using the soup object that was instanstiated
#   from the beautifulsoup. 
specific = soup.p 
# the specific variable will hold the very first p tag. 
# now printing the first p tag. 
print(specific, '\n') 

# to get only the value you can extend the method from the tag using text method. 
specific = soup.p.text
# now printing the first p tag value. 
print(specific) 

# to find a specific element in two or more tags in an html file, 
#   you can use find method.
# the "class_" argmument is to specify the div you are looking for. 
# named "class_" to differentiate it to the class keyword in making class. 
div = soup.find('div', class_ = 'footer')
# now printing the div value that is from class footer.
print(div, '\n')

# to find a specific tag and print its value in a div, you can parse it continiously 
#   just like this 
specific_tag_div = div.p.text 
# now printing the specific value in one of the tags inside a div 
print(specific_tag_div, '\n')

# to find all specific tags, you can use find_all method. 
# this will find all div tags. 
all_div = soup.find_all('div')
# now printing all div tags 
print(all_div, '\n')

# get all tags within a specific container. 
# you can use for loop in order to obrain this 
for article in soup.find_all('div', class_ = 'article'):
    headline = article.h2.a.text
    print(headline)
    
    summary = article.p.text
    print(summary)
    
    print() # for extra space 



