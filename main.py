#Import libraries
import bs4 as bs
import urllib.request
import csv
from time import gmtime, strftime

#Get the Github URL from user input
url = input('Github URL: ')

#Get current date and time
CurrentDateAndTime = strftime("%Y-%m-%d %H:%M:%S", gmtime())

#Get the source code of the website
source = urllib.request.urlopen(url).read()
soup = bs.BeautifulSoup(source, 'lxml')

#CSV File Config
csv_file = open("Github - Scrap.csv", 'w')
csv_writer = csv.writer(csv_file)
csv_writer.writerow(['Repo Title', 'Repo Description', 'Repo Code Language', 'Repo URL', 'Date'])

#Using a for loop to get all the li with the the specific class instead of one
for li in soup.find_all('li', class_='pinned-repo-item p-3 mb-3 border border-gray-dark rounded-1 public source'):
    #Using try so when a variable is empty i can change the variable to text where it says it's empty
    try:
        ReposTitle = li.find('span', class_='repo js-repo').text
        ReposDesc = li.find('p', class_='pinned-repo-desc text-gray text-small d-block mt-2 mb-3').text
        ReposCodeLanguage = li.find('p', class_='mb-0 f6 text-gray').text.strip()
        RepoUrl = str("{}/{}".format(url, ReposTitle))
    #When the variables in 'try' doesn't work
    except Exception as e:
        ReposTitle = 'Title Is Empty'
        ReposDesc = 'Description Is Empty'
        ReposCodeLanguage = 'Coding Language Is Empty'
        RepoUrl = 'Repo URL Is Empty'
    #Output the text

    #Puts the data from the variables into the columns
    csv_writer.writerow([ReposTitle, ReposDesc, ReposCodeLanguage, RepoUrl, CurrentDateAndTime])

#Closes the csv file
csv_file.close()
#End Message
print("Script Ended.")