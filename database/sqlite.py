import sqlite3
from sqlite3 import Error
import configparser

config = configparser.ConfigParser()
config.read('../config.ini')

db_path = config['Database']['db_path']

sql_create_users_table = """CREATE TABLE IF NOT EXISTS Users (
                                id          INTEGER     PRIMARY KEY AUTOINCREMENT,
                                user_id     CHAR(100)   NOT NULL UNIQUE,
                                user_status INTEGER     NOT NULL DEFAULT 1,
                                timezone    CHAR(50)
                            );
                        """
# status: 0 for disable, 1 for enable


sql_create_tasks_table = """CREATE TABLE IF NOT EXISTS Tasks (
                                id                  INTEGER     PRIMARY KEY AUTOINCREMENT,
                                user_id             CHAR(100)   NOT NULL,
                                location            CHAR(50)    NOT NULL,
                                perform_time        TIME        NOT NULL,
                                latest_perform_time TIME
                            );
                        """

sql_add_user = 'INSERT INTO Users(user_id, user_status, timezone) VALUES ("{}", {}, "{}")'  # ("thisisUserID", 1, "thisisTimeZone")
sql_get_user_by_id = 'SELECT * FROM Users WHERE id = {}' # id
sql_get_user_by_userid = 'SELECT * FROM Users WHERE user_id = "{}"' # user_id
sql_del_user_by_id = 'DELETE FROM Users WHERE id = {}' # Users:id
sql_del_user_by_userid = 'DELETE FROM Users WHERE user_id = "{}"' # Users:user_id


sql_add_task = 'INSERT INTO Tasks (user_id, location, perform_time) VALUES ("{}", "{}", "{}")' # ("user_id", "Beijing", "21:46:19")
sql_get_task_by_id = 'SELECT * FROM Tasks WHERE id = {}' # Tasks: id
sql_get_task_by_userid = 'SELECT * FROM Tasks WHERE user_id = "{}"'
sql_del_task_by_id = 'DELETE FROM Tasks WHERE id = {}'
sql_del_task_by_userid = 'DELETE FROM TASKS WHERE user_id = "{}"'


def init_sqlite_db(db_file_path):
    """ Init Sqlite, Create new database and table. """
    conn = None
    try:
        conn = sqlite3.connect(db_file_path)
        print(sqlite3.version)
    except Error as e:
        print(e)
        return False

    cursor = conn.cursor()
    try:
        cursor.execute(sql_create_tasks_table)
        cursor.execute(sql_create_users_table)
    except Error as e:
        print(e)
        return False
    conn.close()
    return True


class User():
    def __init__(self):
        self._db_path = db_path
        self._db_conn = sqlite3.connect(self._db_path)
        self._db_cursor = self._db_conn.cursor()

    def get_by_id(self, id):
        return self._db_cursor.execute(sql_get_user_by_id + id).fetchall()
        
    def get_by_userid(self, user_id):
        return self._db_cursor.execute(sql_get_user_by_userid.format(user_id)).fetchall()

    def insert(self, user_id, status, timezone):
        self._db_cursor.execute(sql_add_user.format(user_id, status, timezone))
        self._db_conn.commit()

    def delete_by_id(self, id):
        self._db_cursor.execute(sql_del_user_by_id.format(id))
        self._db_conn.commit()

    def delete_by_userid(self, user_id):
        self._db_cursor.execute(sql_del_task_by_userid.format(user_id))
        self._db_conn.commit()


class Task():
    def __init__(self):
        self._db_path = db_path
        self._db_conn = sqlite3.connect(self._db_path)
        self._db_cursor = self._db_conn.cursor()

    def get_by_id(self, id):
        return self._db_cursor.execute(sql_get_task_by_id.format(id)).fetchall()
        
    def insert(self, user_id, location, time):
        self._db_cursor.execute(sql_add_task.format(user_id, location, time))
        self._db_conn.commit()

    def delete_by_id(self, id):
        self._db_cursor.execute(sql_del_task_by_id.format(id))
        self._db_conn.commit()

    def delete_by_userid(self, user_id):
        self._db_cursor.execute(sql_del_task_by_userid.format(user_id))
        self._db_conn.commit()




# if __name__ == "__main__":
    # init_sqlite_db("./main.sqlite")
    # user = User()
    # user.insert('user001', '1', 'timezone002')
    # user.delete_by_id('1')
    # user.delete_by_userid('user001')

    # print(user.get_by_userid('user002'))

    # task = Task()
    # task.insert('user001', 'london', '7:28:00')
    # task.delete_by_id('1')
    # print(task.get_by_id('2'))


    # user.add_task_for_user('user001', '4')
    # user.add_task_for_user('user001', '2')