from data_productos import *
from exportar_inventario import *

class Formato_inventario:
    def __init__(self, codigo="", modelo="", cantidad="", precio_u="", costo_p=""):
        self.codigo = codigo
        self.modelo = modelo
        self.cantidad = cantidad
        self.precio_u = precio_u
        self.costo_p = costo_p
   
    def estructura_inventario(self):
        return "Código: {}\nModelo: {}\nCantidad: {}\nPrecio unitario: S/. {}\nCosto por unidad: S/. {}\n ".format(self.codigo,
                                                self.modelo,
                                                self.cantidad,
                                                self.precio_u,   # .formart() sustituye los valores...
                                                self.costo_p)    # \n permite crear un espacio a parte

inventario:Formato_inventario=[]
#permite cargar todos los datos en la lista "inventario"
def cargar_data():
    for data in inventario_general:
        inventario.append(Formato_inventario(data["codigo"],
                                            data["modelo"],
                                            data["cantidad"],
                                            data["precio_u"],
                                            data["costo_p"]))

def registrar_producto():
    codigo:str= input("Código: ")
    modelo:str= input("Modelo: ")
    cantidad:float= input("Cantidad: ")
    precio_u:float= input("Precio unitario: S/.")
    costo_p:float= input("Costo al Público: S/.")
    formato:Formato_inventario = Formato_inventario(codigo,modelo,cantidad,precio_u,costo_p)
    inventario.append(formato)
    return True

def ver_inventario():
    for formato in inventario:
        print(formato.estructura_inventario())

def menu_inicio():
    print("===========MENÚ============")
    print(" 1: Nueva venta")
    print(" 2: Inventario")
    print(" 3: Balance")
    print(" exit")
    print("---------------------------")
    return True


def opcion_inventario():
    programa:bool=True
    while programa:
        print(" 1: Ver el inventario ")
        print(" 2: Registrar un nuevo producto ")
        print(" 3: Menú anterior ")
        opciones:str=str(input("Ingrese una opción: "))
        match opciones:
                case "1":
                    print("----------------------------------------------------------------------------------------------------------------------------")
                    ver_inventario()
                    exportar_inventario()
                    print("----------------------------------------------------------------------------------------------------------------------------")
                case "2":
                    registrar_producto()
                case "3":
                    main()

def main():
    programa:bool=True
    while programa:
        menu_inicio()
        opciones_inicio:str=str(input("Ingrese una opción: "))
        match opciones_inicio:
            case "1":
                opcion_venta()
            case "2":
                opcion_inventario()
            case "3":
                opcion_balance()
            case "exit":
                print(" CIERRE DEL DÍA ")
                programa= False
            case __:
                print("¡¡ Opción Inválida !!")

if __name__=='__main__':
    cargar_data()
    main()

