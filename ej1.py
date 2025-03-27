def CalcImc(w,h):
    imc=w/h**2
    if imc<=18.5:
        talla="S"
    elif imc>18.5 and imc<= 24.5:
        talla="M"
    elif imc>25 and imc<=29.9:
        talla="L"
    elif imc>30:
        talla="XL"
    return imc, talla
if __name__ == "__main__":
    w=float(input("Ingresar peso en kg: "))
    h=float(input("Ingresar altura en metros: "))
    imc, talla=CalcImc(w,h)
    print(f"Segun tu imc de {imc} tu talla es de: {talla}")