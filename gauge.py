import plotly.graph_objects as go

def bar_color(v):
    if v <= 10 : return 'red'
    elif  10 < v <= 20 : return 'yellow'
    elif  20 < v <= 60 : return 'green'

def plot(val):
    fig = go.Figure(go.Indicator(
        mode = "gauge+number+delta",
        value = val,
        delta = {'reference' : 40},
        domain = {'x': [0, 1], 'y': [0, 1]},
        gauge = {
        'axis' : {'range' : [None, 60]},
        'bar' :  {'color' : bar_color(val)},
        'steps' : [
                {'range': [0, 10], 'color': 'lightgrey'},
                {'range': [10,20], 'color': 'darkgrey'},
                {'range': [20,60], 'color': 'grey'}]
                }
    ))
    fig.write_html('gauge.html', auto_open=True)

plot(10)
