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
    "argentina": {"idioma": "español", "comida": "asado", "oceanos": ["atlantico"], "mares": ["mar argentino"], "bandera": ["celeste", "blanco"]},
    "brasil": {"idioma": "portugues", "comida": "feijoada", "oceanos": ["atlantico"], "mares": [], "bandera": ["verde", "amarillo"]},
    "mexico": {"idioma": "español", "comida": "tacos", "oceanos": ["pacifico", "atlantico"], "mares": ["mar caribe"], "bandera": ["verde", "blanco", "rojo"]},
    "chile": {"idioma": "español", "comida": "empanada", "oceanos": ["pacifico"], "mares": [], "bandera": ["rojo", "azul", "blanco"]},
    "peru": {"idioma": "español", "comida": "ceviche", "oceanos": ["pacifico"], "mares": [], "bandera": ["rojo", "blanco"]},
    "colombia": {"idioma": "español", "comida": "arepa", "oceanos": ["pacifico", "atlantico"], "mares": ["mar caribe"], "bandera": ["amarillo", "azul", "rojo"]},
    "venezuela": {"idioma": "español", "comida": "arepa", "oceanos": ["atlantico"], "mares": ["mar caribe"], "bandera": ["amarillo", "azul", "rojo", "blanco"]},
    "ecuador": {"idioma": "español", "comida": "encebollado", "oceanos": ["pacifico"], "mares": [], "bandera": ["amarillo", "azul", "rojo"]},
    "bolivia": {"idioma": "español", "comida": "silpancho", "oceanos": [], "mares": [], "bandera": ["rojo", "amarillo", "verde"]},
    "guatemala": {"idioma": "español", "comida": "pepian", "oceanos": [], "mares": [], "bandera": ["celeste", "blanco"]},
    "honduras": {"idioma": "español", "comida": "baleada", "oceanos": ["atlantico", "pacifico"], "mares": ["mar caribe"], "bandera": ["azul", "blanco"]},
    "cuba": {"idioma": "español", "comida": "ropa vieja", "oceanos": ["atlantico"], "mares": ["mar caribe"], "bandera": ["rojo", "azul", "blanco"]},
    "dominicana": {"idioma": "español", "comida": "mangú", "oceanos": ["atlantico"], "mares": ["mar caribe"], "bandera": ["azul", "rojo", "blanco"]},
    "estados_unidos": {"idioma": "ingles", "comida": "hamburguesa", "oceanos": ["pacifico", "atlantico"], "mares": ["mar de bering", "mar de los sargazos"], "bandera": ["rojo", "blanco", "azul"]},
    "canada": {"idioma": "ingles", "comida": "jarabe de arce", "oceanos": ["atlantico", "pacifico"], "mares": ["mar de labrador"], "bandera": ["rojo", "blanco"]},
    "uruguay": {"idioma": "español", "comida": "chivito", "oceanos": ["atlantico"], "mares": [], "bandera": ["celeste", "blanco", "amarillo"]},
    "paraguay": {"idioma": "español", "comida": "sopa paraguaya", "oceanos": [], "mares": [], "bandera": ["rojo", "blanco", "azul"]},
    "el_salvador": {"idioma": "español", "comida": "pupusa", "oceanos": ["pacifico"], "mares": [], "bandera": ["azul", "blanco"]},
    "costa_rica": {"idioma": "español", "comida": "gallo pinto", "oceanos": ["pacifico", "atlantico"], "mares": ["mar caribe"], "bandera": ["azul", "blanco", "rojo"]},
    "panama": {"idioma": "español", "comida": "sancocho", "oceanos": ["pacifico", "atlantico"], "mares": ["mar caribe"], "bandera": ["rojo", "azul", "blanco"]},
    "nicaragua": {"idioma": "español", "comida": "gallo pinto", "oceanos": ["pacifico", "atlantico"], "mares": ["mar caribe"], "bandera": ["azul", "blanco"]},
    "jamaica": {"idioma": "ingles", "comida": "jerk chicken", "oceanos": ["atlantico"], "mares": ["mar caribe"], "bandera": ["negro", "verde", "amarillo"]},
    "haiti": {"idioma": "frances", "comida": "griot", "oceanos": ["atlantico"], "mares": ["mar caribe"], "bandera": ["azul", "rojo"]},
    "belice": {"idioma": "ingles", "comida": "rice and beans", "oceanos": ["atlantico"], "mares": ["mar caribe"], "bandera": ["azul", "rojo"]},
    "puerto_rico": {"idioma": "español", "comida": "mofongo", "oceanos": ["atlantico"], "mares": ["mar caribe"], "bandera": ["rojo", "blanco", "azul"]},
    "españa": {"idioma": "español", "comida": "paella", "oceanos": ["atlantico"], "mares": ["mar mediterraneo"], "bandera": ["rojo", "amarillo"]},
    "francia": {"idioma": "frances", "comida": "baguette", "oceanos": ["atlantico"], "mares": ["mar mediterraneo"], "bandera": ["azul", "blanco", "rojo"]},
    "italia": {"idioma": "italiano", "comida": "pizza", "oceanos": [], "mares": ["mar mediterraneo"], "bandera": ["verde", "blanco", "rojo"]},
    "alemania": {"idioma": "aleman", "comida": "salchicha", "oceanos": [], "mares": ["mar baltico", "mar del norte"], "bandera": ["negro", "rojo", "amarillo"]},
    "china": {"idioma": "chino", "comida": "arroz frito", "oceanos": ["pacifico"], "mares": ["mar de china meridional", "mar amarillo"], "bandera": ["rojo", "amarillo"]},
    "japon": {"idioma": "japones", "comida": "sushi", "oceanos": ["pacifico"], "mares": ["mar de japon", "mar de china oriental"], "bandera": ["blanco", "rojo"]},
    "portugal": {"idioma": "portugues", "comida": "bacalao", "oceanos": ["atlantico"], "mares": [], "bandera": ["rojo", "verde"]},
    "rusia": {"idioma": "ruso", "comida": "borsch", "oceanos": ["artico", "pacifico"], "mares": ["mar baltico", "mar negro", "mar de okhotsk"], "bandera": ["blanco", "azul", "rojo"]},
    "australia": {"idioma": "ingles", "comida": "meat pie", "oceanos": ["indico", "pacifico"], "mares": ["mar de coral", "mar de tasmania"], "bandera": ["azul", "rojo", "blanco"]},
    "egipto": {"idioma": "arabe", "comida": "koshari", "oceanos": ["atlantico"], "mares": ["mar mediterraneo", "mar rojo"], "bandera": ["rojo", "blanco", "negro", "amarillo"]},
    "sudafrica": {"idioma": "ingles", "comida": "bobotie", "oceanos": ["atlantico", "indico"], "mares": [], "bandera": ["verde", "amarillo", "negro", "blanco", "rojo", "azul"]},
    "india": {"idioma": "hindi", "comida": "curry", "oceanos": ["indico"], "mares": ["mar arabigo", "mar de bengala"], "bandera": ["naranja", "blanco", "verde", "azul"]},
    "marruecos": {"idioma": "arabe", "comida": "cuscus", "oceanos": ["atlantico"], "mares": ["mar mediterraneo"], "bandera": ["rojo", "verde"]},
    "turquia": {"idioma": "turco", "comida": "kebab", "oceanos": ["atlantico"], "mares": ["mar negro", "mar mediterraneo", "mar de marmara", "mar egeo"], "bandera": ["rojo", "blanco"]},
    "grecia": {"idioma": "griego", "comida": "moussaka", "oceanos": ["atlantico"], "mares": ["mar egeo", "mar jónico", "mar mediterraneo"], "bandera": ["azul", "blanco"]},
    "noruega": {"idioma": "noruego", "comida": "salmon", "oceanos": ["atlantico", "artico"], "mares": ["mar del norte", "mar de noruega", "mar de barents"], "bandera": ["rojo", "azul", "blanco"]},
    "suecia": {"idioma": "sueco", "comida": "albondigas", "oceanos": ["atlantico"], "mares": ["mar baltico", "mar del norte"], "bandera": ["azul", "amarillo"]},
    "finlandia": {"idioma": "fines", "comida": "karjalanpiirakka", "oceanos": ["atlantico", "artico"], "mares": ["mar baltico"], "bandera": ["azul", "blanco"]},
    "corea_sur": {"idioma": "coreano", "comida": "kimchi", "oceanos": ["pacifico"], "mares": ["mar amarillo", "mar del este"], "bandera": ["blanco", "rojo", "azul", "negro"]},
    "arabia_saudita": {"idioma": "arabe", "comida": "kabsa", "oceanos": [], "mares": ["mar rojo", "golfo persico"], "bandera": ["verde", "blanco"]}
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

    mares_input = input("¿Con qué mares limita? (separa por comas o escribe 'ninguno'): ").lower().strip()
    if mares_input == "ninguno" or mares_input == "":
        mares = []
    else:
        mares = [m.strip() for m in mares_input.split(",")]

    colores = [c.strip() for c in input("¿Qué colores tiene su bandera? (separados por comas): ").lower().split(",")]

    return {"idioma": idioma, "comida": comida, "oceanos": oceanos, "mares": mares, "bandera": colores}

