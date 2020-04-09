from pymongo import MongoClient
#Creando conexion para comunicar con Mongo DB
client =MongoClient('localhost:27017')
db =client.EmployeeData

#Funcion para actualizar data en Mongo db
def update():
    try:
        criteria=input('\n Ingresar Id para actualizar')
        name =input('\n Ingresar nombre para actualizar \n')
        age= input('\n Ingresar edad para actualizar\n')
        country = input ('\n Ingresar pais para actualizar\n')

        db.Employees.update_one(
        {"id":criteria},
        {
           "$set":{
              "name":name,
              "age":age,
              "country":country

           }
        }
        )
        print("\n Se actualizo correctamente\n")
    except ImportError:
        platform_specific_module = None    
