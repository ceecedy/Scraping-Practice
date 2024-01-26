from bs4 import BeautifulSoup
import requests
import csv

# all contents of this website will become string. 
src_code = requests.get('https://realpython.github.io/fake-jobs/').text

# passing now the source code html from web to beautifulsoup. 
# making the parser mode to be lxml to make it string. 
soup = BeautifulSoup(src_code, 'lxml')

# printing the source code with proper formatting using prettify from bs4.
# print(soup.prettify())

# making a csv_file to save all scraped data from the source code. 
csv_file = open('realpythonjobs_scraped.csv', 'w')

# making a csv_writer to write all the scraped data to the csv_file 
csv_writer = csv.writer(csv_file)

header_title = soup.find('div', class_ = "container mb-5").h1.text
header_content = soup.find('div', class_ = "container mb-5").p.text
print() # space from above.
print(header_title.strip())
print(header_content.strip())

# writing the headline title and content and jobs
csv_writer.writerow([header_title])
csv_writer.writerow([header_content])

for all_job_list in soup.find_all('div', class_ = 'card-content'):
    # title and company 
    for all_titles_company in all_job_list.find_all('div', class_ = 'media-content'):
        title = all_titles_company.h2.text
        company = all_titles_company.h3.text 

        # output 
        print() # spacing 
        print('Job:')
        print('    ', title)
        print('    ', company)
        
        # writing in the csv the scraped content per jobs. 
        csv_writer.writerow(['Job:', 'Company'])
        csv_writer.writerow([title, company])
    
    # content: location and date 
    for content in all_job_list.find_all('div', class_ = 'content'):
        location = content.find('p', class_ = 'location').text 
        date = content.time.text
        
        # output 
        print('    ', 'Location:', location, end='')
        print('  Date:', date)
        
        # writing in the csv the scraped content per jobs. 
        csv_writer.writerow([location + ' ' + date])  # Combine location and date in a single list
        csv_writer.writerow([]) # add one line space 

# closing the csv. 
csv_file.close()

    



