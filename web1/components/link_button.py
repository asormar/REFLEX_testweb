import reflex as rx
import web1.styles.styles as styles

def link_button(title:str, body:str, url:str) -> rx.Component: #es necesario poner :str
    return rx.link(
        rx.button(
            rx.hstack(
                rx.icon(tag="arrow-big-right-dash", width=styles.Spacer.BIG, height=styles.Spacer.BIG),
                rx.vstack(
                    rx.text(title, style=styles.button_title_style),
                    rx.text(body, style=styles.button_body_style)
                )
                
            )
        ),

        href= url,
        is_external=True,
        width="100%"
    )