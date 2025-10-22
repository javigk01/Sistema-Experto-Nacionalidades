"""
Taller 8 - Sistemas Expertos Interactivo (Python)
Tema: Nacionalidades de países del continente americano
Criterios: idioma, comida típica, océano, colores de bandera
Motor: Encadenamiento hacia adelante (forward chaining)
"""

from pprint import pprint

# -----------------------
# Base de conocimiento (hechos fijos de países)
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
    "colombia:oceano:atlantico",
    "colombia:bandera:amarillo",
    "colombia:bandera:azul",
    "colombia:bandera:rojo",

    # Venezuela
    "venezuela:idioma:español",
    "venezuela:comida:arepa",
    "venezuela:oceano:atlantico",
    "venezuela:bandera:amarillo",
    "venezuela:bandera:azul",
    "venezuela:bandera:rojo",

    # Ecuador
    "ecuador:idioma:español",
    "ecuador:comida:encebollado",
    "ecuador:oceano:pacifico",
    "ecuador:bandera:amarillo",
    "ecuador:bandera:azul",
    "ecuador:bandera:rojo",

    # Bolivia
    "bolivia:idioma:español",
    "bolivia:comida:silpancho",
    "bolivia:bandera:rojo",
    "bolivia:bandera:amarillo",
    "bolivia:bandera:verde",

    # Guatemala
    "guatemala:idioma:español",
    "guatemala:comida:pepian",
    "guatemala:bandera:celeste",
    "guatemala:bandera:blanco",

    # Honduras
    "honduras:idioma:español",
    "honduras:comida:baleada",
    "honduras:bandera:azul",
    "honduras:bandera:blanco",

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
    "dominicana:bandera:blanco",

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
    "canada:bandera:blanco"
])

# -----------------------
# Reglas (≥30)
# -----------------------
rules = [
    {"id": 1, "conditions": ["persona:idioma:español", "persona:comida:asado", "persona:oceano:atlantico",
                             "persona:bandera:celeste"], "conclusion": "nacionalidad:argentina", "description": "Idioma español, asado, Atlántico y celeste -> Argentina"},
    {"id": 2, "conditions": ["persona:idioma:portugues", "persona:comida:feijoada", "persona:oceano:atlantico"],
     "conclusion": "nacionalidad:brasil", "description": "Portugués + feijoada + Atlántico -> Brasil"},
    {"id": 3, "conditions": ["persona:idioma:español", "persona:comida:tacos", "persona:oceano:pacifico",
                             "persona:bandera:verde"], "conclusion": "nacionalidad:mexico", "description": "Español + tacos + Pacífico + verde -> México"},
    {"id": 4, "conditions": ["persona:idioma:español", "persona:comida:empanada", "persona:oceano:pacifico"],
     "conclusion": "nacionalidad:chile", "description": "Español + empanada + Pacífico -> Chile"},
    {"id": 5, "conditions": ["persona:idioma:español", "persona:comida:ceviche", "persona:oceano:pacifico"],
     "conclusion": "nacionalidad:peru", "description": "Español + ceviche + Pacífico -> Perú"},
    {"id": 6, "conditions": ["persona:idioma:español", "persona:comida:arepa", "persona:oceano:atlantico"],
     "conclusion": "nacionalidad:colombia", "description": "Español + arepa + Atlántico -> Colombia"},
    {"id": 7, "conditions": ["persona:idioma:español", "persona:comida:arepa", "persona:bandera:amarillo"],
     "conclusion": "nacionalidad:venezuela", "description": "Español + arepa + bandera amarilla -> Venezuela"},
    {"id": 8, "conditions": ["persona:idioma:español", "persona:comida:encebollado"],
     "conclusion": "nacionalidad:ecuador", "description": "Español + encebollado -> Ecuador"},
    {"id": 9, "conditions": ["persona:idioma:español", "persona:comida:silpancho"],
     "conclusion": "nacionalidad:bolivia", "description": "Español + silpancho -> Bolivia"},
    {"id": 10, "conditions": ["persona:idioma:español", "persona:comida:pepian"],
     "conclusion": "nacionalidad:guatemala", "description": "Español + pepián -> Guatemala"},
    {"id": 11, "conditions": ["persona:idioma:español", "persona:comida:baleada"],
     "conclusion": "nacionalidad:honduras", "description": "Español + baleada -> Honduras"},
    {"id": 12, "conditions": ["persona:idioma:español", "persona:comida:ropa vieja", "persona:oceano:atlantico"],
     "conclusion": "nacionalidad:cuba", "description": "Español + ropa vieja + Atlántico -> Cuba"},
    {"id": 13, "conditions": ["persona:idioma:español", "persona:comida:mangú", "persona:oceano:atlantico"],
     "conclusion": "nacionalidad:dominicana", "description": "Español + mangú + Atlántico -> República Dominicana"},
    {"id": 14, "conditions": ["persona:idioma:ingles", "persona:comida:hamburguesa"],
     "conclusion": "nacionalidad:estados_unidos", "description": "Inglés + hamburguesa -> Estados Unidos"},
    {"id": 15, "conditions": ["persona:idioma:ingles", "persona:comida:jarabe de arce"],
     "conclusion": "nacionalidad:canada", "description": "Inglés + jarabe de arce -> Canadá"},

    # Reglas adicionales para reforzar inferencias
    {"id": 16, "conditions": ["persona:bandera:celeste", "persona:bandera:blanco"],
     "conclusion": "posible:argentina", "description": "Celeste y blanco -> posible Argentina o Guatemala"},
    {"id": 17, "conditions": ["persona:bandera:verde", "persona:bandera:amarillo"],
     "conclusion": "posible:brasil", "description": "Verde y amarillo -> posible Brasil"},
    {"id": 18, "conditions": ["persona:bandera:verde", "persona:bandera:rojo"],
     "conclusion": "posible:mexico", "description": "Verde y rojo -> posible México"},
    {"id": 19, "conditions": ["persona:bandera:azul", "persona:bandera:blanco"],
     "conclusion": "posible:honduras", "description": "Azul y blanco -> posible Honduras o El Salvador"},
    {"id": 20, "conditions": ["persona:bandera:amarillo", "persona:bandera:azul", "persona:bandera:rojo"],
     "conclusion": "posible:colombia", "description": "Amarillo, azul y rojo -> posible Colombia, Venezuela o Ecuador"},
    {"id": 21, "conditions": ["persona:bandera:rojo", "persona:bandera:blanco", "persona:bandera:azul"],
     "conclusion": "posible:cuba", "description": "Rojo, blanco y azul -> posible Cuba, Chile o EE.UU."},
    {"id": 22, "conditions": ["persona:oceano:pacifico"], "conclusion": "region:pacifico", "description": "País del Pacífico"},
    {"id": 23, "conditions": ["persona:oceano:atlantico"], "conclusion": "region:atlantico", "description": "País del Atlántico"},
    {"id": 24, "conditions": ["persona:idioma:español"], "conclusion": "idioma_latino", "description": "Habla español -> país latino"},
    {"id": 25, "conditions": ["persona:idioma:ingles"], "conclusion": "idioma_ingles", "description": "Habla inglés -> país angloparlante"},
    {"id": 26, "conditions": ["idioma_ingles", "region:atlantico"], "conclusion": "posible:canada", "description": "Inglés + Atlántico -> posible Canadá"},
    {"id": 27, "conditions": ["idioma_latino", "region:atlantico"], "conclusion": "posible:colombia", "description": "Español + Atlántico -> posible Colombia o Venezuela"},
    {"id": 28, "conditions": ["idioma_latino", "region:pacifico"], "conclusion": "posible:peru", "description": "Español + Pacífico -> posible Perú, Chile o México"},
    {"id": 29, "conditions": ["persona:comida:arepa"], "conclusion": "grupo:andino", "description": "Comida arepa -> país andino"},
    {"id": 30, "conditions": ["persona:comida:asado"], "conclusion": "grupo:conosur", "description": "Asado -> país del Cono Sur"}
]

