from app.database import get_db

class Vino:

    #contructor
    def __init__(self,id_vino=None,nombre=None,nombre_vino=None,año_vino=None,foto=None):
        self.id_vino = id_vino
        self.nombre = nombre
        self.nombre_vino = nombre_vino
        self.año_vino = año_vino
        self.foto = foto

    def serialize(self):
        return {
            'id_vino':self.id_vino,
            'nombre':self.nombre,
            'nombre_vino':self.nombre_vino,
            'año_vino':self.año_vino,
            'foto':self.foto,
        }

    @staticmethod
    def get_all():
        #logica de buscar en la base todos los vinos
        db = get_db()
        cursor = db.cursor()
        query = "SELECT * FROM vinos"
        cursor.execute(query)
        #obtengo resultados
        rows = cursor.fetchall()
        vinos = [Vino(id_vino=row[0], nombre=row[1], nombre_vino=row[2], año_vino=row[3], foto=row[4]) for row in rows]
        #cerramos el cursor
        cursor.close()
        return vinos

    @staticmethod
    def get_by_id(vino_id):
        db = get_db()
        cursor = db.cursor()
        cursor.execute("SELECT * FROM vinos WHERE id_vino = %s", (vino_id,))
        row = cursor.fetchone()
        cursor.close()
        if row:
            return Vino(id_vino=row[0], nombre=row[1], nombre_vino=row[2], año_vino=row[3], foto=row[4])
        return None

    def save(self):
        db = get_db()
        cursor = db.cursor()
        if self.id_vino:
            cursor.execute("""
                UPDATE vinos SET nombre = %s, nombre_vino = %s, año_vino = %s, foto = %s
                WHERE id_vino = %s
            """, (self.nombre, self.nombre_vino, self.año_vino, self.foto, self.id_vino))
        else:
            cursor.execute("""
                INSERT INTO vinos (nombre, nombre_vino, año_vino, foto) VALUES (%s, %s, %s, %s)
            """, (self.nombre, self.nombre_vino, self.año_vino, self.foto))
            #voy a obtener el último id generado
            self.id_vino = cursor.lastrowid
        db.commit() #confirmar la accion
        cursor.close()

   

    def delete(self):
        db = get_db()
        cursor = db.cursor()
        cursor.execute("DELETE FROM vinos WHERE id_vino = %s", (self.id_vino,))
        db.commit()
        cursor.close()
