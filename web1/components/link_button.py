import reflex as rx
import reflex_chakra as rc
import web1.styles.styles as styles

def link_button(title:str, body:str, icon:str, url:str) -> rx.Component: #es necesario poner :str
    return rx.link(
        rc.button(
            rx.hstack(
                rx.image(src=icon,
                        width=styles.Spacer.VERY_LARGE,
                        height=styles.Spacer.VERY_LARGE,
                        margin=styles.Spacer.SMALL),

                rx.vstack(
                    rx.text(title, style=styles.button_title_style, margin_top="8px", margin_bottom="-2px"),
                    rx.text(body, style=styles.button_body_style, margin_top="-1px"),
                    align_items="start",
                    text_align="start",
                    spacing="0" #space among both texts
                )
                
            ),width="100%",
            
            
        ),

        href= url,
        is_external=True,
        width="100%"
    )