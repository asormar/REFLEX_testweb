import reflex as rx
import web1.styles.styles as styles

def title(text:str) -> rx.Component:
    return rx.heading(
        text,
        style=styles.title_style,
        size="6"
)