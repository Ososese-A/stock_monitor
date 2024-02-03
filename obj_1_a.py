import json
import requests

port = {
    "Portfolios": [
        {
            "Portfolio_1": [
                {
                    "name" : "",
                    "symbol": "AVGO"
                },
                {
                    "name" : "",
                    "symbol": "AMZN"
                },
                {
                    "name" : "",
                    "symbol": "ORCL"
                },
                {
                    "name" : "",
                    "symbol": "PARA"
                },
                {
                    "name" : "",
                    "symbol": "DBX"
                },
                {
                    "name" : "",
                    "symbol": "TSLA"
                }
            ],
            "Portfolio_2": [
                {
                    "name" : "",
                    "symbol": "COKE"
                },
                {
                    "name" : "",
                    "symbol": "WMT"
                },
                {
                    "name" : "",
                    "symbol": "GE"
                },
                {
                    "name" : "",
                    "symbol": "WBD"
                },
                {
                    "name" : "",
                    "symbol": "INTC"
                },
                {
                    "name" : "",
                    "symbol": "V"
                },
            ],
            "Portfolio_3": [
                {
                    "name" : "",
                    "symbol": "ADBE"
                },
                {
                    "name" : "",
                    "symbol": "GOOGL"
                },
                {
                    "name" : "",
                    "symbol": "CROX"
                },
                {
                    "name" : "",
                    "symbol": "DELL"
                },
                {
                    "name" : "",
                    "symbol": "MAT"
                },
                {
                    "name" : "",
                    "symbol": "NOK"
                }
            ],
            "Portfolio_4": [
                {
                    "name" : "",
                    "symbol": "NVDA"
                },
                {
                    "name" : "",
                    "symbol": "AAPL"
                },
                {
                    "name" : "",
                    "symbol": "TGT"
                },
                {
                    "name" : "",
                    "symbol": "MNST"
                },
                {
                    "name" : "",
                    "symbol": "HAS"
                },
                {
                    "name" : "",
                    "symbol": "EBAY"
                }
            ],
            "Portfolio_5": [
                {
                    "name" : "",
                    "symbol": "NFLX"
                },
                {
                    "name" : "",
                    "symbol": "PAYC"
                },
                {
                    "name" : "",
                    "symbol": "NKE"
                },
                {
                    "name" : "",
                    "symbol": "MDLZ"
                },
                {
                    "name" : "",
                    "symbol": "HPE"
                },
                {
                    "name" : "",
                    "symbol": "WEN"
                },
                {
                    "name" : "",
                    "symbol": "MD"
                }
            ],
            "Portfolio_6": [
                {
                    "name" : "",
                    "symbol": "LULU"
                },
                {
                    "name" : "",
                    "symbol": "HSY"
                },
                {
                    "name" : "",
                    "symbol": "SONY"
                },
                {
                    "name" : "",
                    "symbol": "SKX"
                },
                {
                    "name" : "",
                    "symbol": "UA"
                },
                {
                    "name" : "",
                    "symbol": "GM"
                }
            ],
            "Portfolio_7": [
                {
                    "name" : "",
                    "symbol": "META"
                },
                {
                    "name" : "",
                    "symbol": "MSFT"
                },
                {
                    "name" : "",
                    "symbol": "DIS"
                },
                {
                    "name" : "",
                    "symbol": "K"
                },
                {
                    "name" : "",
                    "symbol": "U"
                },
                {
                    "name" : "",
                    "symbol": "VSAT"
                }
            ],
            "Portfolio_8": [
                {
                    "name" : "",
                    "symbol": "MCD"
                },
                {
                    "name" : "",
                    "symbol": "DPZ"
                },
                {
                    "name" : "",
                    "symbol": "CSCO"
                },
                {
                    "name" : "",
                    "symbol": "PYPL"
                },
                {
                    "name" : "",
                    "symbol": "JAKK"
                },
                {
                    "name" : "",
                    "symbol": "WKHS"
                }
            ],
        }
    ]
}

def avgo():
    from for_date_time import hr_6
    name =port["Portfolios"][0]["Portfolio_1"][0]["symbol"]

    url= f"https://realstonks.p.rapidapi.com/{name}"
    
    headers = {
    	"X-RapidAPI-Key": "5a15296613msh2a9148c995ff004p11e8ebjsna89f2dd61580",
    	"X-RapidAPI-Host": "realstonks.p.rapidapi.com"
    }
    
    res = requests.get(url, headers=headers)
    result = json.loads(res.text)
    
    price = result['price']
    
    chg = result['change_percentage']
    
    one_stock_res = {"name":name,"time":hr_6(),"price":price,"percentage_change":chg}

    return one_stock_res

def amzn():
    from for_date_time import hr_6
    name =port["Portfolios"][0]["Portfolio_1"][1]["symbol"]

    url= f"https://realstonks.p.rapidapi.com/{name}"
    
    headers = {
    	"X-RapidAPI-Key": "5a15296613msh2a9148c995ff004p11e8ebjsna89f2dd61580",
    	"X-RapidAPI-Host": "realstonks.p.rapidapi.com"
    }
    
    res = requests.get(url, headers=headers)
    result = json.loads(res.text)
    
    price = result['price']
    
    chg = result['change_percentage']
    
    one_stock_res = {"name":name,"time":hr_6(),"price":price,"percentage_change":chg}
    return one_stock_res

