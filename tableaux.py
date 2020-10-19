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
    global letrasPropocisionales
    conectivos=['O','Y','>']
    pila=[]
    for c in A:
        if c in letrasProposicionales:
            pila.append(Tree(c,None,None))
        elif c=='-':
            formulaAux=Tree(c,None,pila[-1])
            del pila[-1]
            pila.append(formulaAux)
        elif c in conectivos:
            formulaAux=Tree(c,pila[-1],pila[-2])
            del pila[-1]
            del pila[-1]
            pila.append(formulaAux)
	else:
            print(u"Hay un problema: el símbolo"+str(c)+"no se reconoce")
    return pila[-1]

def Inorder2Tree(A):
	if len(A) == 1:
		return Tree(A[0], None, None)
	elif A[0] == '-':
		return Tree(A[0], None, Inorder2Tree(A[1:]))
	elif A[0] == "(":
		counter = 0 #Contador de parentesis
		for i in range(1, len(A)):
			if A[i] == "(":
				counter += 1
			elif A[i] == ")":
				counter -=1
			elif (A[i] in ['Y', 'O', '>', '=']) and (counter == 0):
				return Tree(A[i], Inorder2Tree(A[1:i]), Inorder2Tree(A[i + 1:-1]))
	else:
		return -1
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

def no_literales(l):
	# Esta función determina si una lista de fórmulas contiene
	# solo literales
	# Input: l, una lista de fórmulas como árboles
	# Output: None/f, tal que f no es literal
    for f in l:
       	if not es_literal(f):
        	return "No todos son literales: " + Inorder(f)
    return None

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
            
def clasifica_y_extiende(f,h):
	# clasifica una fórmula como alfa o beta y extiende listaHojas
	# de acuerdo a la regla respectiva
	# Input: f, una fórmula como árbol
	# Output: no tiene output, pues modifica la variable global listaHojas
	global listaHojas
	print("Formula: ", Inorder(f))
	print("Hoja: ", imprime_hoja(h))
	
	assert(f in h), "La formula no esta en la lista!"
	
	clase= clasificación(f)
    	print("Clasificada como: ", clase)
    	assert(clase != None), "Formula incorrecta" + imprime_hoja(h)
    
    	if clase == '1-Alfa':
        	aux = [x for x in h]
        	listaHojas.remove(h)
        	aux.remove(f)
        	aux += [f.right.right]
        	listaHojas.append(aux)
    	elif clase == '2-Alfa':
        	aux = [x for x in h]
        	listaHojas.remove(h)
        	aux.remove(f)
        	aux +=[f.left]
        	aux +=[f.right]
        	listaHojas.append(aux)
    	elif clase == '3-Alfa':
	        aux = [x for x in h]
	        listaHojas.remove(h)
	        aux.remove(f)
        	aux+= [Tree('-',None,f.right.right)]
	        aux+= [Tree('-',None,f.right.left)]
	        listaHojas.append(aux)
    	elif clase == '4-Alfa':
	        aux = [x for x in h]
	        listaHojas.remove(h)
        	aux.remove(f)
	        aux+= [f.right.left]
        	aux+= [Tree('-',None,f.right.right)]
        	listaHojas.append(aux)
    	elif clase == '1-Beta':
	        aux = [x for x in h]
	        aux2= [x for x in h]
	        listaHojas.remove(h)
	        aux.remove(f)
        	aux2.remove(f)
        	aux+= [Tree('-',None,f.right.left)]
        	aux2+= [Tree('-',None,f.right.right)]
        	listaHojas.append(aux)
        	listaHojas.append(aux2)
    	elif clase == '2-Beta':
	        aux = [x for x in h]
	        aux2 = [x for x in h]
	        listaHojas.remove(h)
        	aux.remove(f)
        	aux2.remove(f)
        	aux+= [f.left]
        	aux2+= [f.right]
        	listaHojas.append(aux)
        	listaHojas.append(aux2)
    	elif clase == '3-Beta':
	        aux = [x for x in h]
	        aux2 = [x for x in h]
	        listaHojas.remove(h)
	        aux.remove(f)
	        aux2.remove(f)
	        aux+= [Tree('-',None,f.left)]
	        aux2+= [f.right]
		
def Tableaux(f):

	# Algoritmo de creacion de tableau a partir de lista_hojas
	# Imput: - f, una fórmula como string en notación polaca inversa
	# Output: interpretaciones: lista de listas de literales que hacen
	#		 verdadera a f
	global listaHojas
	global listaInterpsVerdaderas

	A = String2Tree(f)
	
	print(u'La fórmula introducida es:\n', Inorder(A))

	listaHojas = [[A]]
    	while (len(listaHojas) > 0):
        	h = choice(listaHojas)
        	print("Trabajando con hoja:\n", imprime_hoja(h))
       		x = no_literales(h)
        	if x == None:
            		if par_complementario(h):
                		listaHojas.remove(h)
            		else:
		                listaInterpsVerdaderas.append(h)
                		listaHojas.remove(h)
        	else:
            		clasifica_y_extiende(x, h)

	return listaInterpsVerdaderas 
