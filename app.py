from modelo.Class import PersonaDAO

def menu():
    
    return int(input("""
    ======= Registro de usuario =======
    ======= 1.Agregar usuario
    ======= 2.Modificar usuario
    ======= 3.Información sobre usuario
    ======= 4.Eliminar usuario
    ======= 5.Salir del registro de usuario
    Opcion:"""))

def menuModificar():
    return int(input("""
    ======= Opciones de modificación =======
    ======= 1.Nombre 
    ======= 2.Edad
    ======= 3.Sexo
    Opcion:"""))

def menuVer():
    return int(input("""
    ======= Opciones de modificación =======
    ======= 1.Ver todas los usuarios
    ======= 2.Ver usuario en especifico
    ======= 3.Salir
    Opcion:"""))

def verUsuarios():

   usuarios = PersonaDAO.listarUsuario()

   for usuario in usuarios:
      print("""
      ========== {} ==========
      ====== Edad: {}
      ====== Sexo: {}
      """.format(usuario.getName(),usuario.getAge(),usuario.getSex()))

def verUsuario():
   name = input("Ingresar el nombre:")
   usuario = PersonaDAO.getUsuario(name)

   print("""
   ========== {} ==========
   ====== Edad: {}
   ====== Sexo: {}
   """.format(usuario.getName(),usuario.getAge(),usuario.getSex()))
   
def main():

    op = menu()
    while(op != 5):

        if(op == 3):
            
            opVer = menuVer()

            while(opVer != 3):

                if(opVer == 1):
                    verUsuarios()
                if(opVer == 2):
                    verUsuario()
               
                opVer = menuVer()
            print("\t=========== Ciudad visualizada ===========")
        op = menu()

    print("\t=========== Programa finalizado ===========")


if __name__ == '__main__':
    main()