from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time
def getSchedule(CRNS, username, password, term):
    try:
        campus = "Urbana-Champaign"
        regTerm = term + " - " + campus

        driver = webdriver.Chrome("chromedriver")
        driver.implicitly_wait(10)

        # go to self service
        driver.get("https://apps.uillinois.edu/selfservice/")

        #press uiuc
        driver.find_element(By.XPATH, "/html/body/form/div[3]/div/div/div/header/div[3]/div[2]/div[2]/div[2]/div/div/div/div[2]/a").click()


        #put in username and password
        driver.find_element("id", "netid").send_keys(username)
        driver.find_element("id", "easpass").send_keys(password)
        driver.find_element("name", "BTN_LOGIN").click()

        driver.find_element(By.XPATH, "//*[contains(text(), 'Registration & Records')]").click()

        driver.find_element(By.XPATH, "//*[contains(text(), 'Enhanced Registration')]").click()

        driver.switch_to.window(driver.window_handles[1])

        driver.find_element("id", "registerLink").click()

        driver.find_element("id", "s2id_txt_term").click()

        driver.find_element("id", "s2id_autogen1_search").send_keys(regTerm)
        time.sleep(1)
        driver.find_element("id", "s2id_autogen1_search").send_keys(Keys.RETURN)
        driver.find_element("id", "term-go").click()


        driver.find_element("id", "enterCRNs-tab").click()
        for CRN in CRNS:
            driver.find_element("id", "txt_crn1").send_keys(CRN)
            driver.find_element("id", "addCRNbutton").click()
            time.sleep(1)

        driver.find_element("id", "saveButton").click()
        
        print("Attempted to register for CRNS: ", CRNS)
        print()
        print("There may be some errors, these are usually safe to ignore")
        print()
        
        try:
            driver.find_element(By.XPATH, "//*[contains(text(), 'Errors Preventing Registration')]")
            return(0)
        except:
            return(1)
        
    except:
        return(-1)
