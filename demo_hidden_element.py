import time
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager

class DemoHiddenElements():
    def demo_is_displayed(self):
        driver = webdriver.Chrome(executable_path=ChromeDriverManager().install())
        driver.get("https://www.w3schools.com/howto/howto_js_toggle_hide_show.asp")
        elem = driver.find_element_by_xpath("//div[@id='myDIV']").is_displayed()
        print(elem)
        driver.find_element_by_xpath( "//button[@class='ws-btn w3-hover-black w3-dark-grey']").click()
        elem = driver.find_element_by_xpath("//div[@id='myDIV']").is_displayed()
        print(elem)

    def demo_is_displayed_yatra(self):
        driver = webdriver.Chrome(executable_path=ChromeDriverManager().install())
        driver.get("https://www.yatra.com/hotels")
        driver.find_element_by_xpath("(//label[normalize-space()='Traveller and Hotel'])[1]").click()
        time.sleep(2)
        driver.find_element_by_xpath("//div[@class='hotel_passengerBox dflex relative']//div[3]//div[1]//div[1]//span[2]")
        time.sleep(2)
        elem = driver.find_element_by_xpath("//select[@class='ageselect']").is_displayed()
        print(elem)
        driver.find_element_by_xpath("//div[@class='hotel_passengerBox dflex relative']//div[3]//div[1]//div[1]//span[1]").click()
        print(elem)


demoDisplayed = DemoHiddenElements()
#Displayed.demo_is_displayed()
demoDisplayed.demo_is_displayed_yatra()