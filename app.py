import flet as ft
import math

# Capacidades de las barcazas iniciales
barcazas = {
    "Angeka": {"A": 50, "B": 30, "C": 40, "tiempo": 5},  # tiempo en horas
    "María": {"A": 20, "B": 50, "C": 50, "tiempo": 6},
    "Hanahui": {"A": 40, "B": 30, "C": 60, "tiempo": 7},
}

# Capacidades de las futuras barcazas
nuevas_barcazas = {
    "Barcaza 1": {"A": 40, "B": 20, "C": 10, "tiempo": 8},
    "Barcaza 2": {"A": 20, "B": 60, "C": 30, "tiempo": 9},
}

# Cantidades de contenedores a transportar
contenedores = {"A": 4500, "B": 4400, "C": 5800}

def calcular_viajes_y_tiempo(contenedores, barcazas, tiempo_retraso):
    resultados = {}
    for nombre, capacidad in barcazas.items():
        viajes = {tipo: math.ceil(contenedores[tipo] / capacidad[tipo]) for tipo in contenedores}
        max_viajes = max(viajes.values())
        tiempo_total = max_viajes * (capacidad["tiempo"] + tiempo_retraso)
        resultados[nombre] = (max_viajes, tiempo_total)
    return resultados

def main(page: ft.Page):
    page.title = "Optimización de Transporte"
    page.scroll = "adaptive"

    # Inputs
    nombre_input = ft.TextField(label="Nombre", width=200)
    carga_a_input = ft.TextField(label="Carga de A", value="4500", width=200)
    carga_b_input = ft.TextField(label="Carga de B", value="4400", width=200)
    carga_c_input = ft.TextField(label="Carga de C", value="5800", width=200)
    tiempo_retraso_input = ft.TextField(label="Tiempo de retraso (horas)", value="0", width=200)

    # Radio button for Retraso
    retraso_radio = ft.RadioGroup(
        content=ft.Row([ft.Radio(value="retraso", label="Retraso")])
    )

    # Containers for results
    results_container = ft.Column()

    def on_calcular_click(e):
        contenedores_actualizados = {
            "Angeka": int(carga_a_input.value),
            "Maria": int(carga_b_input.value),
            "Hanahui": int(carga_c_input.value)
        }
        tiempo_retraso = float(tiempo_retraso_input.value)
        resultados = calcular_viajes_y_tiempo(contenedores_actualizados, barcazas, tiempo_retraso)
        results_container.controls.clear()
        for nombre, (viajes, tiempo_total) in resultados.items():
            results_container.controls.append(ft.Text(f"{nombre} debe hacer {viajes} viajes, tardando un total de {tiempo_total} horas."))
        page.update()

    def on_borrar_click(e):
        nombre_input.value = ""
        carga_a_input.value = ""
        carga_b_input.value = ""
        carga_c_input.value = ""
        tiempo_retraso_input.value = "0"
        results_container.controls.clear()
        page.update()

    def on_agregar_barcazas_click(e):
        barcazas.update(nuevas_barcazas)
        on_calcular_click(e)

    # Buttons
    calcular_button = ft.ElevatedButton(text="Calcular", on_click=on_calcular_click)
    borrar_button = ft.ElevatedButton(text="Borrar", on_click=on_borrar_click)
    agregar_barcazas_button = ft.ElevatedButton(text="Agregar Barcazas", on_click=on_agregar_barcazas_click)

    # Layout
    layout = ft.Column(
        controls=[
            nombre_input,
            carga_a_input,
            carga_b_input,
            carga_c_input,
            ft.Row([retraso_radio, tiempo_retraso_input]),
            results_container,
            ft.Row([borrar_button, calcular_button, agregar_barcazas_button], alignment="center"),
        ],
        alignment="start",
        horizontal_alignment="center",
        expand=True,
    )

    page.add(layout)

ft.app(target=main)