def orcl():
    from for_date_time import hr_6
    name =port["Portfolios"][0]["Portfolio_1"][2]["symbol"]

    url= f"https://realstonks.p.rapidapi.com/{name}"
    
    headers = {
    	"X-RapidAPI-Key": "5a15296613msh2a9148c995ff004p11e8ebjsna89f2dd61580",
    	"X-RapidAPI-Host": "realstonks.p.rapidapi.com"
    }
    
    res = requests.get(url, headers=headers)
    result = json.loads(res.text)
    
    price = result['price']
    
    chg = result['change_percentage']
    
    one_stock_res = {"name":name,"time":hr_6(),"price":price,"percentage_change":chg}
    return one_stock_res

def para():
    from for_date_time import hr_6
    name =port["Portfolios"][0]["Portfolio_1"][3]["symbol"]

    url= f"https://realstonks.p.rapidapi.com/{name}"
    
    headers = {
    	"X-RapidAPI-Key": "5a15296613msh2a9148c995ff004p11e8ebjsna89f2dd61580",
    	"X-RapidAPI-Host": "realstonks.p.rapidapi.com"
    }
    
    res = requests.get(url, headers=headers)
    result = json.loads(res.text)
    
    price = result['price']
    
    chg = result['change_percentage']
    
    one_stock_res = {"name":name,"time":hr_6(),"price":price,"percentage_change":chg}
    return one_stock_res

def dbx():
    from for_date_time import hr_6
    name =port["Portfolios"][0]["Portfolio_1"][4]["symbol"]

    url= f"https://realstonks.p.rapidapi.com/{name}"
    
    headers = {
    	"X-RapidAPI-Key": "5a15296613msh2a9148c995ff004p11e8ebjsna89f2dd61580",
    	"X-RapidAPI-Host": "realstonks.p.rapidapi.com"
    }
    
    res = requests.get(url, headers=headers)
    result = json.loads(res.text)
    
    price = result['price']
    
    chg = result['change_percentage']
    
    one_stock_res = {"name":name,"time":hr_6(),"price":price,"percentage_change":chg}
    return one_stock_res

def tsla():
    from for_date_time import hr_6
    name =port["Portfolios"][0]["Portfolio_1"][5]["symbol"]

    url= f"https://realstonks.p.rapidapi.com/{name}"
    
    headers = {
    	"X-RapidAPI-Key": "5a15296613msh2a9148c995ff004p11e8ebjsna89f2dd61580",
    	"X-RapidAPI-Host": "realstonks.p.rapidapi.com"
    }
    
    res = requests.get(url, headers=headers)
    result = json.loads(res.text)
    
    price = result['price']
    
    chg = result['change_percentage']
    
    one_stock_res = {"name":name,"time":hr_6(),"price":price,"percentage_change":chg}
    return one_stock_res


def port_1():
    from for_date_time import date
    #remeber to convert the items variable to a string before using it 
    items = {"port_1":[avgo(),amzn(),orcl(),para(),dbx(),tsla()]}
    port = open(f"port_1_{date()}.json", "w")
    port.write(json.dumps(items,indent=2))
    port.close()
    
    # #open and read the file after the appending/writing
    # with open(f"port_1_{date()}.json", "r") as file:
    #     json_item = json.loads(file.read())
    # print(json_item)
    # print(items)
    return items


def coke():
    from for_date_time import hr_6
    name =port["Portfolios"][0]["Portfolio_2"][0]["symbol"]

    url= f"https://realstonks.p.rapidapi.com/{name}"
    
    headers = {
    	"X-RapidAPI-Key": "5a15296613msh2a9148c995ff004p11e8ebjsna89f2dd61580",
    	"X-RapidAPI-Host": "realstonks.p.rapidapi.com"
    }
    
    res = requests.get(url, headers=headers)
    result = json.loads(res.text)
    
    price = result['price']
    
    chg = result['change_percentage']
    
    one_stock_res = {"name":name,"time":hr_6(),"price":price,"percentage_change":chg}
    return one_stock_res

def wmt():
    from for_date_time import hr_6
    name =port["Portfolios"][0]["Portfolio_2"][1]["symbol"]

    url= f"https://realstonks.p.rapidapi.com/{name}"
    
    headers = {
    	"X-RapidAPI-Key": "5a15296613msh2a9148c995ff004p11e8ebjsna89f2dd61580",
    	"X-RapidAPI-Host": "realstonks.p.rapidapi.com"
    }
    
    res = requests.get(url, headers=headers)
    result = json.loads(res.text)
    
    price = result['price']
    
    chg = result['change_percentage']
    
    one_stock_res = {"name":name,"time":hr_6(),"price":price,"percentage_change":chg}
    return one_stock_res

