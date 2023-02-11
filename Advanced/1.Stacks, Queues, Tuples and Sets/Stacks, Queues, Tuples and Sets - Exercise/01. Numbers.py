first_integers, second_integers = set(map(int, input().split())), set(map(int, input().split()))

commands = int(input())

for command in range(commands):
    curr_command = input().split()

    if curr_command[0] == "Add":
        if curr_command[1] == "First":
            integers = curr_command[2:]
            [first_integers.add(int(num)) for num in integers]

        elif curr_command[1] == "Second":
            integers = curr_command[2:]
            [second_integers.add(int(num)) for num in integers]

    elif curr_command[0] == "Remove":
        if curr_command[1] == "First":
            integers = curr_command[2:]
            [first_integers.remove(int(num)) for num in integers if int(num) in first_integers]

        elif curr_command[1] == "Second":
            integers = curr_command[2:]
            [second_integers.remove(int(num)) for num in integers if int(num) in second_integers]

    elif curr_command == ['Check', 'Subset']:
        if first_integers.issubset(second_integers) or second_integers.issubset(first_integers):
            print(True)
            continue
        print(False)

print(f"{', '.join([str(num) for num in sorted(first_integers)])}"
      f"\n"
      f"{', '.join([str(num) for num in sorted(second_integers)])}")