#2. Experimente con el concepto de scope:
#    1. Intente accesar a una variable definida dentro de una función desde afuera.
 #   2.  Intente accesar a una variable global desde una función y cambiar su valor.


def tell_me_a_number():
    number=int(input("Tell me a number: "))
    print(number)

print(number)  #no se puede accesar


dollar_to_colon_rate=507.46

def usd_to_crc_rate():
    global dollar_to_colon_rate
    dollar_to_colon_rate=float(input("Enter the new USD to CRC rate:"))
    print(dollar_to_colon_rate)


print(dollar_to_colon_rate)
usd_to_crc_rate()
print(dollar_to_colon_rate)# ahora si cambia su valor