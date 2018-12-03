import re

def transformmed_string(S):
    return re.sub(r'(\w)\1', r'', S)

if __name__ == '__main__':
    S = "ABCBBCBA"

    answer = transformmed_string(S)
    while answer != S:
        S = answer
        answer = transformmed_string(S)
