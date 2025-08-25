from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager
import time

def setup_chrome_driver():
    """
    Set up and configure Chrome WebDriver with optimal settings
    """
    # Chrome options for better performance and stability
    chrome_options = Options()
    
    # Optional: Run in headless mode (no GUI)
    # chrome_options.add_argument("--headless")
    
    # Performance and stability options
    chrome_options.add_argument("--no-sandbox")
    chrome_options.add_argument("--disable-dev-shm-usage")
    chrome_options.add_argument("--disable-gpu")
    chrome_options.add_argument("--window-size=1920,1080")
    chrome_options.add_argument("--disable-blink-features=AutomationControlled")
    chrome_options.add_experimental_option("excludeSwitches", ["enable-automation"])
    chrome_options.add_experimental_option('useAutomationExtension', False)
    
    # Initialize the Chrome WebDriver
    try:
        service = Service(ChromeDriverManager().install())
        driver = webdriver.Chrome(service=service, options=chrome_options)
    except Exception as e:
        print(f"Error initializing ChromeDriver: {e}")
        print("Trying alternative setup...")
        # Fallback: try without service specification
        driver = webdriver.Chrome(options=chrome_options)
    
    # Execute script to remove webdriver property
    driver.execute_script("Object.defineProperty(navigator, 'webdriver', {get: () => undefined})")
    
    return driver

def open_website(driver, url):
    """
    Open a website and wait for it to load
    """
    try:
        print(f"Opening website: {url}")
        driver.get(url)
        
        # Wait for the page to load completely
        WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.TAG_NAME, "body"))
        )
        
        print(f"Successfully opened {url}")
        print(f"Page title: {driver.title}")
        
        return True
        
    except Exception as e:
        print(f"Error opening website: {e}")
        return False

def main():
    """
    Main function to demonstrate Selenium usage
    """
    driver = None
    
    try:
        # Set up the Chrome driver
        print("Setting up Chrome WebDriver...")
        driver = setup_chrome_driver()
        
        # Example: Open a website (you can change this URL)
        website_url = "https://www.instagram.com"
        success = open_website(driver, website_url)
        
        if success:
            # Wait a few seconds to see the page
            print("Waiting 5 seconds to view the page...")
            time.sleep(5)
            
            # Example: Get page information
            print(f"Current URL: {driver.current_url}")
            print(f"Page source length: {len(driver.page_source)} characters")
            
            # Example: Find and interact with elements (uncomment to use)
            # search_box = driver.find_element(By.NAME, "q")
            # search_box.send_keys("Selenium automation")
            # search_box.submit()
            
        else:
            print("Failed to open the website")
            
    except Exception as e:
        print(f"An error occurred: {e}")
        
    finally:
        # Always close the browser
        if driver:
            print("Closing browser...")
            driver.quit()
            print("Browser closed successfully")

if __name__ == "__main__":
    main()
