import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import pandas as pd
import numpy as np
import time

server = "smtp.gmail.com"
port = 587

login = "guimonteiro@sempreceub.com"  
password = "Inglescom12"

df = pd.read_excel(r'C:\Users\guipi\Desktop\python\Inscrição - Oficina de Ciência de Dados (respostas).xlsx')
resultados = df[['Nome completo', 'E-mail (@sempreceub)']]

for _, row in resultados.iterrows():
    nome = row['Nome completo']
    email = row['E-mail (@sempreceub)']
    
    msg = MIMEMultipart()
    msg['From'] = login
    msg['To'] = str(email) 
    msg['Subject'] = "Atividade valendo Menção - Oficina de CD"
    
    body = f"""Boa noite, galera!

Na nossa aula de amanhã, iremos estar disponíveis para sanar dúvidas gerais sobre os conteúdos que já vimos até agora.

Além disso, esta será nossa última aula antes do conteúdo de machine learning, caso tenham dúvidas sobre esta parte, não esqueçam de levá-las.

Em caso de dúvida, não hesitem em mandar mensagem.

Boa noite, até amanhã!
"""
    
    msg.attach(MIMEText(body, 'plain'))
    
    try:
        with smtplib.SMTP(server, port) as smtp_server:
            smtp_server.starttls()  # Iniciar criptografia TLS
            smtp_server.login(login, password)
            time.sleep(10)
            text = msg.as_string()
            smtp_server.sendmail(login, email, text)
            print(f"E-mail enviado com sucesso para {nome}!")
    except Exception as e:
        print(f"Falha ao enviar o e-mail: {e}")
        
