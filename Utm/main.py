from functools import reduce

# Datos (Inmutables)
estudiantes = (
    "Ana",
    "Luis",
    "Carlos",
    "María",
    "Sofía"
)

calificaciones = (
    (90, 85, 88),
    (70, 65, 75),
    (100, 95, 98),
    (80, 78, 85),
    (60, 55, 58)
)
# Funciones Puras


def promedio(notas):
    return reduce(lambda x, y: x + y, notas) / len(notas)


def estado(prom):
    return "Aprobado" if prom >= 70 else "Reprobado"

# map()

promedios = tuple(map(promedio, calificaciones))

# zip()

datos = tuple(zip(estudiantes, promedios))

# map() con lambda
resultado = tuple(
    map(
        lambda x: (x[0], round(x[1], 2), estado(x[1])),
        datos
    )
)

# filter()

aprobados = tuple(
    filter(lambda x: x[2] == "Aprobado", resultado)
)

# reduce()

promedio_general = reduce(
    lambda x, y: x + y,
    promedios
) / len(promedios)
# Función de Primera Clase

def aplicar(funcion, datos):
    return tuple(map(funcion, datos))

nombres_mayusculas = aplicar(lambda x: x.upper(), estudiantes)

# Salida


print("=== RESULTADO FINAL ===")
print(resultado)

print("\n=== APROBADOS ===")
print(aprobados)

print("\n=== PROMEDIO GENERAL ===")
print(round(promedio_general, 2))

print("\n=== NOMBRES EN MAYÚSCULAS ===")
print(nombres_mayusculas)