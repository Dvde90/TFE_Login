import os
import sqlite3
from hashlib import sha1
from sqlite3 import Error

def init_db(conn):
    sql_create_tables = """
        CREATE TABLE IF NOT EXISTS t_logins (
            l_id INTEGER PRIMARY KEY AUTOINCREMENT ,
            username TEXT NOT NULL UNIQUE,
            password TEXT NOT NULL,
            mail  TEXT NOT NULL);
        CREATE TABLE IF NOT EXISTS t_clients (
            c_id integer primary key autoincrement, 
            ref text not null, 
            nom text not null, 
            prenom text, 
            adresse text, 
            ville text, 
            tel integer, 
            email text, 
            tva text);
        CREATE TABLE IF NOT EXISTS T_Produits (
            id_produit integer primary key autoincrement,
            nom_produit text not null,
            lt_prix real not null,
            lt_m2 integer not null,
            libelle_produit text)   
        """

    sql_insert_into_logins = """
        INSERT INTO t_logins (username, password, mail) VALUES (?,?,?);
        """

    qr_ii_produit = """
        INSERT INTO T_Produits (nom_produit, lt_prix, lt_m2, libelle_produit) VALUES (?,?,?,?);
        """

    cursor = conn.cursor()
    cursor.executescript(sql_create_tables)
    cursor.execute(sql_insert_into_logins, ('test', sha1("1234".encode()).hexdigest(), 'test@'))
    cursor.execute(sql_insert_into_logins, ('admin', sha1("admin".encode()).hexdigest(), 'admin@'))
    cursor.execute(qr_ii_produit, ('Shine-On', 45, 20, 'Vitre Auto-Nettoyant'))
    cursor.execute(qr_ii_produit, ('Inducoat', 32, 8, 'Peinture Desinfectant'))
    cursor.execute(qr_ii_produit, ('Oxil-Pro', 28, 300, 'Desinfectant'))
    conn.commit()

def close_db(conn):
    conn.close()

def connect(db_file):
    conn = None
    try:
        if not os.path.isfile(db_file):
            conn = sqlite3.connect(db_file)
            init_db(conn)
        else:
            conn = sqlite3.connect(db_file)
    except Error as e:
        print(e)
    return conn

def log_in(conn, user):
    sql = "SELECT password FROM t_logins WHERE username=?"
    cursor = conn.cursor()
    cursor.execute(sql, (user,))
    row = cursor.fetchone()
    return row

def log_reg(conn, username, password, mail):
    sql = "INSERT INTO t_logins (l_id, username, password, mail) VALUES (NULL,?,?,?)"
    cursor = conn.cursor()
    cursor.execute(sql, (username, sha1(password.encode()).hexdigest(), mail))
    conn.commit()

def log_read(conn):
    sql = "SELECT * FROM t_logins "
    cursor = conn.cursor()
    cursor.execute(sql,)
    rows = cursor.fetchall()
    return rows

def client_add(conn, ref, nom, prenom, adresse, ville, tel, email, tva):
    sql = "INSERT INTO t_clients (c_id, ref, nom, prenom, adresse, ville, tel, email, tva) VALUES (NULL,?,?,?,?,?,?,?,?)"
    cursor = conn.cursor()
    cursor.execute(sql, (ref, nom, prenom, adresse, ville, tel, email, tva))
    conn.commit()

def client_read(conn):
    sql = "SELECT * FROM t_clients"
    cursor = conn.cursor()
    cursor.execute(sql,)
    rows = cursor.fetchall()
    return rows

def client_del(conn, c_id):
    sql = "DELETE FROM t_clients WHERE c_id=? "
    cursor = conn.cursor()
    cursor.execute(sql, (c_id,))
    rows = cursor.fetchall()
    return rows

def client_up(conn, ref, nom, prenom, adresse, ville, tel, email, tva, c_id):
    sql = "UPDATE t_clients SET ref = ?, nom = ?, prenom = ?, adresse = ?, ville = ?, tel = ?, email = ?, tva = ? WHERE c_id = ?"
    cursor = conn.cursor()
    cursor.execute(sql, (ref, nom, prenom, adresse, ville, tel, email, tva, c_id))
    conn.commit()

def client_search(conn, ref, nom, prenom, adresse, ville, tel, email, tva):
    sql = "SELECT * FROM t_clients WHERE ref = ? OR nom = ? OR prenom = ? OR adresse = ? OR ville = ? OR tel = ? OR email = ? OR  tva = ?"
    cursor = conn.cursor()
    cursor.execute(sql, (ref, nom, prenom, adresse, ville, tel, email, tva))
    rows = cursor.fetchall()
    conn.close()
    return rows

def produit_add(conn, nom_produit, lt_prix, lt_m2, libelle_produit):
    sql = "INSERT INTO T_Produits (id_produit, nom_produit, lt_prix, lt_m2, libelle_produit) VALUES (NULL, ?, ?, ?, ?)"
    cursor = conn.cursor()
    cursor.execute(sql, (nom_produit, lt_prix, lt_m2, libelle_produit))
    conn.commit()

def produit_read(conn):
    sql = "SELECT * from T_Produits "
    cursor = conn.cursor()
    cursor.execute(sql,)
    rows = cursor.fetchall()
    return rows

def produit_del(conn, id_produit):
    sql = "DELETE FROM T_Produits WHERE id_produit=? "
    cursor = conn.cursor()
    cursor.execute(sql, (id_produit,))
    rows = cursor.fetchall()
    return rows

def produit_up(conn, nom_produit, lt_prix, lt_m2, libelle_produit, id_produit):
    sql = "UPDATE T_Produits SET nom_produit = ?, lt_prix = ?, lt_m2 = ?, libelle_produit = ? WHERE id_produit = ?"
    cursor = conn.cursor()
    cursor.execute(sql, (nom_produit, lt_prix, lt_m2, libelle_produit, id_produit))
    conn.commit()

def produit_search(conn, nom_produit):
    sql = "SELECT * FROM T_Produits WHERE nom_produit LIKE ? "
    cursor = conn.cursor()
    cursor.execute(sql, (f"%{nom_produit}%",))
    rows = cursor.fetchall()
    return rows