def ge():
    from for_date_time import hr_6
    name =port["Portfolios"][0]["Portfolio_2"][2]["symbol"]

    url= f"https://realstonks.p.rapidapi.com/{name}"
    
    headers = {
    	"X-RapidAPI-Key": "5a15296613msh2a9148c995ff004p11e8ebjsna89f2dd61580",
    	"X-RapidAPI-Host": "realstonks.p.rapidapi.com"
    }
    
    res = requests.get(url, headers=headers)
    result = json.loads(res.text)
    
    price = result['price']
    
    chg = result['change_percentage']
    
    one_stock_res = {"name":name,"time":hr_6(),"price":price,"percentage_change":chg}
    return one_stock_res

def wbd():
    from for_date_time import hr_6
    name =port["Portfolios"][0]["Portfolio_2"][3]["symbol"]

    url= f"https://realstonks.p.rapidapi.com/{name}"
    
    headers = {
    	"X-RapidAPI-Key": "5a15296613msh2a9148c995ff004p11e8ebjsna89f2dd61580",
    	"X-RapidAPI-Host": "realstonks.p.rapidapi.com"
    }
    
    res = requests.get(url, headers=headers)
    result = json.loads(res.text)
    
    price = result['price']
    
    chg = result['change_percentage']
    
    one_stock_res = {"name":name,"time":hr_6(),"price":price,"percentage_change":chg}
    return one_stock_res

def intc():
    from for_date_time import hr_6
    name =port["Portfolios"][0]["Portfolio_2"][4]["symbol"]

    url= f"https://realstonks.p.rapidapi.com/{name}"
    
    headers = {
    	"X-RapidAPI-Key": "5a15296613msh2a9148c995ff004p11e8ebjsna89f2dd61580",
    	"X-RapidAPI-Host": "realstonks.p.rapidapi.com"
    }
    
    res = requests.get(url, headers=headers)
    result = json.loads(res.text)
    
    price = result['price']
    
    chg = result['change_percentage']
    
    one_stock_res = {"name":name,"time":hr_6(),"price":price,"percentage_change":chg}
    return one_stock_res

def v():
    from for_date_time import hr_6
    name =port["Portfolios"][0]["Portfolio_2"][5]["symbol"]

    url= f"https://realstonks.p.rapidapi.com/{name}"
    
    headers = {
    	"X-RapidAPI-Key": "5a15296613msh2a9148c995ff004p11e8ebjsna89f2dd61580",
    	"X-RapidAPI-Host": "realstonks.p.rapidapi.com"
    }
    
    res = requests.get(url, headers=headers)
    result = json.loads(res.text)
    
    price = result['price']
    
    chg = result['change_percentage']
    
    one_stock_res = {"name":name,"time":hr_6(),"price":price,"percentage_change":chg}
    return one_stock_res


def port_2():
    from for_date_time import date
    #remeber to convert the items variable to a string before using it 
    items = {"port_2":[coke(),wmt(),ge(),wbd(),intc(),v()]}
    port = open(f"port_2_{date()}.json", "w")
    port.write(json.dumps(items,indent=2))
    port.close()
    return items


def adbe():
    from for_date_time import hr_6
    name =port["Portfolios"][0]["Portfolio_3"][0]["symbol"]

    url= f"https://realstonks.p.rapidapi.com/{name}"
    
    headers = {
    	"X-RapidAPI-Key": "5a15296613msh2a9148c995ff004p11e8ebjsna89f2dd61580",
    	"X-RapidAPI-Host": "realstonks.p.rapidapi.com"
    }
    
    res = requests.get(url, headers=headers)
    result = json.loads(res.text)
    
    price = result['price']
    
    chg = result['change_percentage']
    
    one_stock_res = {"name":name,"time":hr_6(),"price":price,"percentage_change":chg}
    return one_stock_res

def googl():
    from for_date_time import hr_6
    name =port["Portfolios"][0]["Portfolio_3"][1]["symbol"]

    url= f"https://realstonks.p.rapidapi.com/{name}"
    
    headers = {
    	"X-RapidAPI-Key": "5a15296613msh2a9148c995ff004p11e8ebjsna89f2dd61580",
    	"X-RapidAPI-Host": "realstonks.p.rapidapi.com"
    }
    
    res = requests.get(url, headers=headers)
    result = json.loads(res.text)
    
    price = result['price']
    
    chg = result['change_percentage']
    
    one_stock_res = {"name":name,"time":hr_6(),"price":price,"percentage_change":chg}
    return one_stock_res

def crox():
    from for_date_time import hr_6
    name =port["Portfolios"][0]["Portfolio_3"][2]["symbol"]

    url= f"https://realstonks.p.rapidapi.com/{name}"
    
    headers = {
    	"X-RapidAPI-Key": "5a15296613msh2a9148c995ff004p11e8ebjsna89f2dd61580",
    	"X-RapidAPI-Host": "realstonks.p.rapidapi.com"
    }
    
    res = requests.get(url, headers=headers)
    result = json.loads(res.text)
    
    price = result['price']
    
    chg = result['change_percentage']
    
    one_stock_res = {"name":name,"time":hr_6(),"price":price,"percentage_change":chg}
    return one_stock_res

