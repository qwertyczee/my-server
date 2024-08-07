# Použití oficiálního Python obrazu jako základ
FROM python:3.9-slim

# Nastavení pracovního adresáře
WORKDIR /app

# Kopírování requirements.txt do pracovního adresáře
COPY requirements.txt requirements.txt

# Instalace Python závislostí
RUN pip install -r requirements.txt

# Kopírování zbytku kódu do pracovního adresáře
COPY . .

# Nastavení environmentálních proměnných
ENV PORT=8080

# Exponování portu
EXPOSE 8080

# Spuštění aplikace
CMD ["python", "app.py"]
