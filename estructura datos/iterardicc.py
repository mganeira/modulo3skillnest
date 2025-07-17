parques_nacionales = {
    "Torres del Paine": {
        "region": "Magallanes",
        "superficie": 227298,  # hectáreas
        "año_creacion": 1959,
        "caracteristicas": ["montañas", "lagos", "glaciares", "fauna"],
        "visitantes_anuales": 252000
    },
    "Conguillío": {
        "region": "Araucanía",
        "superficie": 60832,  # hectáreas
        "año_creacion": 1950,
        "caracteristicas": ["volcán Llaima", "araucarias", "lagos", "bosques"],
        "visitantes_anuales": 132000
    },
    "Pan de Azúcar": {
        "region": "Atacama",
        "superficie": 43754,  # hectáreas
        "año_creacion": 1985,
        "caracteristicas": ["desierto", "costa", "fauna marina", "cactus"],
        "visitantes_anuales": 35000
    },
    "Vicente Pérez Rosales": {
        "region": "Los Lagos",
        "superficie": 253780,  # hectáreas
        "año_creacion": 1926,
        "caracteristicas": ["volcán Osorno", "lago Todos los Santos", "saltos del Petrohué", "bosques"],
        "visitantes_anuales": 400000
    },
    "Rapa Nui": {
        "region": "Valparaíso (Isla de Pascua)",
        "superficie": 7130,  # hectáreas
        "año_creacion": 1935,
        "caracteristicas": ["moáis", "cráteres volcánicos", "cultura polinésica", "arqueología"],
        "visitantes_anuales": 120000
    },
    "Lauca": {
        "region": "Arica y Parinacota",
        "superficie": 137883,  # hectáreas
        "año_creacion": 1970,
        "caracteristicas": ["altiplano", "lagos", "fauna andina", "volcanes"],
        "visitantes_anuales": 45000
    }
}

for p in parques_nacionales:
    print(p)

for p in parques_nacionales.values():
    print(p)

for p, i in parques_nacionales.items():
    print(p,i)



#itr anidada

for nombre, info in parques_nacionales.items():
    print(f"{nombre}:")
    for caracteristica in info["caracteristicas"]:
        print(f" - {caracteristica}")