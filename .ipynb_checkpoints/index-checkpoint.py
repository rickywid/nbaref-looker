'''

Write players to CSV file. Import CSV as pandas Dataframe.
Remove any duplicate players.
Check for any missing values.


https://www.basketball-reference.com/teams/TOR/2023.html




from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By

driver = webdriver.Chrome(ChromeDriverManager().install())

driver.get("https://www.basketball-reference.com/teams/TOR/2023.html")
table = driver.find_element(by=By.ID, value="roster")
tbody = table.find_element(by=By.TAG_NAME, value="tbody")
rows = tbody.find_elements(by=By.TAG_NAME, value="tr")

for r in rows:

    # find player link - navigate to player profile page




    name = r.find_elements(By.CLASS_NAME, value="left")
    #name = r.find_element(by=By.TAG_NAME, value="td['data-stat=player']")
    print(name[0].text)



#driver.find_element(by=By.CLASS_NAME, value="button2.prev").click()
#driver.back()
'''

import pandas as pd
import csv  

df = []

teams = [
        'BOS',
        'BRK',
        'TOR',
        'PHI',
        'NYK',
        'MIN',
        'OKC',
        'DEN',
        'POR',
        'UTA',
        'CHI',
        'CLE',
        'DET',
        'IND',
        'MIL',
        'LAL',
        'LAC',
        'GSW',
        'PHO',
        'SAC',
        'WAS',
        'ATL',
        'ORL',
        'MIA',
        'CHO',
        'MEM',
        'NOP',
        'HOU',
        'SAS',
        'DAL'
        ]


def writeToCsv(team):
    data = pd.read_html(f'https://www.basketball-reference.com/teams/{team}/2023.html')
    df.append(data)


for t in teams:
    writeToCsv(t)

len(df)
