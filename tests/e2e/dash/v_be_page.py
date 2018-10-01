# pylint: disable=global-statement
import dash
from dash.dependencies import Input, Output
import dash_html_components as html
import os
import pandas as pd
import sys

sys.path.append(
    os.path.abspath(
        os.path.join(os.path.dirname(sys.argv[0]), os.pardir, os.pardir, os.pardir)
    )
)
module_names = ["dash_table"]
modules = [__import__(module) for module in module_names]
dash_table = modules[0]

url = "https://github.com/plotly/datasets/raw/master/" "26k-consumer-complaints.csv"
df = pd.read_csv(url)
df = df.values

app = dash.Dash()
app.css.config.serve_locally = True
app.scripts.config.serve_locally = True

app.layout = html.Div(
    [
        html.Div(id="container", children="Hello World"),
        dash_table.Table(
            id="table",
            dataframe=[],
            virtualization="be",
            virtualization_settings={
                "displayed_pages": 1,
                "current_page": 0,
                "page_size": 250,
            },
            navigation="page",
            columns=[
                {"id": 0, "name": "Complaint ID"},
                {"id": 1, "name": "Product"},
                {"id": 2, "name": "Sub-product"},
                {"id": 3, "name": "Issue"},
                {"id": 4, "name": "Sub-issue"},
                {"id": 5, "name": "State"},
                {"id": 6, "name": "ZIP"},
                {"id": 7, "name": "code"},
                {"id": 8, "name": "Date received"},
                {"id": 9, "name": "Date sent to company"},
                {"id": 10, "name": "Company"},
                {"id": 11, "name": "Company response"},
                {"id": 12, "name": "Timely response?"},
                {"id": 13, "name": "Consumer disputed?"},
            ],
            n_fixed_columns=2,
            n_fixed_rows=1,
            row_selectable=True,
            row_deletable=True,
            sorting=True,
            editable=True,
        ),
    ]
)


@app.callback(Output("table", "dataframe"), [Input("table", "virtualization_settings")])
def updateDataframe(virtualization_settings):
    print(virtualization_settings)

    current_page = virtualization_settings["current_page"]
    displayed_pages = virtualization_settings["displayed_pages"]
    page_size = virtualization_settings["page_size"]

    start_index = current_page * page_size
    end_index = start_index + displayed_pages * page_size
    print(str(start_index) + "," + str(end_index))

    return df[start_index:end_index]


@app.callback(
    Output("container", "children"),
    [Input("table", "dataframe"), Input("table", "dataframe_previous")],
)
def findModifiedValue(dataframe, previous):
    modification = "None"

    if dataframe is None or previous is None:
        return modification

    for (y, row) in enumerate(dataframe):
        row_prev = previous[y]

        for (x, col) in enumerate(row):
            if col != row_prev[x]:
                modification = "[{}][{}] = {} -> {}".format(y, x, row_prev[x], col)

    return modification


if __name__ == "__main__":
    app.run_server(port=8081, debug=False)