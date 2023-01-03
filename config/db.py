import mariadb


db_conn = mariadb.connect(host="localhost", port=3306, database="test")

cursor = db_conn.cursor(dictionary=True)



