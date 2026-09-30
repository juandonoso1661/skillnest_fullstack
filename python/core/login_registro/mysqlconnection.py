import pymysql
import pymysql.cursors
import os
from dotenv import load_dotenv

load_dotenv()


class MySQLConnection:

    @staticmethod
    def connect_db():
        return pymysql.connect(
            host=os.getenv("DB_HOST"),
            user=os.getenv("DB_USER"),
            password=os.getenv("DB_PASSWORD"),
            database=os.getenv("DB_NAME"),
            cursorclass=pymysql.cursors.DictCursor
        )

    @classmethod
    def query_db(cls, query, data=None):
        connection = cls.connect_db()

        try:
            with connection.cursor() as cursor:

                cursor.execute(query, data)

                if query.strip().lower().startswith("select"):
                    result = cursor.fetchall()
                else:
                    connection.commit()
                    result = cursor.lastrowid

            return result

        except Exception as e:
            print("ERROR:", e)
            return False

        finally:
            connection.close()