# Link to the kata: https://www.codewars.com/kata/5672a98bdbdd995fad00000f/

def rps(p1, p2):
    if ((p1 == 'rock' and p2 == 'scissors') or (p1 == 'paper' and p2 == 'rock')
    or (p1 == 'scissors' and p2 == 'paper')):
        return 'Player 1 won!'
    elif p1 == p2:
        return 'Draw!'
    else: 
        return 'Player 2 won!'
