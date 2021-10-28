import json, requests
import pandas as pd 


def updateTickets(qtoken, baseUrl, fileName):
    df = pd.read_csv(fileName)
    df = df.to_json('data.json')
    with open('data.json') as f:
        dataset = json.load(f)
            
    #setting variables from CSV file
    ticketKey = dataset['ticketKey']
    areaLvlBuid = dataset['AREA_LVL_BUID']
    areaLvlDesc = dataset['AREA_LVL_DESC']
    baseUrl = baseUrl
    headers = {
    "x-api-token": qtoken,
    "Content-Type": 'application/json'
     }
    
    #looping through each row in the CSV and making a POST request to the JSON event endpoint
    for x in range(0,len(ticketKey)):
        try:
            response = requests.post(baseUrl, headers=headers, json={
            "ticketKey": ticketKey[f'{x}']
            "AREA_LVL_BUID": areaLvlBuid[f'{x}']
            "AREA_LVL_DESC": areaLvlDesc[f'{x}']
            })
            print(response.text)
        except:
            print(f"an error occured for ticket {ticketKey[f'{x}']}")

def main():
    #setting constants
    qtoken = ""
    baseUrl = "https://syd1.qualtrics.com/inbound-event/v1/events/JSON/triggers?contextId=OC_1CKhz1NJrDYqdNz&userId=UR_9KWWseklgT2sFXD&brandId=nablistens&triggerId=OC_1CKhz1NJrDYqdNz"
    fileName = "tickets.txt"
    updateTickets(qtoken, baseUrl, fileName)


if __name__== "__main__":
    main()

