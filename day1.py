def solve_captcha(captcha):
    # Start by checking the last against the first
    curr_char = captcha[-1]
    charsum = 0
    for next_char in captcha:
        if next_char == curr_char:
            charsum += int(curr_char)
        curr_char = next_char
    return charsum


def solve_p2(captcha):
    num_chars = len(captcha)
    offset = num_chars // 2
    charsum = 0
    for pos, char in enumerate(captcha):
        if captcha[(pos + offset) % num_chars] == char:
            charsum += int(char)
    return charsum

with open('input_d1.txt') as f:
    lines = [x.strip('\n') for x in f.readlines()]

captcha_in = lines[0]

print solve_captcha(captcha_in)
print solve_p2(captcha_in)
