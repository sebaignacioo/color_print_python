from colorMessage import PrintService as PS

def main():
    ps = PS()
    ps.mensajeError("Mensaje de prueba (error).", inicio = "    ")
    ps.mensaje("Este es un mensaje normal", inicio = "  ")
    ps.mensajeExito("Mensaje de prueba (éxito)")
    ps.mensaje("Este es un mensaje normal", inicio = "    ")
    ps.mensajeImportante("Mensaje de prueba (importante)")
    ps.mensaje("Este es un mensaje normal", inicio = "  ")
    ps.mensajeAdvertencia("Mensaje de prueba (advertencia)", inicio = "    ")

if __name__ == "__main__":
    main()