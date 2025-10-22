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
    "japon": {"idioma": "japones", "comida": "sushi", "oceanos": ["pacifico"], "bandera": ["blanco", "rojo"]},
    "portugal": {"idioma": "portugues", "comida": "bacalao", "oceanos": ["atlantico"], "bandera": ["rojo", "verde"]},
    "rusia": {"idioma": "ruso", "comida": "borsch", "oceanos": ["artico", "pacifico"], "bandera": ["blanco", "azul", "rojo"]},
    "australia": {"idioma": "ingles", "comida": "meat pie", "oceanos": ["indico", "pacifico"], "bandera": ["azul", "rojo", "blanco"]},
    "egipto": {"idioma": "arabe", "comida": "koshari", "oceanos": ["atlantico"], "bandera": ["rojo", "blanco", "negro", "amarillo"]},
    "sudafrica": {"idioma": "ingles", "comida": "bobotie", "oceanos": ["atlantico", "indico"], "bandera": ["verde", "amarillo", "negro", "blanco", "rojo", "azul"]},
    "india": {"idioma": "hindi", "comida": "curry", "oceanos": ["indico"], "bandera": ["naranja", "blanco", "verde", "azul"]},
    "marruecos": {"idioma": "arabe", "comida": "cuscus", "oceanos": ["atlantico"], "bandera": ["rojo", "verde"]},
    "turquia": {"idioma": "turco", "comida": "kebab", "oceanos": ["atlantico"], "bandera": ["rojo", "blanco"]},
    "grecia": {"idioma": "griego", "comida": "moussaka", "oceanos": ["atlantico"], "bandera": ["azul", "blanco"]},
    "noruega": {"idioma": "noruego", "comida": "salmon", "oceanos": ["atlantico", "artico"], "bandera": ["rojo", "azul", "blanco"]},
    "suecia": {"idioma": "sueco", "comida": "albondigas", "oceanos": ["atlantico"], "bandera": ["azul", "amarillo"]},
    "finlandia": {"idioma": "fines", "comida": "karjalanpiirakka", "oceanos": ["atlantico", "artico"], "bandera": ["azul", "blanco"]},
    "corea_sur": {"idioma": "coreano", "comida": "kimchi", "oceanos": ["pacifico"], "bandera": ["blanco", "rojo", "azul", "negro"]},
    "arabia_saudita": {"idioma": "arabe", "comida": "kabsa", "oceanos": [], "bandera": ["verde", "blanco"]}
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
    explicacion = []
    porcentaje = 0.0
    # Idioma
    if usuario["idioma"] == pais["idioma"]:
        porcentaje += 25
        explicacion.append("Coincide el idioma (+25%).")
    else:
        explicacion.append("El idioma no coincide (+0%).")

    # Comida
    if usuario["comida"] == pais["comida"]:
        porcentaje += 25
        explicacion.append("Coincide la comida típica (+25%).")
    else:
        explicacion.append("La comida no coincide (+0%).")

    # Océanos (proporcional)
    pais_oceanos = set(pais["oceanos"])
    usuario_oceanos = set(usuario["oceanos"])
    if pais_oceanos:
        coincidencias_oceanos = len(pais_oceanos & usuario_oceanos)
        prop_oceanos = coincidencias_oceanos / len(pais_oceanos)
        porcentaje += prop_oceanos * 25
        explicacion.append(f"Coincidencia de océanos: {coincidencias_oceanos} de {len(pais_oceanos)} (+{prop_oceanos*25:.2f}%).")
    else:
        if not usuario_oceanos:
            porcentaje += 25
            explicacion.append("Ninguno limita con océano (+25%).")
        else:
            explicacion.append("El país no limita con océanos (+0%).")

    # Colores de bandera (proporcional)
    pais_colores = set(pais["bandera"])
    usuario_colores = set(usuario["bandera"])
    if pais_colores:
        coincidencias_colores = len(pais_colores & usuario_colores)
        prop_colores = coincidencias_colores / len(pais_colores)
        porcentaje += prop_colores * 25
        explicacion.append(f"Coincidencia de colores de bandera: {coincidencias_colores} de {len(pais_colores)} (+{prop_colores*25:.2f}%).")
    else:
        explicacion.append("El país no tiene colores de bandera definidos (+0%).")

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
