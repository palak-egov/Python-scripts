import requests
import json
from datetime import datetime, timedelta

def iterate_data_and_set_date(data, start_date_str, end_date_str):
    api_endpoint = 'http://localhost:8087/national-dashboard/metric/_ingest'
    start_date = datetime.strptime(start_date_str, "%d-%m-%Y")
    end_date = datetime.strptime(end_date_str, "%d-%m-%Y")
    current_date = start_date
    while current_date <= end_date:
        print(current_date.strftime("%d-%m-%Y"))
        data["Data"][0]["date"] = current_date.strftime("%d-%m-%Y")
        current_date += timedelta(days=1)
        response = hit_api(api_endpoint, data)
        if response:
            print("Response:", response)

def read_json_file(file_path):
    try:
        with open(file_path, 'r') as file:
            data = json.load(file)
        return data
    except FileNotFoundError:
        print(f"File '{file_path}' not found.")
        return None
    except json.JSONDecodeError as e:
        print(f"Error decoding JSON: {e}")
        return None

def hit_api(endpoint, data):
    try:
        headers = {'Content-Type': 'application/json'}
        response = requests.post(endpoint, json=data, headers=headers)
        response.raise_for_status()  # Raise an exception for HTTP errors (4xx or 5xx)
        return response.json()
    except requests.exceptions.RequestException as e:
        print(f"Error: {e}")
        return None

if __name__ == "__main__":
    # reading data from json file
    file_path = 'nationalInfo.json'
    json_data = read_json_file(file_path)
    # if json_data:
    #     print("Data from JSON file:")
    #     print(json_data)

    national_dashboard_user = {"SUPERUUID":"efc090de-a1a2-4cbb-9ed2-dd1fb9196ae7","Punjab":"efc090de-a1a2-4cbb-9ed2-dd1fb9196ae7,7455774b-5a47-4d35-889b-9da698144973,0dab864d-e655-456f-a69c-b5c969e9b754","Karnataka":"98c6d961-5daf-4f53-a532-204229f2b8ad","Rajasthan":"4580803f-52e3-4495-911f-2895b65ed928","Goa":"492a8462-4fe3-460d-8b07-b22de30bc00c","Andhra Pradesh":"4275911e-f085-436b-b3df-735095250f01","Madhya Pradesh":"fd98e215-29fa-42a8-812f-49aefa3c3904","Telangana":"89ed69cf-c1c9-461d-9e3c-8cb04555fc49","Tamil Nadu":"63fce6cb-5af6-4fcb-94fa-2b7f0a796660","Chandigarh":"c499b45b-7d65-418f-b003-5ce5db2220d2","Chhattisgarh":"33dc5944-6bd3-46e2-8e90-db32270c9977","Maharashtra":"49ec839a-35be-4347-b166-12cee02cd885","Uttarakhand":"cb343459-62ba-4fa0-9179-bd58ac635ef2","Jharkhand":"3679e706-9893-48f9-b1d8-3b27946a5bd6","Tripura":"2d934def-d9ee-4f79-a2c6-16eabe0e600a"}
    national_dashboard_tenantId = {"SUPERUUID":"pg","Punjab":"pb","Karnataka":"ka","Rajasthan":"rj","Goa":"goa","Andhra Pradesh":"ap","Madhya Pradesh":"mp","Telangana":"tl","Tamil Nadu":"tn","Chandigarh":"chd","Chhattisgarh":"ch","Maharashtra":"mh","Uttarakhand":"uk","Jharkhand":"jh","Tripura":"tr"}

    #iterating in the fetched data
    if json_data:
        national_info = json_data.get("nationalInfo", [])
        for info in national_info:
            state_code = info.get("stateCode")
            code = info.get("code")
            if state_code and code:
                print("State Code:", state_code)
                print("Code:", code)
                print(national_dashboard_user[state_code].split(',')[0])
                print(national_dashboard_tenantId[state_code])
                print()  
                start_date = "01-04-2024"
                end_date = "15-05-2024"

                data = {
                    "RequestInfo": {
                    "apiId": "asset-services",
                    "ver": None,
                    "ts": None,
                    "action": None,
                    "did": None,
                    "key": None,
                    "msgId": "search with from and to values",
                    "authToken": "7112c6a3-41d4-42d0-9ae9-7d2ec08d1a4f",
                    "userInfo": {"id":9709,"uuid": national_dashboard_user[state_code].split(',')[0],"userName":"NDSS1",
                    "name":"State Admin","mobileNumber":"9901888372","emailId":None,"locale":None,"type":"EMPLOYEE","roles":[{"name":"National Dashboard Admin","code":"NATADMIN","tenantId":national_dashboard_tenantId[state_code]},{"name":"Basic employee roles","code":"COMMON_EMPLOYEE","tenantId":national_dashboard_tenantId[state_code]}],"active":True,"tenantId":national_dashboard_tenantId[state_code],"permanentCity":None}
                    },
                    "Data": [ 
                        {
                            "date": "05-01-2022",
                            "module": "OBPS",
                            "ward": "Ajit Nagar",
                            "ulb": code,
                            "region": code,
                            "state": state_code,
                            "metrics": {
                                "ocPlansScrutinized": 120,
                                "plansScrutinized": 540,
                                "ocSubmitted": 50,
                                "applicationsSubmitted": 50,
                                "ocIssued": 19,
                                "landAreaAppliedInSystemForBPA": 23442,
                                "averageDaysToIssuePermit": 10,
                                "averageDaysToIssueOC": 8,
                                "todaysClosedApplicationsOC":10 ,
                                "todaysCompletedApplicationsWithinSLAOC":5 ,
                                "todaysClosedApplicationsPermit": 20,
                                "todaysCompletedApplicationsWithinSLAPermit":10,
                                "slaComplianceOC": 20,
                                "slaCompliancePermit": 40,
                                "applicationsWithDeviation": 20,
                                "averageDeviation": 10,
                                "ocWithDeviation": 30,
                                "todaysCollection": [
                                    {
                                        "groupBy": "paymentMode",
                                        "buckets": [
                                            {
                                                "name": "UPI",
                                                "value": 10000
                                            },
                                            {
                                                "name": "DEBIT.CARD",
                                                "value": 15000
                                            },
                                            {
                                                "name": "CREDIT.CARD",
                                                "value": 8500
                                            }
                                        ]
                                    }
                                ],
                                "permitsIssued": [
                                    {
                                        "groupBy": "riskType",
                                        "buckets": [
                                            {
                                                "name": "LOW",
                                                "value": 150
                                            },
                                            {
                                                "name": "MEDIUM",
                                                "value": 300
                                            },
                                            {
                                                "name": "HIGH",
                                                "value": 600
                                            }
                                        ]
                                    } ,
                                    {
                                        "groupBy": "occupancyType",
                                        "buckets": [
                                            {
                                                "name": "RESIDENTIAL",
                                                "value": 150
                                            },
                                            {
                                                "name": "INSTITUTIONAL",
                                                "value": 180
                                            }
                                        ]
                                    },
                                    {
                                        "groupBy": "subOccupancyType",
                                        "buckets": [
                                            {
                                                "name": "RESIDENTIAL.INDIVIDUAL",
                                                "value": 50
                                            },
                                            {
                                                "name": "RESIDENTIAL.SHARED",
                                                "value": 20
                                            },
                                            {
                                                "name": "INSITUTIONAL.SHARED",
                                                "value": 120
                                            }
                                        ]
                                    }
                                ]
                            }
                        }
                    ]
                }
                iterate_data_and_set_date(data, start_date, end_date)

    
