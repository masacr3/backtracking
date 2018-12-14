def reinas(sol,etapa):
    print("\nentro etapa",etapa+1)
    if etapa > 3: return False

    sol[etapa] = -1

    for i in range(0 , 4):
        sol[etapa] = i
        print("\netapa",etapa+1,sol)
        input("espera")

        if valido( sol, etapa) : #chekea
            if etapa == 3 : return True

            if reinas(sol, etapa + 1):
                return True
    return False

def valido (sol, etapa):

    for i in range(etapa):
        #print("\netapa:",etapa)
        #print("valido\na->",sol[etapa],"= b->",sol[i],sol[etapa] == sol[i])
        #print("valido\nabs a-b ->",valabs(sol[i],sol[etapa]),"= i-k ->",valabs(i,etapa),valabs(sol[i],sol[etapa]) == valabs(i,etapa))
        #input("espera")
        if sol[etapa] == sol[i] or valabs(sol[i],sol[etapa]) == valabs(i,etapa) : return False

    return True

def valabs(i,k):
    return (i - k) if i > k else (k - i)

def main():
    l = [-1,-1,-1,-1]
    reinas(l,0);
    print(l)

main()
