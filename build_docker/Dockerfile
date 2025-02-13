# Dockerfile
FROM python:3.13

WORKDIR /app

# Installation des dépendances python
RUN pip install --upgrade pip
COPY requirements.txt /app
RUN pip3 install -r requirements.txt

# Exposition du port
EXPOSE 8443

# Commande de démarrage (peut être remplacée par un script spécifique)
CMD ["python", "app.py"]