def misca_discurile(x, i, j):
    if x > 1:
        misca_discurile(x-1, i, 6-i-j)
        print(i, ' -> ', j)
        misca_discurile(x-1, 6-i-j, j)
    else:
        print(i, ' -> ', j)

n = int(input('Dati numarul de discuri n: '))
misca_discurile(n, 1, 2)