def dell():
    from for_date_time import hr_6
    name =port["Portfolios"][0]["Portfolio_3"][3]["symbol"]

    url= f"https://realstonks.p.rapidapi.com/{name}"
    
    headers = {
    	"X-RapidAPI-Key": "5a15296613msh2a9148c995ff004p11e8ebjsna89f2dd61580",
    	"X-RapidAPI-Host": "realstonks.p.rapidapi.com"
    }
    
    res = requests.get(url, headers=headers)
    result = json.loads(res.text)
    
    price = result['price']
    
    chg = result['change_percentage']
    
    one_stock_res = {"name":name,"time":hr_6(),"price":price,"percentage_change":chg}
    return one_stock_res

def mat():
    from for_date_time import hr_6
    name =port["Portfolios"][0]["Portfolio_3"][4]["symbol"]

    url= f"https://realstonks.p.rapidapi.com/{name}"
    
    headers = {
    	"X-RapidAPI-Key": "5a15296613msh2a9148c995ff004p11e8ebjsna89f2dd61580",
    	"X-RapidAPI-Host": "realstonks.p.rapidapi.com"
    }
    
    res = requests.get(url, headers=headers)
    result = json.loads(res.text)
    
    price = result['price']
    
    chg = result['change_percentage']
    
    one_stock_res = {"name":name,"time":hr_6(),"price":price,"percentage_change":chg}
    return one_stock_res

def nok():
    from for_date_time import hr_6
    name =port["Portfolios"][0]["Portfolio_3"][5]["symbol"]

    url= f"https://realstonks.p.rapidapi.com/{name}"
    
    headers = {
    	"X-RapidAPI-Key": "5a15296613msh2a9148c995ff004p11e8ebjsna89f2dd61580",
    	"X-RapidAPI-Host": "realstonks.p.rapidapi.com"
    }
    
    res = requests.get(url, headers=headers)
    result = json.loads(res.text)
    
    price = result['price']
    
    chg = result['change_percentage']
    
    one_stock_res = {"name":name,"time":hr_6(),"price":price,"percentage_change":chg}
    return one_stock_res


def port_3():
    from for_date_time import date
    #remeber to convert the items variable to a string before using it 
    items = {"port_3":[adbe(),googl(),crox(),dell(),mat(),nok()]}
    port = open(f"port_3_{date()}.json", "w")
    port.write(json.dumps(items,indent=2))
    port.close()
    return items


def nvda():
    from for_date_time import hr_6
    name =port["Portfolios"][0]["Portfolio_4"][0]["symbol"]

    url= f"https://realstonks.p.rapidapi.com/{name}"
    
    headers = {
    	"X-RapidAPI-Key": "5a15296613msh2a9148c995ff004p11e8ebjsna89f2dd61580",
    	"X-RapidAPI-Host": "realstonks.p.rapidapi.com"
    }
    
    res = requests.get(url, headers=headers)
    result = json.loads(res.text)
    
    price = result['price']
    
    chg = result['change_percentage']
    
    one_stock_res = {"name":name,"time":hr_6(),"price":price,"percentage_change":chg}
    return one_stock_res

def aapl():
    from for_date_time import hr_6
    name =port["Portfolios"][0]["Portfolio_4"][1]["symbol"]

    url= f"https://realstonks.p.rapidapi.com/{name}"
    
    headers = {
    	"X-RapidAPI-Key": "5a15296613msh2a9148c995ff004p11e8ebjsna89f2dd61580",
    	"X-RapidAPI-Host": "realstonks.p.rapidapi.com"
    }
    
    res = requests.get(url, headers=headers)
    result = json.loads(res.text)
    
    price = result['price']
    
    chg = result['change_percentage']
    
    one_stock_res = {"name":name,"time":hr_6(),"price":price,"percentage_change":chg}
    return one_stock_res

def tgt():
    from for_date_time import hr_6
    name =port["Portfolios"][0]["Portfolio_4"][2]["symbol"]

    url= f"https://realstonks.p.rapidapi.com/{name}"
    
    headers = {
    	"X-RapidAPI-Key": "5a15296613msh2a9148c995ff004p11e8ebjsna89f2dd61580",
    	"X-RapidAPI-Host": "realstonks.p.rapidapi.com"
    }
    
    res = requests.get(url, headers=headers)
    result = json.loads(res.text)
    
    price = result['price']
    
    chg = result['change_percentage']
    
    one_stock_res = {"name":name,"time":hr_6(),"price":price,"percentage_change":chg}
    return one_stock_res

def mnst():
    from for_date_time import hr_6
    name =port["Portfolios"][0]["Portfolio_4"][3]["symbol"]

    url= f"https://realstonks.p.rapidapi.com/{name}"
    
    headers = {
    	"X-RapidAPI-Key": "5a15296613msh2a9148c995ff004p11e8ebjsna89f2dd61580",
    	"X-RapidAPI-Host": "realstonks.p.rapidapi.com"
    }
    
    res = requests.get(url, headers=headers)
    result = json.loads(res.text)
    
    price = result['price']
    
    chg = result['change_percentage']
    
    one_stock_res = {"name":name,"time":hr_6(),"price":price,"percentage_change":chg}
    return one_stock_res

