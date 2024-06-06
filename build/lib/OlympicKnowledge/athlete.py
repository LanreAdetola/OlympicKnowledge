import requests
from bs4 import BeautifulSoup
import pandas as pd
from pdf_generator import CustomPDF, generate_pdf_A
import re

def fetch_medalists(url):
    response = requests.get(url)
    response.raise_for_status()
    return BeautifulSoup(response.content, 'html.parser')

def parse_medalists(soup):
    table = soup.find('table', {'class': 'wikitable plainrowheaders'})
    medalists_by_year = {}
    for tr in table.find_all('tr')[1:]:
        cells = tr.find_all(['th', 'td'])
        if len(cells) >= 4:
            year_match = re.search(r'\d{4}', cells[0].text.strip())
            if year_match:
                year = year_match.group()
                medalists = {
                    'Gold': [re.sub(r'\(.*?\)', '', name.strip()) for name in re.split(r',|;', cells[1].text.strip())],
                    'Silver': [re.sub(r'\(.*?\)', '', name.strip()) for name in re.split(r',|;', cells[2].text.strip())],
                    'Bronze': [re.sub(r'\(.*?\)', '', name.strip()) for name in re.split(r',|;', cells[3].text.strip())]
                }
                medalists_by_year[year] = medalists
    return medalists_by_year

def search_player(medalists, player_name):
    player_medals = []
    for year, medalists in medalists.items():
        for medal_type, names in medalists.items():
            if any(player_name.lower() in name.lower() for name in names):
                player_medals.append((year, medal_type))
    return player_medals

def extract_player_link(player_name):
    url = f"https://en.wikipedia.org/wiki/{player_name.replace(' ', '_')}"
    return url


def append_player_links(content):
    for category, df in content.items():
        links = []
        for player_name in df['Medal Type']:  
            link = extract_player_link(player_name)
            links.append(link)
        df['Wikipedia Page'] = links
    return content


def Athlete():
    men_url = 'https://en.wikipedia.org/wiki/List_of_Olympic_medalists_in_handball_(men)'
    women_url = 'https://en.wikipedia.org/wiki/List_of_Olympic_medalists_in_handball_(women)'
    
    men_soup = fetch_medalists(men_url)
    women_soup = fetch_medalists(women_url)
    
    men_medalists = parse_medalists(men_soup)
    women_medalists = parse_medalists(women_soup)
    
    player_name = input("Enter the name of the player you want to search for: ")
    men_player_medals = search_player(men_medalists, player_name)
    women_player_medals = search_player(women_medalists, player_name)

    results = {
        "Men's Handball": men_player_medals,
        "Women's Handball": women_player_medals
    }

    if not men_player_medals and not women_player_medals:
        print(f"No Olympic medals found for {player_name}.")
    else:
        content = {}
        for category, medals in results.items():
            if medals:
                data = {
                    "Year": [medal[0] for medal in medals],
                    "Medal Type": [medal[1] for medal in medals]
                }
                content[category] = pd.DataFrame(data)
        
        content_with_links = append_player_links(content)
        generate_pdf_A(content_with_links, filename=f"{player_name}_handball_medals.pdf")

if __name__ == "__main__":
    Athlete()
