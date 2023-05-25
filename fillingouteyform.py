from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from time import sleep
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
from DataValues import *

options = Options()
options.add_experimental_option('detach', True)
options.add_argument("disable-infobars")
web = webdriver.Chrome()
driver = web
web.get("https://eyglobal.yello.co/external/requisitions/ZBiANni_-QlWFXiJl0Ld5A/apply?locale=en")

# first page
sleep(1)
element = web.find_element(By.XPATH, '//*[@id="cookie-banner-button"]')
element.click()
sleep(1)
element = web.find_element(By.XPATH, "//a[contains(text(), 'User Login')]")
element.click()

# second page
sleep(1)
element = web.find_element(By.XPATH, '//*[@id="cookie-banner-button"]')
element.click()
web.find_element(By.XPATH, '//*[@id="username"]').send_keys(username)
web.find_element(By.XPATH, '//*[@id="password"]').send_keys(password)
element = web.find_element(By.XPATH, "/html/body/div[1]/main/div/div/div/div/div/section/form/span/div[4]/button")
element.click()

# third page
sleep(1)
WebDriverWait(web, 30).until(EC.presence_of_element_located((By.ID, 536)))

web.find_element(By.XPATH, '//*[@id="359"]').send_keys(join_date)
web.find_element(By.XPATH, '//*[@id="536"]').send_keys(cgpa)

# web.find_element(By.XPATH, '//*[@id="main_external_content"]/form/div[1]/div[27]/div/span/span[1]/span').send_keys(
# 'Yes')

# Find the dropdown element for without sponsorship
dropdown_element = WebDriverWait(web, 10).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="main_external_content"'
                                                                                      ']/form/div[1]/div['
                                                                                      '27]/div/span/span[1]/span')))
# Click on the dropdown element to open the options
dropdown_element.click()
# Find the option with value "Yes" and click on it
option_element = WebDriverWait(web, 10).until(
    EC.visibility_of_element_located((By.XPATH, '/html/body/span/span/span[1]/input')))
option_element.send_keys('Yes')
sleep(1)
option_element.send_keys(Keys.ENTER)
# Pressed Yes


web.find_element(By.XPATH, '//*[@id="916"]').send_keys(aadhar)
web.find_element(By.XPATH, '//*[@id="531"]').send_keys('No, Thank You')
web.find_element(By.XPATH, '//*[@id="534"]').send_keys(certification)

# Find the dropdown element for EY website with regards to where did you find the posting
dropdown_element = WebDriverWait(web, 10).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="main_external_content"]'
                                                                                      '/form/div[1]/div[42]'
                                                                                      '/div/span/span[1]/span')))
# Click on the dropdown element to open the options
dropdown_element.click()
sleep(1)
# Find the option with value "Yes" and click on it
option_element = WebDriverWait(web, 10).until(EC.visibility_of_element_located((By.XPATH, '/html/body/span/span/'
                                                                                          'span[1]/input')))
option_element.send_keys('EY website')
sleep(1)
option_element.send_keys(Keys.ENTER)

# Find the dropdown element for OCI Card
dropdown_element = WebDriverWait(web, 10).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="main_external_content"]'
                                                                                      '/form/div[1]/div[43]/'
                                                                                      'div/span/span[1]/span')))
# Click on the dropdown element to open the options
dropdown_element.click()
sleep(1)
# Find the option with value "Yes" and click on it
option_element = WebDriverWait(web, 10).until(EC.visibility_of_element_located((By.XPATH, '/html/body/span/span/'
                                                                                          'span[1]/input')))
option_element.send_keys('No')
sleep(1)
option_element.send_keys(Keys.ENTER)

# Find the dropdown element for Actuary papers - Think doesn't work but it's not necessary anyhow
dropdown_element = WebDriverWait(web, 10).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="main_external_content'
                                                                                      '"]/form/div[1]/div['
                                                                                      '45]/div/div[2]/span/span['
                                                                                      '1]/span')))
