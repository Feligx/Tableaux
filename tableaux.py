#-*-coding: utf-8-*-
from random import choice 
##############################################################################
# Variables globales
##############################################################################

# Crea las letras minúsculas a-z
letrasProposicionales = [chr(x) for x in range(97, 123)]
# inicializa la lista de interpretaciones
listaInterpsVerdaderas = [] 
# inicializa la lista de hojas
listaHojas = []

#ConectivosBinarios = ["Y","O",">","<->"]

##############################################################################
# Definición de objeto tree y funciones de árboles
##############################################################################

class Tree(object):
	def __init__(self, label, left, right):
		self.left = left 
		self.right = right
		self.label = label

def Inorder(f):
    # Imprime una formula como cadena dada una formula como arbol
    # Input: tree, que es una formula de logica proposicional
    # Output: string de la formula
	if f.right == None:
		return f.label
	elif f.label == '-':
		return f.label + Inorder(f.right)
	else:
		return "(" + Inorder(f.left) + f.label + Inorder(f.right) + ")"

def String2Tree(A):
    # Crea una formula como tree dada una formula como cadena escrita en notacion polaca inversa
    # Input: A, lista de caracteres con una formula escrita en notacion polaca inversa
             # letrasProposicionales, lista de letras proposicionales
    # Output: formula como tree

	# OJO: DEBE INCLUIR SU CÓDIGO DE STRING2TREE EN ESTA PARTE!!!!!

	p = letrasProposicionales[0] # ELIMINE ESTA LINEA LUEGO DE INCLUIR EL CODIGO DE STRING2TREE
	return Tree(p, None, None) # ELIMINE ESTA LINEA LUEGO DE INCLUIR EL CODIGO DE STRING2TREE

##############################################################################
# Definición de funciones de tableaux
##############################################################################

def imprime_hoja(H):
	cadena = "{"
	primero = True
	for f in H:
		if primero == True:
			primero = False
		else:
			cadena += ", "
		cadena += Inorder(f)
	return cadena + "}"

P = '-q' 

def complemento(l):
    if len(l) == 1 or len(l)==2:
        if (l[0]=='-' and l[1] != '-'):
            return Inorder(Tree(l[1],None,None))
        elif (l[0] != '-' and len(l)==1):
            return Inorder(Tree('-',None,Tree(l[0],None,None)))
    
print(complemento(P))   

listaliterales=['p','-p','r','-s','s'] 

def par_complementario(l):
	# Esta función determina si una lista de solo literales
	# contiene un par complementario
	# Input: l, una lista de literales
	# Output: True/False
    for i in range(0,len(l)):
        for j in range(1,len(l)):
            if l[i]==complemento(l[j]):
                return True 
    return False 
        
print(par_complementario(listaliterales))  

T2 = Tree("Y",Tree("p",None,None),Tree("q",None,None))
def es_literal(f):
	# Esta función determina si el árbol f es un literal
	# Input: f, una fórmula como árbol
	# Output: True/False
    if f.right == None:
        return True
    elif f.label == '-' and f.right.right== None:
        return es_literal(f.right);
    else:
        return False

print(es_literal(T2)) 

def no_literales(l):
	# Esta función determina si una lista de fórmulas contiene
	# solo literales
	# Input: l, una lista de fórmulas como árboles
	# Output: None/f, tal que f no es literal
	return False

T1 = Tree('O',Tree('-',None,Tree('s',None,None)),Tree('Y',Tree('t',None,None),Tree('>',Tree('u',None,None),Tree('v',None,None))))
def Clasificacion(a): 
    if a.label=="-":
        if (a.right).label=="-":
            return "1-Alfa"
        elif (a.right).label=="O":
            return "3-Alfa"
        elif (a.right).label==">":
            return "4-Alfa"
        elif (a.right).label =="Y":
            return "1-Beta"
        else:
            return "Error en la clasificación"
    else:
        if a.label=="Y":
            return "2-Alfa"
        elif a.label == "O": 
            return "2-Beta"
        elif a.label==">":
            return "3-Beta" 
        else:
            return "Error en la clasificación"

print(Clasificacion(T1))
            
def clasifica_y_extiende(f):
	# clasifica una fórmula como alfa o beta y extiende listaHojas
	# de acuerdo a la regla respectiva
	# Input: f, una fórmula como árbol
	# Output: no tiene output, pues modifica la variable global listaHojas
	global listaHojas

def Tableaux(f):

	# Algoritmo de creacion de tableau a partir de lista_hojas
	# Imput: - f, una fórmula como string en notación polaca inversa
	# Output: interpretaciones: lista de listas de literales que hacen
	#		 verdadera a f
	global listaHojas
	global listaInterpsVerdaderas

	A = String2Tree(f)
	listaHojas = [[A]]

	return listaInterpsVerdaderas
