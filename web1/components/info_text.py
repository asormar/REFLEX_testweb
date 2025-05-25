import reflex as rx
import  web1.styles.styles as styles

def info_text(title:str, body:str) -> rx.Component:
    return rx.box(
        rx.text(title, as_="span", font_weight="bold", color="blue"),
        f" {body}", font_size=styles.Spacer.MEDIUM
    )