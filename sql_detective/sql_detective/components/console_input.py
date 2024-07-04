import reflex as rx

from sql_detective.states.MainState import MainState

def console_input() -> rx.Component:
    return rx.hstack(
        rx.form(
            rx.hstack(
                rx.input(
                    placeholder="Code here...",
                    name="querry",
                    variant="surface",
                    width="80%"
                ),
                rx.button("SEND", type="submit", variant="solid", width="20%"),
            ),
            on_submit=MainState.submit_querry,
            reset_on_submit=False,
        ),
        margin_top="1.5em",
        width="100%"
    )