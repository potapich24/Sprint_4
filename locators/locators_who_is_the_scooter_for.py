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
    CLICK_ON_THE_LIST_TWO = By.XPATH, ".//button[@value='4']"
    TITLE_ABOUT_RENT = By.XPATH, ".//div[text()='Про аренду']"
    CLICK_BUTTON_COOKIES = By.XPATH, ".//button[text()='да все привыкли']"

    WHEN_FIELD = By.XPATH, ".//input[@placeholder='* Когда привезти самокат']"
    RENTAL_PERIOD_FIELD = By.XPATH, ".//div[text()='* Срок аренды']"
    TO_AN_EMPTY_PLAСE = By.XPATH, "//body"
    DAY_VALUE = By.XPATH, ".//div[text()='сутки']"
    SCOOTER_COLOR_FIELD = By.ID, "black"
    COMMENT_FIELD = By.XPATH, ".//input[@placeholder='Комментарий для курьера']"
    BUTTON_ORDER = By.XPATH, ".//div[@class='Order_Buttons__1xGrp']/button[text()='Заказать']"
    BUTTON_YES = By.XPATH, ".//button[text()='Да']"
    TITLE_THE_ORDER_HAS_BEEN_PLACED = By.XPATH, ".//div[text()='Заказ оформлен']"
    BUTTON_VIEW_STATUS = By.XPATH, ".//button[text()='Посмотреть статус']"
