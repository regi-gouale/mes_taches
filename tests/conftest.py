"""
This module contains the fixtures for the tests.
"""
import pytest
import selenium.webdriver as webdriver
import json
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager

@pytest.fixture
def browser(config):
    """Fixture pour le navigateur."""
    if config["browser"] == "Chrome":
        # Créer un navigateur Chrome
        service = Service(ChromeDriverManager().install())
        driver = webdriver.Chrome(service=service)
    elif config["browser"] == "Firefox":
        service = Service(GeckoDriverManager().install())
        driver = webdriver.Firefox(service=service)
    elif config["browser"] == "Headless Chrome":
        # Créer un navigateur Chrome en mode headless
        service = Service(ChromeDriverManager().install())
        options = webdriver.ChromeOptions()
        options.add_argument("--headless")
        driver = webdriver.Chrome(service=service, options=options)
    elif config["browser"] == "Safari":
        driver = webdriver.Safari()
    else:
        raise Exception("Le navigateur n'est pas supporté.")

    
    # On attend 10 secondes pour que la page se charge
    driver.implicitly_wait(config["implicit_wait"])
    
    # On retourne le driver pour qu'il soit utilisé par les tests
    yield driver
    
    # On ferme le navigateur
    driver.quit()

@pytest.fixture
def config(scope="session"):
    """Fixture pour la configuration du site."""
    with open("config.json") as config_file:
        config = json.load(config_file)
    
    assert config["browser"] in ["Firefox", "Chrome", "Headless Chrome", "Safari"]
    assert isinstance(config["implicit_wait"], int)
    assert config["implicit_wait"] > 0

    return config
