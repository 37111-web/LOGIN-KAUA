import sqlite3 
from database.db import get_db_connection  

class FormularioModel:
    
    @staticmethod
    def create_formulario(user_id, nome, email, data_nascimento, cpf, genero):
        conn = get_db_connection()  
        try:
            conn.execute('''INSERT INTO formularios (user_id, nome, email, data_nascimento, cpf, genero)
                             VALUES (?, ?, ?, ?, ?, ?)''', 
                         (user_id, nome, email, data_nascimento, cpf, genero))
            conn.commit()  
            return True  
        except sqlite3.IntegrityError:
            return None  
        finally:
            conn.close()  


    @staticmethod
    def get_formulario(user_id, nome, email, data_nascimento, cpf, genero):
        conn = get_db_connection()  
        try:
            conn.execute('''INSERT INTO formularios (user_id, nome, email, data_nascimento, cpf, genero)
                             VALUES (?, ?, ?, ?, ?, ?)''', 
                         (user_id, nome, email, data_nascimento, cpf, genero))
            conn.commit()  
            return True  
        except sqlite3.IntegrityError:
            return None  
        finally:
            conn.close()  


    @staticmethod
    def put_formulario(user_id, nome, email, data_nascimento, cpf, genero):
        conn = get_db_connection()  
        try:
            conn.execute('''INSERT INTO formularios (user_id, nome, email, data_nascimento, cpf, genero)
                             VALUES (?, ?, ?, ?, ?, ?)''', 
                         (user_id, nome, email, data_nascimento, cpf, genero))
            conn.commit()  
            return True  
        except sqlite3.IntegrityError:
            return None  
        finally:
            conn.close()                  

    @staticmethod
    def delete_formulario(user_id, nome, email, data_nascimento, cpf, genero):
        conn = get_db_connection()  
        try:
            conn.execute('''INSERT INTO formularios (user_id, nome, email, data_nascimento, cpf, genero)
                             VALUES (?, ?, ?, ?, ?, ?)''', 
                         (user_id, nome, email, data_nascimento, cpf, genero))
            conn.commit()  
            return True  
        except sqlite3.IntegrityError:
            return None  
        finally:
            conn.close()  