import json, requests
import pandas as pd 

#setting constants

def updateTickets(qtoken, baseUrl, fileName):
    df = pd.read_csv(fileName)
    df = df.to_json('data.json')
    with open('data.json') as f:
        dataset = json.load(f)
            
    #setting file variables for each row
    ticketKey = dataset['ticketKey']
    areaLvlBuid = dataset['AREA_LVL_BUID']
    areaLvlDesc = dataset['AREA_LVL_DESC']
    baseUrl = baseUrl
    headers = {
    "x-api-token": qtoken,
    "Content-Type": 'application/json'
     }
    
    for x in range(0,len(ticketKey)):
        try:
            response = requests.post(baseUrl, headers=headers, json={
            "ticketKey": ticketKey['{0}'.format(x)],
            "AREA_LVL_BUID": areaLvlBuid['{0}'.format(x)],
            "AREA_LVL_DESC": areaLvlDesc['{0}'.format(x)]
            })
            print(response.text)
        except:
            print(f"an error occured for ticket {ticketKey[f'{x}']}")

def main():
    qtoken = "sZo1RySufQ4HmkfMvADetOIDglBHQt3Y8bA9pvRJ"
    baseUrl = "https://syd1.qualtrics.com/inbound-event/v1/events/JSON/triggers?contextId=OC_1CKhz1NJrDYqdNz&userId=UR_9KWWseklgT2sFXD&brandId=nablistens&triggerId=OC_1CKhz1NJrDYqdNz"
    fileName = "tickets.txt"
    updateTickets(qtoken, baseUrl, fileName)


if __name__== "__main__":
    main()
