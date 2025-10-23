"""
Taller 8 - Sistema Experto Interactivo (Python)
Tema: Nacionalidades de países del continente americano
Motor: Encadenamiento hacia adelante SIMBÓLICO
"""

# -----------------------
# Base de conocimiento: Reglas
# -----------------------
reglas = [
    # Reglas básicas de características - Idioma
    {"condiciones": [("idioma", "==", "español")], "conclusion": "habla_español"},
    {"condiciones": [("idioma", "==", "portugues")], "conclusion": "habla_portugues"},
    {"condiciones": [("idioma", "==", "ingles")], "conclusion": "habla_ingles"},
    {"condiciones": [("idioma", "==", "frances")], "conclusion": "habla_frances"},
    {"condiciones": [("idioma", "==", "italiano")], "conclusion": "habla_italiano"},
    {"condiciones": [("idioma", "==", "aleman")], "conclusion": "habla_aleman"},
    {"condiciones": [("idioma", "==", "chino")], "conclusion": "habla_chino"},
    {"condiciones": [("idioma", "==", "japones")], "conclusion": "habla_japones"},
    {"condiciones": [("idioma", "==", "arabe")], "conclusion": "habla_arabe"},
    {"condiciones": [("idioma", "==", "ruso")], "conclusion": "habla_ruso"},
    {"condiciones": [("idioma", "==", "hindi")], "conclusion": "habla_hindi"},
    {"condiciones": [("idioma", "==", "turco")], "conclusion": "habla_turco"},
    {"condiciones": [("idioma", "==", "griego")], "conclusion": "habla_griego"},
    {"condiciones": [("idioma", "==", "noruego")], "conclusion": "habla_noruego"},
    {"condiciones": [("idioma", "==", "sueco")], "conclusion": "habla_sueco"},
    {"condiciones": [("idioma", "==", "fines")], "conclusion": "habla_fines"},
    {"condiciones": [("idioma", "==", "coreano")], "conclusion": "habla_coreano"},
    
    # Reglas de comida
    {"condiciones": [("comida", "==", "arepa")], "conclusion": "pais_arepa"},
    {"condiciones": [("comida", "==", "asado")], "conclusion": "pais_asado"},
    {"condiciones": [("comida", "==", "feijoada")], "conclusion": "pais_feijoada"},
    {"condiciones": [("comida", "==", "tacos")], "conclusion": "pais_tacos"},
    {"condiciones": [("comida", "==", "empanada")], "conclusion": "pais_empanada"},
    {"condiciones": [("comida", "==", "ceviche")], "conclusion": "pais_ceviche"},
    {"condiciones": [("comida", "==", "paella")], "conclusion": "pais_paella"},
    {"condiciones": [("comida", "==", "pizza")], "conclusion": "pais_pizza"},
    {"condiciones": [("comida", "==", "sushi")], "conclusion": "pais_sushi"},
    {"condiciones": [("comida", "==", "hamburguesa")], "conclusion": "pais_hamburguesa"},
    
    # Reglas de continente
    {"condiciones": [("continente", "==", "america")], "conclusion": "continente_america"},
    {"condiciones": [("continente", "==", "europa")], "conclusion": "continente_europa"},
    {"condiciones": [("continente", "==", "asia")], "conclusion": "continente_asia"},
    {"condiciones": [("continente", "==", "africa")], "conclusion": "continente_africa"},
    {"condiciones": [("continente", "==", "oceania")], "conclusion": "continente_oceania"},
    
    # Reglas de moneda
    {"condiciones": [("moneda", "==", "peso")], "conclusion": "moneda_peso"},
    {"condiciones": [("moneda", "==", "dolar")], "conclusion": "moneda_dolar"},
    {"condiciones": [("moneda", "==", "euro")], "conclusion": "moneda_euro"},
    {"condiciones": [("moneda", "==", "real")], "conclusion": "moneda_real"},
    {"condiciones": [("moneda", "==", "yuan")], "conclusion": "moneda_yuan"},
    {"condiciones": [("moneda", "==", "yen")], "conclusion": "moneda_yen"},
    
    # Reglas de clima
    {"condiciones": [("clima", "==", "tropical")], "conclusion": "clima_tropical"},
    {"condiciones": [("clima", "==", "templado")], "conclusion": "clima_templado"},
    {"condiciones": [("clima", "==", "frio")], "conclusion": "clima_frio"},
    {"condiciones": [("clima", "==", "desertico")], "conclusion": "clima_desertico"},
    {"condiciones": [("clima", "==", "mediterraneo")], "conclusion": "clima_mediterraneo"},
    
    # Reglas de religión
    {"condiciones": [("religion", "==", "catolica")], "conclusion": "religion_catolica"},
    {"condiciones": [("religion", "==", "protestante")], "conclusion": "religion_protestante"},
    {"condiciones": [("religion", "==", "musulmana")], "conclusion": "religion_musulmana"},
    {"condiciones": [("religion", "==", "hindu")], "conclusion": "religion_hindu"},
    {"condiciones": [("religion", "==", "budista")], "conclusion": "religion_budista"},
    
    # Reglas de hemisferio
    {"condiciones": [("hemisferio", "==", "norte")], "conclusion": "hemisferio_norte"},
    {"condiciones": [("hemisferio", "==", "sur")], "conclusion": "hemisferio_sur"},
    
    # Reglas de deporte
    {"condiciones": [("deporte", "==", "futbol")], "conclusion": "deporte_futbol"},
    {"condiciones": [("deporte", "==", "beisbol")], "conclusion": "deporte_beisbol"},
    {"condiciones": [("deporte", "==", "hockey")], "conclusion": "deporte_hockey"},
    
    # Reglas de geografía
    {"condiciones": [("montañas", "==", "si")], "conclusion": "tiene_montañas"},
    {"condiciones": [("selva", "==", "si")], "conclusion": "tiene_selva"},
    {"condiciones": [("desierto", "==", "si")], "conclusion": "tiene_desierto"},
    {"condiciones": [("es_isla", "==", "si")], "conclusion": "es_pais_insular"},
    
    # Reglas de océanos
    {"condiciones": [("oceanos", "in", "pacifico"), ("oceanos", "in", "atlantico")], "conclusion": "pais_bicostal"},
    {"condiciones": [("oceanos", "in", "pacifico")], "conclusion": "costa_pacifico"},
    {"condiciones": [("oceanos", "in", "atlantico")], "conclusion": "costa_atlantico"},
    {"condiciones": [("oceanos", "in", "indico")], "conclusion": "costa_indico"},
    {"condiciones": [("oceanos", "in", "artico")], "conclusion": "costa_artico"},
    {"condiciones": [("oceanos", "==", [])], "conclusion": "sin_costa_oceanica"},
    
    # Reglas de mares
    {"condiciones": [("mares", "in", "mar caribe")], "conclusion": "pais_caribeno"},
    {"condiciones": [("mares", "in", "mar mediterraneo")], "conclusion": "pais_mediterraneo"},
    {"condiciones": [("mares", "in", "mar baltico")], "conclusion": "pais_baltico"},
    {"condiciones": [("mares", "in", "mar negro")], "conclusion": "pais_mar_negro"},
    {"condiciones": [("mares", "in", "mar rojo")], "conclusion": "pais_mar_rojo"},
    {"condiciones": [("mares", "in", "mar de china meridional")], "conclusion": "pais_mar_china"},
    {"condiciones": [("mares", "in", "mar de japon")], "conclusion": "pais_mar_japon"},
    
    # Reglas de banderas
    {"condiciones": [("bandera", "in", "amarillo"), ("bandera", "in", "azul"), ("bandera", "in", "rojo")], "conclusion": "bandera_tricolor_latina"},
    {"condiciones": [("bandera", "in", "verde"), ("bandera", "in", "blanco"), ("bandera", "in", "rojo")], "conclusion": "bandera_tricolor_italiana"},
    {"condiciones": [("bandera", "in", "rojo"), ("bandera", "in", "blanco"), ("bandera", "in", "azul")], "conclusion": "bandera_rojo_blanco_azul"},
    {"condiciones": [("bandera", "in", "celeste"), ("bandera", "in", "blanco")], "conclusion": "bandera_celeste_blanco"},
    {"condiciones": [("bandera", "in", "rojo"), ("bandera", "in", "blanco")], "conclusion": "bandera_rojo_blanco"},
    {"condiciones": [("bandera", "in", "verde"), ("bandera", "in", "amarillo")], "conclusion": "bandera_verde_amarillo"},
    
    # Reglas de clasificación regional (nivel 1 - dependen de hechos básicos)
    {"condiciones": ["habla_español", "continente_america"], "conclusion": "region_hispanoamerica"},
    {"condiciones": ["habla_portugues", "continente_america"], "conclusion": "region_latinoamerica_portuguesa"},
    {"condiciones": ["habla_ingles", "continente_america"], "conclusion": "region_america_anglofona"},
    {"condiciones": ["continente_europa", "moneda_euro"], "conclusion": "region_union_europea"},
    {"condiciones": ["continente_asia", "costa_pacifico"], "conclusion": "region_asia_pacifico"},
    
    # Reglas de clasificación cultural (nivel 2 - dependen de nivel 1)
    {"condiciones": ["region_hispanoamerica", "pais_caribeno"], "conclusion": "cultura_caribe_hispano"},
    {"condiciones": ["region_hispanoamerica", "hemisferio_sur"], "conclusion": "cultura_cono_sur"},
    {"condiciones": ["region_hispanoamerica", "clima_tropical"], "conclusion": "cultura_tropical_hispana"},
    {"condiciones": ["region_union_europea", "pais_mediterraneo"], "conclusion": "cultura_mediterranea_europea"},
    
    # Reglas de identificación geográfica (nivel 2)
    {"condiciones": ["pais_bicostal", "continente_america"], "conclusion": "geografia_bicostal_americana"},
    {"condiciones": ["costa_pacifico", "hemisferio_sur", "tiene_montañas"], "conclusion": "geografia_andina_pacifico"},
    {"condiciones": ["costa_atlantico", "hemisferio_sur", "region_hispanoamerica"], "conclusion": "geografia_atlantico_sur_hispano"},
    {"condiciones": ["costa_pacifico", "continente_asia", "es_pais_insular"], "conclusion": "geografia_insular_pacifico_asiatico"},
    
    # Reglas de características culturales combinadas (nivel 3)
    {"condiciones": ["pais_arepa", "cultura_caribe_hispano"], "conclusion": "caracteristica_caribe_arepa"},
    {"condiciones": ["pais_arepa", "cultura_tropical_hispana"], "conclusion": "caracteristica_tropical_arepa"},
    {"condiciones": ["pais_asado", "cultura_cono_sur"], "conclusion": "caracteristica_cono_sur_asado"},
    {"condiciones": ["pais_empanada", "geografia_andina_pacifico"], "conclusion": "caracteristica_andina_empanada"},
    {"condiciones": ["pais_ceviche", "geografia_andina_pacifico"], "conclusion": "caracteristica_andina_ceviche"},
    
    # Reglas de productos y economía
    {"condiciones": [("producto", "==", "cafe")], "conclusion": "economia_cafetera"},
    {"condiciones": [("producto", "==", "petroleo")], "conclusion": "economia_petrolera"},
    {"condiciones": [("producto", "==", "vino")], "conclusion": "economia_vitivinicola"},
    {"condiciones": [("producto", "==", "cobre")], "conclusion": "economia_minera_cobre"},
    
    # Reglas de tradiciones
    {"condiciones": [("tradicion", "==", "carnaval")], "conclusion": "tradicion_carnaval"},
    {"condiciones": [("tradicion", "==", "tango")], "conclusion": "tradicion_tango"},
    {"condiciones": [("tradicion", "==", "samba")], "conclusion": "tradicion_samba"},
    
    # Reglas de población y desarrollo
    {"condiciones": [("poblacion", "==", "grande")], "conclusion": "pais_poblado"},
    {"condiciones": [("poblacion", "==", "pequeña")], "conclusion": "pais_poco_poblado"},
    
    # Reglas de gobierno
    {"condiciones": [("gobierno", "==", "republica")], "conclusion": "gobierno_republicano"},
    {"condiciones": [("gobierno", "==", "monarquia")], "conclusion": "gobierno_monarquico"},
    
    # Reglas compuestas para identificación final (nivel 4 - Colombia)
    {"condiciones": ["caracteristica_tropical_arepa", "geografia_bicostal_americana", "pais_caribeno", "bandera_tricolor_latina", "economia_cafetera", "tradicion_carnaval"], "conclusion": "colombia"},
    {"condiciones": ["caracteristica_caribe_arepa", "pais_bicostal", "bandera_tricolor_latina", "clima_tropical"], "conclusion": "colombia"},
    
    # Venezuela
    {"condiciones": ["caracteristica_caribe_arepa", "costa_atlantico", "bandera_tricolor_latina", "economia_petrolera"], "conclusion": "venezuela"},
    {"condiciones": ["region_hispanoamerica", "pais_arepa", "pais_caribeno", "bandera_tricolor_latina", "moneda_peso"], "conclusion": "venezuela"},
    
    # Argentina
    {"condiciones": ["caracteristica_cono_sur_asado", "geografia_atlantico_sur_hispano", "bandera_celeste_blanco", "tradicion_tango"], "conclusion": "argentina"},
    {"condiciones": ["cultura_cono_sur", "pais_asado", "bandera_celeste_blanco", "economia_vitivinicola"], "conclusion": "argentina"},
    
    # Brasil
    {"condiciones": ["region_latinoamerica_portuguesa", "pais_feijoada", "costa_atlantico", "bandera_verde_amarillo", "tradicion_samba"], "conclusion": "brasil"},
    {"condiciones": ["habla_portugues", "continente_america", "moneda_real", "pais_poblado"], "conclusion": "brasil"},
    
    # México
    {"condiciones": ["region_hispanoamerica", "pais_tacos", "geografia_bicostal_americana", "hemisferio_norte", "bandera_tricolor_italiana"], "conclusion": "mexico"},
    {"condiciones": ["cultura_caribe_hispano", "pais_tacos", "pais_bicostal", "hemisferio_norte"], "conclusion": "mexico"},
    
    # Chile
    {"condiciones": ["caracteristica_andina_empanada", "bandera_rojo_blanco_azul", "economia_minera_cobre"], "conclusion": "chile"},
    {"condiciones": ["geografia_andina_pacifico", "cultura_cono_sur", "bandera_rojo_blanco_azul"], "conclusion": "chile"},
    
    # Perú
    {"condiciones": ["caracteristica_andina_ceviche", "bandera_rojo_blanco", "region_hispanoamerica"], "conclusion": "peru"},
    {"condiciones": ["geografia_andina_pacifico", "pais_ceviche", "bandera_rojo_blanco"], "conclusion": "peru"},
    
    # España
    {"condiciones": ["cultura_mediterranea_europea", "pais_paella", "habla_español"], "conclusion": "españa"},
    {"condiciones": ["region_union_europea", "habla_español", "pais_mediterraneo", "costa_atlantico"], "conclusion": "españa"},
    
    # Italia
    {"condiciones": ["cultura_mediterranea_europea", "pais_pizza", "bandera_tricolor_italiana"], "conclusion": "italia"},
    {"condiciones": ["region_union_europea", "habla_italiano", "pais_mediterraneo"], "conclusion": "italia"},
    
    # Japón
    {"condiciones": ["geografia_insular_pacifico_asiatico", "pais_sushi", "moneda_yen"], "conclusion": "japon"},
    {"condiciones": ["region_asia_pacifico", "habla_japones", "es_pais_insular", "pais_mar_japon"], "conclusion": "japon"},
    
    # Estados Unidos
    {"condiciones": ["region_america_anglofona", "pais_hamburguesa", "geografia_bicostal_americana", "moneda_dolar"], "conclusion": "estados_unidos"},
    {"condiciones": ["habla_ingles", "pais_bicostal", "continente_america", "hemisferio_norte", "pais_poblado"], "conclusion": "estados_unidos"},
]

