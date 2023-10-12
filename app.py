from selenium import webdriver
from selenium.webdriver.common.by import By
import openpyxl

# Acessar site 
driver = webdriver.Chrome()
driver.get("https://www.novaliderinformatica.com.br/computadores-gamers")
#input() # Mantem o site aberto

# Pegar nome do produto
productName = driver.find_elements(By.XPATH,"//a[@class='nome-produto']")

# Pegar valor de preços
productPrice = driver.find_elements(By.XPATH,"//strong[@class='preco-promocional']")

# Criando a Planilha 
workbook = openpyxl.Workbook()

# Criando a Aba 'produtos' na planilha
workbook.create_sheet('produtos')

# Selecionando a Aba 'produtos' na planilha 
aba_produtos = workbook['produtos']

# Criando o cabeçalho da planilha 
aba_produtos['A1'].value = 'Produto'
aba_produtos['B1'].value = "Preço"


# Truque para pegar somente produtos que tiver (nome e preço)
# Inserir  nome de produtos e preços na Planilha Excel
for produto,preco in zip(productName,productPrice):
    aba_produtos.append([produto.text, preco.text])
    
# Salvar dados em planilhas
workbook.save('produtos.xlsx')
print("Fim da execução ")
