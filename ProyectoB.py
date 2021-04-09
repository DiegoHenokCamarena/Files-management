import os
import random

#Variables necesarias para el hash:
p=101 
a=454
b=873
datos = [] #Aquí se guardarán los datos que se van a escribir en el archivo "nombre".txt

def CrearTabla(tam): #Creamos tabla Hash
    T=[]
    for i in range(tam):
        a=[] 
        T.append(a) #Lista T inicializada con arreglos
    return T

def Insertar(T,cp,col,est,mun,cd): #Se inserta a la tabla cada elemento por su código postal
    indice=UniversalHashing(cp,len(T))
    dicc={ #Los diccionarios se crearán con los datos que necesitamos escribir en el archivo "nombre".txt
        "CP": cp,
        "Colonia": col,
        "Estado": est,
        "Municipio": mun,
        "Ciudad": cd
        }
    T[indice].append(dicc)

def BusquedaPorCodigoPostal(T,cp): #Esta función hará todo el trabajo "pesado"
    indice=UniversalHashing(cp,len(T)) #Busqueda hash
    ListaInt=T[indice]  
    listaColonias = []   #Lista para guardar todas las colonias con el mismo CP
    for dic in ListaInt:  
        if dic["CP"]==cp: 
            listaColonias.append( dic["Colonia"] ) #Aqui se guardan las colonias
            #Dado que todas las colonias con el mismo CP pertenecen a la misma ciudad, municipio y estado,
            municipio = dic["Municipio"] #hice una variable para cada uno que los contenga
            estado = dic["Estado"]   
            ciudad = dic["Ciudad"]  #dichas variables se estarán sobreescribiendo cada ciclo con los mismos datos

    if(len(listaColonias) == 0): #Por si el código postal no existe pero el hashing sí direcciona a una posición en 
        print("Tu busqueda no existe") #la lista (ya me pasó)
        return False

    if(len(listaColonias)!=1): #Este es el menú por si hay más de una colonia con el mismo CP
        print("Se encontraron varias colonias. Elige la tuya")
        for i in range (len(listaColonias)):
            print("[",i,"]",listaColonias[i]) #Se enlistan de acuerdo a su índice en listaColonias

        while(True):   
            n = int(input()) #El usuario ingresa el índice 
            try: #Por si el usuario se equivoca y escribe un numero fuera del rango
                datos.append( "Colonia: "+str(listaColonias[n])+"\n" )
                datos.append( "Estado: "+str(estado)+"\n" )
                datos.append( "Municipio: "+str(municipio)+"\n" )
                datos.append( "Ciudad: "+str(ciudad)+"\n" )
                return True
            except:
                print("Ingresa correctamente el número correspondiende a tu colonia")
    else:   #Si solo hay una colonia, se guarda listaColonias[0], es decir, la única que existe 
        datos.append( "Colonia: "+str(listaColonias[0])+"\n" )
        datos.append( "Estado: "+str(estado)+"\n" )
        datos.append( "Municipio: "+str(municipio)+"\n" )
        datos.append( "Ciudad: "+str(ciudad)+"\n" )
        return True    

def UniversalHashing(key,T):
    ascii=0
    for i in range(len(key)):
        suma=ord(key[i])
        ascii=suma+ascii
    x=a*ascii+b
    y=x%p
    X=y%T
    return X

with open('C:/Users/52552/Documents/2020-2/EDA II/ProyectoB/CPdescarga.txt','r') as file: #Path
    lineas = file.readlines() 
    Tabla = CrearTabla( 45 ) #Tamaño optimo de tabla ((Explicación en el reporte))
    for i in range(1, len(lineas)):
        l = lineas[i]
        registro = l.split('|') 
        # registro[0] es el CP, registro[1] es colonia, registro[3] municipio, registro[4] estado, registro[5] ciudad     
        Insertar( Tabla, registro[0], registro[1], registro[4], registro[3], registro[5] )

x = input("Ingresa tu nombre completo")
datos.append("Nombre: "+x+"\n")
cp = input("Ingresa tu código postal")
datos.append("Código postal: "+cp+"\n")
CPCorrecto =  BusquedaPorCodigoPostal(Tabla,cp) 

if( CPCorrecto == True ): #Para evitar que se creen carpetas con CP's incorrectos

    try:
        os.makedirs(cp)
    except:
        print("") #print vacío solo para evitar la excepcion (Si ya existe una carpeta con el mismo nombre, es decir, el CP)

    with open('C:/Users/52552/Documents/2020-2/EDA II/ProyectoB/'+cp+'/'+x+'.txt','w') as file:
        file.writelines(datos)

    print("Tu direccion es:\n")
    for i in range (2,len(datos)):
        print(datos[i])