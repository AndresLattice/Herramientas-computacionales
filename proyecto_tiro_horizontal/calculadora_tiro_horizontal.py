import math


def convertir(texto):
    texto = texto.strip().replace(",", ".")
    if texto.replace(".", "", 1).isdecimal():
        numero = float(texto)
        if numero == int(numero):
            return int(numero)
        return numero
    return 0


def pedir_numero(mensaje):
    numero = 0
    while numero <= 0:
        numero = convertir(input(mensaje))
        if numero <= 0:
            print("Dato no válido, tiene que ser un número mayor que 0")
    return numero


print("==== CALCULADORA DE TIRO HORIZONTAL ====")
print("Objeto lanzado horizontalmente desde una altura")
print("(se puede usar coma o punto en los decimales)")
print()
print("Valores que se necesitan encontrar:")
print("  - Tiempo que tarda en caer (t)")
print("  - Distancia horizontal a la que llega (d)")

seguir = "s"
while seguir == "s":

    print()
    velocidad_inicial = pedir_numero("Velocidad inicial en x, vix (m/s): ")
    altura = pedir_numero("Altura desde la que se lanza, yi (m): ")
    gravedad = 0
    while gravedad <= 0:
        texto = input("Gravedad g sin el signo (m/s²), Enter para usar 9.81: ")
        if texto.strip() == "":
            gravedad = 9.81
        else:
            gravedad = convertir(texto)
            if gravedad <= 0:
                print("Dato no válido, tiene que ser un número mayor que 0")

    aceleracion = -gravedad
    tiempo_vuelo = math.sqrt(-2 * altura / aceleracion)
    alcance = velocidad_inicial * tiempo_vuelo

    print("\n--- Paso 1: datos ---")
    print("Origen en el suelo, el eje x positivo a la derecha y el eje y positivo hacia arriba")
    print(f"vix = {velocidad_inicial} m/s")
    print("viy = 0 (se lanza horizontal)")
    print(f"yi = {altura} m")
    print("yf = 0 (cuando llega al suelo)")
    print(f"a = g = {aceleracion} m/s² (negativa porque la gravedad apunta hacia abajo)")

    print("\n--- Paso 2: tiempo que tarda en caer ---")
    print("Fórmula: yf = yi + viy·t + ½·a·t²")
    print("Por qué: en y es caída libre y esta ecuación relaciona yf, yi, viy y a con t")
    print("Como yf = 0 y viy = 0:  0 = yi + ½·a·t²  →  t = √(-2·yi / a)")
    print("Solo se toma la raíz positiva porque el tiempo no puede ser negativo")
    print(f"Sustitución: t = √(-2 · {altura} / ({aceleracion}))")
    print(f"Resultado: t = {tiempo_vuelo:.2f} s")

    print("\n--- Paso 3: distancia horizontal ---")
    print("Fórmula: vx = d / t  →  d = vx · t")
    print("Por qué: en x es MRU, la velocidad permanece constante (vx = vix)")
    print(f"Sustitución: d = {velocidad_inicial} · {tiempo_vuelo:.4f}")
    print(f"Resultado: d = {alcance:.2f} m")

    print()
    print(f"Respuesta: tarda {tiempo_vuelo:.2f} s en caer y llega a {alcance:.2f} m")

    seguir = input("\n¿Quieres resolver otro problema? (s/n): ").strip().lower()

print("Fin")
