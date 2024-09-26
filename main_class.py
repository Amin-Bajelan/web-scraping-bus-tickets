from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys


chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)
driver=webdriver.Chrome(options=chrome_options)
Tickets_tab = 'https://safar724.com/bus/tehran-mashhad?date=1403-07-06'
first_tab = 'https://safar724.com/'

driver.get(Tickets_tab)
# origin = driver.find_element(By.ID,'route-panel__origin')
# print(origin .text)
# origin.send_keys(Keys.ENTER)
# origin.send_keys('تهران')
# origin.send_keys(Keys.ENTER)
#
# destination = driver.find_element(By.ID,'route-panel__destination')
# print(destination.text)
# destination.send_keys(Keys.ENTER)
# destination.send_keys('مشهد')
# destination.send_keys(Keys.ENTER)
#
# press_enter = driver.find_element(By.XPATH,'//*[@id="date-panel__btn-search2"]/span')
# press_enter.click()
#


name_of_company = driver.find_elements(By.CLASS_NAME,'ticketDetailRouteInformation_company__7hGqO')

The_time_of_moving = driver.find_elements(By.CLASS_NAME,'ticketAction_time__T9_WZ')

empty_seat = driver.find_elements(By.CSS_SELECTOR,'.ticketAction_seat__QP645 p')

Amount_payable = driver.find_elements(By.CSS_SELECTOR,'.ticketDetailBusInformation_model__05uN0 p')



