for n in range(1, 100):
    s = bin(n)[2:]  # перевод в двоичную систему
    s = str(s)
    s = s[s.find('1'):]
    if s.count('1') > s.count('0'):
        s += '1'
    else:
        s += '0'
    r = int(s, 2)  # перевод в десятичную систему
    if r > 80:
        print(r)
        break