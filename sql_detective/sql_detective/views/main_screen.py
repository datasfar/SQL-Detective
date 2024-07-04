import reflex as rx

from sql_detective.components.mission_card import mission_card

from sql_detective.states.MainState import MainState


def  main_creen() -> rx.Component:
    return rx.tabs.root(
        rx.tabs.list(
            rx.tabs.trigger("Misions", value="tab1"),
            rx.tabs.trigger("Outputs", value="tab2"),
            rx.tabs.trigger("Schemas", value="tab3"),
        ),
        rx.tabs.content(
            rx.foreach(
                MainState.missions,
                mission_card
            ),
            overflow="scroll",
            min_height="70vh",
            max_height="70vh",
            value="tab1",
        ),
        rx.color_mode_cond(
            light=comp_light(),
            dark=comp_dark()
        ),
        rx.tabs.content(
            rx.text(f"Tabla: {MainState.table_title}"),
            rx.foreach(
                MainState.get_schemas,
                lambda x: rx.text(x)
            ),
            overflow="scroll",
            min_height="70vh",
            max_height="70vh",
            value="tab3",
        ),
        default_value="tab2",
    )


def comp_light()-> rx.Component:
    return rx.tabs.content(
            rx.data_table(data=MainState.resultado, pagination=True, resizable=True),
            overflow="scroll",
            min_height="70vh",
            max_height="70vh",
            font_size=".8em",
            style={'.gridjs-footer':{"border_radius":"0px !important"}},
            value="tab2",
        )

def comp_dark()-> rx.Component:
    return rx.tabs.content(
            rx.data_table(data=MainState.resultado, pagination=True, resizable=True),
            overflow="scroll",
            min_height="70vh",
            max_height="70vh",
            font_size=".8em",
            style={'.gridjs-th': {'background_color': '#111113', 'color':"#B0B5BA"},
                   '.gridjs-td': {'background_color': '#111113', 'color':"#EDEEF0"},
                   '.gridjs-pagination': {'background_color': '#111113', 'color':"#B0B5BA"},
                   '.gridjs-footer': {'background_color': '#111113', 'color':"#B0B5BA", "border_radius":"0px !important"},
                   '.gridjs-pages button': {'background_color': '#111113 !important', 'color':"#B0B5BA !important"},
            },
            value="tab2",
        )