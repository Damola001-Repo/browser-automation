from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.expected_conditions import visibility_of_element_located
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import os

# Define driver, options, and service
chrome_option = Options()
chrome_option.add_argument("--disable-search-engine-choice-screen")

download_path = os.getcwd()
prefs = {'download.default_directory': download_path}
chrome_option.add_experimental_option('prefs', prefs)

service = Service('chromedriver-win64/chromedriver.exe')
driver = webdriver.Chrome(options=chrome_option, service=service)

# Load the webpage
driver.get('https://demoqa.com/login')

# Locate username, password, and login button
username_field = WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.ID, 'userName')))
password_field = WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.ID, 'password')))
login_button = WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.ID, 'login')))


# Fill in username and password, and click login button
username_field.send_keys('damolabalogun79@gmail.com')
password_field.send_keys('H@lloWorld142536')
# login_button.click()

# To avoid clicking ads button and not the button intended
driver.execute_script("arguments[0].click();", login_button)

# Locate the elements dropdown and Text Box
elements = WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.XPATH, '//*[@id="app"]/div/div/div/div[1]/div/div/div[1]')))
elements.click()
text_box = WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.ID, 'item-0')))
text_box.click()

# Locate the form fields and submit button
full_name = WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.ID, 'userName')))
email = WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.ID, 'userEmail')))
current_address = WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.ID, 'currentAddress')))
permanent_address = WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.ID, 'permanentAddress')))
submit_button = WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.ID, 'submit')))

# fill in the form fields
full_name.send_keys('John Smith')
email.send_keys('john@gmail.com')
current_address.send_keys('10, My, Address')
permanent_address.send_keys('10, My, Address')
driver.execute_script("arguments[0].click();", submit_button)


# Locate the Upload and Download button and download the file
upload_download = WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.ID, 'item-7')))
upload_download.click()
download_button = WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.ID, 'downloadButton')))
download_button.click()

input("Press enter to quit")
driver.quit()