import os
from dotenv import load_dotenv 

# => Função para ler os emails do arquivo
def ler_emails_arquivo(nome_arquivo):
    with open(nome_arquivo, 'r') as file:
        emails = [linha.strip() for linha in file.readlines()]
    return emails

def ler_template_html(caminho_arquivo):
    with open(caminho_arquivo, 'r', encoding='utf-8') as file:
        return file.read()

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
    
    caminho_templete_html = 'template_email.html'
    corpo_email_html = ler_template_html(caminho_templete_html)
        
    assunto = "Olá Mundo!"
    
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