def has():
    from for_date_time import hr_6
    name =port["Portfolios"][0]["Portfolio_4"][4]["symbol"]

    url= f"https://realstonks.p.rapidapi.com/{name}"
    
    headers = {
    	"X-RapidAPI-Key": "5a15296613msh2a9148c995ff004p11e8ebjsna89f2dd61580",
    	"X-RapidAPI-Host": "realstonks.p.rapidapi.com"
    }
    
    res = requests.get(url, headers=headers)
    result = json.loads(res.text)
    
    price = result['price']
    
    chg = result['change_percentage']
    
    one_stock_res = {"name":name,"time":hr_6(),"price":price,"percentage_change":chg}
    return one_stock_res

def ebay():
    from for_date_time import hr_6
    name =port["Portfolios"][0]["Portfolio_4"][5]["symbol"]

    url= f"https://realstonks.p.rapidapi.com/{name}"
    
    headers = {
    	"X-RapidAPI-Key": "5a15296613msh2a9148c995ff004p11e8ebjsna89f2dd61580",
    	"X-RapidAPI-Host": "realstonks.p.rapidapi.com"
    }
    
    res = requests.get(url, headers=headers)
    result = json.loads(res.text)
    
    price = result['price']
    
    chg = result['change_percentage']
    
    one_stock_res = {"name":name,"time":hr_6(),"price":price,"percentage_change":chg}
    return one_stock_res


def port_4():
    from for_date_time import date
    #remeber to convert the items variable to a string before using it 
    items = {"port_4":[nvda(),aapl(),tgt(),mnst(),has(),ebay()]}
    port = open(f"port_4_{date()}.json", "w")
    port.write(json.dumps(items,indent=2))
    port.close()
    return items


def nflx():
    from for_date_time import hr_6
    name =port["Portfolios"][0]["Portfolio_5"][0]["symbol"]

    url= f"https://realstonks.p.rapidapi.com/{name}"
    
    headers = {
    	"X-RapidAPI-Key": "5a15296613msh2a9148c995ff004p11e8ebjsna89f2dd61580",
    	"X-RapidAPI-Host": "realstonks.p.rapidapi.com"
    }
    
    res = requests.get(url, headers=headers)
    result = json.loads(res.text)
    
    price = result['price']
    
    chg = result['change_percentage']
    
    one_stock_res = {"name":name,"time":hr_6(),"price":price,"percentage_change":chg}
    return one_stock_res

def payc():
    from for_date_time import hr_6
    name =port["Portfolios"][0]["Portfolio_5"][1]["symbol"]

    url= f"https://realstonks.p.rapidapi.com/{name}"
    
    headers = {
    	"X-RapidAPI-Key": "5a15296613msh2a9148c995ff004p11e8ebjsna89f2dd61580",
    	"X-RapidAPI-Host": "realstonks.p.rapidapi.com"
    }
    
    res = requests.get(url, headers=headers)
    result = json.loads(res.text)
    
    price = result['price']
    
    chg = result['change_percentage']
    
    one_stock_res = {"name":name,"time":hr_6(),"price":price,"percentage_change":chg}
    return one_stock_res

def nke():
    from for_date_time import hr_6
    name =port["Portfolios"][0]["Portfolio_5"][2]["symbol"]

    url= f"https://realstonks.p.rapidapi.com/{name}"
    
    headers = {
    	"X-RapidAPI-Key": "5a15296613msh2a9148c995ff004p11e8ebjsna89f2dd61580",
    	"X-RapidAPI-Host": "realstonks.p.rapidapi.com"
    }
    
    res = requests.get(url, headers=headers)
    result = json.loads(res.text)
    
    price = result['price']
    
    chg = result['change_percentage']
    
    one_stock_res = {"name":name,"time":hr_6(),"price":price,"percentage_change":chg}
    return one_stock_res

def mdlz():
    from for_date_time import hr_6
    name =port["Portfolios"][0]["Portfolio_5"][3]["symbol"]

    url= f"https://realstonks.p.rapidapi.com/{name}"
    
    headers = {
    	"X-RapidAPI-Key": "5a15296613msh2a9148c995ff004p11e8ebjsna89f2dd61580",
    	"X-RapidAPI-Host": "realstonks.p.rapidapi.com"
    }
    
    res = requests.get(url, headers=headers)
    result = json.loads(res.text)
    
    price = result['price']
    
    chg = result['change_percentage']
    
    one_stock_res = {"name":name,"time":hr_6(),"price":price,"percentage_change":chg}
    return one_stock_res

def hpe():
    from for_date_time import hr_6
    name =port["Portfolios"][0]["Portfolio_5"][4]["symbol"]

    url= f"https://realstonks.p.rapidapi.com/{name}"
    
    headers = {
    	"X-RapidAPI-Key": "5a15296613msh2a9148c995ff004p11e8ebjsna89f2dd61580",
    	"X-RapidAPI-Host": "realstonks.p.rapidapi.com"
    }
    
    res = requests.get(url, headers=headers)
    result = json.loads(res.text)
    
    price = result['price']
    
    chg = result['change_percentage']
    
    one_stock_res = {"name":name,"time":hr_6(),"price":price,"percentage_change":chg}
    return one_stock_res

