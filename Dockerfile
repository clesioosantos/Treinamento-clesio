# Usar uma imagem base do Python
FROM python:3.8-slim

# Definir o diretório de trabalho no container
WORKDIR /app

# Copiar o arquivo requirements.txt para o container
COPY requirements.txt requirements.txt

# Instalar as dependências
RUN pip install -r requirements.txt

# Copiar o restante dos arquivos da aplicação para o container
COPY . .

# Definir a variável de ambiente para evitar buffer de saída
ENV PYTHONUNBUFFERED=1

# Expor a porta em que o Flask será executado
EXPOSE 5000

# Comando para executar o aplicativo Flask
CMD ["python", "app.py"]