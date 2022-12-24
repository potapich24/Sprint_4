from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

from locators.locators_for_price import LоcatorsDropDownList



# Клас страницы с вопросами
class QuestionsPage:
    def __init__(self, driver):
        self.driver = driver

    def delуte_cookies(self):
        self.driver.delete_cookie("new_cookie")

    def scroll_to_price(self):
        element_1 = self.driver.find_element(*LоcatorsDropDownList.PRICE)

        self.driver.execute_script("arguments[0].scrollIntoView();", element_1)

    def waiting_for_the_main_page_to_load(self):
        WebDriverWait(self.driver, 12).until(expected_conditions.visibility_of_element_located((LоcatorsDropDownList.WAITING_FOR_THE_MAIN_PAGE)))

    def click_price(self):
        self.driver.find_element(*LоcatorsDropDownList.PRICE).click()

    def answer_for_price(self):
        return self.driver.find_element(*LоcatorsDropDownList.PRICE_ANSWER).text

    def click_button_cookies(self):
        self.driver.find_element(*LоcatorsDropDownList.CLICK_BUTTON_COOKIES).click()

    def waiting_for_the_text_answer_1(self):
        WebDriverWait(self.driver, 20).until(
            expected_conditions.visibility_of_element_located((LоcatorsDropDownList.PRICE_ANSWER)))

    def waiting_price(self):
        WebDriverWait(self.driver, 20).until(
            expected_conditions.visibility_of_element_located((LоcatorsDropDownList.PRICE)))

    def scroll_to_several_scooters(self):
        element_2 = self.driver.find_element(*LоcatorsDropDownList.SEVERAL_SCOOTERS)
        self.driver.execute_script("arguments[0].scrollIntoView();", element_2)

    def click_several_scooters(self):
        self.driver.find_element(*LоcatorsDropDownList.SEVERAL_SCOOTERS).click()

    def waiting_for_the_text_answer_2(self):
        WebDriverWait(self.driver, 6).until(
            expected_conditions.visibility_of_element_located((LоcatorsDropDownList.SEVERAL_SCOOTERS_ANSWER)))

    def answer_for_several_scooters(self):
        return self.driver.find_element(*LоcatorsDropDownList.SEVERAL_SCOOTERS_ANSWER).text

    def scroll_to_rental_time(self):
        element_3 = self.driver.find_element(*LоcatorsDropDownList.RENTAL_TIME)
        self.driver.execute_script("arguments[0].scrollIntoView();", element_3)

    def click_rental_time(self):
        self.driver.find_element(*LоcatorsDropDownList.RENTAL_TIME).click()

    def waiting_for_the_text_answer_3(self):
        WebDriverWait(self.driver, 6).until(expected_conditions.visibility_of_element_located((LоcatorsDropDownList.RENTAL_TIME_ANSWER)))

    def answer_for_rental_time(self):
        return self.driver.find_element(*LоcatorsDropDownList.RENTAL_TIME_ANSWER).text

    def waiting_rental_time(self):
        WebDriverWait(self.driver, 6).until(
            expected_conditions.visibility_of_element_located((LоcatorsDropDownList.RENTAL_TIME)))

    def scroll_to_order_today(self):
        element_4 = self.driver.find_element(*LоcatorsDropDownList.ORDER_TODAY)
        self.driver.execute_script("arguments[0].scrollIntoView();", element_4)

    def click_order_today(self):
        self.driver.find_element(*LоcatorsDropDownList.ORDER_TODAY).click()

    def waiting_for_the_text_answer_4(self):
        WebDriverWait(self.driver, 6).until(
            expected_conditions.visibility_of_element_located((LоcatorsDropDownList.ORDER_TODAY_ANSWER)))

    def answer_for_order_today(self):
        return self.driver.find_element(*LоcatorsDropDownList.ORDER_TODAY_ANSWER).text

    def waiting_order_today(self):
        WebDriverWait(self.driver, 6).until(
            expected_conditions.visibility_of_element_located((LоcatorsDropDownList.ORDER_TODAY)))

    def scroll_to_extend_the_order(self):
        element_5 = self.driver.find_element(*LоcatorsDropDownList.EXTEND_THE_ORDER)
        self.driver.execute_script("arguments[0].scrollIntoView();", element_5)

    def click_extend_the_order(self):
        self.driver.find_element(*LоcatorsDropDownList.EXTEND_THE_ORDER).click()

    def waiting_for_the_text_answer_5(self):
        WebDriverWait(self.driver, 6).until(
            expected_conditions.visibility_of_element_located((LоcatorsDropDownList.EXTEND_THE_ORDER_ANSWER)))

    def answer_for_extend_the_order(self):
        return self.driver.find_element(*LоcatorsDropDownList.EXTEND_THE_ORDER_ANSWER).text

    def waiting_extend_the_order(self):
        WebDriverWait(self.driver, 6).until(expected_conditions.visibility_of_element_located((LоcatorsDropDownList.EXTEND_THE_ORDER)))

    def scroll_to_charging(self):
        element_6 = self.driver.find_element(*LоcatorsDropDownList.CHARGING)
        self.driver.execute_script("arguments[0].scrollIntoView();", element_6)

    def click_charging(self):
        self.driver.find_element(*LоcatorsDropDownList.CHARGING).click()

    def waiting_for_the_text_answer_6(self):
        WebDriverWait(self.driver, 6).until(expected_conditions.visibility_of_element_located((LоcatorsDropDownList.CHARGING_ANSWER)))

    def answer_for_charging(self):
        return self.driver.find_element(*LоcatorsDropDownList.CHARGING_ANSWER).text

    def waiting_charging(self):
        WebDriverWait(self.driver, 6).until(expected_conditions.visibility_of_element_located((LоcatorsDropDownList.CHARGING)))

    def scroll_to_cancel_the_order(self):
        element_7 = self.driver.find_element(*LоcatorsDropDownList.CANCEL_THE_ORDER)
        self.driver.execute_script("arguments[0].scrollIntoView();", element_7)

    def click_cancel_the_order(self):
        self.driver.find_element(*LоcatorsDropDownList.CANCEL_THE_ORDER).click()

    def waiting_for_the_text_answer_7(self):
        WebDriverWait(self.driver, 6).until(expected_conditions.visibility_of_element_located((LоcatorsDropDownList.CANCEL_THE_ORDER_ANSWER)))

    def answer_for_cancel_the_order(self):
        return self.driver.find_element(*LоcatorsDropDownList.CANCEL_THE_ORDER_ANSWER).text

    def waiting_cancel_the_order(self):
        WebDriverWait(self.driver, 6).until(expected_conditions.visibility_of_element_located((LоcatorsDropDownList.CANCEL_THE_ORDER)))

    def scroll_to_i_live(self):
        element_8 = self.driver.find_element(*LоcatorsDropDownList.I_LIVE)
        self.driver.execute_script("arguments[0].scrollIntoView();", element_8)

    def click_i_live(self):
        self.driver.find_element(*LоcatorsDropDownList.I_LIVE).click()

    def waiting_for_the_text_answer_8(self):
        WebDriverWait(self.driver, 6).until(expected_conditions.visibility_of_element_located((LоcatorsDropDownList.I_LIVE_ANSWER)))

    def answer_for_i_live(self):
        return self.driver.find_element(*LоcatorsDropDownList.I_LIVE_ANSWER).text

    def waiting_i_live(self):
        WebDriverWait(self.driver, 6).until(expected_conditions.visibility_of_element_located((LоcatorsDropDownList.I_LIVE)))

    def click_logo_yandex(self):
        self.driver.find_element(*LоcatorsDropDownList.LOGO_YANDEX).click()

    def switching_to_a_tab(self):
        self.driver.switch_to.window(self.driver.window_handles[1])

    def waiting_url_yandex_page(self):
        WebDriverWait(self.driver, 15).until(EC.url_to_be('https://dzen.ru/?yredirect=true'))

    def get_current_url_yandex_page(self):
        url = self.driver.current_url
        return url

