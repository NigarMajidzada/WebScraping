from bs4 import BeautifulSoup
import requests
import lxml
import sqlite3

base_url = 'https://books.toscrape.com/'


def get_categories(url):
    response = requests.get(base_url)
    soup = BeautifulSoup(response.content, 'lxml')
    categories = soup.select('.side_categories ul li ul li a')
    result = []
    for idx, cat in enumerate(categories, start=1):
        name = cat.text.strip()
        link = base_url + cat['href']
        result.append((idx, name, link))

    return result


categories = get_categories(base_url)


def get_books(categories):
    book_list = []
    for category_id, category_name, category_link in categories:
        response = requests.get(category_link)
        soup = BeautifulSoup(response.content, 'lxml')
        books = soup.find_all('article', class_='product_pod')

        for book in books:
            title = book.h3.a['title']
            price = book.find('p', class_='price_color').text.strip()
            price = float(price[1:])
            star_tag = book.find('p', class_='star-rating')
            star = star_tag['class'][1]
            link = book.h3.a['href']
            book_list.append((
                category_id,
                title,
                price,
                star
            ))
    return book_list


books = get_books(categories)

conn = sqlite3.connect('mysite.db')
cursor = conn.cursor()

cursor.execute('''CREATE TABLE IF NOT EXISTS Categories
                    ( Category_id INTEGER  PRIMARY KEY ,
                    Category_name  VARCHAR(255),
                    Category_link VARCHAR(255)
                    )'''
               )
conn.commit()

cursor.executemany(''' INSERT INTO Categories (Category_id,Category_name,Category_link)
                        VALUES (?,?,?)

                    ''', categories)

conn.commit()

cursor.execute('''CREATE TABLE IF NOT EXISTS Books
                    ( Book_id INTEGER PRIMARY KEY AUTOINCREMENT,
                     Category_id INTEGER ,
                     Title  VARCHAR(255),
                     Price REAL,
                     Star VARCHAR(255),
                     FOREIGN KEY (Category_id) REFERENCES Categories(Category_id)
                    )'''
               )

cursor.executemany(''' INSERT INTO Books (Category_id,Title,Price,Star)
                        VALUES (?,?,?,?)

                    ''', books)

conn.commit()
conn.close()
