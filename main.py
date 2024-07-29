from bs4 import BeautifulSoup
import requests
import os

def compare_contents(file1, file2, url):                            #function compares file contents to notify changes                           
    with open(file1, 'r') as file1, open(file2, 'r') as file2:
        file1_content = file1.read()
        file2_content = file2.read()

        if file1_content != file2_content:
            return print("New event has been added. \n" + url)
        else:
            return print("No new changes.")

url = "https://en.onepiece-cardgame.com/events/2024/championship/offline_regional_wave3.php"

result = requests.get(url)
doc = BeautifulSoup(result.text, "html.parser")

if os.path.exists('yesterday.txt'):                         #parses html into text files & compares

    with open('today.txt', 'w') as file:
        file.write(doc.prettify())

    compare_contents('today.txt', 'yesterday.txt', url)


    with open('yesterday.txt', 'w') as file:
        file.write(doc.prettify())
    
else:
    print('Creating new file...')
    with open('yesterday.txt', 'w') as file:
        file.write(doc.prettify())

#add cron functionality
#currently only checks for offline regionals, add trasure cup and other pages



