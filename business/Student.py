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
        self.database.create_record((nombre, edad,rut,mail,asignatura,promedio))

    def get_users(self):
        return self.database.read_records()

    def update_user(self, nombre, edad,rut,mail,asignatura,promedio):
        self.database.update_record((nombre, edad,mail,asignatura,promedio), rut)

    def delete_user(self, rut):
        self.database.delete_record(rut)
