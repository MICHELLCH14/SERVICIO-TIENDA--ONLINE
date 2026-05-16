# Integrantes:
# - CHINGA AYORA MICHELLE
# - REVELO BRAVO GENESIS
# - VAQUE REYES DANIELA

from Clase_baselase_base import ServicioTienda
from clase_hija_1 import CompraProducto
from clase_hija_2 import ServicioEnvio
from clase_extra_1 import ClienteOnline
from clase_extra_2 import GestorTienda


def separador(titulo=""):
    print(f"\n{'─'*60}")
    if titulo:
        print(f"  {titulo}")
        print(f"{'─'*60}")


def main():
    print("=" * 60)
    print("   SISTEMA DE GESTIÓN DE SERVICIOS - TIENDA ONLINE")
    print("=" * 60)

    # ─── 1. Crear objetos de las clases hijas ───────────────────
    separador("1. CREANDO SERVICIOS")

    compra1 = CompraProducto(
        codigo="C001",
        descripcion="Compra de laptop",
        fecha="2025-06-01",
        nombre_producto="Laptop Lenovo IdeaPad",
        precio=850.00,
        cantidad=1,
        descuento=10
    )

    compra2 = CompraProducto(
        codigo="C002",
        descripcion="Compra de auriculares",
        fecha="2025-06-02",
        nombre_producto="Auriculares Sony WH-1000XM5",
        precio=120.00,
        cantidad=2,
        descuento=5
    )

    envio1 = ServicioEnvio(
        codigo="E001",
        descripcion="Envío express a Quito",
        fecha="2025-06-01",
        distancia_km=280,
        peso_kg=3.5,
        tipo_entrega="express"
    )

    envio2 = ServicioEnvio(
        codigo="E002",
        descripcion="Envío estándar a Cuenca",
        fecha="2025-06-03",
        distancia_km=450,
        peso_kg=8.0,
        tipo_entrega="estandar"
    )

    envio3 = ServicioEnvio(
        codigo="E003",
        descripcion="Envío mismo día en Guayaquil",
        fecha="2025-06-04",
        distancia_km=15,
        peso_kg=1.2,
        tipo_entrega="mismo_dia"
    )

    print("  Objetos creados exitosamente.")

    # ─── 2. Guardar en lista de la superclase ────────────────────
    separador("2. LISTA DE SERVICIOS (SuperClase ServicioTienda)")

    servicios: list[ServicioTienda] = [compra1, compra2, envio1, envio2, envio3]

    # ─── 3. Imprimir usando __str__() ────────────────────────────
    separador("3. IMPRESIÓN CON __str__()")
    for s in servicios:
        print(f"  {s}")

    # ─── 4. Ejecutar métodos heredados y propios ─────────────────
    separador("4. MÉTODOS PROPIOS DE CADA CLASE HIJA")

    print(f"\n  Costo compra1 (calcular_costo): ${compra1.calcular_costo():.2f}")
    print(f"  Costo compra2 (calcular_costo): ${compra2.calcular_costo():.2f}")
    print(f"  Costo envio1  (calcular_costo): ${envio1.calcular_costo():.2f}")
    print(f"  Costo envio2  (calcular_costo): ${envio2.calcular_costo():.2f}")
    print(f"  Costo envio3  (calcular_costo): ${envio3.calcular_costo():.2f}")

    # ─── 5. Crear clientes y asociar servicios ───────────────────
    separador("5. CLIENTES ONLINE")

    cliente1 = ClienteOnline("CLI-001", "Ana García", "ana.garcia@email.com", es_premium=True)
    cliente2 = ClienteOnline("CLI-002", "Luis Pérez", "luis.perez@email.com", es_premium=False)

    cliente1.agregar_servicio(compra1)
    cliente1.agregar_servicio(envio1)

    cliente2.agregar_servicio(compra2)
    cliente2.agregar_servicio(envio2)
    cliente2.agregar_servicio(envio3)

    print(f"\n  {cliente1}")
    print(f"\n  Servicios de {cliente1.nombre}:")
    cliente1.listar_servicios()

    print(f"\n  {cliente2}")
    print(f"\n  Servicios de {cliente2.nombre}:")
    cliente2.listar_servicios()

    # ─── 6. GestorTienda y métodos POLIMÓRFICOS ──────────────────
    separador("6. GESTOR TIENDA - MÉTODOS POLIMÓRFICOS")

    gestor = GestorTienda("TechShop Ecuador")
    print(f"\n  Registrando servicios en el gestor...")
    for s in servicios:
        gestor.agregar_servicio(s)

    # Método polimórfico 1: calcular_total()
    print(f"\n  [POLIMORFISMO 1] calcular_total():")
    print(f"  Total de todos los servicios: ${gestor.calcular_total():.2f}")

    # Método polimórfico 2: generar_reporte() → llama mostrar_info() en cada objeto
    print(f"\n  [POLIMORFISMO 2] generar_reporte():")
    gestor.generar_reporte()

    # Listar todos los servicios
    gestor.listar_servicios()

    print(f"\n  {gestor}")

    # ─── 7. Validaciones de encapsulamiento ─────────────────────
    separador("7. PRUEBA DE VALIDACIONES (encapsulamiento)")

    print("\n  Intentando asignar precio negativo a compra1...")
    try:
        compra1.precio = -50
    except ValueError as e:
        print(f"  ✔ Error capturado: {e}")

    print("\n  Intentando asignar cantidad cero a compra2...")
    try:
        compra2.cantidad = 0
    except ValueError as e:
        print(f"  ✔ Error capturado: {e}")

    print("\n  Intentando crear cliente con email inválido...")
    try:
        c_invalido = ClienteOnline("CLI-X", "Test", "correo-sin-arroba")
    except ValueError as e:
        print(f"  ✔ Error capturado: {e}")

    print("\n  Intentando crear envío con tipo de entrega inválido...")
    try:
        envio_invalido = ServicioEnvio("E999", "Test", "2025-01-01", 10, 1, "teleporte")
    except ValueError as e:
        print(f"  ✔ Error capturado: {e}")

    separador()
    print("  FIN DEL PROGRAMA - Sistema de Tienda Online")
    print("=" * 60)


if __name__ == "__main__":
    main()