def wen():
    from for_date_time import hr_6
    name =port["Portfolios"][0]["Portfolio_5"][5]["symbol"]

    url= f"https://realstonks.p.rapidapi.com/{name}"
    
    headers = {
    	"X-RapidAPI-Key": "5a15296613msh2a9148c995ff004p11e8ebjsna89f2dd61580",
    	"X-RapidAPI-Host": "realstonks.p.rapidapi.com"
    }
    
    res = requests.get(url, headers=headers)
    result = json.loads(res.text)
    
    price = result['price']
    
    chg = result['change_percentage']
    
    one_stock_res = {"name":name,"time":hr_6(),"price":price,"percentage_change":chg}
    return one_stock_res

def md():
    from for_date_time import hr_6
    name =port["Portfolios"][0]["Portfolio_5"][6]["symbol"]

    url= f"https://realstonks.p.rapidapi.com/{name}"
    
    headers = {
    	"X-RapidAPI-Key": "5a15296613msh2a9148c995ff004p11e8ebjsna89f2dd61580",
    	"X-RapidAPI-Host": "realstonks.p.rapidapi.com"
    }
    
    res = requests.get(url, headers=headers)
    result = json.loads(res.text)
    
    price = result['price']
    
    chg = result['change_percentage']
    
    one_stock_res = {"name":name,"time":hr_6(),"price":price,"percentage_change":chg}
    return one_stock_res


def port_5():
    from for_date_time import date
    #remeber to convert the items variable to a string before using it 
    items = {"port_5":[nflx(),payc(),nke(),mdlz(),hpe(),wen(),md()]}
    port = open(f"port_5_{date()}.json", "w")
    port.write(json.dumps(items,indent=2))
    port.close()
    return items


def lulu():
    from for_date_time import hr_6
    name =port["Portfolios"][0]["Portfolio_6"][0]["symbol"]

    url= f"https://realstonks.p.rapidapi.com/{name}"
    
    headers = {
    	"X-RapidAPI-Key": "5a15296613msh2a9148c995ff004p11e8ebjsna89f2dd61580",
    	"X-RapidAPI-Host": "realstonks.p.rapidapi.com"
    }
    
    res = requests.get(url, headers=headers)
    result = json.loads(res.text)
    
    price = result['price']
    
    chg = result['change_percentage']
    
    one_stock_res = {"name":name,"time":hr_6(),"price":price,"percentage_change":chg}
    return one_stock_res

def hsy():
    from for_date_time import hr_6
    name =port["Portfolios"][0]["Portfolio_6"][1]["symbol"]

    url= f"https://realstonks.p.rapidapi.com/{name}"
    
    headers = {
    	"X-RapidAPI-Key": "5a15296613msh2a9148c995ff004p11e8ebjsna89f2dd61580",
    	"X-RapidAPI-Host": "realstonks.p.rapidapi.com"
    }
    
    res = requests.get(url, headers=headers)
    result = json.loads(res.text)
    
    price = result['price']
    
    chg = result['change_percentage']
    
    one_stock_res = {"name":name,"time":hr_6(),"price":price,"percentage_change":chg}
    return one_stock_res

def sony():
    from for_date_time import hr_6
    name =port["Portfolios"][0]["Portfolio_6"][2]["symbol"]

    url= f"https://realstonks.p.rapidapi.com/{name}"
    
    headers = {
    	"X-RapidAPI-Key": "5a15296613msh2a9148c995ff004p11e8ebjsna89f2dd61580",
    	"X-RapidAPI-Host": "realstonks.p.rapidapi.com"
    }
    
    res = requests.get(url, headers=headers)
    result = json.loads(res.text)
    
    price = result['price']
    
    chg = result['change_percentage']
    
    one_stock_res = {"name":name,"time":hr_6(),"price":price,"percentage_change":chg}
    return one_stock_res

def skx():
    from for_date_time import hr_6
    name =port["Portfolios"][0]["Portfolio_7"][3]["symbol"]

    url= f"https://realstonks.p.rapidapi.com/{name}"
    
    headers = {
    	"X-RapidAPI-Key": "5a15296613msh2a9148c995ff004p11e8ebjsna89f2dd61580",
    	"X-RapidAPI-Host": "realstonks.p.rapidapi.com"
    }
    
    res = requests.get(url, headers=headers)
    result = json.loads(res.text)
    
    price = result['price']
    
    chg = result['change_percentage']
    
    one_stock_res = {"name":name,"time":hr_6(),"price":price,"percentage_change":chg}
    return one_stock_res

def ua():
    from for_date_time import hr_6
    name =port["Portfolios"][0]["Portfolio_6"][4]["symbol"]

    url= f"https://realstonks.p.rapidapi.com/{name}"
    
    headers = {
    	"X-RapidAPI-Key": "5a15296613msh2a9148c995ff004p11e8ebjsna89f2dd61580",
    	"X-RapidAPI-Host": "realstonks.p.rapidapi.com"
    }
    
    res = requests.get(url, headers=headers)
    result = json.loads(res.text)
    
    price = result['price']
    
    chg = result['change_percentage']
    
    one_stock_res = {"name":name,"time":hr_6(),"price":price,"percentage_change":chg}
    return one_stock_res

