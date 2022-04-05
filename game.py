hero = {
    "name":"Batman",
    "hp":100,
    "damage":10,
    "points":0,
    "protection":False,
    "defence_count":3
}
enemy = {
    "name":"Joker",
    "hp":100,
    "damage":10,
    "points":0,
    "protection":False,
    "defence_count":3
}
print(f"Игра начинается: Вы-{hero['name']}, ваш враг-{enemy['name']}")
game_status = True
while game_status:
    #enemy
    print(f"Очередь у {enemy['name']}")
    action = input("Attack/Defence")
    if action.lower() == "attack" and hero["protection"]!=True:
        hero["hp"] -= enemy["damage"]
    elif action.lower() == "defence":
        if enemy["defence_count"] >0:
            enemy["protection"] = True
            enemy["defence_count"] -= 1
        else:
            print("У вас нет защиты")
    elif action.lower() == "attack" and hero["protection"]!=False:
        hero["protection"] = False
        print("у него есть защита \n")
    print(f"Жизнь {hero['name']} -", hero["hp"],"\n" )



    #hero
    print(f"Очередь у {hero['name']}")
    action = input("Attack/Defence") # ask action
    #проверка на действие
    if action.lower() == "attack" and enemy["protection"]!=True:
        enemy["hp"] -= hero["damage"]
    elif action.lower() == "defence":
        if hero["defence_count"] > 0:
            hero["protection"] = True
            hero["defence_count"] -=1
        else:
            print("У вас нет защиты")
    elif action.lower() == "attack" and enemy["protection"]!=False:
        print("У него есть защита")
        enemy["protection"] = False

    print(f"Жизнь {enemy['name']}-", enemy["hp"], "\n")
    if hero["hp"] == 0:
        print("Hero lost! GAME OVER!")
        game_status = False
    elif enemy["hp"] == 0:
        print("Enemy lost! GAME OVER!")
        game_status = False