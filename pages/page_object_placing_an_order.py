from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

from locators.locators_for_price import LоcatorsDropDownList
from locators.locators_placing_an_order import LocatorsWhoIsTheScooterFor


class WhoIsTheScooterFor:
    def __init__(self, driver):
        self.driver = driver

    def waiting_for_the_main_page_to_load(self):
        WebDriverWait(self.driver, 12).until(
            expected_conditions.visibility_of_element_located((LоcatorsDropDownList.WAITING_FOR_THE_MAIN_PAGE)))

    def click_button_top_order(self):
        self.driver.find_element(*LocatorsWhoIsTheScooterFor.BUTTON_TOP_ORDER).click()

    def click_button_bottom_order(self):
        self.driver.find_element(*LocatorsWhoIsTheScooterFor.BUTTON_BOTTOM_ORDER).click()

    def scroll_to_button_bottom_order(self):
        element = self.driver.find_element(*LocatorsWhoIsTheScooterFor.BUTTON_BOTTOM_ORDER)
        self.driver.execute_script("arguments[0].scrollIntoView();", element)

    def waiting_button_bottom_order(self):
        WebDriverWait(self.driver, 12).until(expected_conditions.visibility_of_element_located(
            (LocatorsWhoIsTheScooterFor.BUTTON_BOTTOM_ORDER)))

    def waiting_title_who_is_the_scooter_for(self):
        WebDriverWait(self.driver, 12).until(expected_conditions.visibility_of_element_located(
            (LocatorsWhoIsTheScooterFor.TITLE_FOR_WHOM_IS_THE_SCOOTER)))

    def click_button_cookies(self):
        self.driver.find_element(*LocatorsWhoIsTheScooterFor.CLICK_BUTTON_COOKIES).click()

    def fill_name_field(self, name):
        self.driver.find_element(*LocatorsWhoIsTheScooterFor.NAME_FIELD).send_keys(name)

    def fill_last_name_field(self, last_name):
        self.driver.find_element(*LocatorsWhoIsTheScooterFor.LAST_NAME_FIELD).send_keys(last_name)

    def fill_address_field(self, address):
        self.driver.find_element(*LocatorsWhoIsTheScooterFor.ADDRESS_FIELD).send_keys(address)

    def fill_metro_station_field(self, metro_station):
        self.driver.find_element(*LocatorsWhoIsTheScooterFor.METRO_STATION_FIELD).send_keys(metro_station)

    def waiting_metro_station(self, metro_station):
        WebDriverWait(self.driver, 12).until(expected_conditions.text_to_be_present_in_element_value(
            (LocatorsWhoIsTheScooterFor.MEANING_METRO_STATION, metro_station)))

    def click_metro_station_field(self):
        self.driver.find_element(*LocatorsWhoIsTheScooterFor.METRO_STATION_FIELD).click()

    def click_on_the_list(self):
        self.driver.find_element(*LocatorsWhoIsTheScooterFor.CLICK_ON_THE_LIST).click()

    def click_on_the_list_two(self):
        self.driver.find_element(*LocatorsWhoIsTheScooterFor.CLICK_ON_THE_LIST_TWO).click()

    def fill_phone_field(self, phone):
        self.driver.find_element(*LocatorsWhoIsTheScooterFor.PHONE_FIELD).send_keys(phone)

    def click_button_the_next(self):
        self.driver.find_element(*LocatorsWhoIsTheScooterFor.BUTTON_THE_NEXT).click()

    def waiting_title_about_rent(self):
        WebDriverWait(self.driver, 12).until(
            expected_conditions.visibility_of_element_located((LocatorsWhoIsTheScooterFor.TITLE_ABOUT_RENT)))

    def text_to_title_about_rent(self):
        return self.driver.find_element(*LocatorsWhoIsTheScooterFor.TITLE_ABOUT_RENT).text

    def fill_field_who(self, name, last_name, address, metro_station, phone):
        self.click_metro_station_field()
        self.fill_metro_station_field(metro_station)
        self.click_on_the_list()
        self.fill_name_field(name)
        self.fill_last_name_field(last_name)
        self.fill_address_field(address)
        self.fill_phone_field(phone)
        self.click_button_the_next()

    def fill_field_who_two(self, name, last_name, address, metro_station, phone):
        self.click_metro_station_field()
        self.fill_metro_station_field(metro_station)
        self.click_on_the_list_two()
        self.fill_name_field(name)
        self.fill_last_name_field(last_name)
        self.fill_address_field(address)
        self.fill_phone_field(phone)
        self.click_button_the_next()

    def click_when_field(self):
        self.driver.find_element(*LocatorsWhoIsTheScooterFor.WHEN_FIELD).click()

    def fill_when_field(self, date):
        self.driver.find_element(*LocatorsWhoIsTheScooterFor.WHEN_FIELD).send_keys(date)

    def click_to_an_empty_place(self):
        self.driver.find_element(*LocatorsWhoIsTheScooterFor.TO_AN_EMPTY_PLAСE).click()

    def click_rental_period_field(self, ):
        self.driver.find_element(*LocatorsWhoIsTheScooterFor.RENTAL_PERIOD_FIELD).click()

    def click_day_value(self):
        self.driver.find_element(*LocatorsWhoIsTheScooterFor.DAY_VALUE).click()

    def click_scooter_color(self):
        self.driver.find_element(*LocatorsWhoIsTheScooterFor.SCOOTER_COLOR_FIELD).click()

    def fill_comment_field(self, comment):
        self.driver.find_element(*LocatorsWhoIsTheScooterFor.COMMENT_FIELD).send_keys(comment)

    def click_button_order(self):
        self.driver.find_element(*LocatorsWhoIsTheScooterFor.BUTTON_ORDER).click()

    def click_button_yes(self):
        self.driver.find_element(*LocatorsWhoIsTheScooterFor.BUTTON_YES).click()

    def display_button_view_status(self):
        return self.driver.find_element(*LocatorsWhoIsTheScooterFor.BUTTON_VIEW_STATUS).text

    def fill_field_about_rent(self, date, comment):
        self.fill_when_field(date)
        self.click_to_an_empty_place()
        self.click_rental_period_field()
        self.click_day_value()
        self.click_scooter_color()
        self.fill_comment_field(comment)
        self.click_button_order()
        self.click_button_yes()

    def click_logo_scooter(self):
        self.driver.find_element(*LocatorsWhoIsTheScooterFor.LOGO_SCOOTER).click()

    def title_scooter_for_a_couple_days(self):
        title = self.driver.find_element(*LocatorsWhoIsTheScooterFor.TITLE_SCOOTER_FOR_A_COUPLE_DAYS)
        return title
