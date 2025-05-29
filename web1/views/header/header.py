import reflex as rx
import web1.styles.styles as styles
from web1.styles.colors import TextColor
from web1.styles.colors import Colors
from web1.components.link_icon import link_icon
from web1.components.info_text import info_text

def header() -> rx.Component:
    return rx.vstack(
        rx.hstack(
            rx.avatar(fallback="AS",
                      size="7",
                      src="foto.jpeg",
                      radius="full",
                      bg=Colors.BACKGROUND.value,
                      padding="2px",
                      border="solid 4px",
                      border_color=Colors.PRIMARY.value
                      ),
            rx.vstack(
                rx.heading("Alejandro SM", size="6"), # put here size cause is a reflex conditional, not css
                rx.text("@asormar1",
                        margin_top="-15px",
                        color=TextColor.BODY),

                rx.hstack(
                    link_icon("icons/instagram.png","https://www.instagram.com"),
                    link_icon("icons/chess.png","https://link.chess.com/friend/g9q6ml"),
                    link_icon("icons/book.png","https://www.goodreads.com/user/show/181296324-alejandro-sorolla")
                ),
                
                padding_top=styles.Spacer.DEFAULT
            ),
            spacing="4" #creates an space between avatar and vstack

        ),

        rx.flex(
            info_text("Python", "web development"),
            rx.spacer(), # push the element as far as possible
            info_text("Murakami", "fan reader"),
            rx.spacer(),
            info_text("+21 years", "breaking it"),
            width="100%" # need to make work the spacers
        ),

        rx.text("I am a GTDM student at the Polytechnic University of Valencia and I am creating this web page of links to test the python framework called REFLEX.",
                margin_top= styles.Spacer.DEFAULT.value,
                color=TextColor.BODY),
        align_items="start"
    )