HISTORY_FILE = "operation.txt"

def show_history():
    with open("operation.txt","r") as f:
        lines = f.readlines()
        if len(lines) == 0:
            print("History is empty!")
            return
        else:
            for line in reversed(lines):
                print(line.strip())

def clear_history():
    with open("operation.txt", "w") as f:
        print("History is cleared.")

def save_to_history(equation,result):
    with open("operation.txt", "a") as f:
        f.write(equation + "=" + str(result) + ("\n"))

def calculate(user_input):
    idx = user_input.split()
    if len(idx) != 3:
        print("Invalid operation. Use format : number operation number(eg. 8 + 8)")
        return
    num1 = float(idx[0])
    op = idx[1]
    num2 = float(idx[2])

    if op == "+":
        result = num1 + num2
    elif op == "-":
        result = num1 - num2
    elif op == "*":
        result = num1 * num2
    elif op == "/":
        if num2 == 0:
            print("You can not divide by Zero.")
            return
        result = num1 / num2
    elif op == "**":
        result = num1 ** num2
    elif op == "%":
        result = num1 % num2
    else:
        print("Invalid operator use only =,-,*,/,**,%.")

    if int(result) == result:
        result = int(result)
    print("Result = ",result)
    save_to_history(user_input, result)

def main():
    print("___SIMPLE CALCULATOR (type history, clear or exit)")
    while True:
        user_input = input("Enter calculation (+,-,*,/,**,%) and comand (history, clear or exit)= ")
        if user_input == "history":
            show_history()
        elif user_input == "clear":
            clear_history()
        elif user_input == "exit":
            print("Goodby...")
            break
        else:
            calculate(user_input)

main()