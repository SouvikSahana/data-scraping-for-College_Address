import pandas as pd
import requests
from bs4 import BeautifulSoup

df = pd.read_excel("Web_Scraping_Assignment.xlsx")
clg_data = df[df.columns[1]]
myList = []
columns = ['College Name', 'Address']

# Print the data in the second column
for x in clg_data:
  URL = "https://www.google.com/search?q=" + x.replace(" ", "+").replace(
    ",", "%2C").replace("&", "%26")
  r = requests.get(URL)

  soup = BeautifulSoup(r.content, 'html5lib')

  table = soup.find('span', attrs={'class': 'BNeawe tAd8D AP7Wnd'})
  if (table):
    print(table.text)
    myList.append(table.text)
  else:
    print(" ")
    myList.append(" ")

dg = pd.DataFrame(list(zip(clg_data, myList)), columns=columns)

# Write DataFrame to Excel file with sheet name
dg.to_excel('Result.xlsx', sheet_name='Technologies')
