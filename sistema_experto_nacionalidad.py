"""
Taller 8 - Sistemas Expertos Interactivo (Python)
Tema: Nacionalidades de países del continente americano
Criterios: idioma, comida típica, océano, colores de bandera
Motor: Encadenamiento hacia adelante (forward chaining)
"""

from pprint import pprint

# -----------------------
# Base de conocimiento (hechos fijos de los países)
# -----------------------
facts = set([
    # Argentina
    "argentina:idioma:español",
    "argentina:comida:asado",
    "argentina:oceano:atlantico",
    "argentina:bandera:celeste",
    "argentina:bandera:blanco",
    # Brasil
    "brasil:idioma:portugues",
    "brasil:comida:feijoada",
    "brasil:oceano:atlantico",
    "brasil:bandera:verde",
    "brasil:bandera:amarillo",
    # México
    "mexico:idioma:español",
    "mexico:comida:tacos",
    "mexico:oceano:pacifico",
    "mexico:oceano:atlantico",
    "mexico:bandera:verde",
    "mexico:bandera:blanco",
    "mexico:bandera:rojo",
    # Chile
    "chile:idioma:español",
    "chile:comida:empanada",
    "chile:oceano:pacifico",
    "chile:bandera:rojo",
    "chile:bandera:azul",
    "chile:bandera:blanco",
    # Perú
    "peru:idioma:español",
    "peru:comida:ceviche",
    "peru:oceano:pacifico",
    "peru:bandera:rojo",
    "peru:bandera:blanco",
    # Colombia
    "colombia:idioma:español",
    "colombia:comida:arepa",
    "colombia:oceano:pacifico",
    "colombia:oceano:atlantico",
    "colombia:bandera:amarillo",
    "colombia:bandera:azul",
    "colombia:bandera:rojo",
    # Ecuador
    "ecuador:idioma:español",
    "ecuador:comida:encebollado",
    "ecuador:oceano:pacifico",
    "ecuador:bandera:amarillo",
    "ecuador:bandera:azul",
    "ecuador:bandera:rojo",
    # Uruguay
    "uruguay:idioma:español",
    "uruguay:comida:chivito",
    "uruguay:oceano:atlantico",
    "uruguay:bandera:celeste",
    "uruguay:bandera:blanco",
    # Paraguay
    "paraguay:idioma:español",
    "paraguay:comida:sopa paraguaya",
    "paraguay:bandera:rojo",
    "paraguay:bandera:blanco",
    "paraguay:bandera:azul",
    # Bolivia
    "bolivia:idioma:español",
    "bolivia:comida:salteña",
    "bolivia:bandera:rojo",
    "bolivia:bandera:amarillo",
    "bolivia:bandera:verde",
    # Venezuela
    "venezuela:idioma:español",
    "venezuela:comida:arepa",
    "venezuela:oceano:atlantico",
    "venezuela:bandera:amarillo",
    "venezuela:bandera:azul",
    "venezuela:bandera:rojo",
    "venezuela:bandera:blanco",
    # Guatemala
    "guatemala:idioma:español",
    "guatemala:comida:pepian",
    "guatemala:oceano:pacifico",
    "guatemala:bandera:azul",
    "guatemala:bandera:blanco",
    # Honduras
    "honduras:idioma:español",
    "honduras:comida:baleada",
    "honduras:oceano:pacifico",
    "honduras:oceano:atlantico",
    "honduras:bandera:azul",
    "honduras:bandera:blanco",
    # El Salvador
    "el_salvador:idioma:español",
    "el_salvador:comida:pupusa",
    "el_salvador:oceano:pacifico",
    "el_salvador:bandera:azul",
    "el_salvador:bandera:blanco",
    # Nicaragua
    "nicaragua:idioma:español",
    "nicaragua:comida:gallo pinto",
    "nicaragua:oceano:pacifico",
    "nicaragua:oceano:atlantico",
    "nicaragua:bandera:azul",
    "nicaragua:bandera:blanco",
    # Costa Rica
    "costa_rica:idioma:español",
    "costa_rica:comida:gallo pinto",
    "costa_rica:oceano:pacifico",
    "costa_rica:oceano:atlantico",
    "costa_rica:bandera:azul",
    "costa_rica:bandera:blanco",
    "costa_rica:bandera:rojo",
    # Panamá
    "panama:idioma:español",
    "panama:comida:sancocho",
    "panama:oceano:pacifico",
    "panama:oceano:atlantico",
    "panama:bandera:azul",
    "panama:bandera:blanco",
    "panama:bandera:rojo",
    # Puerto Rico
    "puerto_rico:idioma:español",
    "puerto_rico:comida:mofongo",
    "puerto_rico:oceano:atlantico",
    "puerto_rico:bandera:rojo",
    "puerto_rico:bandera:azul",
    "puerto_rico:bandera:blanco",
    # Estados Unidos
    "estados_unidos:idioma:ingles",
    "estados_unidos:comida:hamburguesa",
    "estados_unidos:oceano:pacifico",
    "estados_unidos:bandera:rojo",
    "estados_unidos:bandera:blanco",
    "estados_unidos:bandera:azul",
    # Canadá
    "canada:idioma:ingles",
    "canada:idioma2:frances",
    "canada:comida:jarabe de arce",
    "canada:oceano:atlantico",
    "canada:bandera:rojo",
    "canada:bandera:blanco",
    # Cuba
    "cuba:idioma:español",
    "cuba:comida:ropa vieja",
    "cuba:oceano:atlantico",
    "cuba:bandera:rojo",
    "cuba:bandera:azul",
    "cuba:bandera:blanco",
    # República Dominicana
    "dominicana:idioma:español",
    "dominicana:comida:mangú",
    "dominicana:oceano:atlantico",
    "dominicana:bandera:azul",
    "dominicana:bandera:rojo",
    "dominicana:bandera:blanco"
])

