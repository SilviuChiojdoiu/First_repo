# Locators in Selenium Python
import time

from selenium import webdriver
from selenium.webdriver.common.by import By

'''
ID (Syntax: find_element_by_id (“test”)
Name (Syntax: find_element_by_name (“software”)
Class Name (Syntax: find_element_by_class_name (“test-auto”)
Tag Name (Syntax: find_element_by_tag_name (“input”)
Link Text (Syntax: find_element_by_link_text (“Selenium Python”)
Partial Link Text (Syntax: find_element_by_partial_link_text (“Selenium”)
CSS Selector
XPath
'''


# ID

chrome_page = webdriver.Chrome() # Chrome este clasa din pachetul Selenium
chrome_page.get("https://the-internet.herokuapp.com/login") # asa accesam pagina html dorita
# time.sleep(5) # asa oprim vizualizarea paginii web timp de 10 secunde sau cate secunde dorim

chrome_page.find_element(By.ID,"username").send_keys('admin') # tiparim admin in caseta username a paginii

chrome_page.find_element(By.ID, "password").send_keys('admin')
time.sleep(2)

chrome_page.find_element(By.TAG_NAME,"button").click()
time.sleep(2)

chrome_page.find_element(By.LINK_TEXT, "Elemental Selenium").click()
time.sleep(5)

# chrome_page.quit() # inchide toata instanta browser-ului . Asta dupa ce testul a fost rulat.
# chrome_page.close() # inchide un singur tab (cel avtiv din instanta de browser)








