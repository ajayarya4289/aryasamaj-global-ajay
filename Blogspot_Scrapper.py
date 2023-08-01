import bs4
import requests
import re
import io
from fake_useragent import UserAgent
import datetime

# List of URLs to scrape
urls = ['','']

# Initializing the UserAgent object
user_agent = UserAgent()

# Starting the loop
for url in urls:
    # Sending an HTTP GET request to the URL with a random User-Agent
    page = requests.get(url, headers={"user-agent": user_agent.chrome})
    
    file_like_obj = io.StringIO(page.text)
    # Storing the content of the page in a variable
    html = file_like_obj.read()
    
    # Creating BeautifulSoup object
    soup = bs4.BeautifulSoup(html, "lxml")
    
    # Extracting specific data from the soup object (Example: extracting the title)
    findID = re.findall(r'post-body-(.*)\' itemprop', html)
    div = soup.find(id="post-body-" + findID[0]).prettify

    timestamp = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")
    # Generating the filename based on the URL and appending .html extension
    filename = f"file_{timestamp}.html"
    
    file_path = 'C:\\Users\\smitp\\Desktop\\Vivek_Arya_Blogs\\new'

    file_name = file_path+'\\'+filename
    # Opening the file in write mode and writing the extracted data to it
    with open(file_name, "w", encoding="utf-8") as file:
        file.write(str(div))

    print(f"Data extracted from '{url}' and saved to '{filename}'.")    