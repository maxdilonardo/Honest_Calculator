
msg_0 = "Enter an equation"
msg_1 = "Do you even know what numbers are? Stay focused!"
msg_2 = "Yes ... an interesting math operation. You've slept through all classes, haven't you?"
msg_3 = "Yeah... division by zero. Smart move..."
msg_4 = "Do you want to store the result? (y / n):"
msg_5 = "Do you want to continue calculations? (y / n):"
msg_6 = " ... lazy"
msg_7 = " ... very lazy"
msg_8 = " ... very, very lazy"
msg_9 = "You are"
msg_10 = "Are you sure? It is only one digit! (y / n)"
msg_11 = "Don't be silly! It's just one number! Add to the memory? (y / n)"
msg_12 = "Last chance! Do you really want to embarrass yourself? (y / n)"

msg_index = ["Enter an equation",
             "Do you even know what numbers are? Stay focused!",
             "Yes ... an interesting math operation. You've slept through all classes, haven't you?",
             "Yeah... division by zero. Smart move...",
             "Do you want to store the result? (y / n):",
             "Do you want to continue calculations? (y / n):",
             " ... lazy",
             " ... very lazy",
             " ... very, very lazy",
             "You are",
             "Are you sure? It is only one digit! (y / n)",
             "Don't be silly! It's just one number! Add to the memory? (y / n)",
             "Last chance! Do you really want to embarrass yourself? (y / n)"]

memory = 0.0


def is_one_digit(v):
    # returns true if v is one digit, false otherwise

    if (v > -10) and (v < 10) and v.is_integer():
        return True
    else:
        return False


def check(v1, v2, v3):
    # checks inputs for a variety of easy to solve cases

    msg = ""
    if is_one_digit(v1) and is_one_digit(v2):
        msg = msg + msg_6
    if (v1 == 1 or v2 == 1) and v3 == "*":
        msg = msg + msg_7
    if (v1 == 0 or v2 == 0) and (v3 == "+" or v3 == "-" or v3 == "*"):
        msg = msg + msg_8
    if msg != "":
        msg = msg_9 + msg
        print(msg)


def check_oper(value):
    # returns true if value is an operation, false if otherwise
    operand_list = ["-", "+", "/", "*"]

    if value in operand_list:
        return True
    else:
        return False


def check_float(num1, num2):
    # returns true if num1 and num2 are float type or "M" string and
    # swaps num1 and num2 with memory if they're "M". Returns false
    # if num1 or num2 are not float type or "M"
    check_var = True

    try:
        num1 = float(num1)
    except ValueError:
        if num1 == "M":
            num1 = memory
            pass
        else:
            check_var = False
    try:
        num2 = float(num2)
    except ValueError:
        if num2 == "M":
            num2 = memory
            pass
        else:
            check_var = False
    return [check_var, num1, num2]


def take_input():
    # begins the calculator interface with user

    global memory
    again = True
    while again:
        print(msg_0)
        calc = input().split()
        x = calc[0]
        y = calc[2]
        oper = calc[1]
        calc = check_float(x, y)
        if calc[0]:
            x = float(calc[1])
            y = float(calc[2])
        else:
            print(msg_1)
            continue

        if check_oper(oper):

            check(x, y, oper)

            if oper == "+":
                result = x + y
            elif oper == "-":
                result = x - y
            elif oper == "*":
                result = x * y
            elif oper == "/" and y == float(0):
                print(msg_3)
                continue
            else:
                result = x / y
        else:
            print(msg_2)
            continue

        print(float(result))

        again = check_for_memory(result)


def check_for_continue():
    # checks to see if the user would like to continue
    # using the calculator

    while True:
        checker = True
        print(msg_5)
        y_or_n = input()
        if y_or_n == "y":
            break
        elif y_or_n == "n":
            checker = False
            break
        else:
            continue
    return checker


def check_for_memory(x1):
    # checks to see if user wants to save the result

    global memory
    while True:
        continue_check = True
        print(msg_4)
        y_or_n = input()
        if y_or_n == "y":
            # memory_snark(x1)
            memory_snark(x1)
            # memory = float(x1)
        elif y_or_n == "n":
            pass
        else:
            continue
        continue_check = check_for_continue()
        break
    return continue_check


def memory_snark(y1):
    # gives the user a hard time if they want to save an
    # answer that is easy to remember

    global memory
    if is_one_digit(y1):
        index = 10
        while True:
            print(msg_index[index])
            reply = input()
            if reply == "y":
                if index < 12:
                    index = index + 1
                else:
                    memory = float(y1)
                    break
            elif reply == "n":
                break
            else:
                continue
    else:
        memory = float(y1)


take_input()
