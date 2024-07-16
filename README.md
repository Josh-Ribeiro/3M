# TCC
    

# Bot de automação para envio de emails 📨

## Imports utilizados 📦
### => smtplib
### => MIMEText from email.mime.text
### => MIMEMultipart from email.mime.multipart

- Nesse código, o objetivo principal é automatizar uma tarefa comum do dia a dia, contudo, fizemos ele pensado em mostrar as diferenças de um BOT para uma IA.
O código consiste em Ler os emails destinatários, copiar a mensagem a ser enviada e depois construi-lá em um corpo de email, depois envia a cada um dos emails destinatários, porém, se o BOT identificar que o email do destinatário não existe (as vezes por erro de sintaxe), ele informa que não foi possível enviar o email ao destinatário.
Foi integrado ao Bot, um template em html para email, para tornar mais didático e "bonito" o projeto, que está atualmene finalizado e sem nenhuma modificação a fazer.
