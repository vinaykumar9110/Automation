from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
import time

# Function to set up the WebDriver
def setup_driver():
    options = webdriver.ChromeOptions()
    options.add_argument("--headless")  # Run in headless mode (no GUI)
    options.add_argument("--no-sandbox")
    options.add_argument("--disable-dev-shm-usage")
    driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()), options=options)
    driver.implicitly_wait(10)  # Wait up to 10 seconds for elements to appear
    return driver

# Function to perform login action
def perform_login(driver, url, username, password):
    driver.get(url)
    driver.maximize_window()  # Optional: Maximize the browser window

    # Locate the username and password fields and enter credentials
    driver.find_element(By.ID, "username").send_keys(username)
    driver.find_element(By.ID, "password").send_keys(password)

    # Locate and click the login button
    driver.find_element(By.ID, "login-button").click()

    # Wait for the page to load
    time.sleep(5)

# Function to verify login success
def verify_login(driver):
    try:
        # Example: Check if a logout button is present to confirm successful login
        logout_button = driver.find_element(By.ID, "logout-button")
        assert logout_button.is_displayed()
        print("Login successful")
    except Exception as e:
        print("Login failed:", e)

# Main function to execute the script
def main():
    driver = setup_driver()
    try:
        url = "https://www.example.com/login"  # Replace with your login page URL
        username = "your_username"  # Replace with your test username
        password = "your_password"  # Replace with your test password
        perform_login(driver, url, username, password)
        verify_login(driver)
    finally:
        driver.quit()  # Ensure the browser is closed after the test

if __name__ == "__main__":
    main()
