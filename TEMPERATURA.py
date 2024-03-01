TEMPERATURA = [
    [# MANTA
        [# SEMANA 1
            {"DIA": "LUNES", "TEMPERATURA": 30},
            {"DIA": "MARTES", "TEMPERATURA": 28},
            {"DIA": "MIERCOLES", "TEMPERATURA": 36},
            {"DIA": "JUEVES", "TEMPERATURA": 22},
            {"DIA": "VIERNES", "TEMPERATURA": 32},
            {"DIA": "SABADO", "TEMPERATURA": 31},
            {"DIA": "DOMINGO", "TEMPERATURA": 34}
        ],
        [# SEMANA 2
            {"DIA": "LUNES", "TEMPERATURA": 30},
            {"DIA": "MARTES", "TEMPERATURA": 34},
            {"DIA": "MIERCOLES", "TEMPERATURA": 34},
            {"DIA": "JUEVES", "TEMPERATURA": 37},
            {"DIA": "VIERNES", "TEMPERATURA": 34},
            {"DIA": "SABADO", "TEMPERATURA": 39},
            {"DIA": "DOMINGO", "TEMPERATURA": 33}
        ],
        [# SEMANA 3
            {"DIA": "LUNES", "TEMPERATURA": 30},
            {"DIA": "MARTES", "TEMPERATURA": 28},
            {"DIA": "MIERCOLES", "TEMPERATURA": 36},
            {"DIA": "JUEVES", "TEMPERATURA": 22},
            {"DIA": "VIERNES", "TEMPERATURA": 32},
            {"DIA": "SABADO", "TEMPERATURA": 31},
            {"DIA": "DOMINGO", "TEMPERATURA": 34}
        ],
        [# SEMANA 4
            {"DIA": "LUNES", "TEMPERATURA": 30},
            {"DIA": "MARTES", "TEMPERATURA": 34},
            {"DIA": "MIERCOLES", "TEMPERATURA": 34},
            {"DIA": "JUEVES", "TEMPERATURA": 37},
            {"DIA": "VIERNES", "TEMPERATURA": 34},
            {"DIA": "SABADO", "TEMPERATURA": 39},
            {"DIA": "DOMINGO", "TEMPERATURA": 33}
        ],
    ],
    [# PORTOVIEJO
        [# SEMANA 1
            {"DIA": "LUNES", "TEMPERATURA": 30},
            {"DIA": "MARTES", "TEMPERATURA": 28},
            {"DIA": "MIERCOLES", "TEMPERATURA": 36},
            {"DIA": "JUEVES", "TEMPERATURA": 22},
            {"DIA": "VIERNES", "TEMPERATURA": 32},
            {"DIA": "SABADO", "TEMPERATURA": 31},
            {"DIA": "DOMINGO", "TEMPERATURA": 34}
        ],
        [# SEMANA 2
            {"DIA": "LUNES", "TEMPERATURA": 30},
            {"DIA": "MARTES", "TEMPERATURA": 34},
            {"DIA": "MIERCOLES", "TEMPERATURA": 34},
            {"DIA": "JUEVES", "TEMPERATURA": 37},
            {"DIA": "VIERNES", "TEMPERATURA": 34},
            {"DIA": "SABADO", "TEMPERATURA": 39},
            {"DIA": "DOMINGO", "TEMPERATURA": 33}
        ],
        [# SEMANA 3
            {"DIA": "LUNES", "TEMPERATURA": 30},
            {"DIA": "MARTES", "TEMPERATURA": 28},
            {"DIA": "MIERCOLES", "TEMPERATURA": 36},
            {"DIA": "JUEVES", "TEMPERATURA": 22},
            {"DIA": "VIERNES", "TEMPERATURA": 32},
            {"DIA": "SABADO", "TEMPERATURA": 31},
            {"DIA": "DOMINGO", "TEMPERATURA": 34}
        ],
        [# SEMANA 4
            {"DIA": "LUNES", "TEMPERATURA": 30},
            {"DIA": "MARTES", "TEMPERATURA": 34},
            {"DIA": "MIERCOLES", "TEMPERATURA": 34},
            {"DIA": "JUEVES", "TEMPERATURA": 37},
            {"DIA": "VIERNES", "TEMPERATURA": 34},
            {"DIA": "SABADO", "TEMPERATURA": 39},
            {"DIA": "DOMINGO", "TEMPERATURA": 33}
        ],
    ],
    [# JIPIJAPA
        [# SEMANA 1
            {"DIA": "LUNES", "TEMPERATURA": 30},
            {"DIA": "MARTES", "TEMPERATURA": 28},
            {"DIA": "MIERCOLES", "TEMPERATURA": 36},
            {"DIA": "JUEVES", "TEMPERATURA": 22},
            {"DIA": "VIERNES", "TEMPERATURA": 32},
            {"DIA": "SABADO", "TEMPERATURA": 31},
            {"DIA": "DOMINGO", "TEMPERATURA": 34}
        ],
        [# SEMANA 2
            {"DIA": "LUNES", "TEMPERATURA": 30},
            {"DIA": "MARTES", "TEMPERATURA": 34},
            {"DIA": "MIERCOLES", "TEMPERATURA": 34},
            {"DIA": "JUEVES", "TEMPERATURA": 37},
            {"DIA": "VIERNES", "TEMPERATURA": 34},
            {"DIA": "SABADO", "TEMPERATURA": 39},
            {"DIA": "DOMINGO", "TEMPERATURA": 33}
        ],
        [# SEMANA 3
            {"DIA": "LUNES", "TEMPERATURA": 30},
            {"DIA": "MARTES", "TEMPERATURA": 28},
            {"DIA": "MIERCOLES", "TEMPERATURA": 36},
            {"DIA": "JUEVES", "TEMPERATURA": 22},
            {"DIA": "VIERNES", "TEMPERATURA": 32},
            {"DIA": "SABADO", "TEMPERATURA": 31},
            {"DIA": "DOMINGO", "TEMPERATURA": 34}
        ],
        [# SEMANA 4
            {"DIA": "LUNES", "TEMPERATURA": 30},
            {"DIA": "MARTES", "TEMPERATURA": 34},
            {"DIA": "MIERCOLES", "TEMPERATURA": 34},
            {"DIA": "JUEVES", "TEMPERATURA": 37},
            {"DIA": "VIERNES", "TEMPERATURA": 34},
            {"DIA": "SABADO", "TEMPERATURA": 39},
            {"DIA": "DOMINGO", "TEMPERATURA": 33}
        ],
    ],
]
suma_temperatura = float()
peomedio_semanal = float()
c = int()
x = int()
for ciudad in TEMPERATURA:
    x += 1
    if x == 1:
        print("=========================================================")
        print("PROMEDIO SEMANAL DE TEMPERATURAS DE LA CIUDAD DE MANTA")
        print("=========================================================")
    if x == 2:
        print("=========================================================")
        print("PROMEDIO SEMANAL DE TEMPERATURAS DE LA CIUDAD PORTOVIEJO")
        print("=========================================================")
    if x == 3:
        print("=========================================================")
        print("PROMEDIO SEMANAL DE TEMPERATURAS DE LA CIUDAD JIPIJAPA")
        print("=========================================================")
    for semana  in ciudad:
        c +=1
        for dia in semana:
            suma_temperatura += dia["TEMPERATURA"]
        promedio_semanal = suma_temperatura / 7
        print(f"la semana {c}, tuvo un promedio de temperatura {promedio_semanal}")
        print()
        suma_temperatura = 0
    c=0