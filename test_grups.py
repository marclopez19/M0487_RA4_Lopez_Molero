import unittest
import sqlite3
import os
from unittest.mock import patch
import gestor_grups

class TestGrupsMusica(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.DB_NAME = "test_grups_musica.db"
        gestor_grups.configurar_bd(cls.DB_NAME)
        gestor_grups.crear_taula()
        
        # Añadir datos iniciales
        conn = sqlite3.connect(cls.DB_NAME)
        cursor = conn.cursor()
        cursor.execute('''
            INSERT INTO grups (nom_grup, any_inici, tipus_musica, num_integrants)
            VALUES (?, ?, ?, ?)
        ''', ('Grupo Existente', 1990, 'Rock', 4))
        conn.commit()
        conn.close()

    @classmethod
    def tearDownClass(cls):
        if os.path.exists(cls.DB_NAME):
            os.remove(cls.DB_NAME)

    def test_afegir_grup(self):
        with patch('builtins.input', side_effect=['Nuevo Grupo', '2000', 'Pop', '5']):
            gestor_grups.afegir_grup()
        
        # Verificar inserción
        conn = sqlite3.connect(self.DB_NAME)
        cursor = conn.cursor()
        cursor.execute('SELECT * FROM grups WHERE nom_grup = "Nuevo Grupo"')
        result = cursor.fetchone()
        conn.close()
        self.assertIsNotNone(result)

    def test_consultar_grup_per_nom(self):
        # Test de grupo existente
        with patch('builtins.print') as mock_print:
            gestor_grups.consultar_grup_per_nom('Grupo Existente')
            self.assertTrue(mock_print.called)
        
        # Test de grupo inexistente
        with patch('builtins.print') as mock_print:
            gestor_grups.consultar_grup_per_nom('No Existo')
            mock_print.assert_called_with("⚠️ No s'ha trobat cap grup amb aquest nom.")

    def test_eliminar_grup(self):
        # Añadir grupo temporal
        with patch('builtins.input', side_effect=['Grupo Temporal', '2010', 'Electrónica', '3']):
            gestor_grups.afegir_grup()
        
        # Eliminar
        gestor_grups.eliminar_grup('Grupo Temporal')
        
        # Verificar eliminación
        conn = sqlite3.connect(self.DB_NAME)
        cursor = conn.cursor()
        cursor.execute('SELECT * FROM grups WHERE nom_grup = "Grupo Temporal"')
        result = cursor.fetchone()
        conn.close()
        self.assertIsNone(result)

    def test_actualitzar_grup(self):
        # Actualizar datos
        with patch('builtins.input', side_effect=['2005', 'Pop Rock', '6']):
            gestor_grups.actualitzar_grup('Grupo Existente')
        
        # Verificar cambios
        conn = sqlite3.connect(self.DB_NAME)
        cursor = conn.cursor()
        cursor.execute('SELECT * FROM grups WHERE nom_grup = "Grupo Existente"')
        result = cursor.fetchone()
        conn.close()
        self.assertEqual(result[2], 2005)
        self.assertEqual(result[3], 'Pop Rock')

if __name__ == "__main__":
    unittest.main()