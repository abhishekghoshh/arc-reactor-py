from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
from bs4 import BeautifulSoup
import json


try:
  chrome_options = Options()
  value=[]
  link="http://192.168.0.1/"
  driver=webdriver.Chrome(r"chromedriver.exe",chrome_options=chrome_options)
  driver.get(link)
  driver.find_element_by_id("userName").send_keys("admin")
  driver.find_element_by_id("pcPassword").send_keys("admin")
  driver.find_element_by_id("loginBtn").click()
  frame1=driver.find_element_by_id("frame1")
  driver.switch_to.frame(frame1)
  driver.find_element_by_id('menu_arp').click()
  driver.find_element_by_id('menu_arplist').click()
  driver.switch_to_default_content()
  frame2=driver.find_element_by_id("frame2")
  driver.switch_to.frame(frame2)
  soup=BeautifulSoup(driver.page_source, 'lxml')
  rows=soup.find('table', id="arptbl").find_all("tr")
  for row in rows:
    datas=row.find_all('td')
    mac=datas[1].string
    ip=datas[2].string
    value.append({"ip":ip,"mac":mac})

  driver.close()
  with open("ipAndMac.json","w") as f:
      json.dump(value,f)
except Exception as e:
  print(e)
  driver.close()