# -----------------------
# Motor de inferencia
# -----------------------
def forward_chaining(facts, rules):
    facts = set(facts)
    fired = []
    changed = True
    while changed:
        changed = False
        for rule in rules:
            if rule["conclusion"] in facts:
                continue
            if all(c in facts for c in rule["conditions"]):
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
    oceano = input("¿Con qué océano limita? (atlantico/pacifico/ninguno): ").lower().strip()
    colores = input("¿Qué colores tiene su bandera? (separados por comas): ").lower().split(",")

    hechos = set()
    hechos.add(f"persona:idioma:{idioma}")
    hechos.add(f"persona:comida:{comida}")
    hechos.add(f"persona:oceano:{oceano}")
    for c in colores:
        hechos.add(f"persona:bandera:{c.strip()}")
    return hechos

# -----------------------
# Ejecución principal
# -----------------------
if __name__ == "__main__":
    print("=== SISTEMA EXPERTO: DETERMINACIÓN DE NACIONALIDAD ===\n")
    hechos_persona = pedir_datos_usuario()

    hechos_totales = facts.union(hechos_persona)

    print("\n--- INFERENCIA EN PROCESO ---\n")
    final_facts, fired = forward_chaining(hechos_totales, rules)

    print("\n--- RESULTADOS ---")
    nacionalidades = [f for f in final_facts if f.startswith("nacionalidad:")]
    if nacionalidades:
        for n in nacionalidades:
            print(f"✅ Nacionalidad inferida: {n.split(':')[1].upper()}")
    else:
        posibles = [f for f in final_facts if f.startswith("posible:")]
        if posibles:
            print("🔎 Posibles nacionalidades:")
            for p in posibles:
                print(f" - {p.split(':')[1].capitalize()}")
        else:
            print("No se pudo determinar la nacionalidad con los datos proporcionados.")
