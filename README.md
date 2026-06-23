<div align="center">
  <br>
  <img src="Clinica/static/Clinica/img/logo.svg" alt="Patitas Felices" width="120">
  <br>
  <h1>🐾 Patitas Felices</h1>
  <p><strong>Sistema de Gestión Veterinaria</strong></p>
  <p>
    <img src="https://img.shields.io/badge/Django-6.0.6-092E20?logo=django&logoColor=white" alt="Django">
    <img src="https://img.shields.io/badge/Python-3.14-3776AB?logo=python&logoColor=white" alt="Python">
    <img src="https://img.shields.io/badge/Bootstrap-5.3-7952B3?logo=bootstrap&logoColor=white" alt="Bootstrap">
    <img src="https://img.shields.io/badge/license-MIT-green" alt="License">
  </p>
  <br>
</div>

---

##  Descripción

**Patitas Felices** es un sistema web desarrollado en Django para la gestión integral de pacientes de una clínica veterinaria. Permite registrar, consultar, modificar y eliminar mascotas de forma sencilla e intuitiva, con una interfaz moderna y responsive.

---

##  Funcionalidades

| Funcionalidad | Descripción |
|---|---|
| **Registro de mascotas** | Formulario con nombre, especie, raza, edad, dueño, teléfono y foto |
| **Listado de pacientes** | Visualización en tarjetas con foto, datos y acciones |
| **Edición** | Modificación de datos de una mascota existente |
| **Eliminación** | Borrado con confirmación previa |
| **Panel admin** | Administración completa vía Django Admin |
| **Subida de fotos** | Cada mascota puede tener una foto asociada |

---

##  Tecnologías

- **Backend:** Django 6.0.6 (Python 3.14)
- **Frontend:** Bootstrap 5.3 + CSS personalizado
- **Iconos:** Bootstrap Icons
- **Imágenes:** SVG vectoriales personalizados
- **Base de datos:** SQLite3 (por defecto)
- **Almacenamiento:** `media/` para imágenes subidas

---

##  Estructura del Proyecto

```
Veterinarias/
├── Clinica/                     # Aplicación principal
│   ├── migrations/              # Migraciones de base de datos
│   ├── static/
│   │   └── Clinica/
│   │       ├── css/
│   │       │   └── styles.css   # Estilos personalizados
│   │       └── img/             # SVG e iconos
│   ├── templates/
│   │   ├── Base.html            # Plantilla base (layout + navbar)
│   │   └── Pages/
│   │       ├── Registro.html    # Formulario de alta/edición
│   │       ├── Mascotas.html    # Grid de mascotas
│   │       └── Confirmacion.html # Confirmación de eliminación
│   ├── __init__.py
│   ├── admin.py                 # Configuración del admin
│   ├── apps.py
│   ├── forms.py                 # FormularioRegistro (ModelForm)
│   ├── models.py                # Modelo Mascota
│   ├── urls.py                  # Rutas de la app
│   └── views.py                 # Vistas del sistema
├── media/
│   └── mascotas/                # Fotos subidas por usuarios
├── Veterinaria/
│   ├── __init__.py
│   ├── settings.py              # Configuración global
│   ├── urls.py                  # Rutas del proyecto
│   └── wsgi.py
├── db.sqlite3                   # Base de datos
├── manage.py
└── README.md
```

---

##  Instalación y Uso

### 1. Clonar el repositorio

```bash
git clone https://github.com/tu-usuario/patitas-felices.git
cd patitas-felices
```

### 2. Crear entorno virtual (opcional pero recomendado)

```bash
python -m venv venv
source venv/bin/activate      # Linux / macOS
venv\Scripts\activate         # Windows
```

### 3. Instalar dependencias

```bash
pip install django pillow
```

### 4. Ejecutar migraciones

```bash
python manage.py migrate
```

### 5. Crear superusuario (opcional)

```bash
python manage.py createsuperuser
```

### 6. Iniciar servidor

```bash
python manage.py runserver
```

### 7. Acceder

| Sitio | URL |
|---|---|
| Página principal | [http://127.0.0.1:8000/](http://127.0.0.1:8000/) |
| Panel admin | [http://127.0.0.1:8000/admin/](http://127.0.0.1:8000/admin/) |

---

##  Rutas de la API

| Método | Ruta | Vista | Descripción |
|---|---|---|---|
| GET | `/` | `Home` | Página de inicio |
| GET/POST | `/Registro/` | `Registro` | Registrar nueva mascota |
| GET | `/Mascotas/` | `VerMascotas` | Listar todas las mascotas |
| GET/POST | `/Modificacion/<id>/` | `Modificacion` | Editar mascota por ID |
| GET | `/Eliminar/<id>/` | `EliminarMascota` | Eliminar mascota por ID |

---

##  Modelo de Datos

### Mascota

| Campo | Tipo | Descripción |
|---|---|---|
| `ID_Mascota` | `AutoField` (PK) | Identificador único |
| `Nombre` | `CharField(50)` | Nombre de la mascota |
| `Especie` | `CharField(20)` | Perro / Gato / Ave / Roedor / Reptil / Otro |
| `Raza` | `CharField(50)` | Raza (opcional) |
| `Edad` | `IntegerField` | Edad en años |
| `Dueno` | `CharField(100)` | Nombre del dueño |
| `Telefono` | `CharField(20)` | Teléfono de contacto |
| `Foto` | `ImageField` | Foto de la mascota (opcional) |
| `Fecha_Registro` | `DateTimeField` | Fecha de alta (automática) |

---

##  Personalización

- **Colores:** Variables CSS en `Clinica/static/Clinica/css/styles.css` (`--primary`, `--secondary`, etc.)
- **Imágenes:** Los SVGs están en `Clinica/static/Clinica/img/` y son fácilmente reemplazables
- **Templates:** Extienden de `Base.html` — modifica el layout global ahí

---


### Usuarios
- User: Gareis o gareis
- Paswword: 1234

---

-User: Pablo o pablo
- Paswword: 1234

---
##  Licencia

Este proyecto está bajo la licencia MIT. Consulta el archivo `LICENSE` para más detalles.


