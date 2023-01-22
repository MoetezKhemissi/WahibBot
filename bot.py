from selenium import webdriver
from selenium_stealth import stealth
from selenium.webdriver.common.by import By
import time
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities


def changevalue(field,value):
    field.click()
    field.clear()
    field.send_keys(value)
    human_delay()
def human_delay():
    time.sleep(1)
def fire_up_chrom_and_go_to(url):
    caps = DesiredCapabilities().CHROME
    #not wait for full load
    caps["pageLoadStrategy"] = "eager" 
    options = webdriver.ChromeOptions()
    options.add_argument("start-maximized")
    options.add_experimental_option("excludeSwitches", ["enable-automation"])
    options.add_experimental_option('useAutomationExtension', False)
    driver = webdriver.Chrome(desired_capabilities=caps,options=options, executable_path=r"C:\Users\Moetez\Desktop\LaTeX-OCR\Count_probability\chromedriver.exe")

    stealth(driver,
            languages=["en-US", "en"],
            vendor="Google Inc.",
            platform="Win32",
            webgl_vendor="Intel Inc.",
            renderer="Intel Iris OpenGL Engine",
            fix_hairline=True,
            )

    url = "https://bot.incolumitas.com/#botChallenge"
    driver.get(url)
    return driver



#------------------MAIN----------------------------
driver=fire_up_chrom_and_go_to("https://bot.incolumitas.com/#botChallenge")

#input username
username = driver.find_element(By.XPATH,"//*[@id='userNameField']/div/input")
changevalue(username,"imed")

#input Email
email = driver.find_element(By.XPATH,"//*[@id='emailField']/div/input")
changevalue(email,"imed@gmail.com")

#input Cookies
cookies = driver.find_element(By.XPATH,"//*[@id='formStuff']/div[3]/div/div/select")
cookies.click()
select = Select(cookies)
select.select_by_visible_text("I want all the Cookies")
human_delay()

#click agree to terms
terms = driver.find_element(By.XPATH,"//*[@id='formStuff']/div[4]/div/label/input")
terms.click()
human_delay()

#BigCat
cats = driver.find_element(By.XPATH,"//*[@id='bigCat']")
cats.click()
human_delay()

#Submit form 
submit=driver.find_element(By.XPATH,"//*[@id='submit']")
submit.click()


time.sleep(50)
driver.quit()