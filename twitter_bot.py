import time
import csv
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
import pandas as pd


# Your Twitter (X) login credentials
TWITTER_USERNAME = "Onome_josph"
TWITTER_PASSWORD = "******"


input_csv_file = "twitter_links.csv"

# To Read Twitter profile links from CSV 
twitter_profiles = []
with open(input_csv_file, mode="r", encoding="utf-8") as file:
    reader = csv.reader(file)
    for row in reader:
        if row: 
            twitter_profiles.append(row[0])

# Setting up Selenium WebDriver
options = Options()
options.add_argument("--headless")  # Running in headless mode
options.add_argument("--disable-gpu")
options.add_argument("--no-sandbox")

chromedriver_path = r"C:/Users/oshev/Downloads/chromedriver-win64/chromedriver-win64/chromedriver.exe" 
driver = webdriver.Chrome(service=Service(chromedriver_path), options=options)

# Function to log in to Twitter
def twitter_login():
    print("[INFO] Logging into Twitter...")
    driver.get("https://twitter.com/login")       # N/B: Has been modified to X
    time.sleep(3)  # Allow time for login page to load

    try:
        # Find username field and enter the username
        username_input = driver.find_element(By.NAME, "text")
        username_input.send_keys(TWITTER_USERNAME)
        username_input.send_keys(Keys.RETURN)
        time.sleep(3)  # Wait for next step

        # Find password field and enter the password
        password_input = driver.find_element(By.NAME, "password")
        password_input.send_keys(TWITTER_PASSWORD)
        password_input.send_keys(Keys.RETURN)
        time.sleep(5)  # Allow time for login
        print("[SUCCESS] Logged in!")
    except Exception as e:
        print(f"[ERROR] Login failed: {e}")
        driver.quit()
        exit()

# Perform login before scraping profiles
twitter_login()


# CSV file setup
csv_filename = "twitter(X)_profiles.csv"
csv_headers = ["Profile URL", "Bio", "Following Count", "Followers Count", "Location", "Website"]

with open(csv_filename, mode="w", newline="", encoding="utf-8") as file:
    writer = csv.writer(file)
    writer.writerow(csv_headers)

    for profile in twitter_profiles:
        driver.get(profile)
        time.sleep(5)  # Wait for elements to load

        try:
            bio = driver.find_element(By.XPATH, "//div[@data-testid='UserDescription']").text
        except:
            bio = "N/A"

        try:
            following = driver.find_element(By.XPATH, "//a[contains(@href, '/following')]//span").text
        except:
            following = "N/A"

        try:
            followers = driver.find_element(By.XPATH, "//a[contains(@href, '/followers')]//span").text
        except:
            followers = "N/A"

        try:
            location = driver.find_element(By.XPATH, "//span[@data-testid='UserLocation']").text
        except:
            location = "N/A"

        try:
            website = driver.find_element(By.XPATH, "//a[@data-testid='UserUrl']").text
        except:
            website = "N/A"

        # Write data to CSV
        writer.writerow([profile, bio, following, followers, location, website])
        print(f"Scraped: {profile}")

driver.quit()
print(f"Scraping complete! Data saved in {csv_filename}")
