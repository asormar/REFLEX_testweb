import reflex as rx
import reflex_chakra as rc
import web1.styles.styles as styles
import web1.styles.colors as colors

def navbar() -> rx.Component:
    return rx.hstack(
        rx.box(
            rc.span("a", color=colors.Colors.PRIMARY),
            rc.span("sor", color=colors.Colors.SECONDARY),
            rc.span("mar", color=colors.Colors.PRIMARY)
        ),
        position="sticky",
        bg=colors.Colors.CONTENT, # https://www.radix-ui.com/colors
        padding_x=styles.Spacer.BIG,
        padding_y=styles.Spacer.DEFAULT,
        z_index=999, # keeps navbar on top
        top=0 # to overpose the navbar while scrolling
    )