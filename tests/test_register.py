"""
Ces tests couvrent l'inscription d'un utilisateur sur le site.
"""

from turtle import home
from pages.register import MesTachesRegisterPage
from pages.home import MesTachesHomePage

def test_register_to_site(browser):
    """
    Teste l'inscription d'un utilisateur sur le site.
    """
    register_page = MesTachesRegisterPage(browser)
    home_page = MesTachesHomePage(browser)

    NAME = "Jean Dubois"
    USERNAME = "jdubois"
    EMAIL = "jean.dubois@monmail.com"
    PASSWORD = "123456"

    # On se rend sur la page d'inscription
    register_page.load()
    
    # On entre le nom d'utilisateur
    register_page.fill_name(NAME)

    # On entre le pseudo de l'utilisateur
    register_page.fill_username(USERNAME)

    # On entre l'adresse email de l'utilisateur
    register_page.fill_email(EMAIL)

    # On entre le mot de passe de l'utilisateur
    register_page.fill_password(PASSWORD)

    # On entre la confirmation du mot de passe de l'utilisateur
    register_page.fill_password_confirm(PASSWORD)

    # On clique sur le bouton d'inscription
    register_page.click_register_button()

    # On vérifie que l'utilisateur est bien redirigé vers la page d'accueil
    assert home_page.is_browser_on_page()
    
    # On vérifie que l'utilisateur est bien connecté
    assert home_page.is_logged_in(USERNAME)

    # On vérifie que le message de succès est bien affiché
    assert home_page.is_success_message_displayed()

    raise NotImplementedError