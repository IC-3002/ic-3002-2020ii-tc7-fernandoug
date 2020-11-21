def encontrar_ruta(C):
    res = []
    
    for i in range(len(C)):
        fila = []
        for j in range(len(C[0])):
            fila += [0]
        res += [fila]

    if encontrar_ruta_aux(C, 0, 0, res):
        return res
    return []

def encontrar_ruta_aux(C, i, j, res):
    alto, largo = len(C), len(C[0])
    
    if i == alto - 1 and j == largo - 1:
        res[i][j] = 1
        return True
    
    if i > -1 and i < alto and j > -1 and j < largo and C[i][j] == 0 and res[i][j] == 0:
        res[i][j] = 1

        if encontrar_ruta_aux(C, i + 1, j, res):
            return True
        if encontrar_ruta_aux(C, i, j + 1, res):
            return True
        if encontrar_ruta_aux(C, i - 1, j, res):
            return True
        if encontrar_ruta_aux(C, i, j - 1, res):
            return True
        
        res[i][j] = 0
        return False
