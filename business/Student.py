class Student():
    rut:str
    nombre:str
    edad:int
    mail:str
    asignatura:str
    promedio:str
    
    def __init__(self, database):
        self.database = database

    def add_user(self, nombre, edad,rut,mail,asignatura,promedio):
        if edad < 0:
            raise ValueError("La edad no puede ser negativa.")
        self.database.create_record("users", (nombre, edad,rut,mail,asignatura,promedio))

    def get_users(self):
        return self.database.read_records()

    def update_user(self, user_id, name, age):
        self.database.update_record("users", (name, age), user_id)

    def delete_user(self, user_id):
        self.database.delete_record("users", user_id)
