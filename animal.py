def greet_user(user_name):
    print(f'Hello, {user_name}')

def main():
    user_name = input('Please enter your name: ')
    greet_user(user_name)


if __name__ == '__main__':
    main()
