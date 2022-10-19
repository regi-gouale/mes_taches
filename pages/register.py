from selenium.webdriver.common.by import By


class MesTachesRegisterPage:
    REGISTER_NAME_INPUT = (By.ID, "name")
    REGISTER_USERNAME_INPUT = (By.ID, "username")
    REGISTER_EMAIL_INPUT = (By.ID, "email")
    REGISTER_PASSWORD_INPUT = (By.ID, "password")
    REGISTER_PASSWORD_CONFIRM_INPUT = (By.ID, "password_confirm")
    
    REGISTER_SUBMIT_BUTTON = (By.ClassName , "btn btn-lg btn-primary btn-block")

    def __init__(self, driver):
        self.driver = driver

    def load(self):
        # TODO: Charger la page d'enregistrement
        pass

    def fill_name(self, name):
        # TODO: Remplir le champ "Votre nom"
        pass

    def fill_username(self, username):
        # TODO: Remplir le champ "Votre pseudo"
        pass

    def fill_email(self, email):
        # TODO: Remplir le champ "Votre adresse email"
        pass

    def fill_password(self, password):
        # TODO: Remplir le champ "Votre mot de passe"
        pass

    def fill_password_confirm(self, password_confirm):
        # TODO: Remplir le champ "Confirmez votre mot de passe"
        pass

    def submit(self):
        # TODO: Soumettre le formulaire
        pass
