def main():
    print("                    ---TODO Application---                    ")
    print("\nYou can track your tasks and increase your productiviy using TODO app.\n")

    while True:
        print("\nOperations:")
        print("1. Add task")
        print("2. View tasks")
        print("3. Delete task")
        print("4. Update task")

        try:
            operation = int(input("\nWhich operation to perform: "))
        except ValueError:
            print("\n          ---Not a valid operation---          ")
        else:
            if operation in [1, 2, 3, 4]:
                break
            print("\n          ---Unkown operation---          ")
    

    if operation == 1:
        ...
    elif operation == 2:
        ...
    elif operation == 3:
        ...
    elif operation == 4:
        ...


if __name__ == "__main__":
    main()
