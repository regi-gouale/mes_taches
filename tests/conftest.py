"""
This module contains the fixtures for the tests.
"""
import pytest
import selenium.webdriver as webdriver

@pytest.fixture
def browser():
    """Fixture pour le navigateur."""

    # On crée une instance de Chrome
    driver = webdriver.Chrome()
    
    # On attend 10 secondes pour que la page se charge
    driver.implicitly_wait(10)
    
    # On retourne le driver pour qu'il soit utilisé par les tests
    yield driver
    
    # On ferme le navigateur
    driver.quit()
