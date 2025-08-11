from data import narudzbine
import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

service = Service(r"C:\Users\StoshkicPC\Desktop\ok\chromedriver.exe")
driver = webdriver.Chrome(service=service)
driver.get("https://rahulshettyacademy.com/seleniumPractise/#/")

time.sleep(2)

def ajmo():
    for product, quantity in narudzbine.items():
        search_box = driver.find_element(By.XPATH, "//input[@placeholder='Search for Vegetables and Fruits']")
        search_box.clear()
        search_box.send_keys(product)
        time.sleep(1)

        broj = 1
        quantity = int(quantity)
        while broj < quantity:
            driver.find_element(By.XPATH, "//a[@class='increment']").click()
            broj += 1

        driver.find_element(By.XPATH, "//button[normalize-space()='ADD TO CART']").click()
        time.sleep(1)

    driver.find_element(By.XPATH, "//img[@alt='Cart']").click()
    time.sleep(1)
    driver.find_element(By.XPATH, "//button[normalize-space()='PROCEED TO CHECKOUT']").click()
    time.sleep(2)

    driver.find_element(By.XPATH, "//button[normalize-space()='Place Order']").click()
    time.sleep(2)

    dropdown_element = driver.find_element(By.XPATH, "//div[@class='wrapperTwo']//div//select")
    select = Select(dropdown_element)
    select.select_by_visible_text("Serbia")

    driver.find_element(By.XPATH, "//input[@type='checkbox']").click()
    driver.find_element(By.XPATH, "//button[normalize-space()='Proceed']").click()

    print("Ordered successfully!")

if __name__ == "__main__":
    ajmo()
