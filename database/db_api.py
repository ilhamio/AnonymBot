import sqlite3


class Database:
    def __init__(self, database_file):
        self.conn = sqlite3.connect(database_file, check_same_thread=False)
        self.cursor = self.conn.cursor()

    # ========= PRIVATE METHODS =========
    # Emptiness
    def _is_empty(self) -> bool:
        with self.conn:
            temp = self.cursor.execute("SELECT * FROM 'queue'").fetchall()
            return not bool(len(temp))

    # starting chat
    def _start_chat(self, chat_id):
        with self.conn:
            peek = self.cursor.execute("SELECT chat_id FROM 'queue'").fetchone()
            self.delete_from_queue(peek[0])
            self.cursor.execute("UPDATE 'users' SET 'companion'=? WHERE chat_id=?", (peek[0], chat_id))
            self.cursor.execute("UPDATE 'users' SET 'companion'=? WHERE chat_id=?", (chat_id, peek[0]))

    # Check for duplicate
    def find_value(self, chat_id, db) -> bool:
        with self.conn:
            temp = self.cursor.execute(f"SELECT * FROM '{db}' WHERE chat_id=?", (chat_id,)).fetchall()
            return bool(len(temp))
    # =========================================

    # ========= OPERATIONS WITH USERS =========
    # Add to users while first start
    def add_to_users(self, chat_id):
        with self.conn:
            if not self.find_value(chat_id, 'users'):
                self.cursor.execute("INSERT INTO 'users' ('chat_id') VALUES (?)", (chat_id,))

    def get_companion(self, chat_id):
        companion = self.cursor.execute("SELECT companion FROM 'users' WHERE chat_id=?", (chat_id,)).fetchone()
        if companion:
            return companion[0]
        else:
            return None

    def close_chat(self, chat_id):
        self.cursor.execute("UPDATE 'users' SET companion=NULL WHERE chat_id=?", (chat_id,))

    # =========================================

    # ========= OPERATIONS WITH QUEUE =========
    # Add to queue
    def add_to_queue(self, chat_id):
        with self.conn:
            if self._is_empty():
                self.cursor.execute("INSERT INTO 'queue' ('chat_id') VALUES (?)", (chat_id,))
                return False
            else:
                self._start_chat(chat_id)
                return True

    # Delete from DB
    def delete_from_queue(self, chat_id):
        with self.conn:
            self.cursor.execute("DELETE FROM 'queue' WHERE chat_id=?", (chat_id,))
    # =========================================

