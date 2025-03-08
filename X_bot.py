from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support import expected_conditions as EC
from bs4 import BeautifulSoup
import time
from datetime import date
import os
import json
import csv



CHROME_DRIVER_PATH = r"C:/Users/oshev/OneDrive/Desktop/JYP/chromedriver-win64/chromedriver.exe"
OP = webdriver.ChromeOptions()
OP.add_argument('--headless')
DRIVER = webdriver.Chrome(service=Service(CHROME_DRIVER_PATH))


def sign_in():
    with open('C:/Users/oshev/OneDrive/Desktop/JYP/twitter automation/config.json') as configFile:
        user_data = json.load(configFile)
        time.sleep(2)
        wait = WebDriverWait(DRIVER, 10)        #Wait for the buttons to be clickable before clicking it

        # Locate the "Sign in" button using XPath
        wait.until(EC.element_to_be_clickable((By.XPATH, '//span[text()="Sign in"]'))).click()
        time.sleep(3)

        phone = wait.until(EC.element_to_be_clickable((By.XPATH, '//input[@name="text"]')))
        phone.clear()
        phone.send_keys(user_data["PHONE"])
        DRIVER.find_element(By.XPATH, '//span[text()="Next"]').click()          # For 'phone no'
        time.sleep(5)

        password = wait.until(EC.element_to_be_clickable((By.XPATH, '//input[@name="password"]')))
        password.clear()
        password.send_keys(user_data["PASSWORD"])
        DRIVER.find_element(By.XPATH, '//span[text()="Log in"]').click()          # For 'Password'
        time.sleep(5)

        user = wait.until(EC.element_to_be_clickable((By.XPATH, '//input[@name="text"]')))
        user.clear()
        user.send_keys(user_data["USERNAME"])
        DRIVER.find_element(By.XPATH, '//span[text()="Next"]').click()          # For 'Username'
        time.sleep(5)




def scrape_twitter_profile(driver, profile_url):
    """
    Scrapes details from a given Twitter profile URL.

   """
    DRIVER.get(profile_url)
    time.sleep(6)  # Wait for page to load
    
    soup = BeautifulSoup(DRIVER.page_source, 'html.parser')

    try:
        name = soup.find('span', {'dir': 'ltr'}).text
    except AttributeError:
        name = "N/A"

    try:
        username = soup.find('div', {'data-testid': 'UserName'}).text
    except AttributeError:
        username = "N/A"

    try:
        bio = soup.find('div', {'data-testid': 'UserDescription'}).text
    except AttributeError:
        bio = "N/A"

    try:
        followers = soup.find('a', {'href': f'{profile_url}/verified_followers'}).text
    except AttributeError:
        followers = "N/A"

    try:
        following = soup.find('a', {'href': f'{profile_url}/following'}).text
    except AttributeError:
        following = "N/A"

    try:
        location = soup.find('div', {'data-testid': 'UserLocation'}).text
    except AttributeError:
        location = "N/A"
 

    return {
        "Name": name,
        "Username": username,
        "Bio": bio,
        "Followers": followers,
        "Following": following,
        "Profile URL": profile_url,
        "Location": location
    }


def save_to_csv(data, filename="twitter_profiles(2.0).csv"):
    """
    Saves extracted profile data into a CSV file.

    """
    headers = ["Name", "Username", "Bio", "Followers", "Following", "Profile URL", "Location"]

    with open(filename, "w", newline="", encoding="utf-8") as file:
        writer = csv.DictWriter(file, fieldnames=headers)
        writer.writeheader()
        writer.writerows(data)


def main():
    try:
        DRIVER.get("https://x.com")
        sign_in()
        
        # List of Twitter profile links
        profile_links = [
            "https://x.com/esports_kobe",
            "https://x.com/JamesDash",
            "https://x.com/CaptainFlowers",
            "https://x.com/MedicCasts",
            "https://x.com/YamatoMebdi",
            "https://x.com/Carzzylol",
            "https://x.com/BroxahLoL",
            "https://x.com/G2Caps",
            "https://x.com/JankosLoL",
            "https://x.com/mikyx",
            "https://x.com/Kuforiji_00",
            "https://x.com/__tangirl"

    ]

        scraped_data = []
        for link in profile_links:
            scraped_data.append(scrape_twitter_profile(DRIVER, link))

        save_to_csv(scraped_data)

        input('Bot Automation Completed. Press any key ...')
        DRIVER.close()
    except Exception as e:
        print(e)

        DRIVER.close()



if __name__ == "__main__":
    main()                  # MAIN function


   
