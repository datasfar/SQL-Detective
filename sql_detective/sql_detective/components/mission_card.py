import reflex as rx

def mission_card(hint:str) -> rx.Component:
    return rx.card(
        rx.hstack(
            rx.color_mode_cond(
                light=rx.image(src="woman2.png", width="30px", margin_right="5px"),
                dark=rx.image(src="woman2.png", width="30px", margin_right="5px", filter="invert(100%)")
            ),
            rx.text(hint),
            align_items="baseline",
        ),
        rx.checkbox(default_checked=False, variant="surface", cursor="none"),
        width="100%",
        display="flex",
        align_items="baseline",
        justify_content="space-between",
        margin_top=".5em"
    )
