# E-food-Python-Scraper-2023
An implementation on Python for scraping E-food's store information and Reviews from users


Features implemented:
1) Scrape restaurants's reviews and store it in csv. The feutures of each review are restaurant's name, year general score, year food quality, year service quality, year speed quality, taste, value for money, food size, consistancy in ordering, delivery service quality and estimated delivery time quality.
2) Scrape a whole area like a city (all restaurants in this region)

How to use:

Directly from the terminal: 

--url : required url of an area from efood page

example:
Python scraper.py --url 'https://www.e-food.gr/shops?address=%CE%9A%CE%B1%CF%81%CE%B1%CE%BF%CE%BB%CE%AE%20%CE%BA%CE%B1%CE%B9%20%CE%94%CE%B7%CE%BC%CE%B7%CF%84%CF%81%CE%AF%CE%BF%CF%85%204%2C%2045332%20%CE%99%CF%89%CE%AC%CE%BD%CE%BD%CE%B9%CE%BD%CE%B1%2C%20%CE%9A%CE%AD%CE%BD%CF%84%CF%81%CE%BF&city=%CE%9A%CE%AD%CE%BD%CF%84%CF%81%CE%BF&county=%CE%99%CF%89%CE%AC%CE%BD%CE%BD%CE%B9%CE%BD%CE%B1&latitude=39.665595&longitude=20.851233&nomap=0&street=%CE%9A%CE%B1%CF%81%CE%B1%CE%BF%CE%BB%CE%AE%20%CE%BA%CE%B1%CE%B9%20%CE%94%CE%B7%CE%BC%CE%B7%CF%84%CF%81%CE%AF%CE%BF%CF%85&street_no=4&zip=45332&area=%CE%9A%CE%AD%CE%BD%CF%84%CF%81%CE%BF&city_transliterated=&slug=%2F&deliverytype=0&scope=personal&t=1612299334489'.

You need webChromeDriver downloaded in the same folder to make it work.

If you have any feature requests, don't hesitate to contact me :)

# Use at your own risk, it might violate Efood policies.
