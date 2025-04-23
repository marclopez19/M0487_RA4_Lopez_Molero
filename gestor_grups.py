import sqlite3
import os
import datetime

# Ruta absoluta al mateix directori que l'script
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
DB_NAME = os.path.join(BASE_DIR, "grups_musica.db")


def crear_taula():
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
    conn.close()


def intro_dades(nom=None):
    """
    Intoducció de dades per a un grup musical.
    """
    if nom:
        nom_grup = nom
    else:
        nom_grup = input("Nom del grup: ").strip()
        if not nom_grup:
            raise ValueError("El nom no pot estar buit.")

    any_inici = input("Any d'inici (≥ 1960): ").strip()
    if not any_inici.isdigit() or int(any_inici) < 1960:
        raise ValueError("L'any ha de ser un enter igual o superior a 1960.")
    any_inici = int(any_inici)

    tipus = input("Tipus de música: ").strip()
    if not tipus or any(char.isdigit() for char in tipus):
        raise ValueError("El tipus de música no pot estar buit ni contenir números.")

    integrants = input("Nombre d'integrants (> 0): ").strip()
    if not integrants.isdigit() or int(integrants) <= 0:
        raise ValueError("El nombre d'integrants ha de ser un enter positiu.")
    integrants = int(integrants)

    return nom_grup, any_inici, tipus, integrants


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
            print("\nLlista de grups:")
            for grup in grups:
                print(f"ID: {grup[0]}, Nom: {grup[1]}, Any inici: {grup[2]}, Tipus: {grup[3]}, Integrants: {grup[4]}")
        else:
            print("\nNo hi ha grups a la base de dades.")
    except Exception as e:
        print(f"Error en mostrar els grups: {e}")


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
    crear_taula()
    while True:
        print("###################################################################")
        print("#################### GRUPS DE MÚSICA en CATALÀ ####################")
        print("###################################################################")
        print("\n--- Menú ---")
        print("1. Afegir un nou grup de música en català")
        print("2. Mostrar tots els grups de música en català")
        print("3. Eliminar un grup de música")
        print("4. Actualitzar un grup de música")
        print("0. Sortir")
        opcio = input("Tria una opció: ")

        if opcio == "1":
            afegir_grup()
        elif opcio == "2":
            mostrar_grups()
        elif opcio == "3":
            nom = input("Nom del grup a eliminar: ")
            eliminar_grup(nom)
        elif opcio == "4":
            nom = input("Nom del grup a actualitzar: ")
            actualitzar_grup(nom)
        elif opcio == "0":
            print("Adéu!")
            break
        else:
            print("Opció no vàlida. Torna-ho a provar.")


if __name__ == "__main__":
    menu()