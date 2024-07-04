import reflex as rx
import sql_detective.styles.styles as styles

from sql_detective.components.dropdown_menu import dropdown_menu

def header() -> rx.Component:
    return rx.hstack(
        dropdown_menu(),
        rx.link(
            rx.color_mode_cond(
                light=rx.image(src="logo_light.png", width="30px", margin_right="5px"),
                dark=rx.image(src="logo_dark.png", width="30px", margin_right="5px")
            ),
            "SQL Detective", 
            href="/",
            style={
                "text_decoration":"none !important",
                "font_size":"1.2em",
                "font_weight":"600",
                "display":"flex",
                "align_items":"center"}
        ),
        rx.color_mode_cond(
                light=rx.stack(
                    rx.link(rx.icon("github", size=24, color="#C84D00")),
                    rx.link(rx.color_mode.button(size="3", color="#C84D00")),
                    align="center",
                ),
                dark=rx.stack(
                    rx.link(rx.icon("github", size=24, color="#F29852")),
                    rx.link(rx.color_mode.button(size="3", color="#F29852")),
                    align="center",
                ),
            ),
        
        justify="between",
        align="center",
        margin_bottom="40px",
    )