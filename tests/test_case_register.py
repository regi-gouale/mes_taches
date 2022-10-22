from selenium.webdriver.common.by import By
import time

def test_user_register(browser):
    #Aller sur la page d'inscription
    browser.get("http://127.0.0.1:5000/register")
    #saisir le nom
    inputName = browser.find_element(By.ID, "name")
    inputName.send_keys("Stepane")
    # Permet d'arreter pendant quelque second 
    #saisir le pseudo
    inputUserName = browser.find_element(By.ID, "username")
    inputUserName.send_keys("Stepane2022")
    #saisir l'email
    inputUserEmail = browser.find_element(By.ID, "email")
    inputUserEmail.send_keys("stephanehozigre@gmail.com")
    #saisir le password
    inputUserPswd = browser.find_element(By.ID, "password")
    inputUserPswd.send_keys("stephane20")
    #saisir la confirmation du password
    inputUserPswd_Conf = browser.find_element(By.ID, "password_confirmation")
    inputUserPswd_Conf.send_keys("stephane20")
    time.sleep(5)
    #cliquer sur le boutoin s'inscrire
    inputBtnInscrire = browser.find_element(By.XPATH, "/html/body/div/form/button")
    inputBtnInscrire.click()
    time.sleep(5)
    #On vérifie qu'on a la page d'accueil  
    accueil = browser.find_element(By.XPATH, "/html/body/div/div[1]/a")
    assert accueil
    print(accueil)
    #On vérifie qu'on a le message de bienvenue
    raise NotImplementedError #Test pas encore prêt

