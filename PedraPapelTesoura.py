import random

def play():
    user = input("Qual Sua Escolha? 'r' para pedra, 'p' para papel, 't' tesoura\n")
    computer = random.choice(['r', 'p', 't'])

    if user == computer:
        return 'Deu Empate!'

    # r > t, t > p, p > r
    if is_win(user, computer):
        return 'Você Venceu! :)'

    return 'Você Perdeu! :('

def is_win(player, opponent):
    # return true if player wins
    # r > t, t > p, p > r
    if (player == 'r' and opponent == 't') or (player == 't' and opponent == 'p') \
        or (player == 'p' and opponent == 'r'):
        return True

print(play())
