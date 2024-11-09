class Motor:
    def __init__(self, numeroCilindros, tipo, registro):
        self.numeroCilindros = numeroCilindros
        self.tipo = tipo
        self.registro = registro
    
    def cambiarRegistro(self, nuevoRegistro):
        self.registro = nuevoRegistro
    
    def asignarTipo(self, nuevoTipo):
        tipos = ["electrico", "gasolina"]
        for elemento in tipos:
            if elemento == nuevoTipo:
                self.tipo = nuevoTipo


class Asiento:
    def __init__(self, color, precio, registro):
        self.color = color
        self.precio = precio
        self.registro = registro
    
    def cambiarColor(self, nuevoColor):
        colores = ["rojo", "verde", "amarillo", "negro", "blanco"]
        for elemento in colores:
            if elemento == nuevoColor:
                self.color = nuevoColor

class Auto:
    cantidadCreados = 0

    def __init__(self, modelo, precio, asientos, marca, motor, registro):
        self.modelo = modelo
        self.precio = precio
        self.asientos = asientos
        self.marca = marca
        self.motor = motor
        self.registro = registro
    
    def cantidadAsientos(self):
        contadorAsientos = 0
        for asiento in self.asientos:
            if asiento == None:
                continue
            else:
                contadorAsientos += 1
        return contadorAsientos

    def verificarIntegridad(self):
        comprobanteIntegridad = False
        mensaje = ""

        if self.registro == self.motor.registro:
            comprobanteIntegridad = True

            for elemento in self.asientos:
                if elemento == None:
                    continue
                elif self.registro != elemento.registro:
                    comprobanteIntegridad = False
                    break
                else:
                    comprobanteIntegridad = True
        
        if comprobanteIntegridad == False:
            mensaje = "Las piezas no son originales"
        else:
            mensaje = "Auto original"
        
        return mensaje