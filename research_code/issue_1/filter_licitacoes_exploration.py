# -*- coding: utf-8 -*-

import requests
from bs4 import BeautifulSoup
from selenium.webdriver.common.by import By
from selenium import webdriver

# TODO: Solucionar a geração da página HTML sem que o Selenium seja necessário
# TODO: Testar o comando find_element (linha 30) em um ambiente virtual ou local
# TODO: Conseguir resolver a "paginação" presente no dropdown de participante e unidades interessadas

# Cria um objeto a partir do endpoint da issue 1 usando BeautifulSoup
url = "https://transparencia.joaopessoa.pb.gov.br/#/licitacoes"
driver = requests.get(url)
soup = BeautifulSoup(driver.content, "html.parser")

print(soup.prettify())

# Como o objeto soup não chegou da forma esperada, utilizamos o selenium para
# a página executar suas ações e gerar o html correto
url = "https://transparencia.joaopessoa.pb.gov.br/#/licitacoes"
driver = webdriver.Chrome()
driver.get(url)
soup = BeautifulSoup(driver.page_source, "html.parser")

print(soup.prettify())

# Como o comando comentado abaixo não funcionou no Google Colab, retiramos os
# html de cada dropdown manualmente, esses arquivos estão em formato html e
# disponibilizados na pasta raw_data
# driver.find_element(By.CLASS_NAME, "ng-tns-c192-5 ng-untouched ng-pristine ng-valid")

driver.quit()

# Secretarias e Orgaos
with open("raw_data/secretarias-orgaos.html") as fp:
  soup = BeautifulSoup(fp, 'html.parser')

for secretaria in soup.find_all('span', {'class' : 'ng-star-inserted'}):
  print(secretaria.text)

# Participante
with open("raw_data/participante.html") as fp:
  soup = BeautifulSoup(fp, 'html.parser')

for participante in soup.find_all('span', {'class' : 'ng-star-inserted'}):
  print(participante.text)

# Unidades Interessadas
with open("raw_data/unidades-interessadas.html") as fp:
  soup = BeautifulSoup(fp, 'html.parser')

for unidades_interessadas in soup.find_all('div', {'class' : 'ng-star-inserted'}):
  print(unidades_interessadas.text)