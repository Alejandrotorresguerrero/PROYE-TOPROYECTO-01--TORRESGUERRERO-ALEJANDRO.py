from bullet import Password

noVendidos=[]
ventas = []
ventas1 = []
searches = []
searches1 = []
productos = []
reseñas = []
reseñaPromedio = []
ventasTotales = []
idProducto = []
devoluciones=[]
reseñaFinal=[]
devolucionListas=[]
vendidos=[]
contador2=0
elementos=0
inicio=0
devolucionTotales=0
score = 0
contadorSearch = 0
contadorSearch1 = 0
contador=0
cont=0
cont1=0
cont2=0
cantNoVendidos=0
from lifestore_file import lifestore_products
from lifestore_file import lifestore_sales
from lifestore_file import lifestore_searches

usuarios = ['emtech','emtech1','Jesus','Carlos']
contraseñas = ['caso1','caso2']
registro ='si'

def login(usuario,contraseña):
    if usuario in usuarios:
      if contraseña in contraseñas[indice]:
          return 1
      else:
          print("\n\tCONTRASEÑA INCORECTA\n")
    elif(usuario not in usuarios):
      print('No existe')
      return 2
    else:
      print('No existe')
      return 2

def registrar():
  nuevoUsuario = (input('Desea agregar nuevo usuario? [Si/No]: ')).lower()
  if nuevoUsuario == 'si':
    usuarios.append(input('Usuario: '))
    contraseñas.append(input('Contraseña: '))  
  elif nuevoUsuario == 'no':
    print('')
    
while registro == 'si':
  usuario = input('Ingrese nombre de usuario: ')
  if usuario not in usuarios:
    indice = len(contraseñas)
    registrar()
    
  else:
    indice = usuarios.index(usuario)
  
  if indice > (len(contraseñas)-1):
    print('No tiene permiso de adminisrador\n')
  else:
    contraseña = Password("Contraseña: ")
    contraseña = contraseña.launch()
  
    if login(usuario,contraseña)==1:
      print('\nBIENVENIDO!! ')
      registro = 'no'
      contadorSales = 0
      z=0
      #MAYORES Y MENORES VENTAS POR PRODUCTO
      for sales in lifestore_sales:
        ventas.append(lifestore_sales[contadorSales][1])
        contadorSales+=1

      for producto in ventas:
        if z != producto:
          con = ventas.count(producto)
          ventas1.append(['Ventas:', con,'Id del Producto:', producto])#Venta, Producto  
        z=producto 

      ventas1.sort(reverse=True)

      print('\n LOS 5 PRODUCTOS MAS VENDIDOS: \n')
      for contadorTop in range (0,5):
        print('Categoria:', lifestore_products[int(ventas1[contadorTop][1])-1][1])
        #print('Id Producto:',ventas1[contadorTop][1])
        #print('Ventas:',ventas1[contadorTop][0],'\n')
        print(ventas1[contadorTop])
      ventas1.sort()  
      print('\n LOS 5 PRODUCTOS MENOS VENDIDOS: \n')
      for contadorBottom  in range (0,5):
        print('Producto:', lifestore_products[int(ventas1[contadorTop][1])-1][1])
        #print('Íd Producto:', ventas1[contadorBottom][1])
        #print('Ventas:',ventas1[contadorTop][0],'\n')
        print(ventas1[contadorBottom])
      contadorSearch = 0
      z=0
      #MAYORES Y MENORES BUSQUEDAS POR PRODUCTO
      for search in lifestore_searches:
        searches.append(lifestore_searches[contadorSearch][1])
        contadorSearch +=1

      for producto in searches:
        if z != producto:
          cont1 = searches.count(producto)
          searches1.append(['Busquedas:', cont1,'Id del Producto:', producto])#Venta, Producto  
        z=producto 

      searches1.sort(reverse=True)

      print('\n LOS 10 PRODUCTOS MAS BUSCADOS: \n')
      for contadorTop in range (0,10):
        print('Producto:', lifestore_products[int(ventas1[contadorTop][1])-1][1])
        print(searches1[contadorTop])
     
  
      searches1.sort()
      print('\n LOS 10 PRODUCTOS MENOS BUSCADOS: \n')
      for contadorBottom  in range (0,10):
        print('Producto:', lifestore_products[int(ventas1[contadorTop][1])-1][1])
        print(searches1[contadorBottom])
        
      for search in lifestore_sales:
        productos.append(lifestore_sales[contadorSearch1][1])
        reseñas.append(lifestore_sales[contadorSearch1][2])
        devoluciones.append(lifestore_sales[contadorSearch1][4])
        contadorSearch1 +=1

      for producto in productos:
        if contador != producto:
          indice = productos.count(producto)
          idProducto.append(producto)
          ventasTotales.append(indice)#Venta, Producto
  
          for contador1 in range(inicio,(indice+inicio)):
            score += reseñas[contador1]  
            devolucionTotales+=devoluciones[contador1]
          devolucionListas.append(devolucionTotales)
          reseñaPromedio.append(score)#Venta, Producto
          inicio=indice+inicio  
        contador=producto
        score=0 
        devolucionTotales=0
        listaV=ventasTotales[0]
        elementos=len(ventasTotales)

      for contador2 in range(elementos):
        listaD=devolucionListas[contador2]#refund
        valorD=listaD*0.4
        listaP=idProducto[contador2]#producto
        listaV=ventasTotales[contador2]#ventas
        valorV=listaV*0.2
        valorR=reseñaPromedio[contador2]#score
        promedioRV=valorR/listaV#promedioScorre
        valorRV=promedioRV*0.4
        promedioTotal=-valorD+valorRV+valorV
  
        listaReseña=['Score:','{:.2f}'.format(promedioTotal), 'Devoluciones:',listaD,'Id del producto', listaP]
        reseñaFinal.append(listaReseña)
  
      reseñaFinal.sort(reverse =True)

      print('\n LOS 5 PRODUCTOS CON MEJORES RESEÑAS: \n')
      for contadorTop in range (0,5):
        print('Producto:', lifestore_products[int(ventas1[contadorTop][1])-1][1])
        print(reseñaFinal[contadorTop])
      reseñaFinal.sort()
      print('\n LOS 5 PRODUCTOS CON MALAS RESEÑAS Y DEVOLUCIONES: \n')
      for contadorTop in range (0,5):
        print('Producto:', lifestore_products[int(ventas1[contadorTop][1])-1][1])
        print(reseñaFinal[contadorTop]) 
        
      for product in lifestore_products:
        vendidos.append(lifestore_products[cont2][0])
        cont2 += 1
        
      for sales in lifestore_sales:
        ventas.append(lifestore_sales[cont][1])
        cont += 1

      for producto in ventas:
        if z != producto:
          con = ventas.count(producto)
          ventas1.append((producto))#Venta, Producto  
        z=producto
        
      for element in ventas1:
        if element in vendidos:
          vendidos.remove(element)
      noVendidos.append(vendidos)
      cantNoVendidos=len(vendidos)
      print('\n PRODUCTOS SIN VENTA:',cantNoVendidos, '\n')
      for contadorTop in range (0,cantNoVendidos):
        print('Id Producto:',noVendidos[0][contadorTop], '\n','Producto ',lifestore_products[contadorTop][1],'\n')

    else:
      print('No registrado')
      registrar()
   
