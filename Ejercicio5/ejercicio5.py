import requests
import time

def check_website(url):
    print("")
    
    try:
        response = requests.get(url)
        print("")
        return response.status_code == 200
    except requests.ConnectionError:
        print(f"Error de conexion con: %s" % url)
        return False

def check_and_notify(url, interval_minutes):
    print("Iniciando: ")
    try:
        while True:
            if check_website(url):
                print(f"The website {url} is up!")
                # time.sleep(float(interval_minutes) * 60)
            else:
                print(f"The website {url} is down!")
            time.sleep(float(interval_minutes) * 60)
    except KeyboardInterrupt:
        print("\Saliendo del programa.")

if __name__ == "__main__":
    website_url = "https://example.com"  
    website_url2 = "http://localhost:8080/"
    check_interval_minutes = input("Please enter the interval in minutes: ")
    if check_interval_minutes == "":
        check_interval_minutes = 1

    check_and_notify(website_url, check_interval_minutes)
