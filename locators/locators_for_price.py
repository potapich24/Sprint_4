from selenium.webdriver.common.by import By


class LоcatorsDropDownList:
    PRICE = By.XPATH, "//div[text() = 'Сколько это стоит? И как оплатить?']"
    PRICE_ANSWER = By.XPATH, './/p[text()="Сутки — 400 рублей. Оплата курьеру — наличными или картой."]'
    SEVERAL_SCOOTERS = By.ID, 'accordion__heading-1'
    SEVERAL_SCOOTERS_ANSWER = By.XPATH, './/p[text()="Пока что у нас так: один заказ — один самокат. Если хотите покататься с друзьями, можете просто сделать несколько заказов — один за другим."]'
    RENTAL_TIME = By.ID, 'accordion__heading-2'
    RENTAL_TIME_ANSWER = By.XPATH, './/p[text()="Допустим, вы оформляете заказ на 8 мая. Мы привозим самокат 8 мая в течение дня. Отсчёт времени аренды начинается с момента, когда вы оплатите заказ курьеру. Если мы привезли самокат 8 мая в 20:30, суточная аренда закончится 9 мая в 20:30."]'
    ORDER_TODAY = By.ID, 'accordion__heading-3'
    ORDER_TODAY_ANSWER = By.XPATH, './/p[text()="Только начиная с завтрашнего дня. Но скоро станем расторопнее."]'
    EXTEND_THE_ORDER = By.ID, 'accordion__heading-4'
    EXTEND_THE_ORDER_ANSWER = By.XPATH, './/p[text()="Пока что нет! Но если что-то срочное — всегда можно позвонить в поддержку по красивому номеру 1010."]'
    CHARGING = By.ID, 'accordion__heading-5'
    CHARGING_ANSWER = By.XPATH, './/p[text()="Самокат приезжает к вам с полной зарядкой. Этого хватает на восемь суток — даже если будете кататься без передышек и во сне. Зарядка не понадобится."]'
    CANCEL_THE_ORDER = By.ID, 'accordion__heading-6'
    CANCEL_THE_ORDER_ANSWER = By.XPATH, '//p[text()="Да, пока самокат не привезли. Штрафа не будет, объяснительной записки тоже не попросим. Все же свои."]'
    I_LIVE = By.ID, 'accordion__heading-7'
    I_LIVE_ANSWER = By.XPATH, './/p[text()="Да, обязательно. Всем самокатов! И Москве, и Московской области."]'
    WAITING_FOR_THE_MAIN_PAGE = By.XPATH, './/img[@alt="Scooter blueprint"]'
    CLICK_BUTTON_COOKIES = By.XPATH, "//button[text() = 'да все привыкли']"

    LOGO_YANDEX = By.XPATH, ".//img[@alt='Yandex']"
