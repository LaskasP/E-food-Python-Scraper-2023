# E-food-Python-Scraper-2021
An implementation on Python for scraping E-food's store information and Reviews from users


Features implemented:
1) Scrape restaurants's reviews and store it in csv. The feutures of each review are restaurant's name, username, date, content, rating 
2) Scrape a whole area like a city (all restaurants in this region)
3) Scrape basic info(Restaurant's name, Address, Average Rating, Food quality rating, Speed quality rating, Service quality rating, Number of reviews) of each restaurant and store it in another csv
4) The click function to collect all reviews from a restaurant
5) The click function to collect only the reviews with comment

How to use:

Directly from the terminal: 


--url : required url of an area from efood page
-c : if you want comments only reviews.

example:
Python scraper.py -c --url 'https://www.e-food.gr/shops?address=%CE%9A%CE%B1%CF%81%CE%B1%CE%BF%CE%BB%CE%AE%20%CE%BA%CE%B1%CE%B9%20%CE%94%CE%B7%CE%BC%CE%B7%CF%84%CF%81%CE%AF%CE%BF%CF%85%204%2C%2045332%20%CE%99%CF%89%CE%AC%CE%BD%CE%BD%CE%B9%CE%BD%CE%B1%2C%20%CE%9A%CE%AD%CE%BD%CF%84%CF%81%CE%BF&city=%CE%9A%CE%AD%CE%BD%CF%84%CF%81%CE%BF&county=%CE%99%CF%89%CE%AC%CE%BD%CE%BD%CE%B9%CE%BD%CE%B1&latitude=39.665595&longitude=20.851233&nomap=0&street=%CE%9A%CE%B1%CF%81%CE%B1%CE%BF%CE%BB%CE%AE%20%CE%BA%CE%B1%CE%B9%20%CE%94%CE%B7%CE%BC%CE%B7%CF%84%CF%81%CE%AF%CE%BF%CF%85&street_no=4&zip=45332&area=%CE%9A%CE%AD%CE%BD%CF%84%CF%81%CE%BF&city_transliterated=&slug=%2F&deliverytype=0&scope=personal&t=1612299334489'.

You need webChromeDriver downloaded in the same folder to make it work.

If you have any feature requests, don't hesitate to contact me :)

Use at own risk, it might violate Efood policies.
