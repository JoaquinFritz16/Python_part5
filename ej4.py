def Secure(password):
    l, u, p, d = 0, 0, 0, 0
    capitalalphabets="ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    smallalphabets="abcdefghijklmnopqrstuvwxyz"
    specialchar="$@_"
    digits="0123456789"
    if (len(password)>8):
        for i in password:
            
            if(i in smallalphabets):
                l+=1
            if(i in specialchar):
                u+=1
            if(i in digits):
                p+=1
            if(i in capitalalphabets):
                d=+1
    if (l>=1 and u>=1 and p>=1 and d>=1 and l+p+u+d==len(password)):
        print("Valid Password")
    else:
        print("Invalid Password")

if __name__ == "__main__":
    password=input("Ingrese una contraseña para su seguridad: ")
    index=""
    print(Secure(password))