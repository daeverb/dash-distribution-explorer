from dash import Dash, html, dcc, callback, Input, Output, State, MATCH, ALL, callback_context
import dash_bootstrap_components as dbc
from constants import DIST_NAMES, DISTNAME2DIST, D2I, I2D, INITIAL_DISTRIBUTION


app = Dash(
    __name__,
    external_stylesheets=[dbc.themes.BOOTSTRAP]
)

dropdown = dbc.DropdownMenu(
    id='distribution-dropdown',
    children=[
        dbc.DropdownMenuItem(
            children=d,
            id={'type':'dist-select', 'index':D2I[d]},
            n_clicks=0,
        ) for d in DIST_NAMES
    ],
    label='Select distribution',
    class_name='w-100'
)

desc_div = html.Div(
    [
        html.H4(
            id='dist-title',
            children=INITIAL_DISTRIBUTION,
        ),
        dcc.Markdown(
            id='dist-description',
            children=[DISTNAME2DIST[INITIAL_DISTRIBUTION].description],
            mathjax=True,
        ),
    ]
)

counter = 0
sliderids2dist = {}
dist_control_divs = {}
for i, d in I2D.items():
    distribution = DISTNAME2DIST[d]
    dist_controls = []
    for parameter, values in distribution.parameters.items():
        label = dbc.Label(parameter + ':')
        slider = dcc.Slider(
            id={'type': 'slider', 'index': counter, 'parameter': parameter},
            min=values['min'],
            max=values['max'],
            value=values['value'],
            step=values['step'],
            marks=None,
            updatemode='drag',
            tooltip={
                "always_visible": True,
                "placement": "bottom"
            },
            className='w-75 align-self-bottom mt-4 mb-2'
        )
        div = html.Div(
            children=[label, slider],
            className='hstack gap-2'
        )
        dist_controls.append(div)
        sliderids2dist[counter] = d
        counter += 1
    dist_control_divs[d] = html.Div(
        id={'type': 'parameter-control-div', 'index': i},
        children=dist_controls
    )


D = DISTNAME2DIST[INITIAL_DISTRIBUTION]
figs = D.get_figures(**{'n':20, 'p':0.5})

graphs = []
for i, f in enumerate(figs):
    graphs.append(
        dcc.Graph(
            id={'type': 'graph', 'index': i},
            figure=f,
            responsive=False,
        )
    )

fig_div = html.Div(
    id='dist-fig-div',
    children=graphs,
    className='d-flex flex-wrap hstack gap-2'
)


app.layout = html.Div([
    dbc.Container(
        [
            dbc.Row(
                dbc.Col(dropdown, class_name='w-100'),
                class_name='m-2 w-100'
            ),
            dbc.Row(
                dbc.Col(desc_div),
                class_name='border rounded m-2'
            ),
            dbc.Row(
                dbc.Col(
                    id='sliders-col',
                    children=dist_control_divs[INITIAL_DISTRIBUTION],
                    class_name='justify-content-center w-100'
                ),
                class_name='border rounded m-2 justify-content-center'
            ),
            dbc.Row(
                dbc.Col(fig_div, class_name='d-flex justify-content-center'),
                class_name='border rounded m-2 align-center'
            ),
        ],
        style={'max-width': '800px'}
    )
])

@callback(
    [
        Output('sliders-col', 'children'),
        Output('dist-description', 'children'),
        Output('dist-title', 'children'),
    ],
    [
        Input({'type':'dist-select', 'index':ALL}, 'n_clicks'),
    ],
    config_prevent_initial_callbacks=True
)
def change_distribution(_):
    ctx = callback_context

    if not ctx.triggered:
        return None, None, None  # No input has triggered the callback, return default or empty

    # Get the id of the component that triggered the callback
    trigger_id = ctx.triggered[0]['prop_id'].split('.')[0]
    trigger_id = eval(trigger_id)  # Convert string representation of dict back to dict

    if trigger_id:
        index = trigger_id['index']  # Extract the index of the triggered component
        dist = dist_control_divs[I2D[index]]
        md = DISTNAME2DIST[I2D[index]].description
        title = I2D[index]
        return dist, md, title

    return None, None, None



@callback(
    Output('dist-fig-div', 'children'),
    [
        Input({'type': 'slider', 'index': ALL, 'parameter': ALL}, 'value'),
        Input('sliders-col', 'children'),
        State({'type': 'slider', 'index': ALL, 'parameter': ALL}, 'id'),
    ]
)
def update_figure(slider_values, _,slider_ids):
    parameters = {}
    for i, slider in enumerate(slider_ids):
        par = slider['parameter']
        parameters[par] = slider_values[i]

    D = DISTNAME2DIST[sliderids2dist[slider_ids[0]['index']]]
    figs = D.get_figures(**parameters)

    graphs = []
    for i, f in enumerate(figs):
        graphs.append(
            dcc.Graph(
                figure=f,
                responsive=False,
            )
        )
    return graphs


if __name__ == '__main__':
    app.run(debug=True)
