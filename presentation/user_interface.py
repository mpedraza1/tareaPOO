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
            name = input("Nombre: ")
            age = int(input("Edad: "))
            rut = input("Rut: ")
            mail = input("Mail: ")
            asignatura = input("Asignatura: ")
            promedio = int(input("Promedio: "))
            user_service.add_user(name,age,rut,mail, asignatura, promedio)
            print("Usuario agregado con éxito.")

        elif option == '2':
            users = user_service.get_users()
          
            showStudentTable(users)
        elif option == '3':
            user_id = int(input("ID del usuario: "))
            name = input("Nuevo nombre: ")
            age = int(input("Nueva edad: "))
            user_service.update_user(user_id, name, age)
            print("Usuario modificado con éxito.")

        elif option == '4':
            user_id = int(input("ID del usuario a eliminar: "))
            user_service.delete_user(user_id)
            print("Usuario eliminado.")

        elif option == '5':
            break

        else:
            print("Opción inválida.")

def showStudentTable(users):

    if not users:
        raise ValueError("No hay registros")
    
    headers = ["RUT", "Nombre", "Edad", "Mail", "Asignatura", "Promedio"]

    print(tabulate(users, headers, tablefmt="grid"))