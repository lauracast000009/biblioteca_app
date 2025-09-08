# 📚 API Biblioteca - Django REST Framework

Este proyecto implementa una API REST para la gestión de una biblioteca.  
Incluye operaciones CRUD para **Autores, Editoriales, Libros, Miembros y Préstamos**, con filtros básicos.

# 📚 API Biblioteca - Django REST Framework

Este proyecto implementa una API REST para la gestión de una biblioteca.  
Incluye operaciones CRUD para **Autores, Editoriales, Libros, Miembros y Préstamos**, con filtros básicos.

---

## ⚙️ Instalación y ejecución

```bash
# Clonar el repositorio
git clone https://github.com/lauracast000009/biblioteca_app.git
cd biblioteca_app

# Crear y activar entorno virtual
python -m venv env
source env/bin/activate   # Linux/Mac
.\env\Scripts\activate    # Windows

# Instalar dependencias
pip install -r requirements.txt

# Migrar la base de datos
python manage.py makemigrations
python manage.py migrate


# Ejecutar servidor
python manage.py runserver

Servidor por defecto:
http://127.0.0.1:8000/api/

## Documentacion
link https://documenter.getpostman.com/view/43885560/2sB3HkrgXS 
También puedes importar directamente el archivo:
Biblioteca.postman_collection.json