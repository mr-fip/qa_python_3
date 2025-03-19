from selenium.webdriver.common.by import By

class HomePageLocators:
    QUESTION = (By.CSS_SELECTOR, '[data-accordion-component="AccordionItemButton"]')
    ANSWER = (By.CSS_SELECTOR, '[data-accordion-component="AccordionItemPanel"]')
    ORDER_BUTTON_HEADER = (By.XPATH, '//button[contains(., "Заказать")][1]')
    ORDER_BUTTON_FOOTER = (By.XPATH, '//button[contains(., "Заказать")][2]')