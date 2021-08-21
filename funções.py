print('--- UTILIZANDO FUNÇÕES---')

def calcAreaTriangulo (base, altura):
    return base*altura/2



def calcAreaCirculo (raio):
    return 3.14 * raio**2


def calcAreaQadrado (base, altura):
    return base * altura

print(calcAreaTriangulo(3,10))
print(calcAreaCirculo(5))
print(calcAreaQadrado(4,4))



areaTerreno = calcAreaQadrado(5.7) + 2*calcAreaCirculo(3.5) + calcAreaTriangulo(4,3)

print(areaTerreno)
