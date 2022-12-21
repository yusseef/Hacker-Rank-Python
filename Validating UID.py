n = int(input())
COND = 0
Alphabet = 0
digits = 0
for i in range(n):
    UID = input()
    if len(UID) == 10:
        COND += 1
    
    Alphabet = sum(1 for char in UID if char.isupper())
    if Alphabet >= 2:
        COND += 1
    

    digits = sum(1 for dig in UID if dig.isdigit()) 
    if digits >= 3:
        COND += 1
   


    hasrepeated = len(set(UID)) != len(UID)

    if hasrepeated == False:
        COND += 1
   

    if UID.isalnum() == True:
        COND += 1
   

    if COND == 5:
        print("Valid")
    else:
        print("Invalid")
    COND = 0