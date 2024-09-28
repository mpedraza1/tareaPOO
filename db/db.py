import pymysql

class MySQLDatabase:
    def __init__(self, host, user, password, database):
        self.connection = pymysql.connect(
            host=host,
            user=user,
            password=password,
            database=database,
            port=3307
        )
        self.cursor = self.connection.cursor()

    def create_record(self, table, data):
        query = f"INSERT INTO alumnos (nombre, edad, rut, mail, asignatura, promedio) VALUES (%s,%s,%s,%s,%s,%s)"
        self.cursor.execute(query, data)
        self.connection.commit()

    def read_records(self):
        query = "SELECT * FROM alumnos"
        self.cursor.execute(query)
        return self.cursor.fetchall()

    def update_record(self, table, data, record_id):
        query = f"UPDATE {table} SET name = %s, age = %s WHERE id = %s"
        self.cursor.execute(query, (*data, record_id))
        self.connection.commit()

    def delete_record(self, table, record_id):
        query = f"DELETE FROM {table} WHERE id = %s"
        self.cursor.execute(query, (record_id,))
        self.connection.commit()

    def close(self):
        self.cursor.close()
        self.connection.close()