# Click on the dropdown element to open the options
dropdown_element.click()
dropdown_element.send_keys(Keys.ENTER)
sleep(2)
# Find the option with value "Yes" and click on it
# option_element = WebDriverWait(web, 10).until(EC.visibility_of_element_located((By.XPATH, '//*['
#                                                                                           '@id="main_external_content'
#                                                                                           '"]/form/div[1]/div['
#                                                                                           '45]/div/div[2]/span/span['
#                                                                                           '1]/span')))
# option_element.send_keys(Keys.ENTER)
# sleep(1)
# option_element.send_keys(Keys.ENTER)

# Find the dropdown element for investigation question
dropdown_element = WebDriverWait(web, 10).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="main_external_content"]'
                                                                                      '/form/div[1]/div['
                                                                                      '46]/div/span/span[1]/span')))
# Click on the dropdown element to open the options
dropdown_element.click()
sleep(1)
# Find the option with value "No" and click on it
option_element = WebDriverWait(web, 10).until(EC.visibility_of_element_located((By.XPATH, '/html/body/span/span/span[1]'
                                                                                          '/input')))
option_element.send_keys('No')
sleep(1)
option_element.send_keys(Keys.ENTER)

# Find the dropdown element for non compliance question
dropdown_element = WebDriverWait(web, 10).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="main_external_content'
                                                                                      '"]/form/div[1]/div['
                                                                                      '48]/div/span/span[1]/span')))
# Click on the dropdown element to open the options
dropdown_element.click()
sleep(1)
# Find the option with value "No" and click on it
option_element = WebDriverWait(web, 10).until(EC.visibility_of_element_located((By.XPATH, '/html/body/span/span/span[1]'
                                                                                          '/input')))
option_element.send_keys('No')
sleep(1)
option_element.send_keys(Keys.ENTER)

# Find the dropdown element for distance learning question
dropdown_element = WebDriverWait(web, 10).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="main_external_content'
                                                                                      '"]/form/div[1]/div['
                                                                                      '50]/div/span/span[1]/span')))
# Click on the dropdown element to open the options
dropdown_element.click()
sleep(1)
# Find the option with value "No" and click on it
option_element = WebDriverWait(web, 10).until(EC.visibility_of_element_located((By.XPATH, '/html/body/span/span/span[1]'
                                                                                          '/input')))
option_element.send_keys('No')
sleep(1)
option_element.send_keys(Keys.ENTER)

# Find the dropdown element for big4
dropdown_element = WebDriverWait(web, 10).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="main_external_content'
                                                                                      '"]/form/div[1]/div['
                                                                                      '51]/div/span/span[1]/span')))
# Click on the dropdown element to open the options
dropdown_element.click()
sleep(1)
# Find the option with value "No" and click on it
option_element = WebDriverWait(web, 10).until(EC.visibility_of_element_located((By.XPATH, '/html/body/span/span/span[1]'
                                                                                          '/input')))
option_element.send_keys('No')
sleep(1)
option_element.send_keys(Keys.ENTER)

# Find the dropdown element for notice period
dropdown_element = WebDriverWait(web, 10).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="main_external_content"]'
                                                                                      '/form/div[1]/div[53]'
                                                                                      '/div/span/span[1]/span')))
# Click on the dropdown element to open the options
dropdown_element.click()
sleep(1)
# Find the option with value "No" and click on it
option_element = WebDriverWait(web, 10).until(EC.visibility_of_element_located((By.XPATH, '/html/body/span/span/span[1]'
                                                                                          '/input')))
option_element.send_keys('No')
sleep(1)
option_element.send_keys(Keys.ENTER)

# Find the dropdown element for compensation
dropdown_element = WebDriverWait(web, 10).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="main_external_content'
                                                                                      '"]/form/div[1]/div['
                                                                                      '54]/div/span/span[1]/span')))
# Click on the dropdown element to open the options
dropdown_element.click()
sleep(1)
# Find the option with value "Not Applicable" and click on it
option_element = WebDriverWait(web, 10).until(EC.visibility_of_element_located((By.XPATH, '/html/body/span/span/span[1]'
                                                                                          '/input')))
option_element.send_keys('Not applicable')
sleep(1)
option_element.send_keys(Keys.ENTER)

