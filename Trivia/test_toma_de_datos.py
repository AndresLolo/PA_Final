import unittest
from unittest.mock import patch
import pandas as pd
from toma_de_datos import toma_de_preguntas, toma_de_respuestas

# Mock data para las pruebas
mock_data = {
    'Question': [
        'Question 1', 
        'Question 2', 
        'Question 3', 
        'Question 4', 
        'Question 5'
    ],
    'Answer': [
        'Answer 1', 
        'Answer 2', 
        'Answer 3', 
        'Answer 4', 
        'Answer 5'
    ]
}

class TestTomaDeDatos(unittest.TestCase):
    
    @patch('toma_de_datos.data_question', pd.DataFrame(mock_data))
    @patch('toma_de_datos.data_answer', pd.DataFrame(mock_data))
    def test_toma_de_preguntas(self):
        preguntas = list(toma_de_preguntas())  # Convertimos el generador en una lista
        
        self.assertEqual(len(preguntas), 5)  # Se deben tomar 5 preguntas
        for pregunta in preguntas:
            self.assertIn('Question', pregunta)
            self.assertIn('Answer', pregunta)
    
    @patch('toma_de_datos.data_question', pd.DataFrame(mock_data))
    @patch('toma_de_datos.data_answer', pd.DataFrame(mock_data))
    def test_toma_de_respuestas(self):
        respuestas = list(toma_de_respuestas())  # Convertimos el generador en una lista
        
        self.assertEqual(len(respuestas), 2)  # Se deben tomar 2 respuestas
        for respuesta in respuestas:
            self.assertIn(respuesta, mock_data['Answer'])

if __name__ == '__main__':
    unittest.main()