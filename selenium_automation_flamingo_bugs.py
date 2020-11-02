import time
from selenium.common.exceptions import ElementNotInteractableException
from selenium.webdriver.common.action_chains import ActionChains
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from xvfbwrapper import Xvfb
import argparse
import warnings
import random  
warnings.simplefilter("ignore")

# In[2]:


def browse_computers(conn):
    opts = webdriver.FirefoxOptions()
    opts.headless = True
    driver = webdriver.Firefox(options=opts)
    try:
        print("executing browse_computers")
        driver.get(conn)

        driver.find_element_by_xpath("//li[4]/a").click()
        driver.find_element_by_xpath("//li[4]/div/a").click()
        
        driver.find_element_by_css_selector('.col-lg-3:nth-child(4) .mask').click()
        
        elem = driver.find_element_by_name("deliveryCode")
        hover = ActionChains(driver).move_to_element(elem)
        hover.perform()
        elem.click()

        driver.find_element_by_css_selector('.clearfix').click()

        driver.find_element_by_css_selector('.active > .nav-link').click()

    except Exception as e:
        print('error in browse_computers\n' + str(e) )
    
    driver.quit()

def browse_headphones(conn):
    opts = webdriver.FirefoxOptions()
    opts.headless = True
    driver = webdriver.Firefox(options=opts)
    try:
        print("executing browse_headphones")
        driver.get(conn)

        driver.find_element_by_xpath("//li[2]/a").click()
        driver.find_element_by_xpath("//li[2]/div/a").click()
        
        driver.find_element_by_css_selector('.col-lg-3:nth-child(6) .mask').click()
        
        elem = driver.find_element_by_name("deliveryCode")
        hover = ActionChains(driver).move_to_element(elem)
        hover.perform()
        elem.click()

        driver.find_element_by_css_selector('.clearfix').click()

        driver.find_element_by_css_selector('.active > .nav-link').click()

    except Exception as e:
        print('error in browse_headphones\n' + str(e) )
    
    driver.quit()
    

def browse_clothing(conn):
    opts = webdriver.FirefoxOptions()
    opts.headless = True
    driver = webdriver.Firefox(options=opts)
    try:
        print("executing browse_clothing")
        driver.get(conn)

        driver.find_element_by_xpath("//li[3]/a").click()
        driver.find_element_by_xpath("//li[3]/a").click()
        
        driver.find_element_by_css_selector('.col-lg-3:nth-child(2) .mask').click()
        
        elem = driver.find_element_by_name("deliveryCode")
        hover = ActionChains(driver).move_to_element(elem)
        hover.perform()
        elem.click()

        driver.find_element_by_css_selector('.clearfix').click()

        driver.find_element_by_css_selector('.active > .nav-link').click()

    except Exception as e:
        print('error in browse_clothing\n' + str(e) )
    
    driver.quit()


def place_order(conn):
    
    
    opts = webdriver.FirefoxOptions()
    opts.headless = True
    driver = webdriver.Firefox(options=opts)
    try:
        print("executing place_order")
        driver.get(conn)
        elem = driver.find_element_by_css_selector('.col-lg-3:nth-child(2) .mask')
        hover = ActionChains(driver).move_to_element(elem)
        hover.perform()

        driver.find_element_by_css_selector('.col-lg-3:nth-child(2) .mask').click()

        driver.find_element_by_css_selector('.btn-primary:nth-child(2)').click()

        driver.find_element_by_xpath("//h6/a").click()
        
        elem = driver.find_element_by_name("deliveryCode")
        hover = ActionChains(driver).move_to_element(elem)
        hover.perform()
        elem.click()
        
        
        elem = driver.find_element_by_css_selector(".btn-primary")
        hover = ActionChains(driver).move_to_element(elem)
        hover.perform()
        elem.click()
        
        
        elem = driver.find_element_by_css_selector(".btn-primary")
        hover = ActionChains(driver).move_to_element(elem)
        hover.perform()
        elem.click()
        
        driver.find_element_by_id("billingAddress.firstname").send_keys('Muhammad')  
        driver.find_element_by_id("billingAddress.lastname").send_keys('Asad')
        driver.find_element_by_id("billingAddress.street").send_keys('angelic')
        driver.find_element_by_id("billingAddress.postCode").send_keys('12345')
        driver.find_element_by_id("billingAddress.city").send_keys('Canada')
        driver.find_element_by_id("billingAddress.email").send_keys('abc@123.com')
        
        driver.find_element_by_css_selector('.custom-checkbox > .custom-control-label').click()
        
        driver.find_element_by_css_selector('.custom-control:nth-child(3) > .custom-control-label').click()
        
    except Exception as e:  
        print('error in browse_computers\n' + str(e) )
    driver.quit()
    


# In[7]:


def search_computers(conn):
    
    opts = webdriver.FirefoxOptions()
    opts.headless = True
    driver = webdriver.Firefox(options=opts)
    try:
        driver.get(conn)
        print("executing search_computers")
        #driver.open('/en/')
        time.sleep(2)
        elem = driver.find_element_by_name('q')
        elem.click()
        elem.send_keys('computer')
        elem.submit()
        time.sleep(2)
        
    except Exception as e:
        print('error in search_computers\n' + str(e) )
    driver.quit()
    
    
def search_headphones(conn):
    
    opts = webdriver.FirefoxOptions()
    opts.headless = True
    driver = webdriver.Firefox(options=opts)
    try:
        driver.get(conn)
        print("executing search_headphones")
        #driver.open('/en/')
        time.sleep(2)
        elem = driver.find_element_by_name('q')
        elem.click()
        elem.send_keys('headphones')
        elem.submit()
        time.sleep(2)

    except Exception as e:
        print('error in search_headphones\n' + str(e) )
    driver.quit()
    
def search_clothing(conn):
    
    opts = webdriver.FirefoxOptions()
    opts.headless = True
    driver = webdriver.Firefox(options=opts)
    try:
        driver.get(conn)
        print("executing search_clothing")
        #driver.open('/en/')
        time.sleep(2)
        elem = driver.find_element_by_name('q')
        elem.click()
        elem.send_keys('clothing')
        elem.submit()
        time.sleep(2)
        
    except Exception as e:
        print('error in search_clothing\n' + str(e) )
    driver.quit()


#getting commandline arguments
parser = argparse.ArgumentParser()
parser.add_argument('--host', help='hostname of host on which application is running e.g http://127.0.0.1', required=True)
parser.add_argument('--port', help='port on which application is running i.e 8080', required=True)
args = parser.parse_args()
host = args.host
#host = 'http://127.0.0.1'
#port = '3210'
port = args.port
conn = host + ':' + port + '/' 
i = 0
functions = [search_computers, search_headphones, search_clothing, browse_computers, browse_headphones, browse_clothing, place_order]


prob = [0.3, 0.3, 0.4, 0, 0, 0, 0]

while 1==1:
    
    print(i)
    
    random.choices(functions, prob)[0](conn)

    i +=1
