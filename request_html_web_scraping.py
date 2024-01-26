# the HTML import from requests_html will parse a html content.
# the HTMLSession import from requests_html will parse a HTML content from a website online. 
from requests_html import HTML, HTMLSession

# import csv to record it to the databse. 
import csv 

# instatiating HTMLSession to get the website link online
session = HTMLSession()

# actual getting process of the website online. 
source = session.get('https://www.one37pm.com/popular-culture/best-anime-fight-scenes')

# opening a file to write everything scraped in the top 28 fights in the website. 
file = open('csv_top28_fights.csv', 'w')

# making a csv_writer to write all the scraped data to the csv_file 
csv_writer = csv.writer(file)

# print the html link format of the website online.
# Important to note that this returns the parsed HTML content, not a URL
# print(source.html)

# main container 
main_container = source.html.find('div', first=True)

# header title 
header_title = main_container.find('h1.hed', first=True).text
print() # one line space.
print(header_title)
# write the header title to the database 
csv_writer.writerow([header_title])
print() # one line space.

# author name 
author_name = main_container.find('div.author', first=True).text 
print(author_name)
# write the author name of this all data in the database. 
csv_writer.writerow([author_name])
print() # one line space.

# body text
header_body = main_container.find('div.body-text', first=True)
header_body_content = header_body.find('p', first=True).text
print(header_body_content)
# write the author name of this all data in the database. 
csv_writer.writerow([header_body_content])
print() # one line space.

# locate the header text 
intro = main_container.find('div.large-image-container', first=True)
intro_text = intro.find('h2.sub-head', first=True).text
csv_writer.writerow([intro_text])

# list contents 
all_fightlist = main_container.find('div.module')

# header of the list.
csv_writer.writerow(['List', 'Anime', 'Brief Comment'])

for fightlist in all_fightlist:
    # make variable contain every list of fights, anime title, and brief comment. 
    per_list = None
    per_title = None
    per_comment = None

    contenders_list = fightlist.find('h2.sub-head')
    for contender in contenders_list: 
        contenders = contender.text
        print(contenders)
        print() # one line space
        per_list = contenders

    # Title of the anime fight 
    # making a loop for the anime title
    anime_title = fightlist.find('h3.sub-head')
    for titles in anime_title:
        title = titles.text
        print(title)
        print() # one line space.
        per_title = title
        
    # content of the fight 
    # making a loop for the fight contents
    fight_contents = fightlist.find('div.body-text.social-embed-body-text')
    for fight_content in fight_contents:
        # making a lopp for every content body 
        for content_body in fight_content.find('p'):
            content = content_body.text 
            print(content)
            print() # one line space.
            per_comment = content
        # making a loop for every commentors in the content body.

    # put all the list data in one row. 
    csv_writer.writerow([per_list, per_title, per_comment])
    
# finally, close the file writing. 
file.close()