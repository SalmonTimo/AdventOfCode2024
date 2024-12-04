from collections import Counter, defaultdict

# Should I learn regex? No it's the children who are wrong.png
def main():
    s = ""
    with open('input.txt') as f:
        s = f.read()
    total = 0
    start_seq = "mul("
    do_pat = "do()"
    dont_pat = "don't()"
    i = 0
    while i < len(s):
        if s[i:i+len(dont_pat)] == dont_pat:
            # continue to next do pat
            while i < len(s) and s[i:i+len(do_pat)] != do_pat:
                i += 1
            continue
        if s[i:i+len(start_seq)] != start_seq:
            # skip this one
            i += 1
            continue
        first_digit = ""
        next_comma = s[i+len(start_seq):].find(',')
        if next_comma == -1:
            break
        next_comma += i+len(start_seq)
        first_digit = s[i+len(start_seq):next_comma]
        if not all(x.isdigit() for x in first_digit):
            i += 1
            continue
        first_digit = int(first_digit)
        next_paren = s[next_comma+1:].find(')')
        if next_paren == -1:
            break
        next_paren += next_comma + 1
        second_digit = s[next_comma+1:next_paren]
        if not all(x.isdigit() for x in second_digit):
            i += 1
            continue
        second_digit = int(second_digit)
        total += (first_digit) * second_digit

        i += 1

    return total

print(main())