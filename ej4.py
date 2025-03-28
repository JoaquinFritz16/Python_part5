def Secure(password):
    l, u, p, d = 0, 0, 0, 0
    capitalalphabets="ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    smallalphabets="abcdefghijklmnñopqrstuvwxyz"
    specialchar="$@_!#%?ª/¡¿₧+ç@½¬_§|·"
    digits="0123456789"
    if len(password)<8:
        return "Password should be at least 8 characters long"    
    for i in password:
        if i in smallalphabets:
            l+=1
        if i in capitalalphabets:
            u+=1
        if i in digits:
            p+=1
        if i in specialchar:
            d+=1
    errores=[]
    if l==0:
        errores.append("Password is missing at least one lowercase letters")
    if u==0:
        errores.append("Password is missing at least one uppercase letters")
    if p==0:
        errores.append("Password is missing at least one digits")
    if d==0:
        errores.append("Password is missing at least one special character")
    
    if errores:
        return "\n".join(errores)
    return "Valid Password"
if __name__ == "__main__":
    while True:
        password=input("Enter a password for your security: ")
        res= Secure(password)
        print(res)

        if res == "Valid Password":
            break
        else:
            print("Please try again")