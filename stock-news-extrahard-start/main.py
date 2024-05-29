STOCK = "TSLA"
COMPANY_NAME = "Tesla Inc"

import requests

stock_end_point="http://www.alphavantage.co/query"
news_end_point="https://newsapi.org/v2/everything"

my_api_key="3KQR1GZSU95OTDV3"
stock_parameters={
    "function":"TIME_SERIES_DAILY",
    "symbol":STOCK,
    "apikey":my_api_key,
}

response=requests.get(url=stock_end_point,params=stock_parameters)
response.raise_for_status()
data=response.json()['Time Series (Daily)']

data_list=[value for (_,value) in data.items()]
for i in range(len(data_list)-1):
    yesterday_close=data_list[i]
    yesterday_closing_price=yesterday_close['4. close']
    
    today_open=data_list[i+1]
    today_opening_price=today_open['1. open']
    
    difference=abs(float(yesterday_closing_price)-float(today_opening_price))
    diff_percentage=(difference/float(yesterday_closing_price))*100
    
    if diff_percentage>=1:
        news_api="d3fad40abaf849f1a3903790613558f2"
        news_parameters={
           'apikey':news_api,
           'qInTitle':COMPANY_NAME,
        }
    
        
      
        response2=requests.get(url=news_end_point,params=news_parameters)
        response2.raise_for_status()
        data1=response2.json()
        articles=data1["articles"]
        three_articles=articles[:3]

        formatted_articles=[f"Heading {article['title']} \n Brief {article['description']}\n" for article in three_articles]

        from twilio.rest import Client
        account_sid="AC3560db8f4ed16b5aca32d5b3d05159e9"
        auth_token="62ee5fd3b745e24758a07ba9c31d68c7"

        for article in formatted_articles:
           client=Client(account_sid,auth_token)
           message=client.messages.create(\
             body=article,\
                from_="+18482807765",\
                   to="+917981192166")
    
    
    
        
        
        
        


