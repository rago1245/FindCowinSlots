from selenium import webdriver
import time
from datetime import datetime

driver = webdriver.Chrome()
#driver.get('https://www.cowin.gov.in/home')
driver.get('https://selfregistration.cowin.gov.in/')
time.sleep(10)
mobileNumberEditBox = driver.find_element_by_xpath('//*[@id="mat-input-0"]')
mobileNumberEditBox.send_keys('9764547977')
OTPButton = driver.find_element_by_xpath('//*[@id="main-content"]/app-login/ion-content/div/ion-grid/ion-row/ion-col/ion-grid/ion-row/ion-col[1]/ion-grid/form/ion-row/ion-col[2]/div/ion-button')
OTPButton.click()
time.sleep(30)
pinCodeList = [ "443101","425306"]

driver.set_window_size(1024, 450)
driver.maximize_window()
driver.execute_script("window.scrollTo(0, 200)") 
for x in range(2): 
    pincodeserachbox = driver.find_element_by_xpath('//*[@id="mat-input-2"]')
    for pinCode in pinCodeList:
        print(pinCode)
        pincodeserachbox.clear()
        pincodeserachbox.send_keys(pinCode)

        #SelectSearchType = driver.find_element_by_xpath('/html/body/app-root/div/app-home/div[2]/div/appointment-table/div/div/div/div/div/div/div/div/div/div/div[2]/form/div/div/div[1]/div/label/div')
        #SelectSearchType.click()

        #distserachboxstate = driver.find_element_by_xpath('//*[@id="mat-select-value-1"]/span')
        #distserachboxstate. ("Maharashtra")

        searchbutton = driver.find_element_by_xpath('//*[@id="main-content"]/app-appointment-table/ion-content/div/div/ion-grid/ion-row/ion-grid/ion-row/ion-col/ion-grid/ion-row/ion-col[2]/form/ion-grid/ion-row/ion-col[3]/ion-button')
        searchbutton.click()
        time.sleep(0.5)
        select_18 = driver.find_element_by_xpath('//*[@id="flexRadioDefault1"]')
        select_18.click()
        now = datetime.now()
        dt_string = now.strftime("%d%m%Y%H%M%S")
        fileName = "F:\CowinScreenShot\pageImage_" + pinCode + "_18_" + dt_string + ".png"
        print(fileName)
        driver.save_screenshot(fileName)

        #time.sleep(5)
        #select_45 = driver.find_element_by_xpath('//*[@id="flexRadioDefault3"]')
        #select_45.click()
        #now1 = datetime.now()
        #dt_string1 = now1.strftime("%d%m%Y%H%M%S")
        #fileName = "F:\CowinScreenShot\pageImage_" + pinCode + "_45_" + dt_string1 + ".png"
        #driver.save_screenshot(fileName)

        time.sleep(5)

    time.sleep(5)    
    #driver.refresh()