# -----------------------
# Reglas (igual que antes, 25+)
# -----------------------
rules = [
    # Argentina
    {"id": 1, "conditions": ["persona:idioma:español", "argentina:idioma:español",
                             "persona:comida:asado", "argentina:comida:asado",
                             "persona:oceano:atlantico", "argentina:oceano:atlantico",
                             "persona:bandera:celeste", "argentina:bandera:celeste"],
     "conclusion": "nacionalidad:argentina",
     "description": "Idioma, comida, océano y bandera coinciden -> Argentina"},
    # Brasil
    {"id": 2, "conditions": ["persona:idioma:portugues", "brasil:idioma:portugues",
                             "persona:comida:feijoada", "brasil:comida:feijoada",
                             "persona:oceano:atlantico", "brasil:oceano:atlantico"],
     "conclusion": "nacionalidad:brasil",
     "description": "Portugués + feijoada + Atlántico -> Brasil"},
    # México
    {"id": 3, "conditions": ["persona:idioma:español", "mexico:idioma:español",
                             "persona:comida:tacos", "mexico:comida:tacos",
                             "persona:oceano:pacifico", "mexico:oceano:pacifico",
                             "persona:bandera:verde", "mexico:bandera:verde"],
     "conclusion": "nacionalidad:mexico",
     "description": "Español + tacos + Pacífico + verde -> México"},
    # Chile
    {"id": 4, "conditions": ["persona:idioma:español", "chile:idioma:español",
                             "persona:comida:empanada", "chile:comida:empanada",
                             "persona:oceano:pacifico", "chile:oceano:pacifico",
                             "persona:bandera:azul", "chile:bandera:azul"],
     "conclusion": "nacionalidad:chile",
     "description": "Español + empanada + Pacífico + azul -> Chile"},
    # Perú
    {"id": 5, "conditions": ["persona:idioma:español", "peru:idioma:español",
                             "persona:comida:ceviche", "peru:comida:ceviche",
                             "persona:oceano:pacifico", "peru:oceano:pacifico"],
     "conclusion": "nacionalidad:peru",
     "description": "Español + ceviche + Pacífico -> Perú"},
    # Colombia
    {"id": 6, "conditions": ["persona:idioma:español", "colombia:idioma:español",
                             "persona:comida:arepa", "colombia:comida:arepa",
                             "persona:oceano:atlantico", "colombia:oceano:atlantico",
                             "persona:bandera:amarillo", "colombia:bandera:amarillo"],
     "conclusion": "nacionalidad:colombia",
     "description": "Español + arepa + Atlántico + amarillo -> Colombia"},
    # Ecuador
    {"id": 11, "conditions": ["persona:idioma:español", "ecuador:idioma:español",
                             "persona:comida:encebollado", "ecuador:comida:encebollado",
                             "persona:oceano:pacifico", "ecuador:oceano:pacifico",
                             "persona:bandera:amarillo", "ecuador:bandera:amarillo"],
     "conclusion": "nacionalidad:ecuador",
     "description": "Español + encebollado + Pacífico + amarillo -> Ecuador"},
    # Uruguay
    {"id": 12, "conditions": ["persona:idioma:español", "uruguay:idioma:español",
                             "persona:comida:chivito", "uruguay:comida:chivito",
                             "persona:oceano:atlantico", "uruguay:oceano:atlantico",
                             "persona:bandera:celeste", "uruguay:bandera:celeste"],
     "conclusion": "nacionalidad:uruguay",
     "description": "Español + chivito + Atlántico + celeste -> Uruguay"},
    # Paraguay
    {"id": 13, "conditions": ["persona:idioma:español", "paraguay:idioma:español",
                             "persona:comida:sopa paraguaya", "paraguay:comida:sopa paraguaya",
                             "persona:bandera:rojo", "paraguay:bandera:rojo"],
     "conclusion": "nacionalidad:paraguay",
     "description": "Español + sopa paraguaya + rojo -> Paraguay"},
    # Bolivia
    {"id": 14, "conditions": ["persona:idioma:español", "bolivia:idioma:español",
                             "persona:comida:salteña", "bolivia:comida:salteña",
                             "persona:bandera:rojo", "bolivia:bandera:rojo"],
     "conclusion": "nacionalidad:bolivia",
     "description": "Español + salteña + rojo -> Bolivia"},
    # Venezuela
    {"id": 15, "conditions": ["persona:idioma:español", "venezuela:idioma:español",
                             "persona:comida:arepa", "venezuela:comida:arepa",
                             "persona:oceano:atlantico", "venezuela:oceano:atlantico",
                             "persona:bandera:amarillo", "venezuela:bandera:amarillo",
                             "persona:bandera:azul", "venezuela:bandera:azul",
                             "persona:bandera:rojo", "venezuela:bandera:rojo"],
     "conclusion": "nacionalidad:venezuela",
     "description": "Español + arepa + Atlántico + amarillo, azul, rojo -> Venezuela"},
    # Guatemala
    {"id": 16, "conditions": ["persona:idioma:español", "guatemala:idioma:español",
                             "persona:comida:pepian", "guatemala:comida:pepian",
                             "persona:oceano:pacifico", "guatemala:oceano:pacifico",
                             "persona:bandera:azul", "guatemala:bandera:azul"],
     "conclusion": "nacionalidad:guatemala",
     "description": "Español + pepian + Pacífico + azul -> Guatemala"},
    # Honduras
    {"id": 17, "conditions": ["persona:idioma:español", "honduras:idioma:español",
                             "persona:comida:baleada", "honduras:comida:baleada",
                             "persona:oceano:pacifico", "honduras:oceano:pacifico",
                             "persona:bandera:azul", "honduras:bandera:azul"],
     "conclusion": "nacionalidad:honduras",
     "description": "Español + baleada + Pacífico + azul -> Honduras"},
    # El Salvador
    {"id": 18, "conditions": ["persona:idioma:español", "el_salvador:idioma:español",
                             "persona:comida:pupusa", "el_salvador:comida:pupusa",
                             "persona:oceano:pacifico", "el_salvador:oceano:pacifico",
                             "persona:bandera:azul", "el_salvador:bandera:azul"],
     "conclusion": "nacionalidad:el_salvador",
     "description": "Español + pupusa + Pacífico + azul -> El Salvador"},
    # Nicaragua
    {"id": 19, "conditions": ["persona:idioma:español", "nicaragua:idioma:español",
                             "persona:comida:gallo pinto", "nicaragua:comida:gallo pinto",
                             "persona:oceano:pacifico", "nicaragua:oceano:pacifico",
                             "persona:bandera:azul", "nicaragua:bandera:azul"],
     "conclusion": "nacionalidad:nicaragua",
     "description": "Español + gallo pinto + Pacífico + azul -> Nicaragua"},
    # Costa Rica
    {"id": 20, "conditions": ["persona:idioma:español", "costa_rica:idioma:español",
                             "persona:comida:gallo pinto", "costa_rica:comida:gallo pinto",
                             "persona:oceano:pacifico", "costa_rica:oceano:pacifico",
                             "persona:bandera:azul", "costa_rica:bandera:azul"],
     "conclusion": "nacionalidad:costa_rica",
     "description": "Español + gallo pinto + Pacífico + azul -> Costa Rica"},
    # Panamá
    {"id": 21, "conditions": ["persona:idioma:español", "panama:idioma:español",
                             "persona:comida:sancocho", "panama:comida:sancocho",
                             "persona:oceano:pacifico", "panama:oceano:pacifico",
                             "persona:bandera:azul", "panama:bandera:azul"],
     "conclusion": "nacionalidad:panama",
     "description": "Español + sancocho + Pacífico + azul -> Panamá"},
    # Puerto Rico
    {"id": 22, "conditions": ["persona:idioma:español", "puerto_rico:idioma:español",
                             "persona:comida:mofongo", "puerto_rico:comida:mofongo",
                             "persona:oceano:atlantico", "puerto_rico:oceano:atlantico",
                             "persona:bandera:rojo", "puerto_rico:bandera:rojo"],
     "conclusion": "nacionalidad:puerto_rico",
     "description": "Español + mofongo + Atlántico + rojo -> Puerto Rico"},
    # Cuba
    {"id": 9, "conditions": ["persona:idioma:español", "cuba:idioma:español",
                             "persona:comida:ropa vieja", "cuba:comida:ropa vieja",
                             "persona:oceano:atlantico", "cuba:oceano:atlantico"],
     "conclusion": "nacionalidad:cuba",
     "description": "Español + ropa vieja + Atlántico -> Cuba"},
    # República Dominicana
    {"id": 10, "conditions": ["persona:idioma:español", "dominicana:idioma:español",
                              "persona:comida:mangú", "dominicana:comida:mangú",
                              "persona:oceano:atlantico", "dominicana:oceano:atlantico"],
     "conclusion": "nacionalidad:dominicana",
     "description": "Español + mangú + Atlántico -> República Dominicana"},
    # Estados Unidos
    {"id": 7, "conditions": ["persona:idioma:ingles", "estados_unidos:idioma:ingles",
                             "persona:comida:hamburguesa", "estados_unidos:comida:hamburguesa",
                             "persona:oceano:pacifico", "estados_unidos:oceano:pacifico"],
     "conclusion": "nacionalidad:estados_unidos",
     "description": "Inglés + hamburguesa + Pacífico -> Estados Unidos"},
    # Canadá
    {"id": 8, "conditions": ["persona:idioma:ingles", "canada:idioma:ingles",
                             "persona:comida:jarabe de arce", "canada:comida:jarabe de arce",
                             "persona:oceano:atlantico", "canada:oceano:atlantico"],
     "conclusion": "nacionalidad:canada",
     "description": "Inglés + jarabe de arce + Atlántico -> Canadá"}
]

