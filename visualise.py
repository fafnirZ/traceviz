from dash import Dash, html
import dash_cytoscape as cyto
from extract import scanFile
from store import allNodeSignatures, allDirectedEdges

app = Dash(__name__)

# scanFile("inputs/samefile.py")
scanFile("inputs/myownExtractfile.py")

elems = []
for node in allNodeSignatures:
    print(node)
    elems.append({
        "data": {
            "id": node,
            "label": node
        },
        "classes": "node"
    })

for edges in allDirectedEdges:
    print(edges)
    src, dest = edges
    elems.append({
        'data': {
            'source': src,
            'target': dest
        },
        'classes': 'directed-edge'
    })

app.layout = html.Div([
    html.P("Dash Cytoscape:"),
    cyto.Cytoscape(
        id='cytoscape',
        elements=elems,
        layout={'name': 'breadthfirst', 'directed': True},
        style={'width': '1920px', 'height': '1080px'},
        stylesheet=[
            {
                'selector': '.directed-edge',
                'style': {
                    'target-arrow-color': 'red',
                    'target-arrow-shape': 'vee',
                    'line-color': 'red',
                    'curve-style': 'straight',
                }
            },
            {
                'selector': '.node',
                'style': {
                    'label': 'data(label)'
                }
            }
        ]
    )
])



app.run_server(debug=True)