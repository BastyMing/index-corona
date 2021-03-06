#-*- coding:utf-8 -*
'''Created on Thu Oct @Autor:Isabel Coronado- Maximiliano Palma'''
from sklearn.feature_extraction.text import CountVectorizer
import os

def leer_documentos(root):
    diccionario = dict()
    labels = [] #tema
    docs = []   #
    for r, dirs, files in os.walk(root):
        for file in files:
            with open(os.path.join(r, file), "r",encoding="latin-1") as f:
                #r es el directorio, y file son los archivos txt dentro, lo que hace
                #esta linea es unir la ruta de forma inteligente
                docs.append(f.read()) #todo el contenido de cada txt
            label = r.replace(root, '') #guarda nombre de cada carpeta y quita el nombre del path principal
            labels.append(label.replace('\\',''))
    for x in range(len(labels)):
        diccionario.setdefault(labels[x], docs[x])
    return diccionario
    #devuelve diccionario con el texto y los nombres de cada carpeta 
keys = []
casos = []
for key in leer_documentos('Temas'):
    keys.append(key)
for key in leer_documentos('Temas'):
    casos.append(key)
data = leer_documentos('Temas')
contar = leer_documentos('Temas')

#____________________Palabras descartadas________________#
prepositions =['a','del','ante','bajo','cabe','cada','con','contra','de','desde','en','entre','hacia','hasta','para','por','según','sin','so','sobre','tras']
prep_alike = ['durante','mediante','excepto','salvo','incluso','más','menos']
adverbs = ['no','si','sí']
articles = ['el','la','los','las','un','una','unos','unas','este','esta','estos','estas','aquel','aquella','aquellos','aquellas','su','sus']
aux_verbs = ['he','has','ha','hemos','habéis','han','había','habías','habíamos','habíais','habían']

#(temas,boletines,palabras_claves,recorrido_for)
def obtener_score(llaves,documentos,data,casos,palabras):
    vectorizer = CountVectorizer(stop_words=prepositions+prep_alike+adverbs+articles+aux_verbs)

    #____________________Conteo de palabras__________________#
    # lista de documentos de texto
    # crear la transformación
    # tokenizar y construir el vocabulario
    cadena = [data[palabras]]
    documentos = [documentos[casos]]
    vectorizer.fit(cadena)
    # resumen
    vocabulario = vectorizer.get_feature_names()
    # codificador de documentos
    vector = vectorizer.transform(documentos)
    
    datos = vector.toarray()
    suma = 0
    for x in range(len(vocabulario)):
        suma = suma + datos[0][x]
    return casos,palabras,suma

def obtener_top(tipocaso):
    tema=[]
    score=[]
    casos=[]
    for y in keys:
        resultados = (obtener_score(keys,contar,data,tipocaso,y))
        casos.append(resultados[0])
        tema.append(resultados[1])
        score.append(resultados[2])
            
    #print(tema)
    #print(score)
    #print(max(score))
    #print(score.index(max(score)))
    temadef = (tema[score.index(max(score))])
    tipocasodef = (casos[score.index(max(score))])
    print("la clasificacion para el Tema es",tipocasodef,"es =",temadef)
    print("-----------------------------------------------------------------")
    

def clasificar():
    for y in casos:
        obtener_top(y)
clasificar()      