#punto de mira

#1 repo
#2 como módulo
#3 importar libreria gráfico
#4 imprimir una coordenada gráfico
#5 imprimir lista


import matplotlib.pyplot as plt

coordenadas = [
        [1,3], [-2,5], [-3, 3], [-1,0],
        [20, 20], [-20, -20]
    ]

def punto_de_mira(coordenadas):
    # plt.plot(3, 3, 'rs', -2, 5, 'g+', -3, 3, 'k^', -1, 0, 'b.')
    # plt.plot(3, 3, 'rs')
    # plt.plot(-2, 5, 'g+')
    # plt.plot( -3, 3, 'k^')
    # plt.plot(-1, 0, 'b.')
    
    for coordenada in coordenadas:
        # coordenada = [1, 3]
        plt.plot(coordenada[0], coordenada[1], 'bo')


    plt.ylabel("y")
    plt.xlabel("x")
    plt.legend()
    plt.show()
    print ("Hola punto de mira")

if __name__ == "__main__":
    punto_de_mira(coordenadas)
    
