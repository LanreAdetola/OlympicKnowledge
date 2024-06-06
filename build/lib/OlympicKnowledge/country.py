import requests
from bs4 import BeautifulSoup
import re
from pdf_generator import CustomPDF, generate_pdf_C
import pandas as pd

def scrape_handball_medalists(url):
    response = requests.get(url)
    response.raise_for_status()

    soup = BeautifulSoup(response.content, 'html.parser')
    table = soup.find('table', {'class': 'wikitable plainrowheaders'})

    headers = []
    for th in table.find_all('th'):
        headers.append(th.text.strip())

    rows = []
    for tr in table.find_all('tr')[1:]:
        cells = tr.find_all(['th', 'td'])
        row = []
        for cell in cells:
            words = cell.text.strip().split()
            trimmed_cell_text = words[:1] if len(words) >= 1 else words
            row.append(' '.join(trimmed_cell_text))
        rows.append(row)

    df = pd.DataFrame(rows, columns=headers)
    return df

def list_medals_by_country(df, country):
    gold_df = df[df['Gold'] == country][['Games', 'Gold']]
    silver_df = df[df['Silver'] == country][['Games', 'Silver']]
    bronze_df = df[df['Bronze'] == country][['Games', 'Bronze']]

    results = {
        "Gold": gold_df,
        "Silver": silver_df,
        "Bronze": bronze_df
    }

    return results

def Country():
    url_men = 'https://en.wikipedia.org/wiki/List_of_Olympic_medalists_in_handball_(men)'
    url_women = 'https://en.wikipedia.org/wiki/List_of_Olympic_medalists_in_handball_(women)'

    df_men = scrape_handball_medalists(url_men)
    df_women = scrape_handball_medalists(url_women)

    df_men.to_csv('handball_medalists_men.csv', index=False)
    df_women.to_csv('handball_medalists_women.csv', index=False)

    country_name = input("Name of Country: ").capitalize()
    
    results_men = list_medals_by_country(df_men, country_name)
    results_women = list_medals_by_country(df_women, country_name)
    
    if results_men["Gold"].empty and results_men["Silver"].empty and results_men["Bronze"].empty and \
       results_women["Gold"].empty and results_women["Silver"].empty and results_women["Bronze"].empty:
        print(f"No medal records found for {country_name}.")
    else:
        results = {
            "Men's Handball Medals": results_men,
            "Women's Handball Medals": results_women
        }

        content = {}
        for category, medals in results.items():
            content[category] = {}
            for medal_type, df in medals.items():
                content[category][medal_type] = df

        generate_pdf_C(content, filename=f"{country_name}_handball_medals.pdf")

if __name__ == "__main__":
    Country()