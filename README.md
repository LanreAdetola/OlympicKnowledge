
# OlympicKnowledge

OlympicKnowledge is a Python package for exploring the history and statistics of Olympic handball. It provides tools to fetch general information, analyze medalists by country, year, and athlete, and generate PDF reports.

## Features

- **General Information**: Fetches a description and image of handball from Wikipedia.
- **Medalists by Country**: Lists all Olympic handball medalists from a specified country, sorted by year and medal type.
- **Medalists by Year**: Displays all medalists (athletes and their countries) for a given year, categorized by medal.
- **Athlete Search**: Shows detailed information and Wikipedia links for a given athlete, including medals won.
- **Handball Leagues**: Retrieves handball league information for a specified country using a public API.
- **PDF Reports**: Generates PDF summaries for all queries using customizable templates.

## Installation

Install dependencies with:

```bash
pip install requests beautifulsoup4 fpdf schedule pillow pandas
```

## Usage

Each module can be run as a script or imported:

- `general.py`: Fetch general info about handball.
- `country.py`: List medalists by country.
- `year.py`: List medalists by year.
- `athlete.py`: Search for athlete details.
- `Find_league.py`: Find handball leagues by country.

Example:

```bash
python OlympicKnowledge/general.py
python OlympicKnowledge/country.py
```

## Data Sources

- Wikipedia (Handball, Olympic medalists)
- RapidAPI (Handball leagues)

## Output

- CSV files for medalist data
- PDF reports for all queries

## License

MIT