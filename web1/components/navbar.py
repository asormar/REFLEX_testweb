import reflex as rx
import web1.styles.styles as styles

def navbar() -> rx.Component:
    return rx.hstack(
        rx.text(
            "ASORMAR",
            weight="medium"
        ),
        position="sticky",
        bg=rx.color("blue",3), # https://www.radix-ui.com/colors
        padding_x=styles.Spacer.DEFAULT,
        padding_y=styles.Spacer.SMALL,
        z_index=999, # keeps navbar on top
        top=0 # to overpose the navbar while scrolling
    )