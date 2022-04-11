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
import pandas as pd
from webdriver_manager.chrome import ChromeDriverManager

data = pd.read_csv("C:/Users/hetan/Downloads/1.csv")

Asin = data.loc[:,"Asin"]
country = data.loc[4:20]

driver = webdriver.Chrome(ChromeDriverManager().install())
driver = webdriver.Chrome (executable_path= "C:/Users/hetan/Desktop/chromedriver.exe")
#driver.get('https://www.amazon.de/dp/000103863X')
for i in Asin:
    driver.get('https://www.amazon.de/dp/' + i)

driver.implicitly_wait(10)
r = 1
templist = []*20
while(r<=19):
    if ( driver.find_element(by=By.XPATH, value='//*[@id="l"]').text):
        Table_dict = {'Title': "NULL",
                  # 'product_image':product_image,
                  # 'product_price':product_price,
                  'product_detail': "NULL"}
        templist.append(Table_dict)
        r += 1
        print(Table_dict)
    else:
        title = driver.find_element(by=By.XPATH, value='//*[@id="productTitle_div/div/"]/html/body/div[2]/div[2]/div[3]/div[1]/div[7]/div[2]').text
    # product_image = driver.find_element(by=By.XPATH, value='//*[@id="imgBlkFront"]').href
    # product_price = driver.find_element(by=By.XPATH, value='//*[@id="booksHeaderSection"]/div/ul/lidiv[2]').text
        product_detail_de = "\nPublisher:" + driver.find_element(by=By.XPATH,value='//*[@id="detailBullets_feature_div"]/ul/li/span/span[2]').text + \
    "\nLanguage:" + driver.find_element(by=By.XPATH,value='//*[@id="detailBullets_feature_div"]/ul/li[2]/span').text + \
    "\nMusic Sheet: " + driver.find_element(by=By.XPATH,value='//*[@id="detailBullets_feature_div"]/ul/li[3]/span/span').text + \
                                "\nISBN-10: " + driver.find_element(by=By.XPATH,
                                                                    value='//*[@id="detailBullets_feature_div"]/ul/li[4]/span/span').text + \
                                "\nISBN-13: " + driver.find_element(by=By.XPATH,
                                                                    value='//*[@id="detailBullets_feature_div"]/ul/li[5]/span/span').text

        Table_dict = {'Title':title,
              #'product_image':product_image,
               # 'product_price':product_price,
                'product_detail':product_detail_de }
        templist.append(Table_dict)
        print(templist)
        print(Table_dict)

        r += 1
print(r)
# saving the dataframe to a csv
df = pd.DataFrame(templist)
df.to_csv('table.csv')
driver.close()
'''# Data to be written
# Serializing json
json_object = json.dumps(Table_dict, indent=4)

# Writing to sample.json
with open("sample.json", "w") as outfile:
    outfile.write(json_object)'''