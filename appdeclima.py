import json, requests, time, os

error = None
city = input("Insira sua cidade: ")
API_KEY = "0eb163f95ef94dcca91225346250508"
site = f"https://api.weatherapi.com/v1/current.json?key={API_KEY}&q={city}&days=1&lang=pt"
info = requests.get(site)
dados = info.json()
if False: #apenas para desenvolvimento
     print(dados)

if info.status_code == 404:
     exit("Aconteceu algum problema, mas não é sua culpa ^-^")
     
try:
     error = True
     print("Erro:",dados['error']['code'])
     time.sleep(0.2)
     print("Mensagem:",dados['error']['message'])
except:
     error = False
     pass

if error:
     exit()

os.system('clear')
print("RESULTADO:")
print(f"Cidade: {dados['location']['name']}")
time.sleep(0.2)
print(f"Estado: {dados['location']['region']}")
time.sleep(0.2)
print(f"País: {dados['location']['country']}")
time.sleep(0.2)
print(f"Tempo atual: {(lambda x: "Dia" if x == 1 else "Noite")(dados['current']['is_day'])}")
time.sleep(0.2)
print(f"Temperatura: {dados['current']['temp_c']}⁰C")
time.sleep(0.2)
print(f"Velocidade do vento: {dados['current']['wind_kph']}km/h")
time.sleep(0.2)
print(f"Direção do vento: {dados['current']['wind_dir']}")
time.sleep(0.2)
print(f"Condição atual: {dados['current']['condition']['text']}")
#print(f"Chance of rain (This day): {dados['forecast']['forecastday']['day']['daily_chance_of_rain']}%")
#Em desenvolvimento ^-^
