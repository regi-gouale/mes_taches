from selenium.webdriver.common.by import By
import time
def test_user_register(browser):
    #Aller sur la page d'inscription
    browser.get('http://127.0.0.1:5000/register')
    #saisir le nom
    inputName=browser.find_element(By.ID,"name")
    inputName.send_keys("Siaka")
    #saisir le pseudo
    inputName=browser.find_element(By.ID,"username")
    inputName.send_keys("Siaka2022")

    inputName=browser.find_element(By.ID,"email")
    inputName.send_keys("siaka@gmail.com")

    inputName=browser.find_element(By.ID,"password")
    inputName.send_keys("Balala@2022")

    inputName=browser.find_element(By.ID,"password_confirmation")
    inputName.send_keys("Balala@2022")

    inputName=browser.find_element(By.XPATH,"/html/body/div/form/button")
    inputName.click()

    #saisir l'email
    #saisir le password
    #saisir la confirmation du password
    #cliquer sur le boutoin s'inscrire
    #On vérifie qu'on a la page d'accueil  
    #On vérifie qu'on a le message de bienvenue
    raise NotImplementedError #Test pas encore prêt

