import pymysql
import pymysql.cursors
import os
from dotenv import load_dotenv

load_dotenv()


class MySQLConnection:
    @staticmethod
    def connect_to_mysql():
        connection = pymysql.connect(
            host=os.getenv("DB_HOST"),
            user=os.getenv("DB_USER"),
            password=os.getenv("DB_PASSWORD"),
            database=os.getenv("DB_NAME"),
            cursorclass=pymysql.cursors.DictCursor
        )

        return connection

    @classmethod
    def query_db(cls, query, data=None):
        connection = cls.connect_to_mysql()

        try:
            with connection.cursor() as cursor:
                cursor.execute(query, data or ())

                if query.strip().lower().startswith("select"):
                    result = cursor.fetchall()
                else:
                    connection.commit()
                    result = cursor.lastrowid

            return result

        except Exception as e:
            connection.rollback()
            print("Error en la consulta:", e)
            return False

        finally:
            connection.close()