# -----------------------
# Motor de inferencia (Encadenamiento hacia adelante)
# -----------------------
def motor_inferencia(hechos_iniciales):
    """
    Motor de inferencia con encadenamiento hacia adelante.
    hechos_iniciales: diccionario con los datos del usuario
    """
    # Conjunto de hechos conocidos (empezamos con hechos derivados de los datos del usuario)
    hechos = set()
    
    # Convertir hechos iniciales en formato simbólico
    print("\n📋 Hechos iniciales:")
    
    # 1. Idioma
    if hechos_iniciales.get("idioma"):
        print(f" - idioma == '{hechos_iniciales['idioma']}'")
    
    # 2. Comida
    if hechos_iniciales.get("comida"):
        print(f" - comida == '{hechos_iniciales['comida']}'")
    
    # 3. Continente
    if hechos_iniciales.get("continente"):
        print(f" - continente == '{hechos_iniciales['continente']}'")
    
    # 4. Océanos
    for oceano in hechos_iniciales.get("oceanos", []):
        print(f" - '{oceano}' in oceanos")
    
    # 5. Mares
    for mar in hechos_iniciales.get("mares", []):
        print(f" - '{mar}' in mares")
    
    # 6. Bandera
    for color in hechos_iniciales.get("bandera", []):
        print(f" - '{color}' in bandera")
    
    # 7. Moneda
    if hechos_iniciales.get("moneda"):
        print(f" - moneda == '{hechos_iniciales['moneda']}'")
    
    # 8. Clima
    if hechos_iniciales.get("clima"):
        print(f" - clima == '{hechos_iniciales['clima']}'")
    
    # 9. Religión
    if hechos_iniciales.get("religion"):
        print(f" - religion == '{hechos_iniciales['religion']}'")
    
    # 10. Hemisferio
    if hechos_iniciales.get("hemisferio"):
        print(f" - hemisferio == '{hechos_iniciales['hemisferio']}'")
    
    # 11. Gobierno
    if hechos_iniciales.get("gobierno"):
        print(f" - gobierno == '{hechos_iniciales['gobierno']}'")
    
    # 12. Capital
    if hechos_iniciales.get("capital"):
        print(f" - capital == '{hechos_iniciales['capital']}'")
    
    # 13. Deporte
    if hechos_iniciales.get("deporte"):
        print(f" - deporte == '{hechos_iniciales['deporte']}'")
    
    # 14. Producto
    if hechos_iniciales.get("producto"):
        print(f" - producto == '{hechos_iniciales['producto']}'")
    
    # 15. Montañas
    if hechos_iniciales.get("montañas"):
        print(f" - montañas == '{hechos_iniciales['montañas']}'")
    
    # 16. Selva
    if hechos_iniciales.get("selva"):
        print(f" - selva == '{hechos_iniciales['selva']}'")
    
    # 17. Desierto
    if hechos_iniciales.get("desierto"):
        print(f" - desierto == '{hechos_iniciales['desierto']}'")
    
    # 18. Es isla
    if hechos_iniciales.get("es_isla"):
        print(f" - es_isla == '{hechos_iniciales['es_isla']}'")
    
    # 19. Población
    if hechos_iniciales.get("poblacion"):
        print(f" - poblacion == '{hechos_iniciales['poblacion']}'")
    
    # 20. Tradición
    if hechos_iniciales.get("tradicion"):
        print(f" - tradicion == '{hechos_iniciales['tradicion']}'")
    
    print()
    
    # Aplicar reglas iterativamente
    cambios = True
    while cambios:
        cambios = False
        for regla in reglas:
            # Si la conclusión ya está en los hechos, saltar
            if regla["conclusion"] in hechos:
                continue
            
            # Verificar si todas las condiciones se cumplen
            todas_cumplen = True
            for condicion in regla["condiciones"]:
                if isinstance(condicion, str):
                    # Es un hecho derivado (debe estar en hechos)
                    if condicion not in hechos:
                        todas_cumplen = False
                        break
                else:
                    # Es una condición sobre datos del usuario
                    campo, operador, valor = condicion
                    
                    if operador == "==":
                        if isinstance(valor, list):
                            # Comparar si no tiene océanos/mares
                            if hechos_iniciales.get(campo, None) != valor:
                                todas_cumplen = False
                                break
                        else:
                            if hechos_iniciales.get(campo) != valor:
                                todas_cumplen = False
                                break
                    elif operador == "in":
                        if valor not in hechos_iniciales.get(campo, []):
                            todas_cumplen = False
                            break
            
            # Si todas las condiciones se cumplen, agregar la conclusión
            if todas_cumplen:
                hechos.add(regla["conclusion"])
                print(f"✅ Regla activada: SI {' and '.join([str(c) if isinstance(c, str) else f'{c[0]} {c[1]} {c[2]}' for c in regla['condiciones']])} → ENTONCES {regla['conclusion']}")
                cambios = True
    
    return hechos