# -----------------------
# Motor de inferencia
# -----------------------
def forward_chaining(facts, rules):
    facts = set(facts)
    fired = []
    changed = True
    # Extraer datos del usuario
    oceanos_usuario = set([f.split(":")[2] for f in facts if f.startswith("persona:oceano:")])
    colores_usuario = set([f.split(":")[2] for f in facts if f.startswith("persona:bandera:")])
    while changed:
        changed = False
        for rule in rules:
            if rule["conclusion"] in facts:
                continue
            # Extraer datos requeridos por la regla
            oceanos_regla = set([c.split(":")[2] for c in rule["conditions"] if c.startswith("persona:oceano:")])
            colores_regla = set([c.split(":")[2] for c in rule["conditions"] if c.startswith("persona:bandera:")])
            otras_condiciones = [c for c in rule["conditions"] if not c.startswith("persona:oceano:") and not c.startswith("persona:bandera:")]
            # Coincidencia exacta de océanos y colores
            if oceanos_regla and oceanos_usuario != oceanos_regla:
                continue
            if colores_regla and colores_usuario != colores_regla:
                continue
            # Coincidencia exacta de otras condiciones
            if not all(c in facts for c in otras_condiciones):
                continue
            facts.add(rule["conclusion"])
            fired.append((rule["id"], rule["description"], rule["conclusion"]))
            print(f"[Regla {rule['id']}] {rule['description']}")
            print(f"  => Se añadió: {rule['conclusion']}\n")
            changed = True
    return facts, fired

