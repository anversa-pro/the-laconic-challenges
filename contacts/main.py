
def solution(a, b, p):

    contacts = []
    index = 0
    for number in b:
        contain = check(number, p)
        if contain:
            contacts.append(a[index])
        index += 1

    if len(contacts) <= 0:
        return "NO CONTACT"
    else:
        contacts.sort()

    return min(contacts, key=len)


def check(string, sub_str):
    if string.find(sub_str) != -1:
        return True
    else:
        return False


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    names = ["Alberto", "Andres", "Antonio", "Armando"]
    numbers = ["997755331", "111222333", "987654321", "657112289"]
    print(solution(names, numbers, "1122"))
    names = ["pim", "pom"]
    numbers = ["999999999", "777888999"]
    print(solution(names, numbers, "88999"))
    names = ["sander", "amy", "ann", "michael"]
    numbers = ["123456789", "234567891", "789123456", "123123123"]
    print(solution(names, numbers, "1"))
    names = ["adam", "eva", "leo"]
    numbers = ["121212121", "111111111", "444555666"]
    print(solution(names, numbers, "112"))


