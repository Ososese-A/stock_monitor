import requests
name = "WBD"
url = f"https://realstonks.p.rapidapi.com/{name}"

headers = {
	"X-RapidAPI-Key": "5a15296613msh2a9148c995ff004p11e8ebjsna89f2dd61580",
	"X-RapidAPI-Host": "realstonks.p.rapidapi.com"
}

response = requests.get(url, headers=headers)

print(response.json())
