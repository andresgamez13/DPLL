import UnitPropagate as UP

def elimina_clausulas(l, string):
    new_clause = ''
    if l in string:
        for x in range(len(string)-1):
            if string[x]+string[x+1] != '-'+l:
                new_clause += string[x]
    new_clause += string[len(string)-1]
    return new_clause


def DPLL(S, I):
    if UP.UnitPropagate(S, I):
       S, I = UP.UnitPropagate(S, I)

    if  [] in S:
        return False, {}

    if  len(S) == 0:
        return True, {}

    for i in S:
        if i[0] != '-':
            l = i[0]
            if l not in I:
                break
        else:
            l = i[1]
            if l not in I:
                break

    print("Escogio:",l)
    new_S = set()
    for i in S:
        new_S.add(elimina_clausulas(l, i).replace(l, ''))

    new_I = {}
    new_I[l] = 1
    print(l)
    if DPLL(new_S, new_I):
        new_I[l] = 0
        return True, new_I

    else:
        new_Sv2 = set()
        for i in S:
            if i[0] != '-':
                l = i[0]
                if l not in I:
                    break
            else:
                l = i[1]
                if l not in I:
                    break
        new_I[l] = 0
        return DPLL(new_Sv2, new_I)


a = {'p-qr', '-pq-r','-p-qr','-p-q-r'}
print(DPLL(a, {}))
