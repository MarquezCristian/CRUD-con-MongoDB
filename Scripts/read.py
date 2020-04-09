from pymongo import MongoClient
#Creando conexiones para conectar con Mongo db
client =MongoClient('localhost:27017')
db= client.EmployeeData

#Funcion para leer data en Mongo db
def read():
    try:
        empcol =db.Employees.find()
        print('\n Toda la informacion de EmployeeData Database\n')
        for emp in empcol:
            print(emp)

    except ImportError:
        platform_specific_module =None         
