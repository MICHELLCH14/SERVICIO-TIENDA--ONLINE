# Integrantes:
# - CHINGA AYORA MICHELLE
# - REVELO BRAVO GENESIS
# - VAQUE REYES DANIELA

from Clase_base import ServicioTienda


class CompraProducto(ServicioTienda):
    """Representa la compra de un producto en la tienda online.
    El costo total se calcula según precio, cantidad y descuento (%)."""

    def __init__(self, codigo, descripcion, fecha, nombre_producto, precio, cantidad, descuento=0):
        super().__init__(codigo, descripcion, fecha)
        self._nombre_producto = nombre_producto
        self.precio = precio
        self.cantidad = cantidad
        self.descuento = descuento

    # --- nombre_producto ---
    @property
    def nombre_producto(self):
        return self._nombre_producto

    @nombre_producto.setter
    def nombre_producto(self, valor):
        if not valor or valor.strip() == "":
            raise ValueError("El nombre del producto no puede estar vacío.")
        self._nombre_producto = valor

    # --- precio ---
    @property
    def precio(self):
        return self._precio

    @precio.setter
    def precio(self, valor):
        if valor < 0:
            raise ValueError("El precio no puede ser negativo.")
        self._precio = valor

    # --- cantidad ---
    @property
    def cantidad(self):
        return self._cantidad

    @cantidad.setter
    def cantidad(self, valor):
        if valor <= 0:
            raise ValueError("La cantidad debe ser mayor a cero.")
        self._cantidad = valor

    # --- descuento ---
    @property
    def descuento(self):
        return self._descuento

    @descuento.setter
    def descuento(self, valor):
        if valor < 0 or valor > 100:
            raise ValueError("El descuento debe estar entre 0 y 100.")
        self._descuento = valor

    def calcular_costo(self):
        """Total = precio * cantidad * (1 - descuento/100)."""
        subtotal = self._precio * self._cantidad
        total = subtotal * (1 - self._descuento / 100)
        return round(total, 2)

    def mostrar_info(self):
        return (f"COMPRA | Producto: {self._nombre_producto} | "
                f"Precio unitario: ${self._precio:.2f} | Cantidad: {self._cantidad} | "
                f"Descuento: {self._descuento}% | Total: ${self.calcular_costo():.2f}")

    def __str__(self):
        return (super().__str__() +
                f" | Producto: {self._nombre_producto} | Total: ${self.calcular_costo():.2f}")
