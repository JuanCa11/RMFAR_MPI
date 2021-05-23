def get_hour_interval(hour):
    if hour < 12:
        return "MAÑANA"
    elif hour > 12 and hour < 13:
        return "MEDIO DIA"
    elif hour > 13 and hour < 18:
        return "TARDE"
    else:
        return "NOCHE"

def get_day_of_week_interval(day):
    if day > 3:
        return "FIN DE SEMANA"
    else:
        return "ENTRE SEMANA"

def get_day_of_month_interval(day):
    if (day > 13 and day <19) or (day > 27 and day <3):
        return "QUINCENA"
    else:
        return "NO QUINCENA"

def get_month_interval(month):
    if month > 10:
        return "FIN DE AÑO"
    elif month < 3:
        return "INICIO DE AÑO"
    elif month > 5 and month < 8:
        return "PRIMA DE MITAD DE AÑO"
    else:
        return "MES COMUN"

def dict_transpose(dict):
        dict_transpose = {}
        for key, value in dict.items():
            for val in value:
                dict_transpose[val] = key
        return dict_transpose
