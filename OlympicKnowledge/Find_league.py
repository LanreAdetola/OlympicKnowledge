import requests
from pdf_generator import CustomPDF, generate_pdf_F

def handball_leagues():
    country = input("Enter the country: ").lower()
    url = "https://api-handball.p.rapidapi.com/leagues"
    querystring = {"country": country}
    headers = {
        "X-RapidAPI-Key": "493f8bc412msh5bcab0fed124539p1c6a96jsn11bf6b4dcd51",
        "X-RapidAPI-Host": "api-handball.p.rapidapi.com"
    }

    try:
        response = requests.get(url, headers=headers, params=querystring)
        response.raise_for_status()  
        leagues = response.json().get('response', [])
        
        if leagues:
            league_names = [league['name'] for league in leagues]
            generate_pdf_F(country, league_names)
        else:
            print(f"No leagues found for country: {country}")

    except requests.exceptions.HTTPError as http_err:
        print(f"HTTP error occurred: {http_err}")
    except requests.exceptions.ConnectionError as conn_err:
        print(f"Connection error occurred: {conn_err}")
    except requests.exceptions.Timeout as timeout_err:
        print(f"Timeout error occurred: {timeout_err}")
    except requests.exceptions.RequestException as req_err:
        print(f"An error occurred: {req_err}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

if __name__ == "__main__":
    handball_leagues()
