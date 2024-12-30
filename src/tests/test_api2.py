import requests

def test_api():
    

    url = 'https://reqres.in/api/users?page=2'
    data = { 
            "first_name" : "Kalpak",
            "last_name" : "Pimpale"
         }

    response = requests.post(url, json=data)


    return response.text

output = test_api()

assert "first_name" in output == "Kalpak"
assert "last_name" in output == "Pimpale"

