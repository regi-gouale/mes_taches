from selenium.webdriver.common.by import By


class MesTachesHomePage:
    HOME_WELCOME_MESSAGE = (By.CSS_SELECTOR, "div.alert.alert-success")
    HOME_TITLE = (By.CSS_SELECTOR, "h1")
    

    def __init__(self, browser):
        self.browser = browser

    def load(self):
        # TODO: Charger la page d'accueil
        self.browser.get("http://127.0.0.1:5000/")

    def is_logged(self, username):
        # Vérifier que l'utilisateur est connecté
        self.HOME_USERNAME = (By.LINK_TEXT, f"Bienvenue {username}")
        return self.browser.find_element(*self.HOME_USERNAME).text == f"Bienvenue {username}"

    def get_success_message(self):
        # TODO: Récupérer le message de succès
        return self.browser.find_element(*self.HOME_WELCOME_MESSAGE).text

    def get_title(self):
        # Récupérer le titre de la page
        return self.browser.title

    def is_browser_on_page(self):
        # Vérifier que le navigateur est sur la bonne page
        return self.get_title() == "Mes Tâches"
