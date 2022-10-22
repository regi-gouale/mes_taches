"""
Ces tests couvrent l'inscription d'un utilisateur sur le site.
"""

from pages.register import MesTachesRegisterPage
from pages.home import MesTachesHomePage
import random
import pytest

@pytest.mark.parametrize("name, username, email, password, password_confirm", [
    ("Jean Bodard", "jbd", "jbd@boada.com", "AZbci124", "AZbci124"),
    ("Toto", "toto", "toto@fin.com", "GIbvieooez", "GIbvieooez"),
])
def test_register_to_site(browser, name, username, email, password, password_confirm):
    """
    Teste l'inscription d'un utilisateur sur le site.
    """
    register_page = MesTachesRegisterPage(browser)
    home_page = MesTachesHomePage(browser)

    # On se rend sur la page d'inscription
    register_page.load()
    
    # On entre le nom d'utilisateur
    register_page.fill_name(name=name)

    # On entre le pseudo de l'utilisateur
    register_page.fill_username(username=username)

    # On entre l'adresse email de l'utilisateur
    register_page.fill_email(email=email)

    # On entre le mot de passe de l'utilisateur
    register_page.fill_password(password=password)

    # On entre la confirmation du mot de passe de l'utilisateur
    register_page.fill_password_confirm(password_confirm=password_confirm)

    # On clique sur le bouton d'inscription
    register_page.submit()

    # On vérifie que l'utilisateur est bien redirigé vers la page d'accueil
    assert home_page.is_browser_on_page()
    
    # On vérifie que l'utilisateur est bien connecté
    assert home_page.is_logged(username=username)

    # On vérifie que le message de succès est bien affiché
    assert home_page.get_success_message()
