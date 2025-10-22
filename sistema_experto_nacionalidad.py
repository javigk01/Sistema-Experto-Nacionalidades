"""
Taller 8 - Sistema Experto Interactivo (Python)
Tema: Nacionalidades de países del continente americano
Criterios: idioma, comida típica, océanos y colores de bandera
Motor: Encadenamiento hacia adelante + cálculo de compatibilidad + explicación textual
"""

# -----------------------
# Base de conocimiento
# -----------------------
paises = {
    "argentina": {"idioma": "español", "comida": "asado", "oceanos": ["atlantico"], "bandera": ["celeste", "blanco"]},
    "brasil": {"idioma": "portugues", "comida": "feijoada", "oceanos": ["atlantico"], "bandera": ["verde", "amarillo"]},
    "mexico": {"idioma": "español", "comida": "tacos", "oceanos": ["pacifico", "atlantico"], "bandera": ["verde", "blanco", "rojo"]},
    "chile": {"idioma": "español", "comida": "empanada", "oceanos": ["pacifico"], "bandera": ["rojo", "azul", "blanco"]},
    "peru": {"idioma": "español", "comida": "ceviche", "oceanos": ["pacifico"], "bandera": ["rojo", "blanco"]},
    "colombia": {"idioma": "español", "comida": "arepa", "oceanos": ["pacifico", "atlantico"], "bandera": ["amarillo", "azul", "rojo"]},
    "venezuela": {"idioma": "español", "comida": "arepa", "oceanos": ["atlantico"], "bandera": ["amarillo", "azul", "rojo", "blanco"]},
    "ecuador": {"idioma": "español", "comida": "encebollado", "oceanos": ["pacifico"], "bandera": ["amarillo", "azul", "rojo"]},
    "bolivia": {"idioma": "español", "comida": "silpancho", "oceanos": [], "bandera": ["rojo", "amarillo", "verde"]},
    "guatemala": {"idioma": "español", "comida": "pepian", "oceanos": [], "bandera": ["celeste", "blanco"]},
    "honduras": {"idioma": "español", "comida": "baleada", "oceanos": ["atlantico", "pacifico"], "bandera": ["azul", "blanco"]},
    "cuba": {"idioma": "español", "comida": "ropa vieja", "oceanos": ["atlantico"], "bandera": ["rojo", "azul", "blanco"]},
    "dominicana": {"idioma": "español", "comida": "mangú", "oceanos": ["atlantico"], "bandera": ["azul", "rojo", "blanco"]},
    "estados_unidos": {"idioma": "ingles", "comida": "hamburguesa", "oceanos": ["pacifico", "atlantico"], "bandera": ["rojo", "blanco", "azul"]},
    "canada": {"idioma": "ingles", "comida": "jarabe de arce", "oceanos": ["atlantico", "pacifico"], "bandera": ["rojo", "blanco"]},
    "uruguay": {"idioma": "español", "comida": "chivito", "oceanos": ["atlantico"], "bandera": ["celeste", "blanco", "amarillo"]},
    "paraguay": {"idioma": "español", "comida": "sopa paraguaya", "oceanos": [], "bandera": ["rojo", "blanco", "azul"]},
    "el_salvador": {"idioma": "español", "comida": "pupusa", "oceanos": ["pacifico"], "bandera": ["azul", "blanco"]},
    "costa_rica": {"idioma": "español", "comida": "gallo pinto", "oceanos": ["pacifico", "atlantico"], "bandera": ["azul", "blanco", "rojo"]},
    "panama": {"idioma": "español", "comida": "sancocho", "oceanos": ["pacifico", "atlantico"], "bandera": ["rojo", "azul", "blanco"]},
    "nicaragua": {"idioma": "español", "comida": "gallo pinto", "oceanos": ["pacifico", "atlantico"], "bandera": ["azul", "blanco"]},
    "jamaica": {"idioma": "ingles", "comida": "jerk chicken", "oceanos": ["atlantico"], "bandera": ["negro", "verde", "amarillo"]},
    "haiti": {"idioma": "frances", "comida": "griot", "oceanos": ["atlantico"], "bandera": ["azul", "rojo"]},
    "belice": {"idioma": "ingles", "comida": "rice and beans", "oceanos": ["atlantico"], "bandera": ["azul", "rojo"]},
    "puerto_rico": {"idioma": "español", "comida": "mofongo", "oceanos": ["atlantico"], "bandera": ["rojo", "blanco", "azul"]},
    "españa": {"idioma": "español", "comida": "paella", "oceanos": ["atlantico"], "bandera": ["rojo", "amarillo"]},
    "francia": {"idioma": "frances", "comida": "baguette", "oceanos": ["atlantico"], "bandera": ["azul", "blanco", "rojo"]},
    "italia": {"idioma": "italiano", "comida": "pizza", "oceanos": [], "bandera": ["verde", "blanco", "rojo"]},
    "alemania": {"idioma": "aleman", "comida": "salchicha", "oceanos": [], "bandera": ["negro", "rojo", "amarillo"]},
    "china": {"idioma": "chino", "comida": "arroz frito", "oceanos": ["pacifico"], "bandera": ["rojo", "amarillo"]},
    "japon": {"idioma": "japones", "comida": "sushi", "oceanos": ["pacifico"], "bandera": ["blanco", "rojo"]}
}

