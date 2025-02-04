# Dashboard de Brain2Gain

Este proyecto integra un dashboard interactivo utilizando Dash para la visualización y FastAPI para la gestión de endpoints y autenticación. La aplicación está diseñada siguiendo principios SOLID y POO, utilizando dataclasses y type hints para mayor claridad y mantenibilidad.

## Características

- **CRUD y Gestión de Datos:**  
  Se manejan transacciones, stock, finanzas y análisis avanzado a través de un modelo de datos basado en dimensiones y hechos, que facilita la inferencia y análisis.
  
- **Dashboard Interactivo:**  
  Implementado con Dash y Plotly, con pestañas para gestionar transacciones, finanzas, indicadores y análisis avanzado.

- **API con FastAPI:**  
  Se exponen endpoints para autenticación y operaciones básicas. La integración se realiza mediante WSGIMiddleware para montar el dashboard en la misma aplicación.

- **Base de Datos PostgreSQL:**  
  Utilizamos PostgreSQL para la persistencia de datos. El esquema incluye tablas de dimensiones (productos, clientes, usuarios, tiempo) y una tabla de hechos (ventas) para análisis.

- **Contenerización:**  
  El proyecto se despliega con Docker y Docker Compose, facilitando su ejecución en entornos de desarrollo y producción.

## Estructura del Proyecto

├── app.py # Integración de FastAPI y montaje de Dash. 
├── dash_app.py # Clase Dashboard que configura el layout y callbacks de Dash. 
├── models.py # Modelos SQLAlchemy usando dataclasses y type hints. 
├── Dockerfile # Imagen Docker para la aplicación. 
├── docker-compose.yml # Orquestación de contenedores (aplicación y PostgreSQL). 
├── requirements.txt # Dependencias del proyecto. 
└── README.md # Este documento.


## Requisitos

- Python 3.9 o superior
- Docker y Docker Compose (opcional para desarrollo local)

## Instalación y Ejecución

1. **Clonar el repositorio:**

```
   git clone <URL_del_repositorio>
   cd my_dashboard
```

2. (Opcional) Crear un entorno virtual:

```
python3 -m venv venv
source venv/bin/activate

```

3. Instalar las dependencias:
```
pip install -r requirements.txt
Crear la base de datos (si no usas Docker Compose):
```


4. Con PostgreSQL instalado localmente, accede a la consola:
```
psql -U postgres
```

5. Luego ejecuta:
```
CREATE DATABASE mi_base;
CREATE USER usuario WITH ENCRYPTED PASSWORD 'contraseña';
GRANT ALL PRIVILEGES ON DATABASE mi_base TO usuario;
\q
```

6. Ejecutar la aplicación. Con Docker Compose:

```
docker-compose up --build
```

7. Sin Docker (local):
```
uvicorn app:app --host 0.0.0.0 --port 8000

```

Acceder a la aplicación:

	- Dashboard: http://localhost:8000/dashboard
	- Formulario de login: http://localhost:8000/logi
