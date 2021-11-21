from selenium import webdriver
import webbrowser
import time

def nextButton(id):
    tempArr=id.split('_')
    tempNum=int(tempArr[1])
    tempNum+=1
    if tempNum>5:
        tempNum%=5
    id=tempArr[0]+'_'+str(tempNum)
    return id

driver = webdriver.Chrome("D:/webdriver/chromedriver")
driver.get("http://127.0.0.1:5501/index.html")
time.sleep(2)
id='button_1'
for i in range(6):
    driver.execute_script(f'document.getElementById("{id}").style.cssText="color: #000000;background-color: #d9cab3;transition: all 1000ms ease;cursor: pointer;"')
    time.sleep(2)
    # button = driver.find_element_by_id(id)
    # button.click()
    driver.execute_script(f'document.getElementById("{id}").style.cssText="color: white;background-color: black"')
    id=nextButton(id)