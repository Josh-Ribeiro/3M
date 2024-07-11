import requests

link = 'https://451f32f1-a729-4d48-82f2-b652cd2768f9-00-2qbbihriywe7h.janeway.replit.dev/'

requisicao = requests.get(link)

print(requisicao.json())