web.find_element(By.XPATH, '//*[@id="559"]').send_keys('Mr.')
web.find_element(By.XPATH, '//*[@id="561"]').send_keys('N/A')
web.find_element(By.XPATH, '//*[@id="562"]').send_keys('N/A')
web.find_element(By.XPATH, '//*[@id="563"]').send_keys('N/A')
web.find_element(By.XPATH, '//*[@id="564"]').send_keys(ParentDetails)

# Find the dropdown element for relationship question
dropdown_element = WebDriverWait(web, 10).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="main_external_content'
                                                                                      '"]/form/div[1]/div['
                                                                                      '60]/div/span/span[1]/span')))
# Click on the dropdown element to open the options
dropdown_element.click()
sleep(1)
# Find the option with value "Father" and click on it
option_element = WebDriverWait(web, 10).until(EC.visibility_of_element_located((By.XPATH, '/html/body/span/span/span[1]'
                                                                                          '/input')))
option_element.send_keys('Father')
sleep(1)
option_element.send_keys(Keys.ENTER)
sleep(1)

web.find_element(By.XPATH, '//*[@id="567"]').send_keys(DadName)

# Find the dropdown element for Dad working question
dropdown_element = WebDriverWait(web, 10).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="main_external_content'
                                                                                      '"]/form/div[1]/div['
                                                                                      '63]/div/span/span[1]/span')))
# Click on the dropdown element to open the options
dropdown_element.click()
sleep(1)
# Find the option with value "Working" and click on it

option_element = WebDriverWait(web, 10).until(EC.visibility_of_element_located((By.XPATH, '/html/body/span/span/span[1]'
                                                                                          '/input')))
option_element.send_keys('Working')
sleep(1)
option_element.send_keys(Keys.ENTER)

option_element = WebDriverWait(web, 10).until(EC.visibility_of_element_located((By.XPATH, '//*[@id="569"]'))).send_keys(
    DadDetails)

web.find_element(By.XPATH, '//*[@id="570"]').send_keys(School1)
web.find_element(By.XPATH, '//*[@id="571"]').send_keys(School2)
web.find_element(By.XPATH, '//*[@id="572"]').send_keys(Uni1)
web.find_element(By.XPATH, '//*[@id="573"]').send_keys(Uni2)

# Find the dropdown element for CA Q
dropdown_element = WebDriverWait(web, 10).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="main_external_content'
                                                                                      '"]/form/div[1]/div['
                                                                                      '69]/div/span/span[1]/span')))
# Click on the dropdown element to open the options
dropdown_element.click()
sleep(1)
# Find the option with value "No" and click on it

option_element = WebDriverWait(web, 10).until(EC.visibility_of_element_located((By.XPATH, '/html/body/span/span/span[1]'
                                                                                          '/input')))
option_element.send_keys('No')
sleep(1)
option_element.send_keys(Keys.ENTER)

# Find the dropdown element for CA Status Q
dropdown_element = WebDriverWait(web, 10).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="main_external_content'
                                                                                      '"]/form/div[1]/div['
                                                                                      '80]/div/span/span[1]/span')))
# Click on the dropdown element to open the options
dropdown_element.click()
sleep(1)
# Find the option with value "Not applied" and click on it

option_element = WebDriverWait(web, 10).until(EC.visibility_of_element_located((By.XPATH, '/html/body/span/span/span[1]'
                                                                                          '/input')))
option_element.send_keys('Not applied for membership')
sleep(1)
option_element.send_keys(Keys.ENTER)

web.find_element(By.XPATH, '//*[@id="608"]').send_keys('02/13/2023')
web.find_element(By.XPATH, '//*[@id="610"]').send_keys('N/A')

# Find the dropdown element for Law Q
dropdown_element = WebDriverWait(web, 10).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="main_external_content'
                                                                                      '"]/form/div[1]/div['
                                                                                      '92]/div/span/span[1]/span')))
# Click on the dropdown element to open the options
dropdown_element.click()
sleep(1)
# Find the option with value "No" and click on it

option_element = WebDriverWait(web, 10).until(EC.visibility_of_element_located((By.XPATH, '/html/body/span/span/span[1]'
                                                                                          '/input')))
option_element.send_keys('No')
sleep(1)
option_element.send_keys(Keys.ENTER)

