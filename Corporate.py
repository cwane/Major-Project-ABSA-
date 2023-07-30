import requests
import csv
import pandas as pd
import codecs
from bs4 import BeautifulSoup

News_headlines = []

# Triggering all 8 pages
for i in range(1, 8):
    url = "https://aarthiknews.com/category/Corporate/?page=" + str(i)
    request = requests.get(url)
    print(request)

    # Extracting all html text containing the classname from the webpage
    soup = BeautifulSoup(request.text, 'lxml')
    news_text = soup.find_all('div', class_='col-lg-9 col-md-12')

    # Extract the headlines from the given div
    for index, news in enumerate(news_text):
        news_header = news.find('a')
        news_headline = news_header.text
        News_headlines.append(news_headline)
    print(len(News_headlines))

# Specify the CSV file path
csv_file_path = "News_Headline_Trade_Corporate.csv"
# Open the CSV file with proper encoding
with codecs.open(csv_file_path, 'w', encoding='utf-8-sig') as file:
    writer = csv.writer(file)

    # Write the headlines to the CSV file
    writer.writerow(["Index", "Headline"])  # Write header
    for index, headline in enumerate(News_headlines, start=1):
        writer.writerow([index, headline])

# Use pandas DataFrame to create a proper tabular view
df = pd.DataFrame({"Headline": News_headlines})

# Convert the DataFrame into a CSV file with proper encoding
df.to_csv("News_Headline_Trade_Corporate.csv", encoding='utf-8-sig', index_label="Index")