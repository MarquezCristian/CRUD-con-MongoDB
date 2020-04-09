from pymongo import MongoClient
#Creando conexion para comunicar con Mongo db
client=MongoClient('localhost:27017')
db =client.EmployeeData

#Funcion para borra data de Mongo db
def delete():
    try:
        criteria = input('\nIngresar Id del empleado para borrar\n')
        db.Employees.delete_many({"id": criteria})
        print('\n Eliminacion satisfactoria\n')
    except ImportError:
        platform_specific_module =None     
