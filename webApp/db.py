import mysql.connector
class con():
    host = 'localhost'
    user = 'root'
    password = ''
    db = 'gembot'

    def __init__(self):
        self.connection = mysql.connector.connect(host=self.host, user=self.user, password=self.password, database=self.db, use_unicode=True,
                                          charset="utf8")
        self.cursor = self.connection.cursor()
    def transaction(self, query, params):
        try:
            self.cursor.execute(query, params)
            self.connection.commit()
        except Exception as ex:
            self.connection.rollback()

    def __del__(self):
        self.connection.close()
