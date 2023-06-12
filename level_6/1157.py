inp = input().upper()
alphabet = [0 for i in range(26)]
for i in inp:
    alphabet[ord(i)-65] += 1
if alphabet.count(max(alphabet)) > 1:
    print("?")
else:
    print(chr(alphabet.index(max(alphabet)) + 65))