import pandas as pd
from bs4 import BeautifulSoup
import requests

url = 'https://ticker.finology.in/'
r = requests.get(url)
print(r)
soup = BeautifulSoup(r.text, "lxml")
table = soup.find("table", class_ = "table table-sm table-hover screenertable")
print(table)
import pandas as pd
import requests
from bs4 import BeautifulSoup

def scrape_sachin_tendulkar_centuries():
    url = "https://en.wikipedia.org/wiki/List_of_international_cricket_centuries_by_Sachin_Tendulkar"
    response = requests.get(url)
    if response.status_code != 200:
        print("Failed to fetch the page.")
        return

    soup = BeautifulSoup(response.text, "html.parser")
    table = soup.find("table", class_="wikitable")

    if not table:
        print("No table found on the page.")
        return

    centuries = []
    for row in table.find_all("tr")[1:]:
        cells = row.find_all("td")
        if len(cells) >= 6:
            match_date = cells[0].text.strip()
            runs_scored = cells[1].text.strip()
            against_team = cells[2].text.strip()
            venue = cells[3].text.strip()
            match_result = cells[4].text.strip()
            match_format = cells[5].text.strip()

            centuries.append({
                "Match Date": match_date,
                "Runs Scored": runs_scored,
                "Against Team": against_team,
                "Venue": venue,
                "Match Result": match_result,
                "Match Format": match_format
            })

    return centuries

if __name__ == "__main__":
    sachin_centuries = scrape_sachin_tendulkar_centuries()
    for index, century in enumerate(sachin_centuries, start=1):
        print(f"Century {index}:")
        for key, value in century.items():
            print(f"{key}: {value}")
        print()


import requests
from bs4 import BeautifulSoup
import csv

def scrape_sachin_tendulkar_centuries():
    url = "https://en.wikipedia.org/wiki/List_of_international_cricket_centuries_by_Sachin_Tendulkar"
    response = requests.get(url)
    if response.status_code != 200:
        print("Failed to fetch the page.")
        return

    soup = BeautifulSoup(response.text, "html.parser")
    table = soup.find("table", class_="wikitable")

    if not table:
        print("No table found on the page.")
        return

    centuries = []
    for row in table.find_all("tr")[1:]:
        cells = row.find_all("td")
        if len(cells) >= 6:
            match_date = cells[0].text.strip()
            runs_scored = cells[1].text.strip()
            against_team = cells[2].text.strip()
            venue = cells[3].text.strip()
            match_result = cells[4].text.strip()
            match_format = cells[5].text.strip()

            centuries.append({
                "Match Date": match_date,
                "Runs Scored": runs_scored,
                "Against Team": against_team,
                "Venue": venue,
                "Match Result": match_result,
                "Match Format": match_format
            })

    return centuries

def save_to_csv(data, filename):
    with open(filename, "w", newline="", encoding="utf-8") as csvfile:
        fieldnames = ["Match Date", "Runs Scored", "Against Team", "Venue", "Match Result", "Match Format"]
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(data)

if __name__ == "__main__":
    sachin_centuries = scrape_sachin_tendulkar_centuries()
    save_to_csv(sachin_centuries, "sachin_tendulkar_centuries.csv")
    print("Data saved to sachin_tendulkar_centuries.csv")

import requests
from bs4 import BeautifulSoup
import csv

def scrape_sachin_test_centuries():
    url = "https://en.wikipedia.org/wiki/List_of_Test_cricket_centuries_by_Sachin_Tendulkar"
    response = requests.get(url)
    if response.status_code != 200:
        print("Failed to fetch the page.")
        return

    soup = BeautifulSoup(response.text, "html.parser")
    table = soup.find("table", class_="wikitable")

    if not table:
        print("No table found on the page.")
        return

    centuries = []
    for row in table.find_all("tr")[1:]:
        cells = row.find_all("td")
        if len(cells) >= 6:
            match_date = cells[0].text.strip()
            runs_scored = cells[1].text.strip()
            against_team = cells[2].text.strip()
            venue = cells[3].text.strip()
            result = cells[4].text.strip()
            centuries.append({
                "Match Date": match_date,
                "Runs Scored": runs_scored,
                "Against Team": against_team,
                "Venue": venue,
                "Result": result
            })

    return centuries

def save_to_csv(data, filename):
    with open(filename, "w", newline="", encoding="utf-8") as csvfile:
        fieldnames = ["Match Date", "Runs Scored", "Against Team", "Venue", "Result"]
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(data)

if __name__ == "__main__":
    sachin_test_centuries = scrape_sachin_test_centuries()
    save_to_csv(sachin_test_centuries, "sachin_test_centuries.csv")
    print("Data saved to sachin_test_centuries.csv")
