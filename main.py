import actions 


def mostrar_menu():
    print("\n" + "="*30)
    print(" Sistema de inventario IT ")
    print("="*30)
    print("1. Registrar nuevo equipo")
    print("2. Ver inventario compelto")
    print("3. Actualizar estado de equipo")
    print("4. Salir")
    print("="*30)
def ejecutar_sistema():
    while True:
        mostrar_menu()
        try:
            opcion = int(input("Seleccione una opción: "))
        except ValueError:
            print("Por favor, ingrese un número válido.")
            continue
        if opcion == 1:
            print("\n-- Registrar nuevo equipo --")
            modelo = input("Modelo (ej. Dell Latitude): ").strip()
            serie = input("Número de serie: ").strip()
            resp_input = input("ID de responsable (dejar vacío si no aplica): 1").strip()    
            id_resp = int(resp_input) if resp_input else None
            
            actions.registrar_equipo(modelo, serie, id_responsable=id_resp)
            
        elif opcion == 2:
            print("\n-- Listado de inventario --")
            equipos = actions.listar_equipos()
            
            if not equipos:
                print("No hay equipos registrados.")
            else:
                for e in equipos: 
                    print(f"ID: {e[0]} | Modelo: {e[1]} | S/N: {e[2]} | Estado: {e[3]} | Resp: {e[4]}")
        
        elif opcion == 3:
            print("\n-- Actualizar estado de equipo --")
            # Pedimos la serie porque es un texto (VARCHAR)
            serie_equipo = input("Ingrese el NÚMERO DE SERIE: ").strip() 
            nuevo_estado = input("Nuevo estado: ").strip()
            
            # Usamos la función de actions que ya sabe manejar texto
            actions.actualizar_estado_por_serie(serie_equipo, nuevo_estado)
        elif opcion == 4:
            print("Saliendo del sistema. ¡Hasta luego!")
            break
        else:
            print("Opción no válida. Intente de nuevo.")
            

            
if __name__ == "__main__":
    ejecutar_sistema()