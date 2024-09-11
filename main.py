import requests as req
from bs4 import BeautifulSoup as BTS
from pprint import pprint
res = req.get('https://books.toscrape.com/index.html')

soup = BTS(res.text, 'html.parser')

"""
def traverse_dom(element, level=0):
    # print actually element
    if element.name:
        print(f"{' ' * level}<{element.name}>")

    # if element have the children

    if hasattr(element, 'chlidren'):
        for child in element.children:
            traverse_dom(child, level + 1)


traverse_dom(soup)
"""

asides = soup.find(name='div', class_='side_categories')
#pprint(asides)
categories_div = asides.find(name='ul').find(name='li').find(name='ul')

categories = [child.text.strip() for child in categories_div.children if child.name]
section_img = soup.find('section').find_all('img')

imgs_src = [img.get('src') for img in section_img]


articles = soup.find_all('article', 'product_pod')
books_titles = [article.find('h3').find('a').get('title') for article in articles if article.find('h3').find('a')]


#books_title = [title.text.strip() for title in h3_title]

print(books_titles)


#print(imgs_src)

"""for category in categories:
    print(category)
"""