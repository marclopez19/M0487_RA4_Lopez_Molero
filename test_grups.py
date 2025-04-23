import unittest
import sqlite3
import os
from unittest.mock import patch
import gestor_grups

class TestGestorGrups(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        # Configurar entorno de prueba
        cls.DB_NAME = "test_grups.db"
        gestor_grups.configurar_bd(cls.DB_NAME)
        gestor_grups.crear_taula()
        
        # Datos iniciales autogenerados
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
        """Test: Añadir grupo válido automáticamente"""
        # Configurar respuestas automáticas
        mock_input.side_effect = ['Nou Grup', '2000', 'Pop', '5']
        
        # Ejecutar función
        gestor_grups.afegir_grup()
        
        # Verificar en BD
        with sqlite3.connect(self.DB_NAME) as conn:
            cursor = conn.cursor()
            cursor.execute('SELECT * FROM grups WHERE nom_grup = "Nou Grup"')
            result = cursor.fetchone()
            
            self.assertIsNotNone(result)
            self.assertEqual(result[2], 2000)  # Any_inici

    def test_consultar_grup_existent(self):
        """Test: Consulta automática de grupo existente"""
        # Ejecutar consulta
        with patch('builtins.print') as mock_print:
            gestor_grups.consultar_grup_per_nom('Grup Existente')
            
            # Verificar salida esperada
            mock_print.assert_any_call("🔍 Grup trobat:")

    @patch('builtins.input')
    def test_actualitzar_grup(self, mock_input):
        """Test: Actualización automática de datos"""
        # Configurar entradas para actualización
        mock_input.side_effect = ['2005', 'Pop Rock', '6']
        
        # Ejecutar actualización
        gestor_grups.actualitzar_grup('Grup Existente')
        
        # Verificar cambios
        with sqlite3.connect(self.DB_NAME) as conn:
            cursor = conn.cursor()
            cursor.execute('SELECT * FROM grups WHERE nom_grup = "Grup Existente"')
            result = cursor.fetchone()
            
            self.assertEqual(result[2], 2005)  # Any_inici
            self.assertEqual(result[3], 'Pop Rock')  # Tipus

    def test_eliminar_grup(self):
        """Test: Eliminación automática de grupo"""
        # Añadir grupo temporal
        with sqlite3.connect(self.DB_NAME) as conn:
            cursor = conn.cursor()
            cursor.execute('''
                INSERT INTO grups (nom_grup, any_inici, tipus_musica, num_integrants)
                VALUES ('Grup Temporal', 2010, 'Electrònica', 3)
            ''')
            conn.commit()
        
        # Ejecutar eliminación
        gestor_grups.eliminar_grup('Grup Temporal')
        
        # Verificar eliminación
        with sqlite3.connect(self.DB_NAME) as conn:
            cursor = conn.cursor()
            cursor.execute('SELECT * FROM grups WHERE nom_grup = "Grup Temporal"')
            self.assertIsNone(cursor.fetchone())

    @patch('builtins.input')
    def test_validacio_dades(self, mock_input):
        """Test: Validaciones automáticas de datos"""
        # Caso 1: Nombre vacío
        mock_input.side_effect = ['', '2000', 'Pop', '5']
        with self.assertRaises(ValueError):
            gestor_grups.intro_dades()

        # Caso 2: Any inválido
        mock_input.side_effect = ['Grup Test', '1950', 'Pop', '5']
        with self.assertRaises(ValueError):
            gestor_grups.intro_dades()

        # Caso 3: Tipo vacío
        mock_input.side_effect = ['Grup Test', '2000', '', '5']
        with self.assertRaises(ValueError):
            gestor_grups.intro_dades()

        # Caso 4: Integrantes inválidos
        mock_input.side_effect = ['Grup Test', '2000', 'Pop', '0']
        with self.assertRaises(ValueError):
            gestor_grups.intro_dades()

if __name__ == "__main__":
    unittest.main()