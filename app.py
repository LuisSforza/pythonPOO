from modelo.Class import conexion,Persona,Usuario

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
   
def main():

    op = menu()
    while(op != 5):

        if(op == 1):
            ingresarCiudad()

        if(op == 2):
            modificarCiudad()

        if(op == 3):
            
            opVer = menuVer()

            while(opVer != 3):

                if(opVer == 1):
                    verUsuarios()
                
                if(opVer == 2):
                    verUsuario()

                opVer = menuVer()

            print("\t=========== Ciudad visualizada ===========")

        if(op == 4):

            print("\nElimnar ciudad")

            ciudad = input("\nIngresar el nombre de la ciudad a eliminar:")

            if deleteCiudad(ciudad):
                print("\n ========== Ciudad elimnana exitosamente ==========")
            else:
                print("========== Error ==========")

        op = menu()

    print("\t=========== Programa finalizado ===========")


if __name__ == '__main__':
    main()