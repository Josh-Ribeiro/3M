import string
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score

# Função para gerar dados de treinamento
def generate_data():
    letters = list(string.ascii_letters)  # Todas as letras maiúsculas e minúsculas
    digits = list(string.digits)          # Todos os dígitos de 0 a 9
    all_characters = letters + digits

    # Cria etiquetas (0 para letras e 1 para números)
    labels = [0] * len(letters) + [1] * len(digits)

    # Converte caracteres para valores numéricos usando seus códigos ASCII
    data = np.array([ord(char) for char in all_characters]).reshape(-1, 1)

    return data, labels

# Gera os dados de treinamento
data, labels = generate_data()

# Divide os dados em conjuntos de treinamento e teste
X_train, X_test, y_train, y_test = train_test_split(data, labels, test_size=0.2, random_state=42)

# Cria e treina o classificador
classifier = RandomForestClassifier(n_estimators=100, random_state=42)
classifier.fit(X_train, y_train)

# Faz previsões no conjunto de teste
y_pred = classifier.predict(X_test)

# Calcula a precisão do classificador
accuracy = accuracy_score(y_test, y_pred)
print(f"Accuracy: {accuracy * 100:.2f}%")

# Função para classificar um caractere
def classify_character(char):
    if char in string.ascii_letters:
        return "Letra"
    elif char in string.digits:
        return "Número"
    else:
        return "Outro"

# Função para classificar e contar tipos de caracteres em uma string
def classify_string(s):
    counts = {"Letra": 0, "Número": 0, "Outro": 0}
    for char in s:
        classification = classify_character(char)
        counts[classification] += 1
    return counts

# Lê o arquivo .txt e classifica cada string
def classify_from_file(file_path):
    try:
        with open(file_path, 'r') as file:
            lines = file.read().splitlines()
        
        for line in lines:
            if line:  # Verifica se a linha não está vazia
                counts = classify_string(line)
                print(f"String: {line}, Classificações: {counts['Letra']} letras, {counts['Número']} números, {counts['Outro']} outros")
    except FileNotFoundError:
        print(f"O arquivo {file_path} não foi encontrado. Verifique o caminho e tente novamente.")

# Testa a função de classificação a partir do arquivo
file_path = '/workspaces/Elysium_py/TCC/input.txt'  # Especifique o caminho absoluto se necessário
classify_from_file(file_path)
