# Recomendaciones para ejecutar el proyecto

Ejecutar los siguiente comandos iniciales:
```cmd
python manage.py migrate
```

```cmd
python manage.py makemigrations
```

```cmd
python manage.py createsuperuser
```

## Ejecutar pruebas unitarias
```cmd
python manage.py test
```

# Variables de entornos
Para que el proyecto lea las variables de entorno se debe crear un archivo llamado _.env_ e incluir las siguientes variables:

```cmd
SECRET_KEY=django-insecure-(w7d9$##n6bp=xep7wx!=aoxczlswf=bo4!$729%_+!zdn$o+!
DEBUG=True
SETTINGS=local
DATABASE_NAME=local
```

# CORS
En la configuracion de la aplicacion (archivo _settings.py_ -> _base.py_ -> variable _CORS_ALLOWED_ORIGINS_) se especifica que la aplicacion solo acepta llamados del _localhost_, para que la aplicacion acepte tambien llamados de alguna aplicacion front su dominio debe agregarse al listado de _CORS_ALLOWED_ORIGINS_.

# Pasos para consumir algun _endpoint_
1. Iniciar sesion: Esto se logra consumiento el endpoint con URI ```/user/login/```, el cual retorno un diccionario con el token de acceso y el token de refresco.
2. Agregar el token de acceso dado, de tipo _Bearer_ a cada peticion realizada a _Task_.

# Diagrama de clases
```mermaid
classDiagram
		%% Classes definition
		class User {
				+Int id
				+Str username
				+Str password
				+Str first_name
				+Str last_name
				+Str email
				+Tasks[0..*] tasks
		}
		<<Default_Django_User_model>> User
		class AbstractTask {
				+Int id
				+Str title
				+Str description
				+Enum state = 0
				+Datetime creation_date = today
				+Boolean deleted = False
		}
		<<Abstract>> AbstractTask
		class Task {
				+Datetime ending_date = None
				+Enum priority = 0
				+Enum tag = "NT"
				+User user
		}
		class State {
				UNCOMPLETED = 0
				COMPLETED = 1
		}
		<<Enumeration>> State
		class Priority {
				LOW = 0
				MEDIUM = 1
				HIGH = 2
		}
		<<Enumeration>> Priority
		class Tag {
				JOB = "JB"
				UNIVERSITY = "UN"
				HOME = "HM"
				SOCIAL = "SC"
				NO_TAG = "NT"
		}
		<<Enumeration>> Tag
		
		%% Relationships
		User "1" -- "0..*" AbstractTask: owns
		AbstractTask <|-- Task
		AbstractTask *-- State
		Task o-- Priority
		Task o-- Tag

		
```

# Modelo entidad-relacion
```mermaid
erDiagram
		USER ||--o{ TASK : owns
		USER {
        int id PK
				string username
				string password
        string first_name
				string last_name
        string email
    }
		TASK {
				int id PK
				string title
				string description
        string state
				datetime creation_date
        boolean deleted
				datetime ending_date
				int priority
				string tag
				int user_id FK
		}
```