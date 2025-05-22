import reflex as rx

def navbar() -> rx.Component:
    return rx.hstack(
        rx.text(
            "ASORMAR",
            height="40px",
            weight="medium"
        ),
        position="sticky",
        bg="red",
        padding_x="16px",
        padding_y="8px",
        z_index=999 # para asegurarse que siempre está en la parte de arriba
    )