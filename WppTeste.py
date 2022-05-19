from selenium.webdriver import Chrome
from selenium.webdriver.common.by import By
from time import sleep
urlbase = 'https://web.whatsapp.com/'
ddi = 55
browser = Chrome(executable_path='C:\DRIVERS\chromedriver.exe')
browser.get(urlbase)
fone = int(input('Qual numero para mandar msg: '))
resposta = str(input('QRCOD Foi lido?')).upper()
if resposta == 'SIM':
    url = f'https://web.whatsapp.com/send?phone={ddi}{fone}&text='
    browser.get(url)
    sleep(4)
    menu = browser.find_element(By.CSS_SELECTOR, '#main')
    menu.find_element(By.CSS_SELECTOR, 'div[data-testid="conversation-menu-button"] ').click()
    #browser.find_elements(By.CSS_SELECTOR, 'li')[-1]
    browser.find_elements(By.CSS_SELECTOR, 'li')[-1].click()
    browser.find_element(By.CSS_SELECTOR, 'div[class*="_2Zdgs"]').click()
    browser.find_element(By.CSS_SELECTOR, 'div[class*="_2Zdgs"]').click()





