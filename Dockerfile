# Usar una imagen base de Python
FROM python:3.10.12

# Establecer el directorio de trabajo en el contenedor
WORKDIR /app

# Copiar los requerimientos e instalar las dependencias
COPY requirements.txt .
RUN python -m pip install --upgrade pip && \
    python -m pip install -r requirements.txt

# Copiar el resto del código de la aplicación
COPY . .

# Ejecutar el comando para aplicar migraciones de Django
RUN python manage.py migrate --noinput

# Ejecutar el comando para recolectar archivos estáticos en la ubicación configurada
RUN python manage.py collectstatic --noinput --clear

# Exponer el puerto 8002 (product_manager usa este puerto por defecto)
EXPOSE 8002

CMD ["python", "manage.py", "runserver", "0.0.0.0:8002"]

