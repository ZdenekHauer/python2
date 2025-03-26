while True:
    a = int(input("Zadejte první číslo"))
    b = int(input("Zadejte druhé číslo"))
    operace = input("Zadejte operaci jako sčítaní, odečítání, násobení či dělení")
    if operace == "sčítání" :
        print ("součet", (a + b))
    elif operace == "Odečítání":
        print ("rozdíl", (a - b))
    elif operace == "násobení" :
        print ("Součin", (a * b))
    elif operace == "dělení" :
        print ("Podíl", (a / b ))
    bye = input ("Pokud nechcete program zopakovat, napište (stop)")
    if bye == "stop":
        break 


