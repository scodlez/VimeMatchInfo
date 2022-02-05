import requests, json, time, os
import colorama
from colorama import Fore
colorama.init()

global nicknames
nicknames = []
match = input("Введите ID матча: ") #
os.system("cls") #Стирает текст


#Отображение хуйни в консоли
actualmatch = json.loads(requests.get("https://api.vimeworld.ru/match/" + match).text)
print(Fore.GREEN, "Игра - ", Fore.WHITE, actualmatch["game"]) #Вывод сервера (OS, BWH)
print(Fore.GREEN, "Карта - ", Fore.WHITE, actualmatch["mapName"])
print(Fore.GREEN, "Сервер - ", Fore.WHITE, actualmatch["server"])
print(Fore.GREEN, "Игра - ", Fore.WHITE, "https://vimetop.ru/matches#" + match)
teamWIN = actualmatch["winner"]["team"]
if teamWIN == "red":
    print(Fore.GREEN, "Команда победителей -", Fore.RED, "Красные")
else:
    print(Fore.GREEN, "Команда победителей -", Fore.CYAN, "Синие")

print("\n\n", Fore.WHITE)
print("Команда -", Fore.CYAN, "Синие")
for rand in range(4):
    usernick = json.loads(
        requests.get(
            "https://api.vimeworld.ru/user/"
            + str(actualmatch["teams"][1]["members"][rand])
        ).text
    )[0]["username"]
    donate = json.loads(
        requests.get(
            "https://api.vimeworld.ru/user/"
            + str(actualmatch["teams"][1]["members"][rand])
        ).text
    )[0]["rank"]
    print(Fore.YELLOW, donate, Fore.WHITE, usernick)
print("\n")
print("Команда -", Fore.RED, "Красные")
for rand1 in range(4):
    usernick = json.loads(
        requests.get(
            "https://api.vimeworld.ru/user/"
            + str(actualmatch["teams"][0]["members"][rand1])
        ).text
    )[0]["username"]
    donate = json.loads(
        requests.get(
            "https://api.vimeworld.ru/user/"
            + str(actualmatch["teams"][0]["members"][rand1])
        ).text
    )[0]["rank"]
    print(Fore.YELLOW, donate, Fore.WHITE, usernick)

#Конец =)
print("" * 3) #Пробел
print(Fore.GREEN, "Нажмите на любую, чтобы закрыть программу")
input()
