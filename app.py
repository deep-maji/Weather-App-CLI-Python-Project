import requests
import math
import datetime

def getApiKey():
    API_KEY = ""
    return API_KEY

def getApiLink(sate):
    Key = getApiKey()
    Link = f"http://api.openweathermap.org/data/2.5/weather?q={sate}&units=metric&appid={Key}"
    return Link

def fetch_the_data(sate="kolkata"):

    weather_url = getApiLink(sate)
    # sent a request at the url
    
    try:
        respons = requests.get(weather_url)
        # store the data at data in json formate
        data = respons.json()
    except requests.exceptions.ConnectionError:
        print("Connection error occurred.")
        return {}
    except requests.exceptions.Timeout:
        print("Request timed out.")
        return {}
    except requests.exceptions.HTTPError as err: 
        print(f"HTTP error occurred: {err}")
        return {}
    except requests.exceptions.RequestException as err:
        print(f"An error occurred: {err}")
        return {}
    finally:
        # Check the data is get or not
        if data['cod'] == 200:
            return data
        else:
            return {}



def get_temp(data,sate="Kolkata"):
    try:
        temp = data["main"]["temp"]
        feels_like = data["main"]["feels_like"]
    except KeyError:
        print("\n")
        print("*"*70)
        print("Data fecth failed.")
        print("*"*70)
        return "fail"
    
    print(f"\n\n*************** Temp in {sate} ***************")
    print(f"Temp : {math.ceil(temp)}c")
    print(f"Feels like : {math.ceil(feels_like)}c")
    print('*'*70)
    return temp,feels_like
    


def main():
    data = fetch_the_data()
    sate = "Kolkata"
    while True:
        print("\n")
        print("||||| Weather App ||||| Temperature |||||")
        print("0. Set Default to Kolkata ")
        print("1. Refresh the app ")
        print("2. Get temperature ")
        print("3. Enter your sate ")
        print("4. Save the data ")
        print("9. Exit : ")
        choice = input("Enter your choice : ")
        match choice:
            case '0':
                data = fetch_the_data("Kolkata")
                sate = "Kolkata"
                print("Set default Done!")
            case '1':
                data = fetch_the_data(sate)
                print("Refresh Done.")
            case '2':
                get_temp(data,sate)
                pass
            case '3':
                sate = input("Enter like 'Kolkata' : ")
                data = fetch_the_data(sate)
                get_temp(data,sate)
            case '4':
                with open("Temperature_data.txt",'a') as file:
                    if data != 'fail':
                        temp,feel = get_temp(data)
                        now = datetime.datetime.now()
                        date = now.date()
                        whole_saved_text = f"\nsate : {sate}\nDate : {date}\nTemperature : {temp}\nFeels Like : {feel}\n"
                        symbols = "*"*20
                        whole_saved_text = whole_saved_text + "\n" + symbols
                        file.write(whole_saved_text)

            case '9':
                break
            case _:
                print("Invaild Choice.") 

if __name__ == "__main__":
    main()

