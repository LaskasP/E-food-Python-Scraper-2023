from selenium.webdriver.common.by import By

from selenium.webdriver.chrome.service import Service

from selenium.webdriver.support import expected_conditions as EC

from webdriver_manager.chrome import ChromeDriverManager

from selenium.webdriver.support.ui import WebDriverWait

from selenium.webdriver.common.action_chains import ActionChains

from bs4 import BeautifulSoup
import csv

from selenium import webdriver
import time
import random

import argparse
import pandas as pd


def get_url_from_args():

    parser = argparse.ArgumentParser()

    parser.add_argument('--url', required=True, help='need starting url')

    args = parser.parse_args()

    return args.url


def get_shops_urls(starting_url, driver, delay):

    shops_urls = []
    action = ActionChains(driver)
    driver.get(starting_url)
    WebDriverWait(driver, delay).until(
        EC.presence_of_all_elements_located((By.CLASS_NAME, 'iTdWU')))
    driver.execute_script("window.scrollBy(0, document.body.scrollHeight)")
    driver.execute_script("window.scrollBy(0, -window.innerHeight)")
    pos = WebDriverWait(driver, delay).until(
        EC.visibility_of_element_located((By.CLASS_NAME, 'cteiAT')))
    driver.execute_script("arguments[0].click();", pos)
    time.sleep(6)
    shop_cards = WebDriverWait(driver, delay).until(
        EC.presence_of_all_elements_located((By.CLASS_NAME, 'card-1-0-shop')))
    for card in shop_cards:
        shops_urls.append(card.find_element(
            By.CSS_SELECTOR, "a").get_attribute('href'))
    # print(len(shop_cards))
    return shops_urls[0:2]


def scrap_shop_info(shop_urls, driver, delay):
    no_data = 'Unknown'
    names = []
    last_year_scores = []
    last_year_qualities = []
    last_year_servicies = []
    last_year_speeds = []
    last_year_speeds_inperson = []
    yummy = []
    values = []
    food_sizes = []
    consistancies_of_orders = []
    delivery_services = []
    estimated_delivery_times = []
    for url in shop_urls:
        driver.get(url)
        driver.execute_script("window.scrollTo(0, 150)")
        review_button = WebDriverWait(driver, delay).until(
            EC.presence_of_element_located((By.CLASS_NAME, 'sc-bcGyXE')))
        review_button.click()
        time.sleep(1)
        soup = BeautifulSoup(driver.page_source, 'html.parser')
        name = soup.find('h2', attrs={'class': 'kfsFho'})
        if name and name.text:
            names.append(name.text)
        else:
            names.append(no_data)
        last_year_score = soup.find('h3', attrs={'class': 'iTgiWN'})
        if last_year_score and last_year_score.text:
            last_year_scores.append(last_year_score.text)
        else:
            last_year_scores.append(no_data)
        last_year_quality = soup.find(
            text='Ποιότητα').parent.find_next_sibling()
        if last_year_quality and last_year_quality.text:
            last_year_qualities.append(last_year_quality.text)
        else:
            last_year_qualities.append(no_data)
        last_year_service = soup.find(
            text='Εξυπηρέτηση').parent.find_next_sibling()
        if last_year_service and last_year_service.text:
            last_year_servicies.append(last_year_quality.text)
        else:
            last_year_servicies.append(no_data)
        last_year_speed = soup.find(
            text='Ταχύτητα').parent.find_next_sibling()
        if last_year_speed and last_year_speed.text:
            last_year_speeds.append(last_year_quality.text)
        else:
            last_year_speeds.append(no_data)
        taste = soup.find(
            text='Γεύση').parent.find_next_sibling().find('span', attrs={'class': 'hMNQNy'})
        if taste and taste.text:
            yummy.append(taste.text[:len(taste.text)-1])
        else:
            yummy.append(no_data)
        value = soup.find(
            text='Σχέση ποιότητας - τιμής').parent.find_next_sibling().find('span', attrs={'class': 'hMNQNy'})
        if value and value.text:
            values.append(value.text[:len(value.text)-1])
        else:
            values.append(no_data)
        food_size = soup.find(
            text='Μέγεθος μερίδας').parent.find_next_sibling().find('span', attrs={'class': 'hMNQNy'})
        if food_size and food_size.text:
            food_sizes.append(food_size.text[:len(food_size.text)-1])
        else:
            food_sizes.append(no_data)
        consistancy_of_orders = soup.find(
            text='Συνέπεια παραγγελίας').parent.find_next_sibling().find('span', attrs={'class': 'hMNQNy'})
        if consistancy_of_orders and consistancy_of_orders.text:
            consistancies_of_orders.append(
                consistancy_of_orders.text[:len(consistancy_of_orders.text)-1])
        else:
            consistancies_of_orders.append(no_data)
        delivery_service = soup.find(
            text='Εξυπηρέτηση από τον διανομέα').parent.find_next_sibling().find('span', attrs={'class': 'hMNQNy'})
        if delivery_service and delivery_service.text:
            delivery_services.append(
                delivery_service.text[:len(delivery_service.text)-1])
        else:
            delivery_services.append(no_data)
        estimated_delivery_time = soup.find(
            text='Εκτιμώμενος χρόνος παράδοσης').parent.find_next_sibling().find('span', attrs={'class': 'hMNQNy'})
        if estimated_delivery_time and estimated_delivery_time.text:
            estimated_delivery_times.append(
                estimated_delivery_time.text[:len(estimated_delivery_time.text)-1])
        else:
            estimated_delivery_times.append(no_data)
        time.sleep(random.randint(0, 2))
    to_csv(names, last_year_scores, last_year_qualities,
           last_year_servicies, last_year_speeds, yummy, values, food_sizes, consistancies_of_orders, delivery_services, estimated_delivery_times)


def to_csv(*args):
    df = pd.DataFrame({'Names': args[0], 'yearly_score': args[1],
                      'yearly_quality': args[2], 'service': args[3], 'speed': args[4], 'taste': args[5], 'value': args[6], 'food_size': args[7], 'consistancy_of_order': args[8], 'delivery_service': args[9], 'estimated_delivery_time': args[10]})
    df.to_csv('storeInfo.csv', index=False, encoding='utf-8')


def main():
    delay = 5  # seconds
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    starting_url = get_url_from_args()
    shops_urls = get_shops_urls(starting_url, driver, delay)
    scrap_shop_info(shops_urls, driver, delay)


if __name__ == "__main__":
    main()
