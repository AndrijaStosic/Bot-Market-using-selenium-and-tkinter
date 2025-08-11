from data import narudzbine
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException, NoSuchElementException
import atexit

driver = None

def pokreni_browser():
    global driver
    if driver is None:
        driver = webdriver.Chrome()
        driver.get("https://rahulshettyacademy.com/seleniumPractise/#/")
        driver.maximize_window()
        atexit.register(zatvori_browser)
    return driver

def zatvori_browser():
    global driver
    if driver:
        try:
            driver.quit()
            print("Browser zatvoren!")
        except Exception as e:
            print(f"Greska pri zatvaranju: {e}")
        finally:
            driver = None

def close_browser():
    zatvori_browser()

def ajmo():
    try:
        trenutni_driver = pokreni_browser()
        cekaj = WebDriverWait(trenutni_driver, 10)
        
        for proizvod, kolicina in narudzbine.items():
            search_box = cekaj.until(
                EC.element_to_be_clickable((By.XPATH, "//input[@placeholder='Search for Vegetables and Fruits']"))
            )
            search_box.clear()
            search_box.send_keys(proizvod)
            
            cekaj.until(
                EC.presence_of_element_located((By.XPATH, "//a[@class='increment']"))
            )

            kolicina = int(kolicina)
            for _ in range(kolicina - 1):
                plus_dugme = cekaj.until(
                    EC.element_to_be_clickable((By.XPATH, "//a[@class='increment']"))
                )
                plus_dugme.click()

            dodaj_dugme = cekaj.until(
                EC.element_to_be_clickable((By.XPATH, "//button[normalize-space()='ADD TO CART']"))
            )
            dodaj_dugme.click()

        korpa_ikona = cekaj.until(
            EC.element_to_be_clickable((By.XPATH, "//img[@alt='Cart']"))
        )
        korpa_ikona.click()
        
        nastavi_dugme = cekaj.until(
            EC.element_to_be_clickable((By.XPATH, "//button[normalize-space()='PROCEED TO CHECKOUT']"))
        )
        nastavi_dugme.click()

        poruci_dugme = cekaj.until(
            EC.element_to_be_clickable((By.XPATH, "//button[normalize-space()='Place Order']"))
        )
        poruci_dugme.click()

        dropdown = cekaj.until(
            EC.presence_of_element_located((By.XPATH, "//div[@class='wrapperTwo']//div//select"))
        )
        select = Select(dropdown)
        select.select_by_visible_text("Serbia")

        checkbox = cekaj.until(
            EC.element_to_be_clickable((By.XPATH, "//input[@type='checkbox']"))
        )
        checkbox.click()
        
        finalno_dugme = cekaj.until(
            EC.element_to_be_clickable((By.XPATH, "//button[normalize-space()='Proceed']"))
        )
        finalno_dugme.click()

        print("Uspesno naruceno!")
        
    except TimeoutException as e:
        print(f"Timeout greska: {e}")
    except NoSuchElementException as e:
        print(f"Element nije pronadjen: {e}")
    except Exception as e:
        print(f"Doslo je do greske: {e}")
    finally:
        narudzbine.clear()

if __name__ == "__main__":
    try:
        ajmo()
    finally:
        zatvori_browser()
