import dash
from dash import html
import dash_bootstrap_components as dbc

def sidebar():
    return html.Div(
        [
        dash.html.Div(
            dash.html.H1("Example of sidebar!")
        ),

        dbc.Nav(
            [
                dbc.NavLink(
                    [
                        html.Div(page["name"], className="ms-2"),
                    ],
                    href=page["path"],
                    active="exact",
                )
                for page in dash.page_registry.values()
                if page["path"].startswith("/test")
            ],
            vertical=True,
            pills=True,
            className="bg-light",
        )
    ]
    )
