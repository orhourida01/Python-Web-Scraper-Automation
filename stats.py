import requests
from bs4 import BeautifulSoup
import pandas as pd

def collect_data():
    print("Bdayna l-ba7t 3la l-akhbar...") # 7yedna l-rocket
    url = "https://news.ycombinator.com/"
    
    try:
        # 1. Requête l l-site
        response = requests.get(url)
        soup = BeautifulSoup(response.text, 'html.parser')
        
        # 2. Extraction dyal s-miyat d l-ma9alat
        news_list = []
        articles = soup.find_all('span', class_='titleline')
        
        for article in articles[:20]: # Akher 20 ma9al
            title = article.text
            link = article.find('a')['href']
            news_list.append({"Titre": title, "Lien": link})
        
        # 3. Sauvegarde f Excel (CSV)
        df = pd.DataFrame(news_list)
        df.to_csv('top_news.csv', index=False, encoding='utf-8')
        
        print("Kolchi nadi! Ghadi tl9a fichier smitou 'top_news.csv' jdid.")
        
    except Exception as e:
        print(f"Kayn mouchkil: {e}")

if __name__ == "__main__":
    collect_data()