from selenium import webdriver
import time

# firefox_options = webdriver.FirefoxOptions()
# prefs = {'download.default_directory': './'}
# firefox_options.add_experimental_option('prefs', prefs)
# driver = webdriver.Firefox(options=firefox_options)

from selenium.webdriver.firefox.service import Service
from webdriver_manager.firefox import GeckoDriverManager
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options


def savefile_chrome(url):
    # Specify the directory where you want to save the downloaded files
    download_dir = "/Users/nafisneehal/Desktop/Mojnu-Bengali-GPT/"  # Change this to your desired path

    chrome_options = Options()
    chrome_options.add_experimental_option("prefs", {
        "download.default_directory": download_dir,
        "download.prompt_for_download": False,  # Disable download prompt
        "download.directory_upgrade": True,
        "safebrowsing.enabled": True,  # Enable Safe Browsing to bypass the warning on certain file types
        "plugins.always_open_pdf_externally": True,  # Automatically download PDFs
        "profile.default_content_settings.popups": 0,  # Disable pop-ups
        "safebrowsing.disable_download_protection": True,  # Disable download protection
        "profile.content_settings.exceptions.automatic_downloads.*.setting": 1
    })

    # Initialize the WebDriver
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=chrome_options)

    # Navigate to the webpage that contains the file to download
    driver.get(url)  # Change this URL to the page with your file

    # If the download doesn't start automatically, you may need to click the download link/button
    # Replace 'xpath_to_download_link' with the actual XPath to the download link on the webpage
    # driver.find_element(By.XPATH, 'xpath_to_download_link').click()

    # Wait for the download to finish (consider using a more explicit waiting mechanism)
    time.sleep(10)  # Example: wait for 10 seconds for the download to complete

    # Quit the driver
    driver.quit()

#url2 = "https://file-examples.com/wp-content/storage/2017/11/file_example_WAV_1MG.wav"
def savefile_firefox(url):

    # Specify your download directory here
    #download_dir = "/Users/nafisneehal/Desktop/Mojnu-Bengali-GPT/"  # Change this to your desired path
    download_dir = "./"

    # Set additional options for the WebDriver
    options = Options()

    # # Set up the Firefox profile with your desired settings
    # options.set_preference("browser.download.folderList", 2)  # Use custom download location
    # options.set_preference("browser.download.manager.showWhenStarting", False)
    # options.set_preference("browser.download.dir", download_dir)
    # options.set_preference("browser.helperApps.neverAsk.saveToDisk", "audio/wav, audio/x-wav")

    # Set Firefox preferences to automate file downloads
    profile = webdriver.FirefoxProfile()
    profile.set_preference("browser.download.folderList", 2)  # 0: desktop, 1: downloads, 2: custom location
    profile.set_preference("browser.download.manager.showWhenStarting", False)  # Don't show download manager when starting a download
    profile.set_preference("browser.download.dir", download_dir)  # Set the custom download directory
    profile.set_preference("browser.helperApps.neverAsk.saveToDisk", "audio/wav")  # MIME type
    # Add more MIME types as needed, e.g., "application/pdf, application/x-rar-compressed, application/octet-stream"

    # Initialize the WebDriver with the specified options
    driver = webdriver.Firefox(service=Service(GeckoDriverManager().install()), firefox_profile = profile)
    #driver = webdriver.Firefox()

    # Navigate to the webpage with the file to download
    driver.get(url)  # Change this URL to your file's location

    # If the download doesn't start automatically, click the download link/button
    # driver.find_element(By.XPATH, 'xpath_to_download_link').click()  # Update the selector as needed

    # Wait for the download to finish (consider implementing a more reliable wait mechanism)
    driver.implicitly_wait(10)  # Adjust the wait time as necessary

    # Quit the driver
    driver.quit()


# url2 = "https://file-examples.com/wp-content/storage/2017/11/file_example_WAV_1MG.wav"
# def try_firefox(url):
#     fp = webdriver.FirefoxProfile()
#     fp.set_preference("browser.download.folderList", 2)
#     fp.set_preference("browser.download.manager.showWhenStarting", True)
#     fp.set_preference("browser.download.dir", "/Users/nafisneehal/Desktop/Mojnu-Bengali-GPT/")
#     fp.set_preference("browser.helperApps.neverAsk.saveToDisk", "audio/wav")
#     driver = webdriver.Firefox(firefox_profile=fp)
#     driver.implicitly_wait(10)
#     driver.get(url)
#     driver.quit()

#try_firefox(url2)
#savefile_firefox(url2)