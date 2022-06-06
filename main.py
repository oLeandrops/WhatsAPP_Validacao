import urllib.parse
from selenium.webdriver import Chrome
from selenium.webdriver.common.by import By
from selenium import webdriver
from time import sleep
import pandas as pd
from selenium.webdriver.common.keys import Keys
options = webdriver.ChromeOptions()
options.add_argument('start-maximized')
options.add_experimental_option('excludeSwitches', ['enable-automation'])
options.add_experimental_option('useAutomationExtension', False)
browser = Chrome(options=options)
browser.implicitly_wait(1)
telefones = pd.read_csv('BASEVALIDAR.csv')
urlprincipal = 'https://web.whatsapp.com/'
browser.get(urlprincipal)
resposta = input('Você já escaneou o QRCODE?')
wppOn = []
wppOff = []
ddi= 55
cont = 0
try:
    while resposta == 'SIM':
        for i in telefones.index:
            sleep(0.3)
            fone = f'{telefones["DDD"][i]}{telefones["TELEFONE"][i]}'
            #mensagem = urllib.parse.quote('hello world')
            url = f'https://web.whatsapp.com/send?phone={ddi}{fone}&text='
            browser.get(url)
            cont += 1
            carregando = browser.find_elements(By.CSS_SELECTOR,'div[class="QgIWN"]')
            while len(carregando) <=0:
                carregando = browser.find_elements(By.CSS_SELECTOR,'div[class="QgIWN"]')
            carregando = browser.find_elements(By.CSS_SELECTOR,'div[class="QgIWN"]')
            while len(carregando) >0:
                carregando = browser.find_elements(By.CSS_SELECTOR,'div[class="QgIWN"]')
            if len(browser.find_elements(By.CSS_SELECTOR,'div[title="Mensagem"]')) > 0:
                wppOn.append(fone)
                if len(browser.find_elements(By.CSS_SELECTOR, '#main')) > 0:
                    menu = browser.find_element(By.CSS_SELECTOR, '#main')
                    menu.find_element(By.CSS_SELECTOR, 'div[data-testid="conversation-menu-button"] ').click()
                    sleep(0.5)
                    browser.find_elements(By.CSS_SELECTOR, 'li')[-1].click()
                    sleep(0.5)
                    browser.find_element(By.CSS_SELECTOR, 'div[class*="_2Zdgs"]').click()
                    sleep(0.5)
                    if len(browser.find_elements(By.CSS_SELECTOR, 'div[class*="_2Zdgs"]')) >0:
                        browser.find_element(By.CSS_SELECTOR, 'div[class*="_2Zdgs"]').click()
                print(f'Total de {len(wppOn)} Validos.')
            elif len(browser.find_elements(By.CSS_SELECTOR, 'div[data-animate-modal-popup="true"]')) > 0:
                wppOff.append(fone)
                print(f'Total de {len(wppOff)} invalidos.')
        if cont >= len(telefones['TELEFONE']):
            print(f'''
            Validação Finalizada:
            Numeros que contém WhatsAPP: {len(wppOn)}
            Numeros que não contém WhatsAPP: {len(wppOff)}
            Total de numeros analisados: {cont}''')
            break
except Exception as erro:
    print(erro)
finally:
    on = pd.DataFrame(wppOn)
    on.to_csv('TelefonesComWhatsapp')
    off = pd.DataFrame(wppOff)
    off.to_csv('TelefonesSemWhatsapp')
