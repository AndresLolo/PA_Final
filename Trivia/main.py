from typing import Dict, List, Tuple
from toma_de_datos import toma_de_preguntas
from auxiliares import flujo_preguntas


if __name__ == '__main__':

    preguntas_gen = toma_de_preguntas()
    preguntas = list(preguntas_gen)  

    resultados = flujo_preguntas(preguntas=preguntas, resultados=0, numero_pregunta=1)  
    print(f'Has acertado {resultados} pregunta(s)')
    
    puntaje = lambda resultados: resultados * 10
    print(f'Tu puntaje es {puntaje(resultados)}')
    
    
    

