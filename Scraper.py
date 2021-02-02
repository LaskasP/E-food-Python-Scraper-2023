import requests 
from bs4 import BeautifulSoup
import csv 
from selenium import webdriver
import time
import random
import argparse

parser = argparse.ArgumentParser()
parser.add_argument('--url', required=True, help ='need starting url')
parser.add_argument('-c', '--comment', action='store_true', help="shows output")
args = parser.parse_args()
startingUrl = args.url 
if args.comment:
    comments = True

pathToReviews = "EfoodReviews.csv"
pathToStoreInfo = "EfoodStoresInfo.csv"
numreviews = 0

page = requests.get(startingUrl)
soup = BeautifulSoup(page.text, 'html.parser')
shopUrls = soup.find('div', class_='shops-listings-shops-list')
reviewsUrlpre = shopUrls.find_all('a', class_ = 'shops-listing-shop position-relative')
reviewsUrls = []
print('katasthmata: ' + str(len(reviewsUrlpre)))
driver = webdriver.Chrome('E-food-Python-Scraper-2021\chromedriver.exe')

for url in reviewsUrlpre:
    reviewsUrls.append('https://www.e-food.gr' + str(url.get('href')))

for url in reviewsUrls:
    driver.get(url)
    driver.find_element_by_xpath("//ul[@id='pills-tab']//li[3]").click()
    buttonTextEnable = driver.find_elements_by_xpath("//div[@class='input-radio-mark without_comment_only position-relative']//label[@class='mb-0']")
    time.sleep(random.randint(0,3))
    #if you want reviews with comments only
    if comments:
        buttonTextEnable[0].click()
    #Show all comments
    try:
        while True:
            button = driver.find_element_by_xpath("//button[@class='btn btn-sm btn-secondary shop-profile-more-ratings']")
            if button.get_attribute("style") == 'display: none;':
                break
            time.sleep(random.randint(0,1))
            driver.execute_script("arguments[0].click();", button)
    except Exception:
        print('No more pages')
        time.sleep(random.randint(0,1))
    
    response = BeautifulSoup(driver.page_source, 'html.parser')
    #STORE'S AVERAGE RATING
    storeAvgRating = response.find('span', class_= 'mr-2 small font-weight-bold text-yellow').text
    #STORE'S NUMBER OF REVIEWS
    storeNoOfReviews = response.find('span', class_= 'small text-muted').text
    #STORE'S FOOD QUALITY, SPEED QUALITY, SERVICE QUALITY RATINGS
    storeRating = response.find_all('p', class_='mb-0 text-center position-absolute')
    #STORE'S ADDRESS
    try:
        shopAddress = response.find('span', class_='text-muted mb-3 mb-lg-0').text.strip()
    except:
        shopAddress = 'Unknown Address'
    #STORE'S NAME
    try:
        shopName = response.find('h1', class_='mb-3 mb-lg-2').text.strip()
    except Exception:
        shopName = response.find('h1', class_='mb-3 mb-lg-2 h2').text.strip()

    #STORE INFO TO CSV
    try:
        with open(pathToStoreInfo, mode='a', encoding="utf-8") as store_data:
            data_writer = csv.writer(store_data, delimiter = ',', quotechar = '"', quoting = csv.QUOTE_MINIMAL)
            data_writer.writerow([shopName, shopAddress, storeAvgRating, storeRating[0].text.strip(), storeRating[1].text.strip(), storeRating[2].text.strip(), storeNoOfReviews[1:len(storeNoOfReviews) - 1]])
    except:
        print('error with store writer')
    #REVIEWS
    reviews = response.find_all('li', class_ = 'ratigns-tab-ratings-list-item p-5 pb-9 p-md-9 border-bottom')
    for review in reviews:
        #USER'S RATING
        UserRating = review.find('span', class_= 'text-yellow').text.strip()
        nameAndDate = review.find('span',class_ = 'font-weight-bold my-md-auto text-truncate col-8 px-0').text.split()
        #USERNAME
        userName = nameAndDate[0]
        #DATE
        date = nameAndDate[2]
        #CONTENT OF REVIEW
        content = review.find('p', class_ = 'shop-ratings-comment').text
        #REVIEW INFO TO CSV
        try:
            with open(pathToReviews, mode='a', encoding="utf-8") as efood_data:
                numreviews += 1
                data_writer = csv.writer(efood_data, delimiter = ',', quotechar = '"', quoting = csv.QUOTE_MINIMAL)
                data_writer.writerow([shopName, userName, date, content, UserRating])
        except:
            print('Error with review writer')

print(numreviews)

