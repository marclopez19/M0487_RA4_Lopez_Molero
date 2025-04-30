import unittest
import sqlite3
import os
from unittest.mock import patch
import gestor_grups

class TestGestorGrups(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.DB_NAME = "test_grups.db"
        gestor_grups.configurar_bd(cls.DB_NAME)
        gestor_grups.crear_taula()
        with sqlite3.connect(cls.DB_NAME) as conn:
            cursor = conn.cursor()
            cursor.execute('''
                INSERT INTO grups (nom_grup, any_inici, tipus_musica, num_integrants)
                VALUES ('Grup Existente', 1990, 'Rock', 4)
            ''')
            conn.commit()

    @classmethod
    def tearDownClass(cls):
        if os.path.exists(cls.DB_NAME):
            os.remove(cls.DB_NAME)

    @patch('builtins.input')
    def test_afegir_grup_valid(self, mock_input):
        mock_input.side_effect = ['Nou Grup', '2000', 'Pop', '5']
        gestor_grups.afegir_grup()
        with sqlite3.connect(self.DB_NAME) as conn:
            cursor = conn.cursor()
            cursor.execute('SELECT * FROM grups WHERE nom_grup = "Nou Grup"')
            result = cursor.fetchone()
            self.assertIsNotNone(result)
            self.assertEqual(result[2], 2000)

    def test_consultar_grup_existent(self):
        with patch('builtins.print') as mock_print:
            gestor_grups.consultar_grup_per_nom('Grup Existente')
            mock_print.assert_any_call("🔍 Grup trobat:")

    @patch('builtins.input')
    def test_actualitzar_grup(self, mock_input):
        mock_input.side_effect = ['2005', 'Pop Rock', '6']
        gestor_grups.actualitzar_grup('Grup Existente')
        with sqlite3.connect(self.DB_NAME) as conn:
            cursor = conn.cursor()
            cursor.execute('SELECT * FROM grups WHERE nom_grup = "Grup Existente"')
            result = cursor.fetchone()
            self.assertEqual(result[2], 2005)
            self.assertEqual(result[3], 'Pop Rock')

    def test_eliminar_grup(self):
        with sqlite3.connect(self.DB_NAME) as conn:
            cursor = conn.cursor()
            cursor.execute('''
                INSERT INTO grups (nom_grup, any_inici, tipus_musica, num_integrants)
                VALUES ('Grup Temporal', 2010, 'Electrònica', 3)
            ''')
            conn.commit()
        gestor_grups.eliminar_grup('Grup Temporal')
        with sqlite3.connect(self.DB_NAME) as conn:
            cursor = conn.cursor()
            cursor.execute('SELECT * FROM grups WHERE nom_grup = "Grup Temporal"')
            self.assertIsNone(cursor.fetchone())

    def test_nom_buit(self):
        with self.assertRaises(ValueError):
            gestor_grups.intro_dades(nom='', any_inici=2000, tipus='Pop', integrants=5)

    def test_any_invalid(self):
        with self.assertRaises(ValueError):
            gestor_grups.intro_dades(nom='Grup', any_inici=1950, tipus='Pop', integrants=5)

    def test_tipus_invalid(self):
        with self.assertRaises(ValueError):
            gestor_grups.intro_dades(nom='Grup', any_inici=2000, tipus='P0p', integrants=5)

    def test_integrants_invalid(self):
        with self.assertRaises(ValueError):
            gestor_grups.intro_dades(nom='Grup', any_inici=2000, tipus='Pop', integrants=0)

if __name__ == "__main__":
    unittest.main()