class PageHome():
    def __init__(self,driver):
        self.driver=driver #initialiser avec le browser defini
    
    def load_page(self):
        self.driver.get('http://127.0.0.1:5000/register')
        