import actions 


def show_menu():
    print("\n" + "="*40)
    print("      IT Inventory Management System      ")
    print("="*40)
    print("1. Register new equipment")
    print("2. View full inventory")
    print("3. Update equipment status (by serial number)")
    print("4. Register new responsible person")
    print("5. View list of responsible persons")
    print("6. Exit")
    print("="*40)
    
def run_system():
    while True:
        show_menu()
        try:
            option = int(input("Select an option: "))
        except ValueError:
            print("Please enter a valid number.")
            continue
        if option == 1:
            print("\n-- Registrar nuevo equipo --")
            modelo = input("Modelo: ").strip()
            serie = input("Número de serie: ").strip()
            # Sugerencia: Primero ver la lista de responsables (Opción 5) para saber el ID
            resp_input = input("ID de responsable (Enter si no tiene): ").strip()    
            id_resp = int(resp_input) if resp_input else None
            actions.registrar_equipo(modelo, serie, id_responsable=id_resp)

        elif option == 2:
            print("\n-- Listado de inventario --")
            equipos = actions.listar_equipos()
            if not equipos:
                print("No hay equipos registrados.")
            else:
                for e in equipos: 
                    print(f"ID: {e[0]} | Modelo: {e[1]} | S/N: {e[2]} | Estado: {e[3]} | Resp ID: {e[4]}")

        elif option == 3:
            print("\n-- Actualizar estado de equipo --")
            serie = input("Ingrese el NÚMERO DE SERIE: ").strip()
            nuevo_estado = input("Nuevo estado: ").strip()
            actions.actualizar_estado_por_serie(serie, nuevo_estado)

        elif option == 4:
            print("\n-- Registrar nuevo responsable --")
            id_emp = input("employee ID: ").strip()
            emp_name = input("Full name: ").strip()
            departamento = input("Department: ").strip()
            email = input("Email (optional): ").strip()
            actions.registrar_responsable(id_emp, emp_name, departamento, email)

        elif option == 5:
            print("\n-- Lista de responsables --")
            resps = actions.listar_responsables()
            if not resps:
                print("Theres no registered responsible persons.")
            else:
                for r in resps:
                    print(f"ID: {r[0]} | Nombre: {r[1]} | Área: {r[2]}")

        elif option == 6:
            print("Getting out... Goodbye!")
            break

            
if __name__ == "__main__":
    run_system()