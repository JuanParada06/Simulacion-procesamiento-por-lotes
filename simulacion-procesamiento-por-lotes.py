import os
import time

lista_lotes = []
lotes = []
proc_terminados = []

class Proceso:
    def __init__(self):
        self.programador = ""
        self.operacion = ""
        self.numero1 = 0
        self.numero2 = 0
        self.tiempo_maximo = 0
        self.id_programa = 0
        self.resultado_operacion = 0
        self.cadena_operacion = ""
        self.porcentaje = 0  # Agregado para el porcentaje


def funcionOperacion(operador, proceso):
    while True:
        numero = input("Ingresa el numero 1: ")
        if numero.isdigit():
            proceso.numero1=int(numero)
            break
        else:
            print("INGRESA UN DIGITO")
    while True:
        numero = input("Ingresa el numero 2: ")
        if numero.isdigit():
            proceso.numero2=int(numero)
            break
        else:
            print("INGRESA UN DIGITO")
    proceso.cadena_operacion = '{}{}{}'.format(proceso.numero1, operador, proceso.numero2)
    if operador == "/" or operador=='%':
        if proceso.numero2==0:
            print("No se puede dividir entre 0")
            funcionOperacion(operador,proceso)


def porcentaje(operador, proceso):
    while True:
        numero = input("Ingresa el numero 1: ")
        if numero.isdigit():
            proceso.numero1=int(numero)
            break
        else:
            print("INGRESA UN DIGITO")
    while True:
        numero = input("Ingresa el numero 2: ")
        if numero.isdigit():
            proceso.numero2=int(numero)
            break
        else:
            print("INGRESA UN DIGITO")
    if proceso.numero2==0:
        print("El segundo numero no puede ser 0")
        porcentaje(operador,proceso)
    proceso.porcentaje = (proceso.numero1 / proceso.numero2) * 100


def main():
    while True:
        dato = input("Ingrese la cantidad de procesos a realizar: ")
        if dato.isdigit():
            cantidad=int(dato)
            break
        else:
            print("INGRESA UN DIGITO")
    for x in range(cantidad):
        proceso = Proceso()

        print('\n---------Proceso {}---------'.format(len(lotes) + 1))

        proceso.programador = input("Ingresa el nombre del programador: ")

        while True:
            proceso.operacion = input("Ingrese la operacion a realizar (+, -, *, /, %): ")
            if proceso.operacion in ['+', '-', '*', '/', '%']:
                if proceso.operacion == '%':
                    a=int(input("1.Residuo 2.Porcentaje \nEleccion:"))
                    if a==2:
                        porcentaje(proceso.operacion, proceso)
                        proceso.resultado_operacion = (proceso.porcentaje)
                        break
                    else:
                        funcionOperacion(proceso.operacion, proceso)
                        proceso.resultado_operacion = eval(proceso.cadena_operacion)
                        break
                else:
                    funcionOperacion(proceso.operacion, proceso)
                    proceso.resultado_operacion = eval(proceso.cadena_operacion)
                    break
            else:
                print("Operacion invalida, ingresala de nuevo")

        while True:
                tiempo=input("Ingresa el Tiempo Maximo Estimado del proceso: ")
                if tiempo.isdigit():
                    proceso.tiempo_maximo = int(tiempo)
                    if proceso.tiempo_maximo > 0:
                        break
                    else:
                        print("El tiempo debe ser mayor a 0, ingresalo de nuevo")
                else:
                    print("INGRESA UN DATO VALIDO")

        while True:
            id_p=input("Ingrese el ID: ")
            if id_p.isdigit():
                proceso.id_programa = int(id_p)
                if proceso.id_programa in [p.id_programa for p in lotes]:
                    print("El id ingresado ya ha sido utilizado, ingrese uno nuevo")
                else:
                    lotes.append(proceso)
                    break
            else:
                print("INGRESA UN DIGITO")

    # Se segmentan los lotes (5 procesos por lote)
    for i in range(0, len(lotes), 5):
        lista_lotes.append(lotes[i:i + 5])

    contador_global = 0

    # Impresion de datos
    for i, lote in enumerate(lista_lotes):
        for j, proceso in enumerate(lote):
            tiempoRestante = proceso.tiempo_maximo

            while tiempoRestante >= 0:
                os.system("cls" if os.name == "nt" else "clear")

                print('----Cantidad de lotes pendientes---')
                print(len(lista_lotes) - (i+1))

                print('---------Lote en Ejecucion---------')
                for k in range(j+1, len(lote)):
                    print(' Nombre: {} TME: {}'.format(lote[k].programador, lote[k].tiempo_maximo), end=' |')

                print('\n-------Proceso en Ejecucion--------')
                print(
                    "Nombre: {} \nOperacion: {} \nTME: {} \nId: {} \nTiempo trascurrido: {} \nTiempo restante: {}".format(
                        proceso.programador, proceso.operacion, proceso.tiempo_maximo, proceso.id_programa,
                        contador_global, tiempoRestante))

                if tiempoRestante == 0:
                    proc_terminados.append([proceso.id_programa, proceso.operacion, proceso.resultado_operacion, i + 1])

                print('--------Procesos Terminados--------')
                for proc in proc_terminados:
                    print(
                        "Id: {} Operacion: {} Resultado {:.2f} --> Lote: {}".format(proc[0], proc[1], proc[2], proc[3]))

                tiempoRestante -= 1
                contador_global += 1
                time.sleep(1)

        print('----Cantidad de lotes pendientes---')
        print(len(lista_lotes) - i - 1)
        print('---------Lote en Ejecucion---------')
        print('\n-------Proceso en Ejecucion--------')
        print('--------Procesos Terminados--------')
        for proc in proc_terminados:
            print(
                "Id: {} Operacion: {} Resultado {:.2f} --> Lote: {}".format(proc[0], proc[1], proc[2], proc[3]))


if __name__ == "__main__":
    main()