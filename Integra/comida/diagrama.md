classDiagram
    class Plato {
        -nombre: str
        -precio: float
        +__init__(nombre, precio)
        +__str__(): str
    }

    class Menu {
        -platos: dict
        +__init__()
        +agregar_plato(nombre, precio)
        +obtener_plato(nombre): Plato
    }

    class Pedido {
        -platos: list
        +__init__()
        +agregar_plato(plato: Plato)
        +calcular_total(): float
    }

    class Restaurante {
        -menu: Menu
        -pedidos: list
        +__init__(menu: Menu)
        +crear_pedido(): Pedido
        +agregar_plato_a_pedido(pedido: Pedido, nombre_plato: str): bool
    }

    Menu --> Plato : crea/contiene
    Pedido --> Plato : contiene
    Restaurante --> Menu : usa
    Restaurante --> Pedido : crea/gestiona
