

class LoginPage:
    textbox_username_id = "Email"
    textbox_password_id = "password"
    button_login_Xpath = "/html/body/nav/a[3]"
    link_logout_linktext = "Logout"

    def __init__(self):
        self.driver = driver
        self.driver = webdriver.Firefox()
        # self.driver.get("https://www.linkedin.com/home")

    def setUserName(self, username):
        self.driver.find_element_by_id(self.textbox_username_id).send_keys(username)

    def setPassword(self, password):
        self.driver.find_element_by_id(self.textbox_password_id).send_keys(password)

    def clickLogin(self):
        self.driver.find_element_by_xpath(self.button_login_Xpath).click()

    def clickLogout(self, username):
        self.driver.find_element_by_xpath(self.link_logout_linktext).click()
