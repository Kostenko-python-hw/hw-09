from functools import reduce

shutdown_commands = ('good bye', 'close', 'exit')

data_base = {}




def input_error(func):
    def inner(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except KeyError:
            return 'This contact is missing, try another one.'
        except ValueError:
            return 'The phone has to be a number.'
        except IndexError:
            return 'Give me name and phone please.'
    return inner




def input_handler():
    while True:
        input_date = input('Enter the command:').strip().lower()

        if input_date == '.':
            break

        if input_date in shutdown_commands:
            print("Good bye!")
            break

        if input_date == 'hello':
            print('How can I help you?')
        elif not input_date:
            print('Blank line is not a command.')
        else:
            cmd_parser(input_date.split(' '))
            



def cmd_parser(splitted_cmd):
    if splitted_cmd[0] == 'add' and len(splitted_cmd) <= 3:
        print(add_user_handler(splitted_cmd[1:]))
    elif splitted_cmd[0] == 'change' and len(splitted_cmd) <= 3:
        print(change_phone_handler(splitted_cmd[1:]))
    elif splitted_cmd[0] == 'phone' and len(splitted_cmd) <= 2:
        print(show_phone_handler(splitted_cmd[1:]))
    elif splitted_cmd[0] == 'show' and splitted_cmd[1] == 'all' and len(splitted_cmd) == 2:
        print(show_all_handler())
    else:
        print('Command not recognized')




@input_error
def add_user_handler(data):
    name = data[0]
    phone = int(sanitize_phone_number(data[1]))
    if name in data_base:
        return 'This contact already exists.'
    else:
        data_base[name] = phone 
        return f'Contact {name.capitalize()} has been successfully added.'
    



@input_error
def change_phone_handler(data):
    name = data[0]
    phone = int(sanitize_phone_number(data[1]))
    if name in data_base:
        data_base[name] = phone 
        return f'contact {name.capitalize()} has been successfully changed.'
    else:
        # return 'This contact is missing, try another one'
        raise KeyError()




@input_error
def show_phone_handler(data):
    return data_base[data[0]]



        
def show_all_handler():
    if len(data_base) == 0:
        return 'You don\'t have any contacts yet.'
    else:
        contacts = reduce(lambda acc, val: acc + f'{val[0].capitalize()}: {val[1]}, ', data_base.items(), '')
        return contacts.removesuffix(', ')
    



def sanitize_phone_number(phone):
    new_phone = (
        phone.strip()
        .removeprefix("+")
        .replace("(", "")
        .replace(")", "")
        .replace("-", "")
        .replace(" ", "")
    )
    return new_phone




def main():
    input_handler()




if __name__ == '__main__':
    main()
