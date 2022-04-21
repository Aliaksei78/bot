import os
import booking.constants as const
from selenium import webdriver
from selenium.webdriver.common.by import By


class Booking(webdriver.Chrome):
    def __init__(self, driver_path=r"C:\SeleniumDrivers"):
        self.driver_path = driver_path
        os.environ["PATH"] += self.driver_path
        super(Booking, self).__init__()
        self.implicitly_wait(15)
        self.maximize_window()

    def land_first_page(self):
        self.get(const.BASE_URL)

    def set_currency(self, currency=None):
        currency_selection = self.find_element(By.CSS_SELECTOR, 'button[data-tooltip-text = "Выберите валюту"]')
        currency_selection.click()
        selected_currency = self.find_element(By.CSS_SELECTOR,
                                              f'a[data-modal-header-async-url-param *= "selected_currency={currency}"]')
        selected_currency.click()

    def select_destination(self, destination=None):
        input_destination = self.find_element(By.ID, 'ss')
        input_destination.clear()
        input_destination.send_keys(destination)
        first_result = self.find_element(By.CSS_SELECTOR, 'li[data-i="0"]')
        first_result.click()

    def check_dates(self, check_in_date, check_out_date):
        check_in_element = self.find_element(By.CSS_SELECTOR, f'td[data-date="{check_in_date}"]')
        check_in_element.click()
        check_out_date_element = self.find_element(By.CSS_SELECTOR, f'td[data-date="{check_out_date}"]')
        check_out_date_element.click()

    def number_of_adults(self, adults=1):
        guests_element = self.find_element(By.ID, 'xp__guests__toggle')
        guests_element.click()
        number_of_guests_view = self.find_element(By.ID, 'group_adults')
        number_of_guests = number_of_guests_view.get_attribute('value')
        i = int(number_of_guests)
        decrease_number_of_guests = self.find_element(By.CSS_SELECTOR,
                                                      'button[aria-label="Взрослых: уменьшить количество"]')
        while i > 1:
            decrease_number_of_guests.click()
            i -= 1
        increase_number_of_guests = self.find_element(By.CSS_SELECTOR,
                                                      'button[aria-label="Взрослых: увеличить количество"]')
        j = 1
        while j < adults:
            increase_number_of_guests.click()
            j += 1

    def search_of_variants(self):
        search_button = self.find_element(By.CSS_SELECTOR, 'button[data-sb-id="main"]')
        search_button.click()
