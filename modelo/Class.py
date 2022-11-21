from pymongo import MongoClient

def getConexion():
    MONGO_URL = 'mongodb://localhost' #La ubicación de la base de datos

    client = MongoClient(MONGO_URL)

    db = client['Pruebas'] #la base de datos

    collection =db['Usuario'] #La coleccion

    return collection

class Persona:

    # ========= Atributos =========
    name = '' #Solo se puede usar en la misma clase
    age = 0
    sex = ''

    # ========= Metodos de la clase =========

    def __init__(self,name,age,sex): #Contructor
       self.name = name
       self.age = age
       self.sex = sex
    
    def getSex(self):
        return self.sex
    
    def getAge(self):
        return self.age
    
    def getName(self):
        return self.name

    def toString(self):
        return "Datos usuario:\n {} \n {} \n {}".format(self.getName(),self.getAge(),self.getSex())


class UsuarioDAO:

    def listarUsuario():

        conexion = getConexion()

        usuarios = conexion.find()
        list = []
        for usuario in usuarios:
            user = Persona(usuario['name'],usuario['age'],usuario['sex'])
            list.append(user)
        
        return list


i = 0
list = UsuarioDAO.listarUsuario()

#p = Persona("Luis",28,"Hombre");
#p2 = Persona("Manuel",28,"Hombre");

#list.append(p)
#list.append(p2)

while i < len(list):
    print(i)
    print(list[i].toString())
    i +=1
print()