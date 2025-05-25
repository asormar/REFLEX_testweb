import reflex as rx
import web1.styles.styles as styles
from web1.styles.colors import TextColor
from web1.components.link_icon import link_icon
from web1.components.info_text import info_text

def header() -> rx.Component:
    return rx.vstack(
        rx.hstack(
            rx.avatar(fallback="AS", size="7", radius="full", bg=rx.color("blue",3)),
            rx.vstack(
                rx.heading("Alejandro SM", size="6", color=TextColor.HEADER),
                rx.text("@asormar1", margin_top="-15px", color=TextColor.BODY),

                rx.hstack(
                    link_icon("https://www.instagram.com"),
                    link_icon("https://link.chess.com/friend/g9q6ml"),
                    link_icon("https://www.goodreads.com/user/show/181296324-alejandro-sorolla")
                ),
                
                padding_top=styles.Spacer.DEFAULT
            ),
            spacing="4" #creates an space between avatar and vstack

        ),

        rx.flex(
            info_text("Python", "web development"),
            rx.spacer(), # push the element as far as possible
            info_text("Murakami", "fan reader"),
            rx.spacer(),
            info_text("+21 years", "breaking it"),
            width="100%" # need to make work the spacers
        ),

        rx.text("Soy estudiante de GTDM en la Universidad Politécnica de Valencia y estoy creando esta página web de enlaces para probar el framework de python llamado REFLEX",
                margin_top= styles.Spacer.DEFAULT.value,
                color=TextColor.BODY),
        align_items="start"
    )