import reflex as rx
import  web1.styles.styles as styles
import  web1.styles.colors as colors

def info_text(title:str, body:str) -> rx.Component:
    return rx.box(
        rx.text(
            title,
            as_="span",
            font_weight="bold",
            color=colors.Colors.PRIMARY),
        
        f" {body}",
        font_size=styles.Spacer.MEDIUM,
        color= colors.TextColor.BODY
    )