from pymongo import MongoClient
#Creando conexiones que se comuniquen con Mongo # DEBUG:
client=MongoClient('localhost:27017')
db = client.EmployeeData

#Funcion para insertar data en mongo db
def insert():
    try:
        employeeid = input('Ingresa ID del empleado: ')
        employeename = input('Ingresar nombre: ')
        employeeage =input('Ingresar edad: ')
        employeecountry = input('Ingresar pais: ')
        db.Employees.insert_one (
        {
            "id": employeeid,
            "name": employeename,
            "age": employeeage,
            "country":employeecountry
        }
        )
        print ('Inserted data successfully')

    except ImportError:
        platform_specific_module = None
