from get_input import get_input

response = get_input(22)
data = response.text.strip().split('\n\n')
players = [a.split('\n') for a in data]
player_data = {p[0].split('Player ')[1].split(':')[0]: list(map(int, p[1:])) for p in players}

def score(cards):
    out = 0
    for i, card in enumerate(cards[::-1]):
        out += (i + 1) * card
    return out

def get_winner(draw_1, draw_2, player_1, player_2):
    if draw_1 > draw_2:
        return player_1 + [draw_1, draw_2], player_2
    else:
        return player_1, player_2 + [draw_2, draw_1]

def to_strng(player_1, player_2):
    return '{};{}'.format(','.join(map(str, player_1)), ','.join(map(str, player_2)))

def game(player_1, player_2, win_func = get_winner):
    record = [to_strng(player_1, player_2)]
    while len(player_1) > 0 and len(player_2) > 0:
        player_1, player_2 = win_func(player_1[0], player_2[0], player_1[1:], player_2[1:])
        record.append(to_strng(player_1, player_2))
        if len(record) != len(list(set(record))):
            return player_1, player_2
    return player_1, player_2

player_1, player_2 = game(player_data['1'], player_data['2'])
if len(player_1) == 0:
    print(score(player_2))
else:
    print(score(player_1))

def get_winner_recursive(draw_1, draw_2, player_1, player_2):
    if len(player_1) >= draw_1 and len(player_2) >= draw_2:
        sub_1, sub_2 = game(player_1[:draw_1], player_2[:draw_2], get_winner_recursive)
        if len(sub_1) == 0:
            return player_1, player_2 + [draw_2, draw_1]
        else:
            return player_1 + [draw_1, draw_2], player_2
    else:
        return get_winner(draw_1, draw_2, player_1, player_2)

player_1, player_2 = game(player_data['1'], player_data['2'], get_winner_recursive)
if len(player_1) == 0:
    print(score(player_2))
else:
    print(score(player_1))

