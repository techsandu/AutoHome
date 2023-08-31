import psycopg2
from utility.commonClass import MyCustomException as ex
from utility.config import DB as db
dbParams = {
            "host": db.host,
            "database": db.database,
            "user": db.user,
            "password": db.password
        }
class SqlUtility:
    def insertQuery(query,data):
        insert_query = query
        try:
            conn = psycopg2.connect(**dbParams)
            cursor = conn.cursor()
            cursor.execute(insert_query,data)
            conn.commit()
            print("Data inserted successfully!")
            lastwor = cursor.lastrowid
            conn.close()
            return lastwor

        except(Exception,psycopg2.Error)  as err :
            print("Error",err)
            raise ex(err)
    def selectQuery(query,data):
        try:
            conn = psycopg2.connect(**dbParams)
            cursor = conn.cursor()
            cursor.execute(query,data)
            result = cursor.fetchall()
            conn.close()
            return result
        except(Exception, psycopg2.Error) as err:
            print("Error", err)
            raise ex(err)







