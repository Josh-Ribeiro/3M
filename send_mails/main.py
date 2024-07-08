import os
from dotenv import load_dotenv 

if __name__ == "__main__":
    os.chdir('/workspaces/Elysium_py/TCC')
    load_dotenv()

    import smtplib
    from email.mime.text import MIMEText
    from email.mime.multipart import MIMEMultipart

    # => Substitua pelos seus dados
    seu_email = os.getenv('login_email')
    app_password = os.getenv('password_app')

    destinatarios = ['csbj0714@gmail.com', 'josufribeiro@gmail.com', 'hugosantoss093@gmail.com']
    assunto = "Olá Mundo!"
    corpo_email = "Este é um email de teste usando a biblioteca smtplib em Python."

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
                corpo_msg = MIMEText(corpo_email, 'plain')
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