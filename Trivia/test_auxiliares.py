import unittest
from unittest.mock import patch
from auxiliares import flujo_preguntas

class TestFlujoPreguntas(unittest.TestCase):
    def setUp(self):
        self.preguntas = [
            {'Question': '¿Cuál es la capital de Francia?', 'Answer': 'París'},
            {'Question': '¿Cuál es el color del cielo?', 'Answer': 'Azul'},
            {'Question': '¿Cuál es 2+2?', 'Answer': '4'},
            {'Question': '¿Cuál es el océano más grande?', 'Answer': 'Pacífico'},
            {'Question': '¿Cuál es el país más poblado?', 'Answer': 'China'}
        ]

    @patch('builtins.input', side_effect=['1', '1', '1', '1', '1'])
    @patch('builtins.print')
    def test_flujo_preguntas(self, mock_print, mock_input):
        resultados = flujo_preguntas(preguntas=self.preguntas, resultados=0, numero_pregunta=1)
        print(f"Resultados esperados: 5, Resultados obtenidos: {resultados}")
        self.assertEqual(resultados, 5)  # Se espera que todas las respuestas sean correctas

    @patch('builtins.input', side_effect=['1', '1', '1', '1', '2'])
    @patch('builtins.print')
    def test_flujo_preguntas_con_errores(self, mock_print, mock_input):
        resultados = flujo_preguntas(preguntas=self.preguntas, resultados=0, numero_pregunta=1)
        print(f"Resultados esperados: 4, Resultados obtenidos: {resultados}")
        self.assertEqual(resultados, 4)  # Se espera que solo cuatro respuestas sean correctas

if __name__ == '__main__':
    unittest.main()