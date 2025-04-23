import unittest
from gestor_grups import intro_dades

class TestValidacions(unittest.TestCase):
    def test_nom_buit(self):
        with self.assertRaises(ValueError):
            intro_dades(nom='')

    def test_any_inici_invalid(self):
        with self.assertRaises(ValueError):
            input_values = ['1950', 'rock', '4']
            with unittest.mock.patch('builtins.input', side_effect=input_values):
                intro_dades()

    def test_integrants_negatius(self):
        with self.assertRaises(ValueError):
            input_values = ['Nom', '1990', 'pop', '-3']
            with unittest.mock.patch('builtins.input', side_effect=input_values):
                intro_dades()

if __name__ == '__main__':
    unittest.main()