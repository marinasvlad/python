nr_sol = 0
n = int(input('Introdu-l pe n: '))
coloana = [0 for x in range(30)]


def afisare():
    global nr_sol
    nr_sol += 1
    print('Solutia nr. :', nr_sol)
    for i in range(n):
        for j in range(n):
            if j == coloana[i]:
                print(' * ', end=' ')
            else:
                print(' # ', end=' ')
        print()


def plaseaza_regina(k):
    if k == n:
        afisare()
    else:
        for i in range(n):
            ok = 1
            for j in range(k):
                if coloana[j] == i or abs(coloana[j]-i) == k-j:
                    ok = 0
            if ok == 1:
                coloana[k] = i
                plaseaza_regina(k+1)


plaseaza_regina(0)

