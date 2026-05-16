# Integrantes:
# -  CHINGA AYORA MICHELLE
# - REVELO BRAVO GENESIS
# - VAQUE REYES DANIELA

from Clase_base import ServicioTienda


# Tarifas por tipo de entrega (precio base en dólares)
TARIFAS_ENTREGA = {
    "estandar": 2.50,
    "express": 5.00,
    "mismo_dia": 8.00,
}


class ServicioEnvio(ServicioTienda):
    """Representa el servicio de envío de un pedido.
    El costo se calcula según distancia (km), peso (kg) y tipo de entrega."""

    def __init__(self, codigo, descripcion, fecha, distancia_km, peso_kg, tipo_entrega="estandar"):
        super().__init__(codigo, descripcion, fecha)
        self.distancia_km = distancia_km    # usa setter con validación
        self.peso_kg = peso_kg              # usa setter con validación
        self.tipo_entrega = tipo_entrega    # usa setter con validación

    # --- distancia_km ---
    @property
    def distancia_km(self):
        return self._distancia_km

    @distancia_km.setter
    def distancia_km(self, valor):
        if valor <= 0:
            raise ValueError("La distancia debe ser mayor a cero.")
        self._distancia_km = valor

    # --- peso_kg ---
    @property
    def peso_kg(self):
        return self._peso_kg

    @peso_kg.setter
    def peso_kg(self, valor):
        if valor <= 0:
            raise ValueError("El peso debe ser mayor a cero.")
        self._peso_kg = valor

    # --- tipo_entrega ---
    @property
    def tipo_entrega(self):
        return self._tipo_entrega

    @tipo_entrega.setter
    def tipo_entrega(self, valor):
        if valor not in TARIFAS_ENTREGA:
            raise ValueError(f"Tipo de entrega inválido. Opciones: {list(TARIFAS_ENTREGA.keys())}")
        self._tipo_entrega = valor

    # --- Métodos polimórficos ---
    def calcular_costo(self):
        """Costo = tarifa_base + (distancia * 0.05) + (peso * 0.30)."""
        tarifa_base = TARIFAS_ENTREGA[self._tipo_entrega]
        costo = tarifa_base + (self._distancia_km * 0.05) + (self._peso_kg * 0.30)
        return round(costo, 2)

    def mostrar_info(self):
        return (f"ENVÍO | Tipo: {self._tipo_entrega.upper()} | "
                f"Distancia: {self._distancia_km} km | Peso: {self._peso_kg} kg | "
                f"Costo envío: ${self.calcular_costo():.2f}")

    def __str__(self):
        return (super().__str__() +
                f" | Tipo envío: {self._tipo_entrega} | Costo: ${self.calcular_costo():.2f}")
