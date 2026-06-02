# Mutual Fund Project

A comprehensive mutual fund analysis and management project that includes data ingestion, live NAV (Net Asset Value) fetching, data analysis, SQL database integration, and reporting capabilities.

## Project Structure

```
MutualFund_Project/
├── Dashboard/          # Dashboard and visualization files
├── Data/              # Data files and datasets
├── NoteBooks/         # Jupyter notebooks for analysis
├── reports/           # Generated reports
├── SQL/               # SQL scripts and database schemas
├── data_ingestion.py  # Script for data ingestion
├── live_nav_fetch.py  # Script to fetch live NAV data
└── requirements.txt   # Python dependencies
```

## Files Description

- **data_ingestion.py**: Handles the ingestion of mutual fund data from various sources
- **live_nav_fetch.py**: Fetches live NAV (Net Asset Value) data for mutual funds
- **requirements.txt**: Python package dependencies

## Getting Started

1. Clone this repository
2. Install dependencies: `pip install -r requirements.txt`
3. Run data ingestion: `python data_ingestion.py`
4. Fetch live NAV data: `python live_nav_fetch.py`

## Requirements

See `requirements.txt` for all Python dependencies.

## License

MIT License
