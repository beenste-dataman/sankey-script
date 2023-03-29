import pandas as pd
import plotly.graph_objects as go

# Replace this with your actual dataframe
data = {
    'step1': ['A', 'A', 'B', 'B'],
    'step2': ['C', 'D', 'C', 'D'],
    'step3': ['E', 'E', 'F', 'F'],
    'step4': ['G', 'H', 'G', 'H'],
    'value': [10, 15, 5, 20]
}

df = pd.DataFrame(data)

def create_sankey_dataframe(df):
    nodes = set()
    for col in df.columns[:-1]:
        nodes.update(df[col].unique())

    nodes = sorted(list(nodes))
    node_dict = {node: i for i, node in enumerate(nodes)}

    links = []
    for _, row in df.iterrows():
        for i in range(len(df.columns) - 2):
            source = node_dict[row[i]]
            target = node_dict[row[i + 1]]
            value = row[-1]

            links.append({
                'source': source,
                'target': target,
                'value': value
            })

    sankey_df = pd.DataFrame(links)
    return sankey_df, nodes

def create_sankey_plot(df):
    sankey_df, nodes = create_sankey_dataframe(df)

    fig = go.Figure(data=[go.Sankey(
        node=dict(pad=15, thickness=20, line=dict(color='black', width=0.5), label=nodes),
        link=dict(source=sankey_df['source'], target=sankey_df['target'], value=sankey_df['value'])
    )])

    fig.update_layout(title_text='Sankey Diagram', font_size=10)
    fig.show()

create_sankey_plot(df)
