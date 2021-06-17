def cafeteria():
    cedula= input("cedula: ")
    rol= input("rol: ")
    catalogo={}
    variable=0
    lost=False
    while not lost:
        producto=int(input("producto: "))
        nombre= input("nombre: ")
        unidades=input("unidades: ")
        precio= int(input("precio: "))
        catalogo[producto]=[nombre,unidades, precio]
        if rol=="estudiante":
            #print("50% de descuento")
            variable= 0.5
        elif rol=="profesor":
            #print("20% de decuento")
            variable= 0.2
        else:
            lost=True
        for i in range(len(catalogo)):
            x=catalogo[producto][2]
            y= x*variable
            total=x-y
            print("El", rol, "con cedula Numero", cedula, "debe pagar $",total,"por el producto",producto)
cafeteria()
