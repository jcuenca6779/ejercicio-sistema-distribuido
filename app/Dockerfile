# app/Dockerfile
# Usamos una imagen de Python oficial
FROM python:3.9-slim

# Establecemos el directorio de trabajo dentro del contenedor
WORKDIR /code

# Copiamos el archivo de requisitos e instalamos las librerías
COPY requirements.txt .
RUN pip install -r requirements.txt

# Copiamos el código de nuestra aplicación
COPY app.py .

# Exponemos el puerto en el que corre la app
EXPOSE 5000

# Comando para ejecutar la aplicación
CMD ["python", "app.py"]