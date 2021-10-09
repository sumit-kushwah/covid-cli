import requests

BASE_URL = 'https://covid-193.p.rapidapi.com/'
ENDPOINT = 'history'
API_KEY = '687dbfe6b7msh0e5814a43c930b7p11d7cdjsn493dc356cfb6'

def history(day, country):
    params = {
        'country': country,
        'day': day
    }

    headers = {
        'x-rapidapi-key': API_KEY,
    }

    response = requests.get(BASE_URL + ENDPOINT, params=params, headers=headers)

    result = dict()

    json_res = response.json()
    try:
        result['code'] = 200
        result["day"] = json_res["parameters"]["day"]
        result["country"] = json_res["parameters"]["country"]
        cases_list = dict()
        for res in json_res["response"]:
            cases_list["new"] = res["cases"]["new"]
            cases_list["active"] = res["cases"]["active"]
            cases_list["death"] = res["deaths"]["new"]
        result["cases"] = cases_list
    except:
        result['code'] = 400
    
    return result

