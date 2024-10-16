
import os
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
import time
import schedule

# baixa o editor de navergador pra dev antes de usar, lembra de baixar na mesma versão do seu navegador
# tambem não esquece de trocar a função do webdriver se vc não for usar o chrome como navegador
# emoji não funciona 

# cria um diretorio pra armazenar o historico de usuario, isso é pra não ter q  ficar scaneando qrcode
data_dir = r"C:\Users\guipi\Documents\New User Data"

# pra cirar o diretorio
if not os.path.exists(data_dir):
    os.makedirs(data_dir)

# coloca o caminho do seu navegador pra dev, acho bom colocar na mesma pasta que seu navegador estiver instalado
service = Service(r'C:\Program Files\Google\Chrome\Application\chromedriver.exe')

# Configura o driver do navegador, deixei a variavel com nome edge, preguiça
edge_options = Options()
edge_options.add_argument(f"--user-data-dir={data_dir}")
# edge_options.add_argument("--headless=new") # tira o comentario depois de rodar uma vez


driver = webdriver.Chrome(service=service, options=edge_options) # coloca a função respectiva do seu navegador
time.sleep(10)

driver.get("https://web.whatsapp.com/")

def grupo(group_name):
    try:
        # Localiza o grupo pelo nome
        search_box = driver.find_element("xpath", 
                                         '//*[@id="side"]/div[1]/div/div[2]/div[2]/div/div/p') 
        search_box.click()
        search_box.send_keys(group_name)
        search_box.send_keys(Keys.ENTER)
        time.sleep(5)

        print(f"Mensagem enviada para o grupo '{group_name}' com sucesso!")
    except Exception as e:
        print(f"Erro ao encontrar o grupo: {e}")

def envia_msg(mensagem):
    try:
        msg_box = driver.find_element("xpath", 
                                      '//*[@id="main"]/footer/div[1]/div/span[2]/div/div[2]/div[1]/div/div[1]/p') 
        msg_box.click()
        
        linhas = mensagem.split('\n') 
        
        for i, linha in enumerate(linhas):
            for char in linha:
                msg_box.send_keys(char)
                time.sleep(0.0001)  # Tempo de espera para simular digitação
            
            if i < len(linhas) - 1:  # Se não for a última linha
                # Simula Shift + Enter para quebra de linha
                ActionChains(driver).key_down(Keys.SHIFT).send_keys(Keys.ENTER).key_up(Keys.SHIFT).perform()
                time.sleep(0.1)
            
        time.sleep(10)
        msg_box.send_keys(Keys.ENTER)
        time.sleep(10)

        print(f"Mensagem enviada com sucesso!")
    except Exception as e:
        print(f"Erro ao enviar a mensagem: {e}")


mensagens = [

 """Aprofunde Seus Conhecimentos em Tecnologia! 

Oficinas de Backend 

Mergulhe no mundo do backend com Java, PHP, Python e Linux. 
Aprenda como essas tecnologias funcionam, e como criar soluções eficientes para suas aplicações. Ideal para quem quer conhecer como funciona a programação BackEnd!

PHP:
Data: 19/08/2024 a 02/12/2024
Hora: 14h às 16h, aulas todas Segundas e Quintas
Local: Campus Asa Norte, laboratório 1017
Inscrições: https://docs.google.com/forms/d/e/1FAIpQLSdsj0Vs2_5TfK1qnj7Mlk4ul9jt1tExfGvQabLuZAuAwNS0fw/viewform

Java:
Data: 19/08/2024 a 02/12/2024
Hora: 11h às 13h, aulas todas Terças e Quintas
Local: Campus Asa Norte, laboratório 1002
Inscrições: https://docs.google.com/forms/d/e/1FAIpQLSc7QTLL5BNPb-iOZfh9zltkJeysCKpWenDT3InLnYmcHZ0VKA/viewform

Python:
Data: 19/08/2024 a 02/12/2024
Hora: 17h30 às 19h, aulas todas Terças e Sextas
Local: Campus Asa Norte, laboratório 1002
Inscrições: https://docs.google.com/forms/d/e/1FAIpQLSdW-PdFqqx0eauY4lWfbFy37GZuFhVl6RIsCP92lXkQN6aZDQ/viewform

Linux:
Data: 19/08/2024 a 02/12/2024
Hora: 17h00 às 19h00, aulas todas as Quartas
Local: Campus Asa Norte, laboratório 5100
Inscrições: https://docs.google.com/forms/d/e/1FAIpQLScKiDu21zv3RLt7W2muhjTolgRcyNTjrNISw5tdNi0NdMOFmQ/viewform""", 
"""Aprofunde Seus Conhecimentos em Tecnologia! 

 Oficinas de Frontend 

Explore tecnologias como Flutter, React e Angular. Entenda como cada uma dessas tecnologias funciona, seus principais aspectos e como usá-las para desenvolver seus projetos!
Ideal para quem quer conhecer o desenvolvimento frontend com as ferramentas mais modernas!

Flutter:
Data: 19/08/2024 a 02/12/2024
Hora: 11h às 13h, aulas Segundas e Sextas
Local: Campus Asa Norte, laboratório 1017
Inscrições: https://docs.google.com/forms/d/e/1FAIpQLSczlRL-6vL7IfggaUpbcvkXDfjnKgboD_eCyp55RCVpsgmzXw/viewform

React:
Data: 19/08/2024 a 02/12/2024
Hora: das 17h às 19h, aulas todas Segundas e Quintas
Local: Campus Asa Norte, laboratório 1002
Inscrições: https://docs.google.com/forms/d/e/1FAIpQLSczlRL-6vL7IfggaUpbcvkXDfjnKgboD_eCyp55RCVpsgmzXw/viewform

Angular:
Data: 19/08/2024 a 02/12/2024
Hora: 14h às 16h, aulas todas Terças e Sextas
Local: Campus Asa Norte, laboratório 1002
Inscrições: https://docs.google.com/forms/d/e/1FAIpQLSczlRL-6vL7IfggaUpbcvkXDfjnKgboD_eCyp55RCVpsgmzXw/viewform""",
    """Aprofunde Seus Conhecimentos em Tecnologia! 

Oficina de Ciência de Dados 

Participe de um projeto completo em Ciência de Dados! Vamos passar por todas as etapas, desde a Análise Exploratória de Dados (EDA), Modelagem, até o Deploy com BI. 
Terá dinâmica para apresentar a área, ideal para quem deseja entender como funciona a Ciência de Dados e como ela pode transformar decisões e estratégias.

Ciência de Dados:
Data: 21/08/2024 a 04/12/2024
Hora: 11h às 13h, aulas todas as Quartas
Local: Campus Asa Norte, laboratório 1002
Inscrições: https://docs.google.com/forms/d/e/1FAIpQLSf0qJQzwtaX3y_gSmDYHouEnfYeQoX57qvctZDskwHOrVgb3A/viewform?usp=sf_link"""
]

indice_mensagem = 0

def job():
    grupo('Monitoria do Curso TI - Asa Norte')

    global indice_mensagem
    envia_msg(mensagens[indice_mensagem])
    
    # proximo indice
    indice_mensagem = (indice_mensagem + 1) % len(mensagens)
    
# timer para o bot, mudar para .minutes ou .hours
schedule.every(3).hours.do(job) 

print("Bot iniciado. Enviando mensagens a cada tres horas")

# executar
while True:
    
    schedule.run_pending()
    time.sleep(1)
