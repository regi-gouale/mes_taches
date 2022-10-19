from selenium.webdriver.common.by import By


class MesTachesHomePage:
    HOME_WELCOME_MESSAGE = (By.CSS_SELECTOR, "div.alert.alert-success")
    HOME_TITLE = (By.CSS_SELECTOR, "h1")
    HOME_USERNAME = (By.CSS_SELECTOR, "a.nav-link")

    def __init__(self, browser):
        self.browser = browser

    def load(self):
        # TODO: Charger la page d'accueil
        pass

    def is_logged(self):
        # TODO: Vérifier que l'utilisateur est connecté
        return True

    def get_success_message(self):
        # TODO: Récupérer le message de succès
        return ""

    def get_title(self):
        # TODO: Récupérer le titre de la page
        return ""

    def is_browser_on_page(self):
        # TODO: Vérifier que le navigateur est sur la bonne page
        return True
