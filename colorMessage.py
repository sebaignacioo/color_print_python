class ColorMessage:
    def __init__(self):
        self.__colorDict = {
            "red": "\u001b[31m",
            "green": "\u001b[32m",
            "blue": "\u001b[34m",
            "yellow": "\u001b[33m",
            "reset": "\u001b[0m"
        }

    def __resetColor(self):
        print(self.__colorDict["reset"], end="")

    def printColor(self, value, color = "", inicio = "", fin = "\n"):
        if self.__colorDict.get(color) != None:
            print(f"{self.__colorDict.get(color)}{inicio}{value}", end = fin)
        else:
            print(f"{inicio}{value}", end = fin)
        self.__resetColor()

class PrintService:
    def __init__(self):
        self.colorMsg = ColorMessage()

    def mensaje(self, mensaje, inicio = "", fin = "\n"):
        print(f"{inicio}{mensaje}", end = fin)

    def mensajeImportante(self, mensaje, inicio = "", fin = "\n"):
        self.colorMsg.printColor(f"{mensaje}", "blue", inicio, fin)

    def mensajeError(self, mensaje, inicio = "", fin = "\n"):
        self.colorMsg.printColor(f"=> ERROR: {mensaje}", "red", inicio, fin)

    def mensajeExito(self, mensaje, inicio = "", fin = "\n"):
        self.colorMsg.printColor(f"=> EXITO: {mensaje}", "green", inicio, fin)

    def mensajeAdvertencia(self, mensaje, inicio = "", fin = "\n"):
        self.colorMsg.printColor(f"=> ADVERTENCIA: {mensaje}", "yellow", inicio, fin)