def gm():
    from for_date_time import hr_6
    name =port["Portfolios"][0]["Portfolio_6"][5]["symbol"]

    url= f"https://realstonks.p.rapidapi.com/{name}"
    
    headers = {
    	"X-RapidAPI-Key": "5a15296613msh2a9148c995ff004p11e8ebjsna89f2dd61580",
    	"X-RapidAPI-Host": "realstonks.p.rapidapi.com"
    }
    
    res = requests.get(url, headers=headers)
    result = json.loads(res.text)
    
    price = result['price']
    
    chg = result['change_percentage']
    
    one_stock_res = {"name":name,"time":hr_6(),"price":price,"percentage_change":chg}
    return one_stock_res


def port_6():
    from for_date_time import date
    #remeber to convert the items variable to a string before using it 
    items = {"port_6":[lulu(),hsy(),sony(),skx(),ua(),gm()]}
    port = open(f"port_6_{date()}.json", "w")
    port.write(json.dumps(items,indent=2))
    port.close()
    return items


def meta():
    from for_date_time import hr_6
    name =port["Portfolios"][0]["Portfolio_7"][0]["symbol"]

    url= f"https://realstonks.p.rapidapi.com/{name}"
    
    headers = {
    	"X-RapidAPI-Key": "5a15296613msh2a9148c995ff004p11e8ebjsna89f2dd61580",
    	"X-RapidAPI-Host": "realstonks.p.rapidapi.com"
    }
    
    res = requests.get(url, headers=headers)
    result = json.loads(res.text)
    
    price = result['price']
    
    chg = result['change_percentage']
    
    one_stock_res = {"name":name,"time":hr_6(),"price":price,"percentage_change":chg}
    return one_stock_res

def msft():
    from for_date_time import hr_6
    name =port["Portfolios"][0]["Portfolio_7"][1]["symbol"]

    url= f"https://realstonks.p.rapidapi.com/{name}"
    
    headers = {
    	"X-RapidAPI-Key": "5a15296613msh2a9148c995ff004p11e8ebjsna89f2dd61580",
    	"X-RapidAPI-Host": "realstonks.p.rapidapi.com"
    }
    
    res = requests.get(url, headers=headers)
    result = json.loads(res.text)
    
    price = result['price']
    
    chg = result['change_percentage']
    
    one_stock_res = {"name":name,"time":hr_6(),"price":price,"percentage_change":chg}
    return one_stock_res

def dis():
    from for_date_time import hr_6
    name =port["Portfolios"][0]["Portfolio_7"][2]["symbol"]

    url= f"https://realstonks.p.rapidapi.com/{name}"
    
    headers = {
    	"X-RapidAPI-Key": "5a15296613msh2a9148c995ff004p11e8ebjsna89f2dd61580",
    	"X-RapidAPI-Host": "realstonks.p.rapidapi.com"
    }
    
    res = requests.get(url, headers=headers)
    result = json.loads(res.text)
    
    price = result['price']
    
    chg = result['change_percentage']
    
    one_stock_res = {"name":name,"time":hr_6(),"price":price,"percentage_change":chg}
    return one_stock_res

def k():
    from for_date_time import hr_6
    name =port["Portfolios"][0]["Portfolio_7"][3]["symbol"]

    url= f"https://realstonks.p.rapidapi.com/{name}"
    
    headers = {
    	"X-RapidAPI-Key": "5a15296613msh2a9148c995ff004p11e8ebjsna89f2dd61580",
    	"X-RapidAPI-Host": "realstonks.p.rapidapi.com"
    }
    
    res = requests.get(url, headers=headers)
    result = json.loads(res.text)
    
    price = result['price']
    
    chg = result['change_percentage']
    
    one_stock_res = {"name":name,"time":hr_6(),"price":price,"percentage_change":chg}
    return one_stock_res

def u():
    from for_date_time import hr_6
    name =port["Portfolios"][0]["Portfolio_7"][4]["symbol"]

    url= f"https://realstonks.p.rapidapi.com/{name}"
    
    headers = {
    	"X-RapidAPI-Key": "5a15296613msh2a9148c995ff004p11e8ebjsna89f2dd61580",
    	"X-RapidAPI-Host": "realstonks.p.rapidapi.com"
    }
    
    res = requests.get(url, headers=headers)
    result = json.loads(res.text)
    
    price = result['price']
    
    chg = result['change_percentage']
    
    one_stock_res = {"name":name,"time":hr_6(),"price":price,"percentage_change":chg}
    return one_stock_res

def vsat():
    from for_date_time import hr_6
    name =port["Portfolios"][0]["Portfolio_7"][5]["symbol"]

    url= f"https://realstonks.p.rapidapi.com/{name}"
    
    headers = {
    	"X-RapidAPI-Key": "5a15296613msh2a9148c995ff004p11e8ebjsna89f2dd61580",
    	"X-RapidAPI-Host": "realstonks.p.rapidapi.com"
    }
    
    res = requests.get(url, headers=headers)
    result = json.loads(res.text)
    
    price = result['price']
    
    chg = result['change_percentage']
    
    one_stock_res = {"name":name,"time":hr_6(),"price":price,"percentage_change":chg}
    return one_stock_res


