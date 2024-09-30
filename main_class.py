import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import tkinter
from tkinter import messagebox

import store_data

url_pages = str('splide02-slide0')
current_page = int(1)
num_primary_key = int(1)
main_url = str


def find_ticket():
    global num_primary_key

    global main_url
    name_origin_city = str(entry_origin.get())
    if name_origin_city == '':
        messagebox.showerror("Error", "Please enter name for origin")
        return None
    name_destination_city = str(entry_destination.get())
    if name_destination_city == '':
        messagebox.showerror("Error", "Please enter name for destination")
        return None

    try:

        chrome_options = webdriver.ChromeOptions()
        chrome_options.add_experimental_option("detach", True)
        driver = webdriver.Chrome(options=chrome_options)
        First_tab = 'https://safar724.com/'

        driver.get(First_tab)
        origin = driver.find_element(By.ID, 'route-panel__origin')
        origin.send_keys(Keys.ENTER)
        origin.send_keys(name_origin_city)
        origin.send_keys(Keys.ENTER)

        destination = driver.find_element(By.ID, 'route-panel__destination')
        destination.send_keys(Keys.ENTER)
        destination.send_keys(name_destination_city)
        destination.send_keys(Keys.ENTER)

        press_enter = driver.find_element(By.XPATH, '//*[@id="date-panel__btn-search2"]/span')
        press_enter.click()

        main_url = str(driver.current_url)
        go_to_next_page = tkinter.Label(text="If you want to switch between pages, press the buttons",
                                        font=('Arial', 12))
        go_to_next_page.place(x=50, y=200)
        btn_next_page = tkinter.Button(text="next page", font=('Arial', 12), command=lambda: switch_page('next'),
                                       width=15)
        btn_next_page.place(x=250, y=240)
        btn_previous_page = tkinter.Button(text='previous page', font=('Arial', 12),
                                           command=lambda: switch_page('previous'), width=15)
        btn_previous_page.place(x=50, y=240)

        return_date(str(driver.current_url))

        name_of_company = driver.find_elements(By.CLASS_NAME, 'ticketDetailRouteInformation_company__7hGqO')

        the_time_of_moving = driver.find_elements(By.CLASS_NAME, 'ticketAction_time__T9_WZ')

        empty_seat = driver.find_elements(By.CSS_SELECTOR, '.ticketAction_seat__QP645 p')

        amount_payable = driver.find_elements(By.CSS_SELECTOR, '.ticketAction_price__Sk7X3 p')

        model_bus = driver.find_elements(By.CSS_SELECTOR, '.ticketDetailBusInformation_model__05uN0 p')

        for i in range(len(empty_seat)):
            store_data.add_data(int(num_primary_key),str(name_of_company[i].text), str(the_time_of_moving[i].text), str(empty_seat[i].text), str(amount_payable[i].text), str(model_bus[i].text))

            num_primary_key += 1


    except:
        messagebox.showerror("Error", "Please try again something went wrong..")


def switch_page(state):
    global num_primary_key
    global url_pages
    global current_page
    global main_url

    if state == 'next':
        chrome_options = webdriver.ChromeOptions()
        chrome_options.add_experimental_option("detach", True)
        driver = webdriver.Chrome(options=chrome_options)
        First_tab = str(main_url)
        driver.get(First_tab)

        num = str(int(current_page) + 1)
        current_page = int(current_page) + 1
        new_url = str(url_pages + str(num))
        press_btn = driver.find_element(By.ID, new_url)
        press_btn.click()
        main_url = str(driver.current_url)

        return_date(str(driver.current_url))

        name_of_company = driver.find_elements(By.CLASS_NAME, 'ticketDetailRouteInformation_company__7hGqO')

        the_time_of_moving = driver.find_elements(By.CLASS_NAME, 'ticketAction_time__T9_WZ')

        empty_seat = driver.find_elements(By.CSS_SELECTOR, '.ticketAction_seat__QP645 p')

        amount_payable = driver.find_elements(By.CSS_SELECTOR, '.ticketAction_price__Sk7X3 p')

        model_bus = driver.find_elements(By.CSS_SELECTOR, '.ticketDetailBusInformation_model__05uN0 p')
        for i in range(len(empty_seat)):
            store_data.add_data(int(num_primary_key),str(name_of_company[i].text), str(the_time_of_moving[i].text), str(empty_seat[i].text), str(amount_payable[i].text), str(model_bus[i].text))

            num_primary_key += 1
    elif state == 'previous':
        chrome_options = webdriver.ChromeOptions()
        chrome_options.add_experimental_option("detach", True)
        driver = webdriver.Chrome(options=chrome_options)
        First_tab = str(main_url)
        driver.get(First_tab)

        num = str(int(current_page) - 1)
        current_page = int(current_page) - 1
        new_url = str(url_pages + str(num))
        press_btn = driver.find_element(By.ID, new_url)
        press_btn.click()
        main_url = str(driver.current_url)

        return_date(str(driver.current_url))

        name_of_company = driver.find_elements(By.CLASS_NAME, 'ticketDetailRouteInformation_company__7hGqO')

        the_time_of_moving = driver.find_elements(By.CLASS_NAME, 'ticketAction_time__T9_WZ')

        empty_seat = driver.find_elements(By.CSS_SELECTOR, '.ticketAction_seat__QP645 p')

        amount_payable = driver.find_elements(By.CSS_SELECTOR, '.ticketAction_price__Sk7X3 p')

        model_bus = driver.find_elements(By.CSS_SELECTOR, '.ticketDetailBusInformation_model__05uN0 p')
        for i in range(len(empty_seat)):
            store_data.add_data(int(num_primary_key),str(name_of_company[i].text), str(the_time_of_moving[i].text), str(empty_seat[i].text), str(amount_payable[i].text), str(model_bus[i].text))

            num_primary_key += 1


def return_date(page_url):
    my_list = list(page_url)
    size = len(my_list)
    first_size = size

    second_size = size - 8
    date = ''
    for i in range(int(second_size), int(first_size)):
        date += my_list[i]
    print(f'Date of today\'s tickets: {date}')
    time.sleep(3)


window = tkinter.Tk()

window.title("Scraping Website")
window.geometry("500x500")
window.minsize(500, 500)
window.maxsize(500, 500)

label_origin = tkinter.Label(window, text="Please enter your origin:", font=("Arial", 12))
label_origin.place(x=50, y=50)
entry_origin = tkinter.Entry(window, font=("Arial", 12))
entry_origin.place(x=250, y=50)
label_destination = tkinter.Label(window, text="Please enter your destination:", font=("Arial", 12))
label_destination.place(x=50, y=100)
entry_destination = tkinter.Entry(window, font=("Arial", 12))
entry_destination.place(x=280, y=100)
btn_check = tkinter.Button(window, text="Check", font=("Arial", 12), command=find_ticket, width=15)
btn_check.place(x=50, y=150)

window.mainloop()



