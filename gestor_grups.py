import sqlite3
import os

# Ruta absoluta al directori de l'script
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
DB_NAME = os.path.join(BASE_DIR, "grups_musica.db")

def configurar_bd(nombre_bd: str):
    global DB_NAME
    DB_NAME = nombre_bd

def crear_taula():
    try:
        conn = sqlite3.connect(DB_NAME)
        cursor = conn.cursor()
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS grups (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                nom_grup TEXT NOT NULL,
                any_inici INTEGER,
                tipus_musica TEXT,
                num_integrants INTEGER
            )
        ''')
        conn.commit()
    except Exception as e:
        print(f"Error creant taula: {e}")
    finally:
        conn.close()

def intro_dades(nom=None, any_inici=None, tipus=None, integrants=None):
    if nom is None:
        nom = input("Nom del grup: ").strip()
    if not nom:
        raise ValueError("El nom no pot estar buit.")

    if any_inici is None:
        any_inici_input = input("Any d'inici (≥ 1960): ").strip()
        if any_inici_input.isdigit():
            any_inici = int(any_inici_input)
    if not isinstance(any_inici, int) or any_inici < 1960:
        raise ValueError("L'any ha de ser un enter igual o superior a 1960.")

    if tipus is None:
        tipus = input("Tipus de música: ").strip()
    if not tipus or any(char.isdigit() for char in tipus):
        raise ValueError("El tipus de música no pot estar buit ni contenir números.")

    if integrants is None:
        integrants_input = input("Nombre d'integrants (> 0): ").strip()
        if integrants_input.isdigit():
            integrants = int(integrants_input)
    if not isinstance(integrants, int) or integrants <= 0:
        raise ValueError("El nombre d'integrants ha de ser un enter positiu.")

    return nom, any_inici, tipus, integrants

def afegir_grup():
    try:
        dades = intro_dades()
        conn = sqlite3.connect(DB_NAME)
        cursor = conn.cursor()
        cursor.execute('''
            INSERT INTO grups (nom_grup, any_inici, tipus_musica, num_integrants)
            VALUES (?, ?, ?, ?)
        ''', dades)
        conn.commit()
        print(f"Grup '{dades[0]}' afegit correctament.")
    except Exception as e:
        print(f"Error al afegir el grup: {e}")
    finally:
        conn.close()

def mostrar_grups():
    try:
        conn = sqlite3.connect(DB_NAME)
        cursor = conn.cursor()
        cursor.execute('SELECT * FROM grups')
        grups = cursor.fetchall()
        conn.close()

        if grups:
            print("\n Llista de grups:")
            for grup in grups:
                print(f"ID: {grup[0]}, Nom: {grup[1]}, Any inici: {grup[2]}, Tipus: {grup[3]}, Integrants: {grup[4]}")
        else:
            print("\n No hi ha grups a la base de dades.")
    except Exception as e:
        print(f" Error en mostrar els grups: {e}")

def consultar_grup_per_nom(nom_grup):
    try:
        conn = sqlite3.connect(DB_NAME)
        cursor = conn.cursor()
        cursor.execute('SELECT * FROM grups WHERE nom_grup = ?', (nom_grup,))
        grup = cursor.fetchone()
        conn.close()

        if grup:
            print("Grup trobat:")
            print(f"ID: {grup[0]}, Nom: {grup[1]}, Any inici: {grup[2]}, Tipus: {grup[3]}, Integrants: {grup[4]}")
        else:
            print("No s'ha trobat cap grup amb aquest nom.")
    except Exception as e:
        print(f"Error en consultar el grup: {e}")

def eliminar_grup(nom_grup):
    try:
        conn = sqlite3.connect(DB_NAME)
        cursor = conn.cursor()
        cursor.execute('DELETE FROM grups WHERE nom_grup = ?', (nom_grup,))
        conn.commit()
        print(f"Grup '{nom_grup}' eliminat correctament.")
    except sqlite3.Error as e:
        print(f"Error al eliminar el grup: {e}")
    finally:
        conn.close()

def actualitzar_grup(nom_grup):
    try:
        conn = sqlite3.connect(DB_NAME)
        cursor = conn.cursor()

        cursor.execute('SELECT * FROM grups WHERE nom_grup = ?', (nom_grup,))
        grup = cursor.fetchone()

        if grup:
            print(f"Grup trobat: {grup}")
            dades = intro_dades(nom_grup)
            cursor.execute('''
                UPDATE grups
                SET nom_grup = ?, any_inici = ?, tipus_musica = ?, num_integrants = ?
                WHERE nom_grup = ?
            ''', (*dades, nom_grup))
            conn.commit()
            print(f"Grup '{nom_grup}' actualitzat correctament.")
        else:
            print("No s'ha trobat cap grup amb aquest nom.")
    except Exception as e:
        print(f"Error al actualitzar el grup: {e}")
    finally:
        conn.close()

def menu():
    """Mostra el menú principal i gestiona les opcions."""
    crear_taula()
    while True:
        print("###################################################################")
        print("#################### GRUPS DE MÚSICA en CATALÀ ####################")
        print("###################################################################")
        print("\n--- Menú ---")
        print("1. Afegir un nou grup de música en català")
        print("2. Mostrar tots els grups de música en català")
        print("3. Consultar un grup pel seu nom")
        print("4. Eliminar un grup de música")
        print("5. Actualitzar un grup de música")
        print("0. Sortir")
        opcio = input("Tria una opció: ")

        if opcio == "1":
            afegir_grup()
        elif opcio == "2":
            mostrar_grups()
        elif opcio == "3":
            nom = input("Nom del grup a consultar: ")
            consultar_grup_per_nom(nom)
        elif opcio == "4":
            nom = input("Nom del grup a eliminar: ")
            eliminar_grup(nom)
        elif opcio == "5":
            nom = input("Nom del grup a actualitzar: ")
            actualitzar_grup(nom)
        elif opcio == "0":
            print("Adéu!")
            break
        else:
            print("Opció no vàlida. Torna-ho a provar.")

if __name__ == "__main__":
    menu()