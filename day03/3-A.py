from collections import Counter, defaultdict

def main():
    s = ""
    with open('input.txt') as f:
        s = f.read()
    total = 0
    start_seq = "mul("
    for i in range(len(s)):
        if s[i:i+len(start_seq)] != start_seq:
            # check this one
            continue
        first, first_digit = i+len(start_seq), ""
        next_comma = s[i+len(start_seq):].find(',')
        if next_comma == -1:
            break
        next_comma += i+len(start_seq)
        first_digit = s[i+len(start_seq):next_comma]
        if not all(x.isdigit() for x in first_digit):
            continue
        first_digit = int(first_digit)
        next_paren = s[next_comma+1:].find(')')
        if next_paren == -1:
            break
        next_paren += next_comma + 1
        second_digit = s[next_comma+1:next_paren]
        if not all(x.isdigit() for x in second_digit):
            continue
        second_digit = int(second_digit)
        total += (first_digit) * second_digit

    return total

print(main())