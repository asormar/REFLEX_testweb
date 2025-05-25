import reflex as rx
import reflex_chakra as rc
import web1.styles.styles as styles

def link_button(title:str, body:str, url:str) -> rx.Component: #es necesario poner :str
    return rx.link(
        rc.button(
            rx.hstack(
                rx.icon(tag="arrow-big-right-dash",
                        width=styles.Spacer.BIG,
                        height=styles.Spacer.BIG,
                        margin=styles.Spacer.SMALL),

                rx.vstack(
                    rx.text(title, style=styles.button_title_style, margin_top="7px"),
                    rx.text(body, style=styles.button_body_style),
                    spacing="1" #space among both texts
                )
                
            )
        ),

        href= url,
        is_external=True,
        width="100%"
    )