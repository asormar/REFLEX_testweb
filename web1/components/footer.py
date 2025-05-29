import reflex as rx
import reflex_chakra as rc
import datetime
import web1.styles.styles as styles
import web1.styles.colors as colors

def footer() -> rx.Component:
    return rx.vstack(
        rx.image(src="logo.png",
                 width=styles.Spacer.VERY_BIG,
                 height="auto"),
        rc.link(
            f"2022-{datetime.date.today().year} asormar as Alejandro Sorolla Martínez",
            href="https://www.linkedin.com/in/alejandro-sorolla-74a262275/",
            is_external=True,
            trim="end",
            font_size=styles.Spacer.MEDIUM,
            color=colors.TextColor.FOOTER
        ),
        rx.text("TRYING TO BUILD SOME PROJECTS FROM VALENCIA", font_size=styles.Spacer.MEDIUM, margin_top="-8px"),
        margin_top=styles.Spacer.BIG,
        margin_bottom=styles.Spacer.BIG,
        padding_bottom=styles.Spacer.BIG,
        align="center",
        color=colors.TextColor.FOOTER
    )