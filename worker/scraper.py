import requests
from bs4 import BeautifulSoup

def scrapeUrl(url):
    HEADERS = {
        'User-Agent':'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/44.0.2403.157 Safari/537.36',
        'Accept-Language': 'en-US, en;q=0.5'
    }
    
    # Making the HTTP Request
    webpage = requests.get(url, headers=HEADERS)

    # Creating the Soup Object containing all data
    soup = BeautifulSoup(webpage.content, "lxml")
    
    title = soup.find("a", "novel-title")
    content = soup.find_all("p")
    
    

print(scrapeUrl("https://novelbin.com/b/my-living-shadow-system-devours-to-make-me-stronger/chapter-1-the-academys-weakest"))