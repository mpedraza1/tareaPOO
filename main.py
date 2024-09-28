from db.db import MySQLDatabase
from business.Student import Student
from presentation.user_interface import handle_input
from config import DB_CONFIG

def main():
    # Inicializar la base de datos
    database = MySQLDatabase(**DB_CONFIG)
    
    # Inicializar el servicio de usuario
    user_service = Student(database)
    
    # Ejecutar la interfaz de consola
    handle_input(user_service)
    
    # Cerrar la conexión a la base de datos al final
    database.close()

if __name__ == '__main__':
    main()
