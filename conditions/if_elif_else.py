# usando if, elif e else básicos 

name = input("Qual é o seu nome? \n")
age = int(input("Qual é a sua idade? \n"))  

if age >= 0 and age <= 12:
    print(f"{name}, you are a child.")
elif age >= 13 and age <= 17:
    print(f"{name}, you are a teenager.")
elif age >= 18 and age <= 25:
    print(f"{name}, you are a young adult.")
elif age >= 26 and age <= 40:
    print(f"{name}, you are an adult.")
elif age >= 41 and age <= 65:
    print(f"{name}, you are a mature adult.")
elif age > 65 and age <= 120:  
    print(f"{name}, you are a senior.")
else:
    print(f"{name}, invalid age.")


