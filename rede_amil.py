from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
import os

options = webdriver.ChromeOptions()
options.add_argument('--no-sandbox')
options.add_argument('--ignore-certificate-errors-spki-list')
options.add_argument('--ignore-ssl-errors')
options.add_argument('--ignore-certificate-errors')
options.add_experimental_option('excludeSwitches', ['enable-logging'])

driver = webdriver.Chrome(options=options)
driver.minimize_window()

print("\nCarregando...\n")
driver.get("https://planosodontologicoamil.com.br/rede-credenciada-rio-de-janeiro/")
bairros_busca = driver.find_elements_by_class_name("accredited-network__result__neighbourhood")
bairros = list(set([x.text for x in bairros_busca]))
bairros.sort()

def busca():
    output = open("output.txt", "w")
    bloco_busca = 0
    erro = False
    
    while erro == False:
        
        try:
            clinica = driver.find_elements_by_class_name("accredited-network__result ")[bloco_busca]
            bairro_check = driver.find_elements_by_class_name("accredited-network__result__neighbourhood")[bloco_busca]
            
            if bairro_check.text == bairros[bairro_escolhido]:
                print("+1")
                output.write(clinica.text + "\n==============================================================\n\n")
                bloco_busca += 1
            else:
                bloco_busca += 1
        
        except NoSuchElementException:
            erro = True
    
    output.close()
    print("Cabo")

os.system('cls')

print('''
======================================
        BUSCAR REDES AMIL DENTAL
======================================
''')

for numero, bairro in enumerate(bairros):
    print(numero, bairro)

bairro_escolhido = int(input("\nDigite a opção escolhida: "))

print("\nCarregando...\n")

busca()