# -----------------------
# Función para leer datos desde archivo
# -----------------------
def leer_datos_desde_archivo(nombre_archivo="datos_entrada.txt"):
    """
    Lee los datos desde un archivo de texto.
    Formato esperado: clave = valor
    Para listas: clave = valor1, valor2, valor3
    """
    print("=== SISTEMA EXPERTO: DETERMINACIÓN DE NACIONALIDAD ===")
    print("(Motor de encadenamiento hacia adelante simbólico)\n")
    print(f"📂 Leyendo datos desde: {nombre_archivo}\n")
    
    datos = {
        "idioma": "",
        "comida": "",
        "continente": "",
        "oceanos": [],
        "mares": [],
        "bandera": [],
        "moneda": "",
        "clima": "",
        "religion": "",
        "hemisferio": "",
        "gobierno": "",
        "capital": "",
        "deporte": "",
        "producto": "",
        "montañas": "",
        "selva": "",
        "desierto": "",
        "es_isla": "",
        "poblacion": "",
        "tradicion": ""
    }
    
    try:
        with open(nombre_archivo, 'r', encoding='utf-8') as archivo:
            for linea in archivo:
                # Ignorar comentarios y líneas vacías
                linea = linea.strip()
                if not linea or linea.startswith('#'):
                    continue
                
                # Separar clave y valor
                if '=' in linea:
                    clave, valor = linea.split('=', 1)
                    clave = clave.strip()
                    valor = valor.strip().lower()
                    
                    # Procesar según el tipo de dato
                    if clave in ["oceanos", "mares", "bandera"]:
                        # Son listas
                        if valor == "ninguno" or valor == "":
                            datos[clave] = []
                        else:
                            datos[clave] = [v.strip() for v in valor.split(",")]
                    else:
                        # Son valores simples
                        datos[clave] = valor
        
        print("✅ Datos cargados correctamente desde el archivo.\n")
        return datos
    
    except FileNotFoundError:
        print(f"❌ Error: No se encontró el archivo '{nombre_archivo}'")
        print("💡 Crea un archivo 'datos_entrada.txt' con el formato adecuado.")
        return None
    except Exception as e:
        print(f"❌ Error al leer el archivo: {e}")
        return None