# -----------------------
# Interacción con el usuario
# -----------------------
def pedir_datos_usuario():
    idioma = input("¿Qué idioma habla la persona? (español/portugues/ingles): ").lower().strip()
    comida = input("¿Cuál es la comida típica del país?: ").lower().strip()
    oceanos = [o.strip() for o in input("¿Con qué océano(s) limita? (atlantico/pacifico, separados por comas si son varios): ").lower().split(",")]
    colores = [c.strip() for c in input("¿Qué colores tiene su bandera? (separados por comas): ").lower().split(",")]

    hechos = set()
    hechos.add(f"persona:idioma:{idioma}")
    hechos.add(f"persona:comida:{comida}")
    for oceano in oceanos:
        hechos.add(f"persona:oceano:{oceano}")
    for c in colores:
        hechos.add(f"persona:bandera:{c}")
    return hechos

# -----------------------
# Ejecución principal
# -----------------------
if __name__ == "__main__":
    print("=== SISTEMA EXPERTO: DETERMINACIÓN DE NACIONALIDAD ===\n")
    hechos_persona = pedir_datos_usuario()

    # Unir hechos del usuario con la base de conocimiento
    hechos_totales = facts.union(hechos_persona)

    print("\n--- INFERENCIA EN PROCESO ---\n")
    final_facts, fired = forward_chaining(hechos_totales, rules)

    print("\n--- RESULTADOS ---")
    nacionalidades = [f for f in final_facts if f.startswith("nacionalidad:")]
    if nacionalidades:
        for n in nacionalidades:
            print(f"✅ Nacionalidad inferida: {n.split(':')[1].upper()}")
    else:
        print("No se pudo determinar la nacionalidad con los datos proporcionados.")
