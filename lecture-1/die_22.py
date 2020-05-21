import random

def bot_count(current_num, turn):
    '''
    This function return a number of count
    whether 1 or 2 to kill the player hehe!
    
    Input:
    current_num(int) - the number that is currently counted to
    turn(int) - the turn number

    Output:
    count(int) - how many count further, by napat
    '''

    if current_num % 3 == 0:
        return random.randint(1,2)

    else:
        return 3 - (current_num % 3)

def game_22(player, current_num, count):
    assert count in [1,2], f"Your count is not 1 or 2, it is {count}"

    dis_count = ""
    for i in range(1, count+1):
        dis_count += str(current_num + i) + " "
    
    print(f"{player} count: {dis_count}")

    if current_num + count >= 22:
        print(f"{player} die")
        return "die"

    else:
        return "alive"


if __name__ == "__main__":
    player1 = "bot1"
    player2 = "bot2"
    current_player = player1

    status = "alive"
    current_num = 0
    turn = 1
    while status == "alive":
        player_count = bot_count(current_num, turn)
        status = game_22(current_player, current_num, player_count)

        # Swap player
        if current_player == player1:
            current_player = player2
        else:
            current_player = player1

        turn += 1
        current_num += player_count
