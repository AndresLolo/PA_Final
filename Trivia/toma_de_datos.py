import pandas as pd
from typing import Dict, List

# Se lee el archivo CSV
data = pd.read_csv('Datos/reduced_question_set.csv', encoding='ISO-8859-1')

# Se toman las columnas de pregunta y respuesta
data_question = data[['Question', 'Answer']]
data_answer = data[['Answer']]

def toma_de_preguntas():
    
    for _, row in data_question.sample(n=5).iterrows():
        yield row.to_dict()

def toma_de_respuestas():
    
    for respuesta in data_answer.sample(n=2)['Answer']:
        yield respuesta

        
