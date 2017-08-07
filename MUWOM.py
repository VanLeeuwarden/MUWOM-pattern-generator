import matplotlib.pyplot as plt
import sys

base_characters = ['M', 'W', 'O', 'U']

def input_to_MOWOM(user_input):
    out = []
    user_input = user_input.upper()
    for ii in user_input:
        if ii in base_characters:
            out.append(ii)
        else:
            out.append('O')
    return out

def value_to_letter(letter):
    if letter == 'M':
        value = -1
        return value
    if letter == 'W':
        value = 1
        return value
    return 0
    
def flip_value(prior_shift, letter):
    if letter == 'U':
        prior_shift = prior_shift * -1
    return prior_shift

def loopdraw(successive_pos_x, successive_pos_y, prior_shift_x, prior_shift_y):
    if successive_pos_x >= len(X) or successive_pos_x < 0:
        return
    if successive_pos_y >= len(Y) or successive_pos_y < 0:
        return
    if (value_to_letter(X[successive_pos_x]), value_to_letter(Y[successive_pos_y])) != (0,0):
        return
    if (X[successive_pos_x], Y[successive_pos_y]) == ('U', 'U'):
        return
    new_shift_x = flip_value(prior_shift_x, X[successive_pos_x])
    new_shift_y = flip_value(prior_shift_y, Y[successive_pos_y])
    future_pos_x = successive_pos_x + new_shift_x
    future_pos_y = successive_pos_y + new_shift_y
    plt.plot([successive_pos_x, future_pos_x], [successive_pos_y, future_pos_y], color='b')
    loopdraw(future_pos_x, future_pos_y, new_shift_x, new_shift_y)

def draw(pos_x, pos_y):
    shift_x = value_to_letter(X[pos_x])
    shift_y = value_to_letter(Y[pos_y])
    plt.plot([pos_x, pos_x + shift_y], [pos_y, pos_y + shift_x])
    if (shift_x, shift_y) != (0,0):
        loopdraw(pos_x + shift_y, pos_y + shift_x, shift_y, shift_x)
    
if __name__ == "__main__":
    X = input_to_MOWOM(str(sys.argv[1]))
    Y = input_to_MOWOM(str(sys.argv[2]))
    for ii in range(len(X)):
        for jj in range(len(Y)):
            draw(ii, jj)
    plt.axis('off')
    plt.show()
