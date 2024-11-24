from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
from concurrent.futures import ThreadPoolExecutor
from time import sleep

# Configure Chrome to run in headless mode
chrome_options = Options()
chrome_options.add_argument("--headless")  # Run in headless mode
chrome_options.add_argument("--disable-gpu")  # Disable GPU for headless compatibility
chrome_options.add_argument("--no-sandbox")  # Sandbox is not needed for headless mode
chrome_options.add_argument("--disable-dev-shm-usage")  # Avoid shared memory issues
chrome_options.add_argument("--enable-unsafe-swiftshader") # something

# List of URLs, each one will be opened by a different driver
urls = [
    'https://www.example.com',
]


# Function to scroll to the bottom of a page
def scroll_to_bottom_loop(driver):
    # method 1
    last_height = driver.execute_script("return document.body.scrollHeight")
    while True:
        driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        sleep(2)
        new_height = driver.execute_script("return document.body.scrollHeight")
        if new_height == last_height:
            break
        last_height = new_height

def scroll_to_bottom_key(driver):
    # method 2
    body = driver.find_element(By.TAG_NAME, 'body')
    body.send_keys(Keys.END)

def open_and_process_url(url):
    # Initialize the WebDriver with headless options
    driver = webdriver.Chrome(options=chrome_options)
    driver.get(url)
    sleep(1)  # Allow the page to load

    scroll_to_bottom_loop(driver)
    # scroll_to_bottom_key(driver)

    driver.quit()

i = 0
while True:
    print(f"Starting iteration {i + 1}...")

    # Use ThreadPoolExecutor to run multiple drivers in parallel with their own links
    with ThreadPoolExecutor(max_workers=5) as executor:  # Adjust max_workers as needed
        executor.map(open_and_process_url, urls)

    print(f"Completed iteration {i + 1}. Waiting before the next iteration...")
    i += 1
