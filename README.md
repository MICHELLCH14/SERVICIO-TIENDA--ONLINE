# FG26
# Sistema de Gestión de Servicios - Tienda Online
## Proyecto Primer Parcial — Programación Orientada a Objetos

---

## Descripción
Sistema desarrollado en Python que simula la gestión de servicios de una tienda en línea. Permite registrar compras de productos y servicios de envío, asociarlos a clientes y generar reportes con costos totales.

---

## Diagrama de Clases

```
ServicioTienda  (superclase)
│   - _codigo
│   - _descripcion
│   - _fecha
│   + calcular_costo()  ← polimórfico
│   + mostrar_info()    ← polimórfico
│
├── CompraProducto  (clase hija 1)
│       - _nombre_producto
│       - _precio
│       - _cantidad
│       - _descuento
│       + calcular_costo()  → precio * cantidad * (1 - descuento/100)
│       + mostrar_info()
│
└── ServicioEnvio  (clase hija 2)
        - _distancia_km
        - _peso_kg
        - _tipo_entrega
        + calcular_costo()  → tarifa_base + dist*0.05 + peso*0.30
        + mostrar_info()

ClienteOnline  (clase adicional 1)
    - _id_cliente
    - _nombre
    - _email
    - _es_premium
    - _servicios (lista)
    + agregar_servicio()
    + total_gastado()

GestorTienda  (clase adicional 2)
    - _nombre_tienda
    - _servicios (lista de ServicioTienda)
    + calcular_total()   ← método polimórfico
    + generar_reporte()  ← método polimórfico
```

---

## Estructura del repositorio

```
ProyectoPOO_Parcial1/
├── clase_base.py       → Superclase ServicioTienda
├── clase_hija_1.py     → Clase hija CompraProducto
├── clase_hija_2.py     → Clase hija ServicioEnvio
├── clase_extra_1.py    → Clase adicional ClienteOnline
├── clase_extra_2.py    → Clase adicional GestorTienda
├── main.py             → Programa principal
└── README.md
```

---

## Instrucciones de ejecución

1. Clonar el repositorio:
```bash
git clone https://github.com/usuario/ProyectoPOO_Parcial1.git
cd ProyectoPOO_Parcial1
```

2. Ejecutar el programa (requiere Python 3.8+):
```bash
python main.py
```

---

## Conceptos aplicados

| Concepto         | Implementación |
|-----------------|----------------|
| Encapsulamiento | Todos los atributos son privados (`_atributo`), con `@property` y `@setter` con validaciones |
| Herencia        | `CompraProducto` y `ServicioEnvio` heredan de `ServicioTienda` |
| Polimorfismo    | `calcular_total()` y `generar_reporte()` llaman `calcular_costo()` y `mostrar_info()` sobre cualquier objeto de la superclase |
| Clases          | 5 clases en total (1 superclase + 2 hijas + 2 adicionales) |

---

## Integrantes
# - CHINGA AYORA MICHELLE
# - REVELO BRAVO GENESIS
# - VAQUE REYES DANIELA

---

## Video explicativo
[Enlace al video — agregar aquí]