from random import randint

npcs_list = []

player = {
    "name": "Vinicius",
    "level": 1,
    "exp": 0,
    "exp_max": 30,
    "hp": 100,
    "hp_max": 100,
    "damage": 25,
}

def create_npc(level):

    new_npc = {
        "name": f"NPC #{level}",
        "level": level,
        "damage": 5 * level,
        "hp": 100 * level,
        "hp_max": 100 * level,
        "exp": 7 * level, 
    }

    return new_npc

def create_npcs(n_npcs):
    for x in range(n_npcs):
        new_npc = create_npc(x + 1)
        npcs_list.append(new_npc)

def show_npcs():
    for npc in npcs_list:
        show_npc(npc)

def show_npc(npc):
    print(f"Name: {npc['name']} // Level: {npc['level']} // Damage: {npc['damage']} // HP: {npc['hp']} // EXP: {npc['exp']}")

def show_player():
    print(f"Name: {player['name']} // Level: {player['level']} // Damage: {player['damage']} // HP: {player['hp']} / {player['hp_max']} // EXP: {player['exp']} / {player['exp_max']}")

def reset_player():
    player['hp'] = player['hp_max']

def reset_npc(npc):
    npc['hp'] = npc['hp_max']

def level_up():
    if player['exp'] >= player['exp_max']:
        player['level'] += 1
        player['exp'] = 0
        player['exp_max'] *= 2
        player['hp_max'] += 20

def start_match(npc):
    while player['hp'] > 0 and npc['hp'] > 0:
        atack_npc(npc)
        atack_player(npc)
        show_info_match(npc)
    
    if player['hp'] > 0: #player win
        print(f"O {player['name']} venceu e ganhou {npc['exp']} de EXP!")
        player['exp'] += npc['exp']
        show_player()
    else: # npc win
        print(f"O {npc['name']} venceu!")
        show_npc(npc)

    level_up()
    reset_player()
    reset_npc(npc)


def atack_player(npc):
    player['hp'] = player['hp'] - npc['damage']

def atack_npc(npc):
    npc['hp'] = npc['hp'] - player['damage']

def show_info_match(npc):
    print(f"Player: {player['hp']} / {player['hp_max']}")
    print(f"NPC: {npc['name']}: {npc['hp']} / {npc['hp_max']}")
    print("----------------------------------------------------\n")

create_npcs(5)
# show_npcs()
select_npc = npcs_list[0]
start_match(select_npc)
start_match(select_npc)
start_match(select_npc)
start_match(select_npc)
start_match(select_npc)
show_player()