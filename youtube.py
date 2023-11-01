#! C:\Users\Julia\webcrawler\.venv\Scripts\python.exe
import requests
from bs4 import BeautifulSoup

url = "https://www.youtube.com/results?search_query=casino+trailer"

try:
    response = requests.get(url)
    response.raise_for_status()  # Check for HTTP request error

    if len(response.content) > 0:
        print("Response received!")
        
        # Save the response content to a file
        with open("response.html", "w", encoding="utf-8") as file:
            file.write(response.content.decode('utf-8'))

        # Continue with parsing and extraction
        soup = BeautifulSoup(response.content, 'html.parser')
        video_elements = soup.find_all('a', class_='yt-simple-endpoint', id='video-title')
        for video_element in video_elements:
            href_value = video_element.get('href')
            if href_value:
                print(href_value)

    else:
        print("Response is empty")

except requests.exceptions.RequestException as e:
    print("An error occurred:", e)
except Exception as e:
    print("An unexpected error occurred:", e)
