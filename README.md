# Aplicación de Gestión de Productos

## Características

- Crear, ver, actualizar y eliminar productos.
- Crear, ver, actualizar y eliminar huella del producto.
- Crear, ver, actualizar y eliminar precios.
- Crear, ver, actualizar y eliminar descuentos.
- Crear, ver, actualizar y eliminar impuestos.
- Filtrar huellas por producto.
- Filtrar precios por producto.
- Filtrar descuentos por producto.
- Filtrar impuestos por producto.

## Tecnologías Utilizadas

- Django: Framework web de alto nivel escrito en Python.
- PostgreSQL: Sistema de gestión de bases de datos relacional.

## Configuración del Entorno

###  Clona el repositorio desde GitHub:

git clone https://github.com/dgguzmangr/product_manager.git

### Crea y activa un entorno virtual:

python -m venv venv
source venv/bin/activate  # En Linux/Mac
source\venv\Scripts\activate   # En Windows

### Instala las dependencias del proyecto:

pip install -r requirements.txt

### Configura la base de datos PostgreSQL en settings.py:

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': config('db_name'),
        'USER': config('user_db'),
        'PASSWORD': config('password'),
        'HOST': config('db_host'),
        'PORT': config('db_port'),
    }
}

### Realiza las migraciones:

python manage.py makemigrations
python manage.py migrate

### Ejecuta el servidor de desarrollo:

python manage.py runserver

## Uso

Abre tu navegador web y accede a
- http://localhost:8000/redoc/
- http://localhost:8000/swagger/
- http://127.0.0.1:8000/admin/