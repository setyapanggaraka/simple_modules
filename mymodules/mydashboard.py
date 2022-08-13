from dash import Dash, dash_table
import pandas as pd
from dash import Dash, dcc, html, Input, Output
import json

class dashboard():
    def __init__(self, tbName, cnxn):
        self.tbName = tbName
        self.cnxn = cnxn
    
    # select data to display on dashboard
    def selectData(self, colum1, colum2, colum3):
        self.colum1 = colum1
        self.colum2 = colum2
        self.colum3 = colum3 
        self.query = "SELECT * FROM {}".format(self.tbName)
        #self.query = "SELECT JSON_ARRAYAGG(JSON_OBJECT('name', {}, 'value', {}, 'detection', {})) FROM {}".format(self.colum1, self.colum2, self.colum3, self.tbName)
        self.result = pd.read_sql(self.query, self.cnxn)
        #self.resultJson = json.dumps(self.result.to_dict('records'), indent=4)
        #self.resultJson = json.dumps(self.result)
        #print(self.resultJson)
        self.app = Dash(__name__)
        self.app.layout =dash_table.DataTable(self.result.to_dict('records'),
                                         [{"name": i, "id": i}
                                          for i in self.result.columns])
        
        if __name__ == '__main__':
            self.app.run_server(debug=True)
        return self.app.run_server()
    
    # edit layout
    def layout(self):
        app.layout = html.Div([
            html.H6("Change the value in the text box to see callbacks in action!"),
            html.Div([
                "Input: ",
                dcc.Input(id='my-input', value='initial value', type='text')
                ]),
            html.Br(),
            html.Div(id='my-output'),

])
