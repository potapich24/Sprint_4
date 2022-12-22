from selenium.webdriver.common.by import By


class LocatorsWhoIsTheScooterFor:
    BUTTON_TOP_ORDER = By.XPATH, ".//div[starts-with(@class,'Header_Nav')]/button[text()='Заказать']"
    BUTTON_BOTTOM_ORDER = By.XPATH, ".//div[starts-with(@class,'Home_FinishButton')]/button[text()='Заказать']"
    TITLE_FOR_WHOM_IS_THE_SCOOTER = By.XPATH, ".//div[text()='Для кого самокат']"
    NAME_FIELD = By.XPATH, ".//input[@placeholder='* Имя']"
    LAST_NAME_FIELD = By.XPATH, ".//input[@placeholder='* Фамилия']"
    ADDRESS_FIELD = By.XPATH, ".//input[@placeholder='* Адрес: куда привезти заказ']"
    METRO_STATION_FIELD = By.XPATH, ".//input[@placeholder='* Станция метро']"
    MEANING_METRO_STATION = By.XPATH, ".//input[@placeholder='* Станция метро']"
    PHONE_FIELD = By.XPATH, ".//input[@placeholder='* Телефон: на него позвонит курьер']"
    BUTTON_THE_NEXT = By.XPATH, ".//button[text()='Далее']"
    CLICK_ON_THE_LIST = By.XPATH, ".//button[@value='2']"
    TITLE_ABOUT_RENT = By.XPATH, ".//div[text()='Про аренду']"
    CLICK_BUTTON_COOKIES = By.XPATH, ".//button[text()='да все привыкли']"
