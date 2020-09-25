


![the_raking_project](imagenes/cabecera.png)











# The Ranking. Desarrollo de API e integración con MongoDB

En este proyecto el objetivo principal es analizar las pull request que hemos realizado en GitHub, hasta el momento, los alumnos del bootcamp de data de Ironhack 0820.
Para ello desarrollaremos una API en Flask e integraremos esta API con la base de datos MongoDB.


## Procedimiento

1. En el archivo api_github buscamos los todos los datos que necesitamos con la API de GithHuh y los guardamos en un archivo json que luego importaremos a MongoDB.

2. Para acceder a la información almacenada, a través de un servidor local, realizamos peticiones a nuestra base de datos.

## Archivos

- server.py: Configuración de servidor local.
- database.py: Conexión de la base de datos de MongoDB.
- src/app.py: Creación de Flask para poder lanzar la API.
- controllers (labs & students): código para los endpoints solicitados en el ejercicio.
- .env: Aloja la key para conectarnos con la API de GitHub, el puerto y la URL para acceder a base de datos de MongoDB.


## Endpoints

1. Students

- /student/create/<studentname> (GET)
    
Enviamos el nombre de un alumno que no está en la base de datos y crea un resgistro nuevo devolviendo un id para esa persona.
    
- /student/all (GET)

Devuelve el listado de todos los alumnos contemplados en la base de datos.
      
2. Labs
    
- /lab/create/<name> (POST)
    
Buscamos un lab para anazalizarlo y la base de datos devuelve el identificador de dicho ejercicio.
    
- /lab/<Title>/meme
    
Obtenemos un meme al azar de las pull request de los alumnos.
    
## Principales fuentes consultadas
    
[Flask](https://flask.palletsprojects.com/en/1.1.x/)
[PyMongo](https://pymongo.readthedocs.io/en/stable/)
[MongoDB](https://www.mongodb.com/)
    

    





    
    
    
    
    
    

