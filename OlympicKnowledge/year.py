import requests
from bs4 import BeautifulSoup
import re
import pandas as pd
from pdf_generator import CustomPDF, generate_pdf_Y

def get_handball_medalists(url):
    response = requests.get(url)
    response.raise_for_status()

    soup = BeautifulSoup(response.content, 'html.parser')
    table = soup.find('table', {'class': 'wikitable plainrowheaders'})

    headers = [th.text.strip() for th in table.find_all('th')]

    medalists_by_year = {}

    for tr in table.find_all('tr')[1:]:
        cells = tr.find_all(['th', 'td'])
        year = None
        medalists = {'Gold': [], 'Silver': [], 'Bronze': []}
        for i, cell in enumerate(cells):
            text = cell.text.strip()
            if i == 0:  
                year = re.search(r'\d{4}', text).group() if re.search(r'\d{4}', text) else text
            elif i in [1, 2, 3]:  
                names = []
                for name_tag in cell.find_all('a'):
                    name = name_tag.text.strip()
                    names.append(name)
                medalists[headers[i]] = names
        if year:
            medalists_by_year[year] = medalists

    return medalists_by_year

def Year():
    men_url = 'https://en.wikipedia.org/wiki/List_of_Olympic_medalists_in_handball_(men)'
    men_medalists = get_handball_medalists(men_url)

    women_url = 'https://en.wikipedia.org/wiki/List_of_Olympic_medalists_in_handball_(women)'
    women_medalists = get_handball_medalists(women_url)

    year_input = input("Enter the year you want to search for: ")
    men_year_medalists = men_medalists.get(year_input, {})
    women_year_medalists = women_medalists.get(year_input, {})

    content = {
        "Men's Handball": men_year_medalists,
        "Women's Handball": women_year_medalists
    }

    generate_pdf_Y(content, filename=f"{year_input}_medalists.pdf")

if __name__ == "__main__":
    Year()