# -----------------------
# Cálculo de compatibilidad y explicación
# -----------------------
def calcular_compatibilidad(usuario, pais):
    explicacion = []
    porcentaje = 0.0
    # Cada criterio vale 20%
    # Idioma
    if usuario["idioma"] == pais["idioma"]:
        porcentaje += 20
        explicacion.append("Coincide el idioma (+20%).")
    else:
        explicacion.append("El idioma no coincide (+0%).")

    # Comida
    if usuario["comida"] == pais["comida"]:
        porcentaje += 20
        explicacion.append("Coincide la comida típica (+20%).")
    else:
        explicacion.append("La comida no coincide (+0%).")

    # Océanos (proporcional)
    pais_oceanos = set(pais["oceanos"])
    usuario_oceanos = set(usuario["oceanos"])
    if pais_oceanos:
        coincidencias_oceanos = len(pais_oceanos & usuario_oceanos)
        prop_oceanos = coincidencias_oceanos / len(pais_oceanos)
        porcentaje += prop_oceanos * 20
        explicacion.append(f"Coincidencia de océanos: {coincidencias_oceanos} de {len(pais_oceanos)} (+{prop_oceanos*20:.2f}%).")
    else:
        if not usuario_oceanos:
            porcentaje += 20
            explicacion.append("Ninguno limita con océano (+20%).")
        else:
            explicacion.append("El país no limita con océanos (+0%).")

    # Mares (proporcional)
    pais_mares = set(pais.get("mares", []))
    usuario_mares = set(usuario.get("mares", []))
    if pais_mares:
        coincidencias_mares = len(pais_mares & usuario_mares)
        prop_mares = coincidencias_mares / len(pais_mares)
        porcentaje += prop_mares * 20
        explicacion.append(f"Coincidencia de mares: {coincidencias_mares} de {len(pais_mares)} (+{prop_mares*20:.2f}%).")
    else:
        if not usuario_mares:
            porcentaje += 20
            explicacion.append("Ninguno limita con mar (+20%).")
        else:
            explicacion.append("El país no limita con mares (+0%).")

    # Colores de bandera (proporcional)
    pais_colores = set(pais["bandera"])
    usuario_colores = set(usuario["bandera"])
    if pais_colores:
        coincidencias_colores = len(pais_colores & usuario_colores)
        prop_colores = coincidencias_colores / len(pais_colores)
        porcentaje += prop_colores * 20
        explicacion.append(f"Coincidencia de colores de bandera: {coincidencias_colores} de {len(pais_colores)} (+{prop_colores*20:.2f}%).")
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
