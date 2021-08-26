import pandas as pd 
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
import urllib
import pyautogui


pyautogui.alert('o envio de mensagens irá começar certifique-se que a planilha com o nome "Enviar.xlsx" estaja na mesma pasta que esse executável e que ela esteja formatada corretamente')
contatos_df = pd.read_excel('Enviar.xlsx')
print(contatos_df)

navegador = webdriver.Chrome()
navegador.get('https://web.whatsapp.com')

while len(navegador.find_elements_by_id('pane-side')) < 1:
    time.sleep(3)

for i, mensagem in enumerate(contatos_df['Mensagem']):
    pessoa = contatos_df.loc [i,'Pessoa']
    numero = contatos_df.loc [i, 'Número']
    texto = urllib.parse.quote(mensagem)
    link = f'https://web.whatsapp.com/send?phone={numero}&text={texto}'
    navegador.get(link)
    while len(navegador.find_elements_by_id('pane-side')) < 1:
        time.sleep(3)
    navegador.find_element_by_xpath('//*[@id="main"]/footer/div[1]/div[2]/div/div[1]/div/div[2]').send_keys(Keys.ENTER)
    time.sleep(20)
    pyautogui.alert(f'O Código finalizou a execuçao {i} mensagens enviadas')