# -----------------------
# Ejecución principal
# -----------------------
if __name__ == "__main__":
    # Leer datos desde archivo
    usuario = leer_datos_desde_archivo("datos_entrada.txt")
    
    if usuario is None:
        print("⚠️  No se pudieron cargar los datos. Terminando programa.")
        exit(1)
    
    # Ejecutar motor de inferencia
    hechos_inferidos = motor_inferencia(usuario)
    
    # Buscar países inferidos (filtrar todos los hechos intermedios)
    hechos_no_paises = {
        # Idiomas
        "habla_español", "habla_portugues", "habla_ingles", "habla_frances", "habla_italiano",
        "habla_aleman", "habla_chino", "habla_japones", "habla_arabe", "habla_ruso",
        "habla_hindi", "habla_turco", "habla_griego", "habla_noruego", "habla_sueco",
        "habla_fines", "habla_coreano",
        # Comidas
        "pais_arepa", "pais_asado", "pais_feijoada", "pais_tacos", "pais_empanada",
        "pais_ceviche", "pais_paella", "pais_pizza", "pais_sushi", "pais_hamburguesa",
        # Geografía
        "pais_bicostal", "costa_pacifico", "costa_atlantico", "costa_indico", "costa_artico",
        "sin_costa_oceanica", "pais_caribeno", "pais_mediterraneo", "pais_baltico",
        "pais_mar_negro", "pais_mar_rojo", "pais_mar_china", "pais_mar_japon",
        "tiene_montañas", "tiene_selva", "tiene_desierto", "es_pais_insular",
        # Banderas
        "bandera_tricolor_latina", "bandera_tricolor_italiana", "bandera_rojo_blanco_azul",
        "bandera_celeste_blanco", "bandera_rojo_blanco", "bandera_verde_amarillo",
        # Continentes y regiones
        "continente_america", "continente_europa", "continente_asia", "continente_africa",
        "continente_oceania",
        # Regiones culturales (nivel 1)
        "region_hispanoamerica", "region_latinoamerica_portuguesa", "region_america_anglofona",
        "region_union_europea", "region_asia_pacifico",
        # Culturas (nivel 2)
        "cultura_caribe_hispano", "cultura_cono_sur", "cultura_tropical_hispana",
        "cultura_mediterranea_europea",
        # Geografía regional (nivel 2)
        "geografia_bicostal_americana", "geografia_andina_pacifico",
        "geografia_atlantico_sur_hispano", "geografia_insular_pacifico_asiatico",
        # Características combinadas (nivel 3)
        "caracteristica_caribe_arepa", "caracteristica_tropical_arepa",
        "caracteristica_cono_sur_asado", "caracteristica_andina_empanada",
        "caracteristica_andina_ceviche",
        # Monedas
        "moneda_peso", "moneda_dolar", "moneda_euro", "moneda_real", "moneda_yuan", "moneda_yen",
        # Clima
        "clima_tropical", "clima_templado", "clima_frio", "clima_desertico", "clima_mediterraneo",
        # Religión
        "religion_catolica", "religion_protestante", "religion_musulmana", "religion_hindu", "religion_budista",
        # Hemisferios
        "hemisferio_norte", "hemisferio_sur",
        # Deportes
        "deporte_futbol", "deporte_beisbol", "deporte_hockey",
        # Economía
        "economia_cafetera", "economia_petrolera", "economia_vitivinicola", "economia_minera_cobre",
        # Tradiciones
        "tradicion_carnaval", "tradicion_tango", "tradicion_samba",
        # Población
        "pais_poblado", "pais_poco_poblado",
        # Gobierno
        "gobierno_republicano", "gobierno_monarquico"
    }
    
    paises_encontrados = [h for h in hechos_inferidos if h not in hechos_no_paises]
    
    print("\n--- CONCLUSIÓN ---")
    if paises_encontrados:
        for pais in paises_encontrados:
            print(f"🌎 Nacionalidad inferida: {pais.upper()}")
    else:
        print("❌ No se pudo inferir la nacionalidad con los datos proporcionados.")
        print("💡 Hechos derivados:", hechos_inferidos)
