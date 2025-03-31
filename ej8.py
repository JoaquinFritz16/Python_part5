import random
def RandomPassword(length):
    capitalalphabets="ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    smallalphabets="abcdefghijklmnñopqrstuvwxyz"
    specialchar="^$@_!#%?ª/¡¿₧+ç@½¬_§|·*-+"
    digits="0123456789"
    chars = capitalalphabets + smallalphabets + digits + specialchar
    password = ''.join(random.choice(chars) for i in range(length)) 
    print (password)
if __name__ == "__main__":
    length = int(input("Enter the length of the password: "))
    
    RandomPassword(length)