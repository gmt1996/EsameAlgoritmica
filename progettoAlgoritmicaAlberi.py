# funzioni per l'implementazione dell'albero
def nodo(x, s, d):
    return [x, s, d]


def vuoto():
    return None


def foglia(x):
    return [x, None, None]


def radice(T):
    return T[0]


def sinistro(T):
    return T[1]


def destro(T):
    return T[2]


def isVuoto(T):
    return T is None

# funzione per trovare il massimo di un albero binario
def massimo(T):
    if isVuoto(destro(T)):
        return radice(T)
    return massimo(destro(T))

# funzione per trovare il minimo di un albero binario
def minimo(T):
    if isVuoto(sinistro(T)):
        return radice(T)
    return minimo(sinistro(T))

# funzione che calcola la media tra il massimo del sottoalbero sinistro e il minimo del sottoalbero destro
def m(T):
    # controllo sel il nodo radice abbia entrambi i sottoalberi per poter procedere con il programma
    if sinistro(T) == None:
        return "Sotto albero sinistro vuoto"
    # assegno alla variabile il risultato dell'esecuzione della funzione massimo eseguita a partire dal sottoalbero sinistro
    maxSottoAlberoSx = massimo(sinistro(T))
    if destro(T) == None:
        return "Sotto albero destro vuoto"
    # assegno alla variabile il risultato dell'esecuzione della funzione minimo eseguita a partire dal sottoalbero destro
    minSottoAlberoDX = minimo(destro(T))
    # ritorno la media tra il massimo del sottoalbero sinistro e il minimo del sottoalbero destro
    return (maxSottoAlberoSx + minSottoAlberoDX) / 2


E1 = nodo(2, nodo(1, foglia(0), vuoto()), foglia(3))
E2 = nodo(8, nodo(7, foglia(6), vuoto()), foglia(9))
A = nodo(5, E1, E2)
print (m(A))

# risultato dell'esecuzione
4.5