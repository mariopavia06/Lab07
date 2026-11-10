from database.DB_connect import DBConnect
from model.libro_DTO import Libro

"""
    LIBRO DAO
    Gestisce le operazioni di accesso al database relative ai libri (Effettua le Query).
"""

class LibroDAO:
    def __init__(self):
        pass

    def get_generi(self):
        cnx = DBConnect.get_connection()
        result = []
        if cnx is None:
            return result

        cursor = cnx.cursor(dictionary=True)
        query = "SELECT DISTINCT genere FROM libro WHERE genere IS NOT NULL AND genere != '' ORDER BY genere"
        cursor.execute(query)

        for row in cursor:
            result.append(row["genere"])

        cursor.close()
        cnx.close()
        return result

    def get_libri_filtrati(self, biblioteca: str, genere: str):
        cnx = DBConnect.get_connection()
        result = []
        if cnx is None:
            return result

        cursor = cnx.cursor(dictionary=True)

        # Query diretta sulla tabella libro, dato che id_biblioteca è già lì dentro
        query = """
                SELECT DISTINCT l.id, l.titolo, l.autore, l.genere, l.anno_pubblicazione, l.id_biblioteca
                FROM libro l
                WHERE 1=1
            """

        condizioni = []
        parametri = []

        if biblioteca:
            condizioni.append("l.id_biblioteca = %s")
            parametri.append(biblioteca)

        if genere:
            condizioni.append("l.genere = %s")
            parametri.append(genere)

        if condizioni:
            query += " AND " + " AND ".join(condizioni)

        query += " ORDER BY l.titolo"

        cursor.execute(query, tuple(parametri))


        for row in cursor:
            libro = Libro(
                id=row["id"],
                titolo=row["titolo"],
                autore=row["autore"],
                genere=row["genere"],
                anno_pubblicazione=row["anno_pubblicazione"],
                id_biblioteca=row["id_biblioteca"]
            )

            result.append(libro)

        cursor.close()
        cnx.close()
        return result