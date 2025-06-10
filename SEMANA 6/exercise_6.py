#6. Cree una función que acepte un string con palabras separadas por un guión y retorne un string igual pero ordenado alfabéticamente.
#   1. Hay que convertirlo a lista, ordenarlo, y convertirlo nuevamente a string.
#   2. “python-variable-funcion-computadora-monitor” → “computadora-funcion-monitor-python-variable”


def ordered_text(text_to_analyze):
    string_as_list=list(text_to_analyze.split("-"))
    string_as_list.sort()
    new_string="-".join(string_as_list)
    print(string_as_list)

ordered_text("python-variable-funcion-computadora-monitor")