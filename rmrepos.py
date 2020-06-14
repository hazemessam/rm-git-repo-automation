from selenium import webdriver
from time import sleep
from getpass import getpass
from os import system, remove
from sys import exit


open('targetrepos.txt', 'w').close()
system('targetrepos.txt')

username = input('> Username: ')
password = getpass('> Password: ')

# option = webdriver.ChromeOptions()
# option.add_argument('headless')
driver = webdriver.Chrome()
driver.maximize_window()
driver.get('https://github.com/login')

username_inp = driver.find_element_by_xpath('//*[@id="login_field"]')
username_inp.send_keys(username)
password_imp = driver.find_element_by_xpath('//*[@id="password"]')
password_imp.send_keys(password)
signin_btn = driver.find_element_by_xpath('//*[@id="login"]/form/div[4]/input[9]')
signin_btn.click()

file = None
try:
    file = open('targetrepos.txt', 'r')
except:
    print("Can't open reposlist.txt!")
    file.close()
    exit()

success = True
try:   
    for repo in file:
        if repo.startswith('#'):
            continue
        fullname = repo.strip()
        driver.get(f'https://github.com/{fullname}/settings')

        del_link = driver.find_element_by_xpath('//*[@id="options_bucket"]/div[9]/ul/li[4]/details/summary')
                                                
        del_link.click()

        reponame_inp = driver.find_element_by_xpath('//*[@id="options_bucket"]/div[9]/ul/li[4]/details/details-dialog/div[3]/form/p/input')
        reponame_inp.send_keys(fullname)
        sleep(1)
        del_btn = driver.find_element_by_xpath('//*[@id="options_bucket"]/div[9]/ul/li[4]/details/details-dialog/div[3]/form/button')
        del_btn.click()
        sleep(1)
except Exception as e:
    print(e)
    success = False
finally:
    file.close()
    remove('targetrepos.txt')
    remove('reposlist.txt')
    
if success:
    print('All done!')
    sleep(2)
    driver.close()

