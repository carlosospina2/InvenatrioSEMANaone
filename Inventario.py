name =  input("nombre del producto: ") #
while name.isnumeric():
    print("tiene que ser un texto!")
    name =  input("nombre del producto: ") 



validacion = True

while validacion:
        try:
           price = float (input("precio del producto: "))
           if price <0:
               raise ValueError
           print("Entrada correcta")
           validacion= False
        except ValueError:
          print("No es un número válido")
        


amount = int (input("cantidad de productos: "))
while validacion:
        try:
           amount = float (input("cantidad del producto: "))
           if amount <0:
               raise ValueError
           print("Entrada correcta")
           validacion= False
        except ValueError:
          print("No es un número válido")
if amount < 0 :
    print("valor inavalido! ")


