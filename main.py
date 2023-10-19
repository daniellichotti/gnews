import requests
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
import re
from datetime import datetime

def enviar(corpo,destinos):
    # Configurações do servidor SMTP do Gmail
    smtp_server = 'smtp.gmail.com'
    smtp_port = 587  # Usar 465 para SSL
    smtp_username = 'danielclichotti@gmail.com'
    smtp_password = 'uvuz muoa vtdl zlde'

    # Configurações do e-mail
    de = 'danielclichotti@gmail.com'
    para = 'danielclichotti@gmail.com'
    assunto = 'news'

    # Criar a mensagem de e-mail
    mensagem = MIMEMultipart()
    mensagem['From'] = de
    mensagem['To'] = ', '.join(destinos)
    mensagem['Subject'] = assunto

    # Adiciona a parte do corpo do e-mail
    parte_html = MIMEText(corpo, 'html')
    mensagem.attach(parte_html)

    # Configuração do servidor SMTP e envio do e-mail
    try:
        servidor_smtp = smtplib.SMTP(smtp_server, smtp_port)
        servidor_smtp.starttls()  # Use esta linha se estiver usando TLS
        servidor_smtp.login(smtp_username, smtp_password)
        texto_do_email = mensagem.as_string()
        servidor_smtp.sendmail(de, destinos, texto_do_email)
        servidor_smtp.quit()
        print("E-mail enviado com sucesso!")
    except Exception as e:
        print(f"Erro ao enviar o e-mail: {str(e)}")

def info():
    url = "https://gnews.io/api/v4/top-headlines?category=general&lang=pt-br&country=br&max=20&apikey=07572f54960cfa96749c8b74f2830255"
    response = requests.get(url)
    # Verifica se a requisição foi bem-sucedida (código de status 200)
    if response.status_code == 200:
        
        data = response.json()  # Converte a resposta para JSON, se aplicável
        #print(type(data["articles"][0]))
        corpo_email = ''
        for artigos in data["articles"]:
            title = artigos['title']
            description = artigos['description']
            content = artigos['content']
            content = re.sub(r'\s*\[.*\]$', '', content)
            url = artigos['url']
            image = artigos['image']
            publishedAt = artigos['publishedAt']
            publishedAt = datetime.strptime(publishedAt, "%Y-%m-%dT%H:%M:%SZ")
            publishedAt = publishedAt.strftime("%d/%m/%Y às %H:%M:%S")
            sourceName = artigos['source']['name']
            sourceUrl = artigos['source']['url']
            #print('Título: '+title)x
            #print('Descrição: '+description)x
            #print('Conteúdo: '+content)*****
            #print('Link: '+url)x
            #print('Imagem: '+image)
            #print('Data: '+publishedAt)x
            #print('Fonte: '+sourceName)
            #print('Link da fonte: '+sourceUrl)
            texto = f'<hr><h2>{title}</h2>\n<img class="imagem" src="{image}" alt="">\n<h3>{description}</h3>\n<p>{content}</p>\n<p>Fonte: <a href="{url}">{sourceName}</a><br>{publishedAt}</p>\n'
            corpo_email = corpo_email + texto
        #corpo_email = f'Título: {title}\nDescrição: {description}\nLink: {url}\nData: {publishedAt}\n'
        style = """
            h1 {
            font-family: 'Comic Neue', cursive, sans-serif;
            font-weight: bold;
            font-size: 3rem;
            color: #FF0000;
        }
            h2 {
            font-family: 'Comic Neue', cursive, sans-serif;
            font-weight: bold;
            font-size: 2rem;
        }
            h3 {
            font-family: 'Comic Neue', cursive, sans-serif;
            font-weight: light;
            font-size: 1rem;
        }
        p {
            font-family: 'Comic Neue', cursive, sans-serif;
            font-weight: light;
            font-size: 1rem;
        }
        .imagem {
                width: 300px;  /* Defina a largura desejada para as imagens */
                height: auto;  /* Mantenha a proporção original da imagem */
                margin: 10px;  /* Adicione margens para espaçamento entre as imagens */
            }
        """
        corpo_html = f"""
        <html>
        <head>
        <link rel="preconnect" href="https://fonts.googleapis.com">
        <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
        <link href="https://fonts.googleapis.com/css2?family=Comic+Neue:wght@300;700&display=swap" rel="stylesheet"><style>
        {style}
        </style>
        </head>
        <body>
            <h1>Dani news, suas notícias em comic sans!</h1>
            {corpo_email}
        </body>
        </html>
        """
        
        destinos = ['danielclichotti@gmail.com', 'aida.lichotti@gmail.com', 'epelizon@gmail.com']
        enviar(corpo_html, destinos)
        #enviar(corpo_email)
    else:
        print(f"Erro na requisição: {response.status_code}")
    

def main():
    # Lógica principal do programa
    info()

# Verifica se o script está sendo executado como o programa principal
if __name__ == "__main__":
    main()



