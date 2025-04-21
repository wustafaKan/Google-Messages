from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException, NoSuchElementException
import logging
import time

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

options = webdriver.ChromeOptions()
options.add_argument("--start-maximized")


logging.info("WebDriver ayarları oluşturuldu.")


driver = webdriver.Chrome(options=options)


logging.info("WebDriver oluşturuldu.")


driver.get("https://messages.google.com/web/authentication")


logging.info("Google Messages web sitesine gidildi.")

try:

    buton = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//*[@id='mat-mdc-slide-toggle-0-button']")))
    buton.click()

    logging.info("Butona tıklandı.")
except TimeoutException:

    logging.error("Butona tıklanamadı.")
    driver.quit()

try:

    WebDriverWait(driver, 60).until(EC.url_to_be("https://messages.google.com/web/conversations"))
 
    logging.info("QR kodu okutuldu.")
except TimeoutException:

    logging.error("QR kodu okutulamadı.")
    driver.quit()


try:
  
    ben_span = WebDriverWait(driver, 10).until(EC.presence_of_all_elements_located((By.XPATH, "//span[@data-e2e-conversation-name='']")))
    for span in ben_span:
        if span.text == "Ben":
            span.click()
  
            logging.info("Sohbet başlatıldı.")
            time.sleep(2)
            break
    else:
     
        logging.error("Ben metni olan span etiketi bulunamadı.")
except TimeoutException:
  
    logging.error("Sohbet başlatılamadı.")
    driver.quit()


try:
    mesaj_input = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//textarea[@placeholder='Mesajlaşma']")))
    mesaj_input.click()
   
    logging.info("Mesaj input alanına tıklandı.")
    

    mesaj_metni = "Merhaba, nasılsınız?"
    

    mesaj_input.send_keys(mesaj_metni)

    logging.info("Mesaj input alanına mesaj metni yapıştırıldı.")

    mesaj_input.send_keys("\n")

    logging.info("ENTER tuşuna basıldı.")
except TimeoutException:

    logging.error("Mesaj gönderilemedi.")
    driver.quit()
