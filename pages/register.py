from selenium.webdriver.common.by import By


class MesTachesRegisterPage:
    URL = "http://127.0.0.1:5000/register"

    REGISTER_NAME_INPUT = (By.ID, "name")
    REGISTER_USERNAME_INPUT = (By.ID, "username")
    REGISTER_EMAIL_INPUT = (By.ID, "email")
    REGISTER_PASSWORD_INPUT = (By.ID, "password")
    REGISTER_PASSWORD_CONFIRM_INPUT = (By.ID, "password_confirmation")
    
    REGISTER_SUBMIT_BUTTON = (By.CSS_SELECTOR, "button.btn-lg.btn-primary")

    def __init__(self, driver):
        self.driver = driver

    def load(self):
        # Charger la page d'enregistrement
        self.driver.get(self.URL)

    def fill_name(self, name):
        # Remplir le champ "Votre nom"
        name_input = self.driver.find_element(*self.REGISTER_NAME_INPUT)
        name_input.send_keys(name)

    def fill_username(self, username):
        # Remplir le champ "Votre pseudo"
        username_input = self.driver.find_element(*self.REGISTER_USERNAME_INPUT)
        username_input.send_keys(username)

    def fill_email(self, email):
        # Remplir le champ "Votre adresse email"
        email_input = self.driver.find_element(*self.REGISTER_EMAIL_INPUT)
        email_input.send_keys(email)

    def fill_password(self, password):
        # Remplir le champ "Votre mot de passe"
        password_input = self.driver.find_element(*self.REGISTER_PASSWORD_INPUT)
        password_input.send_keys(password)

    def fill_password_confirm(self, password_confirm):
        # Remplir le champ "Confirmez votre mot de passe"
        password_confirm_input = self.driver.find_element(*self.REGISTER_PASSWORD_CONFIRM_INPUT)
        password_confirm_input.send_keys(password_confirm)

    def submit(self):
        # Soumettre le formulaire
        submit_button = self.driver.find_element(*self.REGISTER_SUBMIT_BUTTON)
        submit_button.click()
