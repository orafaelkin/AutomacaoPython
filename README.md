# coletaDados
from selenium import webdriver # permite criar o navegador
from selenium.webdriver.common.keys import Keys #permite escrever no navegador e apertar um tecla do teclado "enter"
from selenium.webdriver.common.by import By #permite selecionar itens no navegador

#Passo 1: pegar a cotacao do dolar
 #abrir o navegador
navegador = webdriver.Chrome()
 #entrar no google
navegador.get("https://www.google.com/")
#pesquisar no google por cotacao dolar
navegador.find_element("xpath",'//*[@id="APjFqb"]').send_keys("cotação dólar") # send_keys() usado para escrever no elemento e find_element('xpath','') usado para identificar o elemento da tela
navegador.find_element("xpath",'//*[@id="APjFqb"]').send_keys(Keys.ENTER) #keys.ENTER ( sempre com 'K' e ENTER maiusculo) usado para apertar uma tecla do teclado

#pegar a cotacao
cotacao_dolar =  navegador.find_element('xpath','//*[@id="knowledge-currency__updatable-data-column"]/div[1]/div[2]/span[1]').get_attribute('data-value') #get_attribute usado para coletar o "valor" do elemento
print(cotacao_dolar)

#Passo 2: pegar a cotacao do euro
navegador.get("https://www.google.com/")
navegador.find_element("xpath",'//*[@id="APjFqb"]').send_keys("cotação Euro")
navegador.find_element("xpath",'//*[@id="APjFqb"]').send_keys(Keys.ENTER)
cotacao_euro =  navegador.find_element('xpath','//*[@id="knowledge-currency__updatable-data-column"]/div[1]/div[2]/span[1]').get_attribute('data-value')
print(cotacao_euro)

#Passo 3: pegar a cotacao do ouro
navegador.get('https://www.melhorcambio.com/ouro-hoje')
cotacao_ouro = navegador.find_element('xpath','//*[@id="comercial"]').get_attribute('value')

cotacao_ouro = cotacao_ouro.replace(",",".") #usado para trocar virgula por ponto (python nao reconhece virgula)
print(cotacao_ouro)

navegador.quit()

