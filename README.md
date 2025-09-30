# COVID-19 Dashboard 🌍

A **Streamlit dashboard** to visualize global COVID-19 data, including cases, deaths, and trends.  
Users can filter by country, select a date range, and view **summary metrics, interactive charts, and country flags**.

---

## Features

- Filter data by **country** and **date range**.
- Display **total and new cases**, **total and new deaths**.
- Show **country flags** dynamically.
- Interactive **line charts** for total and new cases.
- Interactive **bar charts** for new deaths.
- Clean, wide layout for an elegant UI.

---

## Screenshots

![Dashboard Screenshot](assets/screenshot.png)  

---

## Installation

1. Clone the repository:

```bash
git clone https://github.com/luchiri/COVID-19-Dashboard.git
cd covid-dashboard
Create a virtual environment:

bash
Copy code
python -m venv .venv
Activate the virtual environment:

Windows (PowerShell):

powershell
Copy code
.\.venv\Scripts\Activate.ps1
Windows (cmd):

cmd
Copy code
.\.venv\Scripts\activate
macOS / Linux:

bash
Copy code
source .venv/bin/activate
Install dependencies:

bash
Copy code
pip install -r requirements.txt
Run the dashboard locally:

bash
Copy code
streamlit run app.py
Data
The app uses OWID COVID-19 dataset (owid-covid-data.csv) to fetch historical data for each country.
Country flags are stored locally in the assets/flags folder.

Deployment
You can deploy the dashboard for free using Streamlit Community Cloud:

Push your project to GitHub.

Go to Streamlit Share and sign in.

Click New App, select your repository, branch, and app.py.

Your dashboard will be live!

Requirements
Python 3.9+

pandas

streamlit

plotly

License
This project is MIT licensed.
