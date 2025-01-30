# def greet(name):
#     return f"Hello, {name}!"


if __name__ == "__main__":
    # user_name = input("Enter your name: ")
    # print(greet(user_name))
    for num in range(1, 21):
        if num > 1:
            for i in range(2, num):
                if num % i == 0:
                    break
            else:
                if num > 6:
                    print(num)
