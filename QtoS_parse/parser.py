import json
import requests
import csv
from bs4 import BeautifulSoup

URL = 'http://quotes.toscrape.com'
json_file = open('parsed_data/data.json', 'w')
txt_file = open('parsed_data/data.txt', 'w')
csv_file = open('parsed_data/data.csv', 'w+')
all_parsed_quotes = 0 # variable for calculate items

def recording_data(*args):
    # function records data in json and txt files
    json.dump(args, json_file, indent=4)
    txt_file.write(str(args) + '\n')
    csv_writer = csv.writer(csv_file)
    csv_writer.writerow(args)

def scrap_all_pages(url):
    # function parses pages recursively
    quotes_page = requests.get(url)
    # quotes_page.status_code
    quotes_page_soup = BeautifulSoup(quotes_page.text, 'html.parser')
    quotes = quotes_page_soup.find_all('div', class_='quote')

    global all_parsed_quotes
    all_parsed_quotes += scrap_one_page(quotes)

    next_page_url = URL + quotes_page_soup.find('li', class_='next') \
	.find('a')['href']

    print('Procetion... {} items done'.format(all_parsed_quotes))
    try:
        (scrap_all_pages(next_page_url))
    except AttributeError:
        print('Scrapping stoped! Parsed {} items'.format(all_parsed_quotes))

def scrap_one_page(items):
    parsed_quotes = 0
    for quote in items:
        # text
        text = (quote.find('span').contents[0])[1:-1]
        # author
        author = quote.find('small', class_='author').contents[0]
        author_url = URL + (quote.select('span a'))[0]['href']
        author_page = requests.get(author_url)
        # author_page.status_code
        author_page_soup = BeautifulSoup(author_page.text, 'html.parser')
        author_title = author_page_soup.find('h3').contents[0]
        born_date = author_page_soup.find('span', class_='author-born-date') \
        .contents[0]
        born_place = (author_page_soup.find('span', \
        class_='author-born-location').contents[0])[3:]
        about = (author_page_soup.find('div', class_='author-description') \
        .contents[0])[9:]
        # tags
        tags_dict = {}
        tags = quote.find_all('a', class_='tag')
		
        for tag in tags:
            tag_name = tag.contents[0]
            tag_url = URL + tag['href']
            tags_dict[tag_name] = [tag_name, tag_url, text, author, author_url]
        parsed_quotes += 1

        recording_data(text, {author: [author_url, author_title, born_date, born_place, about]}, {'tags': tags_dict})

    return parsed_quotes

# scrap_all_pages(URL)


# json_file.close()
# txt_file.close()