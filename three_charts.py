import plotly
import plotly.graph_objs as go

import plotly
import plotly.graph_objs as go

import plotly.graph_objects as go

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


date_list = [x["date"] for x in line_data]

price_list = [y["stock_price_usd"] for y in line_data]



plotly.offline.plot({
    "data": [go.Scatter(x=date_list, y=price_list)],
    "layout": go.Layout(title="Stock Price Over Time")
}, auto_open=True)

print("----------------")
print("GENERATING LINE GRAPH...")


## PIE CHART ##

#pie_data = [
#    {"company": "Company X", "market_share": 0.55},
#    {"company": "Company Y", "market_share": 0.30},
#    {"company": "Company Z", "market_share": 0.15}
#]
#
#company_list = [x["company"] for x in pie_data]
#market_amount = [y["market_share"] for y in pie_data]
#
#
#trace = go.Pie(labels=company_list, values=market_amount)
#
#plotly.offline.plot([trace], filename="basic_pie_chart.html", auto_open=True)
#
#print("----------------")
#print("GENERATING PIE CHART...")
#print(pie_data) 


## Horizonal Bar ##

#bar_data = [
    #{"genre": "Thriller", "viewers": 123456},
    #{"genre": "Mystery", "viewers": 234567},
    #{"genre": "Sci-Fi", "viewers": 987654},
    #{"genre": "Fantasy", "viewers": 876543},
    #{"genre": "Documentary", "viewers": 283105},
    #{"genre": "Action", "viewers": 544099},
    #{"genre": "Romantic Comedy", "viewers": 121212}
##
#genre_list = [x["genre"] for x in bar_data]
#viewers_amount = [y["viewers"] for y in bar_data]
#
#
#fig = go.Figure(go.Bar(
#            x=genre_list,
#            y=viewers_amount,
#            orientation='h'))
#
#fig.show()
#
#print("----------------")
#print("GENERATING PIE CHART...")
#print(bar_data) 