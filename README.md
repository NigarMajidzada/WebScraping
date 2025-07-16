# WebScraping
Web scraping project with Python that collects data from websites and saves it into an SQLite database.

# Books and Categories Scraper

This Python project crawls book data from [books.toscrape.com](https://books.toscrape.com/), extracts **categories** and **books with details**, and stores them into a **SQLite database**.

##  Features
- Fetches all book categories from the website.
- Extracts each book’s:
  - Title
  - Price
  - Star rating
  - Category
- Saves the data in two normalized tables: `Categories` and `Books`.

##  Technologies
- Python 3
- [BeautifulSoup4](https://www.crummy.com/software/BeautifulSoup/)
- [Requests](https://docs.python-requests.org/)
- [lxml](https://lxml.de/)
- [SQLite3](https://www.sqlite.org/index.html)

# Books & Categories to SQLite

##  Database Schema

- **Categories**
  | Column         | Type          |
  |----------------|---------------|
  | Category_id    | INTEGER (PK)  |
  | Category_name  | TEXT          |
  | Category_link  | TEXT          |

- **Books**
  | Column         | Type          |
  |----------------|---------------|
  | Book_id        | INTEGER (PK)  |
  | Category_id    | INTEGER (FK)  |
  | Title          | TEXT          |
  | Price          | REAL          |
  | Star           | TEXT          |

##  How to Run

1 Clone or download this repository.

2 Install dependencies:
```bash
pip install requests beautifulsoup4 lxml

