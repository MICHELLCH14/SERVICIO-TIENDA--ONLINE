# Integrantes:
# - CHINGA AYORA MICHELLE
# - REVELO BRAVO GENESIS
# - VAQUE REYES DANIELA

class ServicioTienda:
    """Superclase base para todos los servicios de la tienda online."""

    def __init__(self, codigo, descripcion, fecha):
        self._codigo = codigo
        self._descripcion = descripcion
        self._fecha = fecha

    # --- codigo ---
    @property
    def codigo(self):
        return self._codigo

    @codigo.setter
    def codigo(self, valor):
        if not valor or valor.strip() == "":
            raise ValueError("El código no puede estar vacío.")
        self._codigo = valor

    # --- descripcion ---
    @property
    def descripcion(self):
        return self._descripcion

    @descripcion.setter
    def descripcion(self, valor):
        if not valor or valor.strip() == "":
            raise ValueError("La descripción no puede estar vacía.")
        self._descripcion = valor

    # --- fecha ---
    @property
    def fecha(self):
        return self._fecha

    @fecha.setter
    def fecha(self, valor):
        if not valor or valor.strip() == "":
            raise ValueError("La fecha no puede estar vacía.")
        self._fecha = valor

    # --- Métodos polimórficos (a sobreescribir en clases hijas) ---
    def calcular_costo(self):
        raise NotImplementedError("Cada clase hija debe implementar calcular_costo().")

    def mostrar_info(self):
        raise NotImplementedError("Cada clase hija debe implementar mostrar_info().")

    def __str__(self):
        return (f"[{self.__class__.__name__}] Código: {self._codigo} | "
                f"Descripción: {self._descripcion} | Fecha: {self._fecha}")
