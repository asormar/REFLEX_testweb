import reflex as rx
import datetime

def footer() -> rx.Component:
    return rx.vstack(
        rx.image(src="favicon.ico"),
        rx.link(
            f"2022-{datetime.date.today().year} ASORMAR BY ALEJANDRO SOROLLA MARTÍNEZ",
            href="https://www.linkedin.com/in/alejandro-sorolla-74a262275/",
            is_external=True,
            trim="end",
        ),
        rx.text("BUILDING SOFTWARE WITH LOVE FROM VALENCIA"),
        align="center"
    )