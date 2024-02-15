WHITELIST = "aoieu"


for _ in range(int(input())):
    result = ""
    data = input()
    allow_next = False

    for char in data:
        if allow_next:
            allow_next = False
            result += char
        elif char in WHITELIST:
            allow_next = True

    print(result)
