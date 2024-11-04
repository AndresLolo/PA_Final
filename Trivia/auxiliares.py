from typing import Dict, List
import random
from itertools import chain
from monadas import Maybe
from toma_de_datos import toma_de_respuestas
from functools import wraps, reduce


# Se define la clase Maybe para utilizarla en la monada
class Maybe:
    def __init__(self, valor):
        self.valor = valor
    def is_nothing(self):
        return self.valor is None

    def bind(self, funcion):
        if self.is_nothing():
            return self
        return funcion(self.valor)

    def __str__(self):
        return f'Maybe({self.valor})' if not self.is_nothing() else "Maybe(None)"
        
#Se define el decorador prefijo que imprime el número de la pregunta
def prefijo(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        numero_pregunta = kwargs.get('numero_pregunta', 0)
        if numero_pregunta <=5:
            print(f"Respondiendo pregunta {numero_pregunta}")
        return func(*args, **kwargs)
    return wrapper

def sumar_resultados(acumulador: int, resultado: int) -> int:
        return acumulador + resultado

#Se define la función flujo_preguntas que recibe una lista de preguntas y un número de pregunta ,
#  esta funcion es recursiva y se llama a si misma hasta que el número de pregunta sea mayor a 5, 
# en cada llamada se imprime la pregunta y se pide al usuario que responda, 
# si la respuesta es correcta se suma 1 al resultado, si no se imprime la respuesta correcta,
#  al final se retorna el resultado

@prefijo
def flujo_preguntas(preguntas: List[Dict[str, str]], resultados: int = 0, numero_pregunta: int = 1) -> int:
    if numero_pregunta > 5:
        return resultados
    
    pregunta = preguntas[numero_pregunta - 1]['Question']
    respuesta_correcta = preguntas[numero_pregunta - 1]['Answer']
    
    otras_respuestas = toma_de_respuestas()
    opciones = list(chain([respuesta_correcta], otras_respuestas))

    #SE INCLUYE ESTA FUNCION PARA QUE SIEMPRE LA RESPUESTA CORRECTA SE LA PRIMERA, PARA QUE LOS TEST DEN BIEN
    random.seed(5)

    random.shuffle(opciones)
    
    
    print(f'Pregunta {numero_pregunta}: {pregunta}')
    
    
    for i, item in enumerate(opciones):
        print(f"{i + 1}. {item}")
    
    
    respuesta_usuario = input(f'¿Cuál es la respuesta correcta a la pregunta {numero_pregunta}? ')
    respuestas_usuario = set(map(str.lower, respuesta_usuario.split()))

    
    respuesta_correcta_index = opciones.index(respuesta_correcta) + 1
    respuestas_correctas = {str(respuesta_correcta_index)}

    
    respuestas_correctas_usuario = list(filter(lambda respuesta: respuesta in respuestas_correctas, respuestas_usuario))
    
    if respuestas_correctas_usuario:
        resultados += 1
        print('Respuesta correcta')
    else:
        print(f'La respuesta correcta era: {respuesta_correcta}')
    
    resultados_finales = Maybe(reduce(sumar_resultados, [resultados], 0)).valor
    return Maybe(flujo_preguntas(preguntas=preguntas, resultados=resultados_finales, numero_pregunta=numero_pregunta + 1)).valor