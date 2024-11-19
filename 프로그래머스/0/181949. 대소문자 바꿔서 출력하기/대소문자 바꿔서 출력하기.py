str = input()
new_str = ''
for chr in str:
    if ord(chr) <= 96:
        new_str += chr.lower()
    else:
        new_str += chr.upper()

print(new_str)