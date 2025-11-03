if __name__  == '__main__':
    
    command = input()
    command = command.split(' ')
    action = command[0]
    arg1 = int(command[1])

    print(f'CDM: {action} + Arg1: {arg1}')

    match action.lower():
        case "hello":
            print("Hi!")
        case "jump":
            print(f'Ok, I will jump {arg1} times') 