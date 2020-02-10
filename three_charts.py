import plotly
import plotly.graph_objs as go


## CHART 2 (LINE CHART) ##

line_data = [
   {"date": "2019-01-01", "stock_price_usd": 100.00},
   {"date": "2019-01-02", "stock_price_usd": 101.01},
   {"date": "2019-01-03", "stock_price_usd": 120.20},
   {"date": "2019-01-04", "stock_price_usd": 107.07},
   {"date": "2019-01-05", "stock_price_usd": 142.42},
   {"date": "2019-01-06", "stock_price_usd": 135.35},
   {"date": "2019-01-07", "stock_price_usd": 160.60},
   {"date": "2019-01-08", "stock_price_usd": 162.62},
]
#
#print("----------------")
#print("GENERATING LINE GRAPH...")
#print(line_data) # TODO: create a line graph based on the line_data

date_list = [x["date"] for x in line_data]

price_list = [y["stock_price_usd"] for y in line_data]



plotly.offline.plot({
    "data": [go.Scatter(x=date_list, y=price_list)],
    "layout": go.Layout(title="Stock Price Over Time")
}, auto_open=True)

print("----------------")
print("GENERATING LINE GRAPH...")


