from selenium import webdriver
import webbrowser
import time

def nextButton(id):
    tempArr=id.split('_')
    tempNum=int(tempArr[1])
    tempNum+=1
    if tempNum>3:
        tempNum%=3
    id=tempArr[0]+'_'+str(tempNum)
    return id

driver = webdriver.Chrome("C:/webdrivers/chromedriver")
driver.get("http://127.0.0.1:3000/index.html")
time.sleep(2)
id='button_1'
for i in range(6):
    driver.execute_script(f'document.getElementById("{id}").style.border="thick solid black"')
    time.sleep(2)
    # button = driver.find_element_by_id(id)
    # button.click()
    driver.execute_script(f'document.getElementById("{id}").style.border="none"')
    id=nextButton(id)