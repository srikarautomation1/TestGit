import time
from selenium import webdriver
from selenium.webdriver.support.select import Select

"""
1) Verify all lables are displayed
2) click on the button to submit
3) get the header text and compare with the expected text
4. testing git file update
5.... test git
6... test branch 1 code
7... asdfsfsdf
8.. new line 1
9..test new 2
10. test new 3
"""
driver = webdriver.Chrome(executable_path="../exeFiles/chromedriver.exe")
try:
    url = "https://www.seleniumeasy.com/test/input-form-demo.html"
    driver.get(url)
    driver.maximize_window()
    time.sleep(4)
    time.sleep(6)
    time.sleep(8)
    try:
        driver.find_element_by_css_selector("a#at-cv-lightbox-close").click()
    except:
        print("no alert so handling it using except block")
    fnBool = driver.find_element_by_xpath("//label[text()='First Name']").is_displayed()
    lnBool = driver.find_element_by_xpath("//label[text()='Last Name']").is_displayed()

    print("first name Label : "+str(fnBool))
    print("last name Label : "+str(lnBool))

    driver.find_element_by_name("first_name").send_keys("cfName")
    driver.find_element_by_name("last_name").send_keys("clName")

    driver.find_element_by_name("email").send_keys("cfclName@g.com")
    driver.find_element_by_name("phone").send_keys("12345678")
    addLoc = driver.find_element_by_name("address")
    addLoc.send_keys("address One")

    driver.find_element_by_name("city").send_keys("Hyd")

    stateLoc = driver.find_element_by_name("state")
    select_state = Select(stateLoc)
    select_state.select_by_visible_text("Alaska")

    driver.find_element_by_name("zip").send_keys("30030")
    driver.find_element_by_xpath("//label[normalize-space()='Yes']").click()

    driver.find_element_by_name("comment").send_keys("Proj Desc")
    time.sleep(6)
    driver.get_screenshot_as_file("screenshot1.png")

except:
    print("error in the execution")  # some code it will report the defect
finally:
    driver.close()