# -----------------------
# Función para pedir datos
# -----------------------
def pedir_datos_usuario():
    print("=== SISTEMA EXPERTO: DETERMINACIÓN DE NACIONALIDAD ===\n")
    idioma = input("¿Qué idioma habla la persona? (español/portugues/ingles): ").lower().strip()
    comida = input("¿Cuál es la comida típica del país?: ").lower().strip()
    oceanos_input = input("¿Con qué océanos limita? (separa por comas o escribe 'ninguno'): ").lower().strip()

    if oceanos_input == "ninguno" or oceanos_input == "":
        oceanos = []
    else:
        oceanos = [o.strip() for o in oceanos_input.split(",")]

    colores = [c.strip() for c in input("¿Qué colores tiene su bandera? (separados por comas): ").lower().split(",")]

    return {"idioma": idioma, "comida": comida, "oceanos": oceanos, "bandera": colores}

# -----------------------
# Cálculo de compatibilidad y explicación
# -----------------------
def calcular_compatibilidad(usuario, pais):
    total_criterios = 4
    coincidencias = 0
    explicacion = []

    # Comparar idioma
    if usuario["idioma"] == pais["idioma"]:
        coincidencias += 1
        explicacion.append("Coincide el idioma.")
    else:
        explicacion.append("El idioma no coincide.")

    # Comparar comida
    if usuario["comida"] == pais["comida"]:
        coincidencias += 1
        explicacion.append("Coincide la comida típica.")
    else:
        explicacion.append("La comida no coincide.")

    # Comparar océanos (coincidencia exacta)
    if set(usuario["oceanos"]) == set(pais["oceanos"]):
        coincidencias += 1
        if not usuario["oceanos"]:
            explicacion.append("Ninguno limita con océano (coincide exactamente).")
        else:
            explicacion.append("Coinciden exactamente los océanos.")
    else:
        explicacion.append("Los océanos no coinciden exactamente.")

    # Comparar colores de bandera (coincidencia exacta)
    if set(usuario["bandera"]) == set(pais["bandera"]):
        coincidencias += 1
        explicacion.append("Coinciden exactamente los colores de la bandera.")
    else:
        explicacion.append("Los colores de la bandera no coinciden exactamente.")

    porcentaje = (coincidencias / total_criterios) * 100
    return porcentaje, explicacion

# -----------------------
# Ejecución principal
# -----------------------
if __name__ == "__main__":
    usuario = pedir_datos_usuario()

    print("\n--- CÁLCULO DE COMPATIBILIDAD ---\n")
    resultados = {}
    explicaciones = {}

    for nombre, datos in paises.items():
        compat, explicacion = calcular_compatibilidad(usuario, datos)
        resultados[nombre] = compat
        explicaciones[nombre] = explicacion
        print(f"{nombre.title()}: {compat:.2f}%")

    mejor_pais = max(resultados, key=resultados.get)
    mejor_porcentaje = resultados[mejor_pais]
    mejor_explicacion = explicaciones[mejor_pais]

    print("\n--- RESULTADO FINAL ---")
    if mejor_porcentaje == 0:
        print("❌ No hay coincidencias suficientes para determinar la nacionalidad.")
    else:
        print(f"✅ La nacionalidad más probable es: {mejor_pais.upper()} ({mejor_porcentaje:.1f}% de compatibilidad)\n")

        print("📘 Explicación del resultado:")
        for e in mejor_explicacion:
            print(f" - {e}")