# Find the dropdown element for Sanad
dropdown_element = WebDriverWait(web, 10).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="main_external_content'
                                                                                      '"]/form/div[1]/div['
                                                                                      '93]/div/span/span[1]/span')))
# Click on the dropdown element to open the options
dropdown_element.click()
sleep(1)
# Find the option with value "Not Applicable" and click on it

option_element = WebDriverWait(web, 10).until(EC.visibility_of_element_located((By.XPATH, '/html/body/span/span/span[1]'
                                                                                          '/input')))
option_element.send_keys('Not Applicable')
sleep(1)
option_element.send_keys(Keys.ENTER)

web.find_element(By.XPATH, '//*[@id="615"]').send_keys('N/A')
web.find_element(By.XPATH, '//*[@id="616"]').send_keys('02/13/2023')
web.find_element(By.XPATH, '//*[@id="617"]').send_keys('N/A')
web.find_element(By.XPATH, '//*[@id="618"]').send_keys('02/13/2023')
web.find_element(By.XPATH, '//*[@id="620"]').send_keys('N/A')
web.find_element(By.XPATH, '//*[@id="621"]').send_keys('05/12/2023')

# Find the dropdown element for Acknowledgement
dropdown_element = WebDriverWait(web, 10).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="main_external_content'
                                                                                      '"]/form/div[1]/div['
                                                                                      '102]/div/span/span[1]/span')))
# Click on the dropdown element to open the options
dropdown_element.click()
sleep(1)
# Find the option with value "Yes" and click on it

option_element = WebDriverWait(web, 10).until(EC.visibility_of_element_located((By.XPATH, '/html/body/span/span/span[1]'
                                                                                          '/input')))
option_element.send_keys('Yes')
sleep(1)
option_element.send_keys(Keys.ENTER)

# Find the dropdown element for Gender
dropdown_element = WebDriverWait(web, 10).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="main_external_content'
                                                                                      '"]/form/div[1]/div['
                                                                                      '103]/div/span/span[1]/span')))
# Click on the dropdown element to open the options
dropdown_element.click()
sleep(1)
# Find the option with value "Male", go one step down because Female is selected at default and click on it

option_element = WebDriverWait(web, 10).until(EC.visibility_of_element_located((By.XPATH, '/html/body/span/span/span[1]'
                                                                                          '/input')))
option_element.send_keys('Male')
sleep(1)
option_element.send_keys(Keys.ARROW_DOWN)  # skip this line if female
option_element.send_keys(Keys.ENTER)

# Find the dropdown element for Disability
dropdown_element = WebDriverWait(web, 10).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="main_external_content'
                                                                                      '"]/form/div[1]/div['
                                                                                      '104]/div/span/span[1]/span')))
# Click on the dropdown element to open the options
dropdown_element.click()
sleep(1)
# Find the option with value "No" and click on it

option_element = WebDriverWait(web, 10).until(EC.visibility_of_element_located((By.XPATH, '/html/body/span/span/span[1]'
                                                                                          '/input')))
option_element.send_keys('No')
sleep(1)
option_element.send_keys(Keys.ENTER)

# Find the dropdown element for Illeness
dropdown_element = WebDriverWait(web, 10).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="main_external_content'
                                                                                      '"]/form/div[1]/div['
                                                                                      '105]/div/span/span[1]/span')))
# Click on the dropdown element to open the options
dropdown_element.click()
sleep(1)
# Find the option with value "No" and click on it

option_element = WebDriverWait(web, 10).until(EC.visibility_of_element_located((By.XPATH, '/html/body/span/span/span[1]'
                                                                                          '/input')))
option_element.send_keys('No')
sleep(1)
option_element.send_keys(Keys.ENTER)

# web.find_element(By.XPATH, '//*[@id="536"]').send_keys('Passed with merit-61.4%')
# web.find_element(By.XPATH, '//*[@id="536"]').send_keys('Passed with merit-61.4%')
# web.find_element(By.XPATH, '//*[@id="536"]').send_keys('Passed with merit-61.4%')
# web.find_element(By.XPATH, '//*[@id="536"]').send_keys('Passed with merit-61.4%')


while True:
    pass
print('pass over')
