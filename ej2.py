
def ConverserFahrenheit(grades_c):
    aux=9/5
    grades_f=grades_c*aux + 32

    return grades_f
if __name__ =="__main__":
    grades_c=float(input("Ingrese la temparuta Celsius: "))
    grades_f=ConverserFahrenheit(grades_c)
    
    print(f"La temperatura ingresada de {grades_c} fue convertida existosamente a Fahrenheit: {grades_f}")