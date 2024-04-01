from selenium.webdriver.common.by import By


class ForgotPasswordLocators:
    FORGOT_LOGIN_BUTTON = (By.PARTIAL_LINK_TEXT, 'Forgot')
    VALIDATE_ACCOUNT_PAGE = (By.CSS_SELECTOR, '.title')
    FIRST_NAME_FIELD = (By.CSS_SELECTOR, '#firstName')
    LAST_NAME_FIELD = (By.CSS_SELECTOR, '#lastName')
    ADDRESS_FIELD = (By.CSS_SELECTOR, 'input[id="address.street"]')
    CITY_FIELD = (By.CSS_SELECTOR, 'input[id="address.city"]')
    STATE_FIELD = (By.CSS_SELECTOR, 'input[id="address.state"]')
    ZIP_CODE_FIELD = (By.CSS_SELECTOR, 'input[id="address.zipCode"]')
    SSN_FILED = (By.CSS_SELECTOR, '#ssn')
    FIND_LOGIN_INFO_BUTTON = (By.CSS_SELECTOR, 'input[value="Find My Login Info"]')
    FNAME_ERROR = (By.CSS_SELECTOR, 'span[id="firstName.errors"]')
    LNAME_ERROR = (By.CSS_SELECTOR, 'span[id="lastName.errors"]')
    ADDRESS_ERROR = (By.CSS_SELECTOR, 'span[id="address.street.errors"]')
    CITY_ERROR = (By.CSS_SELECTOR, 'span[id="address.city.errors"]')
    STATE_ERROR = (By.CSS_SELECTOR, 'span[id="address.state.errors"]')
    ZIPCODE_ERROR = (By.CSS_SELECTOR, 'span[id="address.zipCode.errors"]')
    SSN_ERROR = (By.CSS_SELECTOR, 'span[id="ssn.errors"]')
    ERROR_MESSAGE = (By.CSS_SELECTOR, '.error')
    GET_INFORMATION_PAGE = (By.XPATH, '//*[@id="rightPanel"]/p[1]')
    LOG_OUT = (By.PARTIAL_LINK_TEXT, 'Log')

