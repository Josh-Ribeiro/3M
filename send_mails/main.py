import os
from dotenv import load_dotenv 

# => Função para ler os emails do arquivo
def ler_emails_arquivo(nome_arquivo):
    with open(nome_arquivo, 'r') as file:
        emails = [linha.strip() for linha in file.readlines()]
    return emails

if __name__ == "__main__":
    os.chdir('/workspaces/Elysium_py/TCC')
    load_dotenv()

    import smtplib
    from email.mime.text import MIMEText
    from email.mime.multipart import MIMEMultipart

    # => Substitua pelos seus dados
    seu_email = os.getenv('login_email')
    app_password = os.getenv('password_app')

    caminho_arquivo_emails = 'emails.txt'
    destinatarios = ler_emails_arquivo(caminho_arquivo_emails)
    
    assunto = "Olá Mundo!"
    corpo_email_html ="""
    <html>
<head>
    <meta charset="UTF-8">
    <title>Exemplo de Template de Email</title>
    <link rel="preconnect" href="https://fonts.googleapis.com">
    <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
    <link href="https://fonts.googleapis.com/css2?family=Hanalei+Fill&family=Rock+Salt&family=Vina+Sans&family=Wittgenstein:ital,wght@0,400..900;1,400..900&display=swap" rel="stylesheet">
    <style>
        body {
            font-family: "Wittgenstein", serif;
            font-optical-sizing: auto;
            font-weight: 500;
            font-style: normal;
            margin: 1%;
            padding: 1px;
            background-image: url(fundo.jpg);
            background-size: 100%;
            padding: center;
        }

        ::-webkit-scrollbar { 
            width: 0px;
        } 

        .container {
            background: fixed;
            width: 100%;
            max-width: 600px;
            margin: auto;
            padding: 20px;
            height: 700px;
            background-color: #2D2B33;
            border-radius: 3%;
            box-shadow: 0 0 10px;

        }
        .header {
            background-color:#2D2B33;
            background: fixed;
            color: white;
            text-align: center;
            padding: 10px 0;
        }
        .content {
            padding: 20px;
            background-color:#2D2B33;
            background: fixed;
        }
        .footer {
            text-align:center;
            padding: 0px;
            width: 600px;
            font-size: 18px;
            color: #fcfcfc;
            background: fixed;
        }

        p {
            color: white;
        }
    </style>
</head>
<body>
    <div class="container">
        <div class="header">
            <h1>Equipe JHC</h1>
        </div>
        <div class="content">
            <p>Olá,</p>
            <p>Esse e-mail foi criado pela equipe JHC, ele é um bot que envia e-mails automaticamente. Apelidado de Botin :D, Ele foi desenvolvido para servir de projeto para o TCC da equipe.</p>
            <p>Obrigado pela atenção! 💻</p>
            <iframe src="https://giphy.com/embed/26tn33aiTi1jkl6H6" width="580" height="269" style="" frameBorder="0" class="giphy-embed" allowFullScreen></iframe><p><a href="https://giphy.com/gifs/screen-monitor-closeup-26tn33aiTi1jkl6H6"></a>
        </div>
        <div class="footer">
            <p>Serviços JHC.</p>
        </div>
    </div>
</body>
</html>"""

    try:

        # => Crie uma conexão com o servidor SMTP
        with smtplib.SMTP("smtp.gmail.com", 587) as smtp_server:
        # => Ative a segurança TLS
            smtp_server.starttls()
        # => Faça login no servidor
            smtp_server.login(seu_email, app_password)

            for destinatario in destinatarios:
                msg = MIMEMultipart()
                msg['From'] = seu_email
                msg['To'] = destinatario
                msg['Subject'] = assunto

                # => Crie um objeto MIMEText para o corpo do email
                corpo_msg = MIMEText(corpo_email_html, 'html')
                msg.attach(corpo_msg)

                # => Envia o email
                smtp_server.sendmail(seu_email, destinatario, msg.as_string())
                print(f"Email enviado para {destinatario}")

        print("Todos os emails foram enviados com sucesso!")
    except smtplib.SMTPAuthenticationError:
        print("Erro de autenticação. Verifique seu email e senha.")
    except smtplib.SMTPException as e:
        print(f"Ocorreu um erro ao enviar o email: {e}")
    except Exception as e:
        print(f"Ocorreu um erro inesperado: {e}")