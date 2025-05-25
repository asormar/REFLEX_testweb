import reflex as rx
import datetime
import web1.styles.styles as styles

def footer() -> rx.Component:
    return rx.vstack(
        rx.image(src="favicon.ico"),
        rx.link(
            f"2022-{datetime.date.today().year} asormar as Alejandro Sorolla Martínez",
            href="https://www.linkedin.com/in/alejandro-sorolla-74a262275/",
            is_external=True,
            trim="end",
            font_size=styles.Spacer.MEDIUM,
        ),
        rx.text("TRYING TO BUILD SOME PROJECTS FROM VALENCIA", font_size=styles.Spacer.MEDIUM, margin_top="-8px"),
        margin_bottom=styles.Spacer.BIG,
        align="center"
    )