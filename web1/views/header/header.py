import reflex as rx
import web1.styles.styles as styles
from web1.components.link_icon import link_icon

def header() -> rx.Component:
    return rx.vstack(
        rx.hstack(
            rx.avatar(fallback="AS", size="7", radius="full", bg=rx.color("blue",3)),
            rx.vstack(
                rx.heading("Alejandro SM", size="6"),
                rx.text("@asormar1", margin_top="-15px"),

                rx.hstack(
                    link_icon("https://www.instagram.com"),
                    link_icon("https://link.chess.com/friend/g9q6ml"),
                    link_icon("https://www.goodreads.com/user/show/181296324-alejandro-sorolla")
                ),
                
                padding_top=styles.Spacer.DEFAULT
            )

        ),
        rx.text("Soy estudiante de GTDM en la Universidad Politécnica de Valencia y estoy creando esta página web de enlaces para probar el framework de python llamado REFLEX",
                margin_top= styles.Spacer.DEFAULT.value),
        align_items="start"
    )