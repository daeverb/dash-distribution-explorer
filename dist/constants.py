import plotly.graph_objects as go

BASE_FIGURE_LAYOUT = go.Layout(
    width=360,
    height=300,
    margin=dict(l=0, r=0, t=50, b=50),
    xaxis=dict(zeroline=True, zerolinewidth=1, zerolinecolor='#333333'),
    yaxis=dict(zeroline=True, zerolinewidth=1, zerolinecolor='#333333'),
    paper_bgcolor='rgba(255,255,255,1)',
    plot_bgcolor='rgba(255,255,255,1)',
)