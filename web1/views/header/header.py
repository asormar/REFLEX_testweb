import reflex as rx

def header() -> rx.Component:
    return rx.vstack(
        rx.avatar(fallback="AS", size="8", radius="full", bg="orange"),
        rx.text("@asormar1"),
        rx.text("HOLA MI NOMBRE ES ALEJANDRO"),
        rx.text("Soy estudiante de GTDM en la Universidad Politécnica de Valencia y estoy creando esta página web de enlaces para probar el framework de python llamado REFLEX"),
        align="center"
    )