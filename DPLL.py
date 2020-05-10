import UnitPropagate as UP


def DPLL(S, I):
    S, I = UP.UnitPropagate(S, I)

    if  [] in S:
        return "Insatisfacible", {}

    if not S:
        return "Satisfacible", I

    for i in S:
        for x in i:
            if x not in I and x[:0] + x[1:] not in I and '-'+x not in I:
                l = x
                break
        if l:
            break



    if l[0] != '-':
        lcomp = '-'+l
    elif l[0] == '-':
        lcomp = l[:0] + l[1:]

    new_S = []
    for i in S:
        new_clause = []
        for x in i:
            if lcomp != x:
                if l not in i:
                    new_clause.append(x)
        if new_clause not in new_S and new_clause:
            new_S.append(new_clause)
    I[l] = 1
    new_I = I.copy()
    new_I[l] = 0
    if DPLL(new_S, I) == ("Satisfacible", new_I):
        return "Satisfacible", new_I
    
    else:
        new_Sv2 = []
        for i in S:
            new_clause = []
            for x in i:
                if l != x:
                    if lcomp not in i:
                        new_clause.append(x)
            if new_clause not in new_Sv2 and new_clause:
                new_Sv2.append(new_clause)
        return DPLL(new_Sv2, new_I)





b = [['p', '-q', 'r'], ['-p', 'q', '-r'], ['-p', '-q', 'r'], ['-p', '-q', '-r']]
print(DPLL(b, {}))
