from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support.ui import WebDriverWait
import time
import pandas as pd
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.keys import Keys
import csv
import json
from selenium.webdriver.support import expected_conditions as EC
import pandas as pd
from webdriver_manager.chrome import ChromeDriverManager

# for holding the resultant list
element_list = []*5
data = pd.read_csv("C:/Users/hetan/Downloads/Amazon Scrapping.csv")
Asin = data.loc[:,"Asin"]
country = data.loc[4:20]
for i in (Asin):

    page_url = 'https://www.amazon.de/dp/' + i
    driver = webdriver.Chrome(ChromeDriverManager().install())
    driver.get(page_url)

    try:
        # identify element
        title = driver.find_element_by_css_selector("#productTitle").text
        # prodDetails=driver.find_element_by_css_selector(by=By.CSS_SELECTOR, value="#detailBullets_feature_div > ul")
        # image_Url=driver.find_element_by_css_selector("#imgBlkFront").url
        # prodPrice=driver.find_element_by_css_selector(by=By.CSS_SELECTOR, value="#a-autoid-1-announce > span.a-color-base > span")
        table={"Title":title}


        element_list.append(table)
# NoSuchElementException thrown if not present
    except NoSuchElementException:
        table={"Title":"Null"}
        element_list.append(table)

    # price = driver.find_elements_by_class_name("price")
    # description = driver.find_elements_by_class_name("description")
    # rating = driver.find_elements_by_class_name("ratings")


print(element_list)
# df = pd.DataFrame(element_list)
# df.to_csv('table.csv')
json_object = json.dumps(element_list, indent=4)
# Writing to sample.json
with open("sample.json", "w") as outfile:
    outfile.write(json_object)
# closing the driver
driver.close()
