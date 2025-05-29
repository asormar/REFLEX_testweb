import reflex as rx
from web1.styles.styles import Spacer

def link_icon(image:str, url:str) -> rx.Component:
    return rx.link(
        rx.image(
            src=image,
            width= Spacer.DEFAULT.value
        ),
        href=url,
        is_external=True
    )