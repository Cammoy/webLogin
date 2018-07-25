'''
Created on 24 Jul 2018

@author: Mary
'''
#open a login page
#fill in fields 'username' and 'password'
#validate if login was successful or not

from selenium import webdriver
from selenium.common.exceptions import TimeoutException

def choice1():
    login_page = "http://www.facebook.com"
    givenUsername = input("Please enter username: ")
    givenPassword = input("Please enter password: ")
    
    browser = webdriver.Firefox()
    browser.get( login_page )
    
    username = browser.find_element_by_id( "email" )
    password = browser.find_element_by_name( "pass" )
    submit = browser.find_element_by_id( "u_0_2" )

    #the submit id may change depending on how many tabs have been opened previously
    #keep on '2' for now
    
    username.send_keys(givenUsername)
    password.send_keys(givenPassword)

    submit.click()

    wait = WebDriverWait(browser, 5)

    try:
        page_loaded = wait.until_not(
            lambda browser: browser.current_url == login_page
        )

    except TimeoutException:
        self.fail( "Loading timeout expired" )
  
    self.assertEqual(
        browser.current_url,
        correct_page,
        msg = "Successful Login"
    )


def choice2():
    login_page = "https://twitter.com/Twitter?ref_src=twsrc%5Egoogle%7Ctwcamp%5Eserp%7Ctwgr%5Eauthor"
    givenUsername = input("Please enter username: ")
    givenPassword = input("Please enter password: ")
    
    browser = webdriver.Firefox()
    browser.get( login_page )
    
    username = browser.find_element_by_name("session[username_or_email]" )
    password = browser.find_element_by_name('session[password]')
    submit = browser.find_element_by_css_selector('input[type="submit"]')

    username.send_keys(givenUsername)
    password.send_keys(givenPassword)
    
    submit.click()

    wait = WebDriverWait(browser, 5)

    try:
        page_loaded = wait.until_not(
            lambda browser: browser.current_url == login_page
        )

    except TimeoutException:
        self.fail( "Loading timeout expired" )
  
    self.assertEqual(
        browser.current_url,
        correct_page,
        msg = "Successful Login"
    )
    
def choice3():
    login_page = "https://www.instagram.com/accounts/login/?hl=en"
    givenUsername = input("Please enter username: ")
    givenPassword = input("Please enter password: ")

    browser = webdriver.Firefox()
    browser.get( login_page )

    username = browser.find_element_by_id( "f14e9e191af58" )
    password = browser.find_element_by_id( "f30c4377c58658" )
    submit = browser.find_element_by_id( "_5f5mN jIbKX KUBKM pm766" )
    
    username.send_keys(givenUsername)
    password.send_keys(givenPassword)

    submit.click()

    wait = WebDriverWait(browser, 5)

    try:
        page_loaded = wait.until_not(
            lambda browser: browser.current_url == login_page
        )

    except TimeoutException:
        self.fail( "Loading timeout expired" )
  
    self.assertEqual(
        browser.current_url,
        correct_page,
        msg = "Successful Login"
    )
    

print("What website would you like to log in to?")
choice = int(input("1) Facebook, 2) Gmail, 3) Instagram "))

if choice == 1:
    choice1()
elif choice == 2:
    choice2()
elif choice == 3:
    choice3()
else:
    print("Invalid input")

#can't get password done for gmail
#can't get id for instagram
