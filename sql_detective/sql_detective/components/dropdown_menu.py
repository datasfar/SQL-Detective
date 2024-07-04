import reflex as rx
from sql_detective.states.MainState import MainState
def dropdown_menu() -> rx.Component:
    return rx.flex(
    rx.menu.root(
        rx.menu.trigger(
            rx.button(rx.icon("menu"), variant="ghost", size="2", 
            style={
                "_focus":{
                  "border":"none !important"
              }
            }),
        ),
        rx.menu.content(
            rx.menu.item("New Game", on_click=MainState.generate_misions),
            rx.menu.item("Save Game" ),
            rx.menu.separator(),
            rx.menu.item("Ranking"),
            size="2",
        ),
    ),
    spacing="3",
    align="center",
)