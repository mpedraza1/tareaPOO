from tabulate import tabulate

def display_menu():
    print("1. Agregar Usuario")
    print("2. Ver Usuarios")
    print("3. Modificar Usuario")
    print("4. Eliminar Usuario")
    print("5. Salir")

def handle_input(user_service):
    while True:
        display_menu()
        option = input("Selecciona una opción: ")

        if option == '1':
            nombre = input("Nombre: ")
            edad = int(input("Edad: "))
            rut = input("Rut: ")
            mail = input("Mail: ")
            asignatura = input("Asignatura: ")
            promedio = int(input("Promedio: "))
            user_service.add_user(nombre,edad,rut,mail,asignatura,promedio)
            print("Usuario agregado con éxito.")

        elif option == '2':
            users = user_service.get_users()
            showStudentTable(users)

        elif option == '3':
            users = user_service.get_users()
            showStudentTable(users)

            rut = input("Rut del usuario a modificar: ")
            validacion=next((num[0] for num in users if num[0] == rut),None)
            if not validacion:
                print("No existe registro")

            nombre = input("Nuevo nombre: ")
            edad = int(input("Nueva edad: "))
            mail = input("Mail: ")
            asignatura = input("Asignatura: ")
            promedio = int(input("Promedio: "))
            user_service.update_user(nombre,edad,rut,mail,asignatura,promedio)
            print("Usuario modificado con éxito.")

        elif option == '4':
            rut = input("Rut del usuario a eliminar: ")
            user_service.delete_user(rut)
            print("Usuario eliminado.")

        elif option == '5':
            break

        else:
            print("Opción inválida.")

def showStudentTable(users):

    if not users:
        print("No hay usuarios")
        return
    
    headers = ["RUT", "Nombre", "Edad", "Mail", "Asignatura", "Promedio"]

    print(tabulate(users, headers, tablefmt="fancy_grid"))