# Integrantes:
# - CHINGA AYORA MICHELLE
# - REVELO BRAVO GENESIS
# - VAQUE REYES DANIELA

class GestorTienda:
    """Gestiona todos los servicios registrados en la tienda online.
    Implementa las funciones polimórficas principales."""

    def __init__(self, nombre_tienda):
        self._nombre_tienda = nombre_tienda
        self._servicios = []    # lista de objetos ServicioTienda (superclase)

    # --- nombre_tienda ---
    @property
    def nombre_tienda(self):
        return self._nombre_tienda

    @nombre_tienda.setter
    def nombre_tienda(self, valor):
        if not valor or valor.strip() == "":
            raise ValueError("El nombre de la tienda no puede estar vacío.")
        self._nombre_tienda = valor

    # --- Gestión de servicios ---
    def agregar_servicio(self, servicio):
        self._servicios.append(servicio)
        print(f"  ✔ Servicio '{servicio.codigo}' agregado correctamente.")

    def listar_servicios(self):
        print(f"\n{'='*60}")
        print(f"  SERVICIOS REGISTRADOS EN '{self._nombre_tienda}'")
        print(f"{'='*60}")
        if not self._servicios:
            print("  No hay servicios registrados.")
        for s in self._servicios:
            print(f"  {s}")
        print(f"{'='*60}")

    # --- Métodos polimórficos ---
    def calcular_total(self):
        """Suma los costos de TODOS los servicios registrados (polimorfismo)."""
        total = 0
        for servicio in self._servicios:
            total += servicio.calcular_costo()
        return round(total, 2)

    def generar_reporte(self):
        """Genera un reporte completo llamando mostrar_info() en cada servicio (polimorfismo)."""
        print(f"\n{'='*60}")
        print(f"  REPORTE DE SERVICIOS - {self._nombre_tienda}")
        print(f"{'='*60}")
        if not self._servicios:
            print("  Sin servicios para reportar.")
        for servicio in self._servicios:
            print(f"  {servicio.mostrar_info()}")
        print(f"\n  TOTAL ACUMULADO: ${self.calcular_total():.2f}")
        print(f"{'='*60}")

    def __str__(self):
        return (f"GestorTienda: {self._nombre_tienda} | "
                f"Servicios registrados: {len(self._servicios)}")