def port_7():
    from for_date_time import date
    #remeber to convert the items variable to a string before using it 
    items = {"port_7":[meta(),msft(),dis(),k(),u(),vsat()]}
    port = open(f"port_7_{date()}.json", "w")
    port.write(json.dumps(items,indent=2))
    port.close()
    return items


def mcd():
    from for_date_time import hr_6
    name =port["Portfolios"][0]["Portfolio_8"][0]["symbol"]

    url= f"https://realstonks.p.rapidapi.com/{name}"
    
    headers = {
    	"X-RapidAPI-Key": "5a15296613msh2a9148c995ff004p11e8ebjsna89f2dd61580",
    	"X-RapidAPI-Host": "realstonks.p.rapidapi.com"
    }
    
    res = requests.get(url, headers=headers)
    result = json.loads(res.text)
    
    price = result['price']
    
    chg = result['change_percentage']
    
    one_stock_res = {"name":name,"time":hr_6(),"price":price,"percentage_change":chg}
    return one_stock_res

def dpz():
    from for_date_time import hr_6
    name =port["Portfolios"][0]["Portfolio_8"][1]["symbol"]

    url= f"https://realstonks.p.rapidapi.com/{name}"
    
    headers = {
    	"X-RapidAPI-Key": "5a15296613msh2a9148c995ff004p11e8ebjsna89f2dd61580",
    	"X-RapidAPI-Host": "realstonks.p.rapidapi.com"
    }
    
    res = requests.get(url, headers=headers)
    result = json.loads(res.text)
    
    price = result['price']
    
    chg = result['change_percentage']
    
    one_stock_res = {"name":name,"time":hr_6(),"price":price,"percentage_change":chg}
    return one_stock_res

def csco():
    from for_date_time import hr_6
    name =port["Portfolios"][0]["Portfolio_8"][2]["symbol"]

    url= f"https://realstonks.p.rapidapi.com/{name}"
    
    headers = {
    	"X-RapidAPI-Key": "5a15296613msh2a9148c995ff004p11e8ebjsna89f2dd61580",
    	"X-RapidAPI-Host": "realstonks.p.rapidapi.com"
    }
    
    res = requests.get(url, headers=headers)
    result = json.loads(res.text)
    
    price = result['price']
    
    chg = result['change_percentage']
    
    one_stock_res = {"name":name,"time":hr_6(),"price":price,"percentage_change":chg}
    return one_stock_res

def pypl():
    from for_date_time import hr_6
    name =port["Portfolios"][0]["Portfolio_8"][3]["symbol"]

    url= f"https://realstonks.p.rapidapi.com/{name}"
    
    headers = {
    	"X-RapidAPI-Key": "5a15296613msh2a9148c995ff004p11e8ebjsna89f2dd61580",
    	"X-RapidAPI-Host": "realstonks.p.rapidapi.com"
    }
    
    res = requests.get(url, headers=headers)
    result = json.loads(res.text)
    
    price = result['price']
    
    chg = result['change_percentage']
    
    one_stock_res = {"name":name,"time":hr_6(),"price":price,"percentage_change":chg}
    return one_stock_res

def jakk():
    from for_date_time import hr_6
    name =port["Portfolios"][0]["Portfolio_8"][4]["symbol"]

    url= f"https://realstonks.p.rapidapi.com/{name}"
    
    headers = {
    	"X-RapidAPI-Key": "5a15296613msh2a9148c995ff004p11e8ebjsna89f2dd61580",
    	"X-RapidAPI-Host": "realstonks.p.rapidapi.com"
    }
    
    res = requests.get(url, headers=headers)
    result = json.loads(res.text)
    
    price = result['price']
    
    chg = result['change_percentage']
    
    one_stock_res = {"name":name,"time":hr_6(),"price":price,"percentage_change":chg}
    return one_stock_res

def wkhs():
    from for_date_time import hr_6
    name =port["Portfolios"][0]["Portfolio_8"][5]["symbol"]

    url= f"https://realstonks.p.rapidapi.com/{name}"
    
    headers = {
    	"X-RapidAPI-Key": "5a15296613msh2a9148c995ff004p11e8ebjsna89f2dd61580",
    	"X-RapidAPI-Host": "realstonks.p.rapidapi.com"
    }
    
    res = requests.get(url, headers=headers)
    result = json.loads(res.text)
    
    price = result['price']
    
    chg = result['change_percentage']
    
    one_stock_res = {"name":name,"time":hr_6(),"price":price,"percentage_change":chg}
    return one_stock_res


def port_8():
    from for_date_time import date
    #remeber to convert the items variable to a string before using it 
    items = {"port_8":[mcd(),dpz(),csco(),pypl(),jakk(),wkhs()]}
    port = open(f"port_8_{date()}.json", "w")
    port.write(json.dumps(items,indent=2))
    port.close()
    return items


def port_all():
    from for_date_time import date
    #remeber to convert the items variable to a string before using it 
    items = {"port_all":[port_1(),port_2(),port_3(),port_4(),port_5(),port_6(),port_7(),port_8()]}
    port = open(f"port_all_{date()}.json", "w")
    port.write(json.dumps(items,indent=2))
    port.close()
    print(items)
    return items

port_all()