stack = []

while True:
    print("\nStack Operations:\n1. Push\n2. Pop\n3. Display\n4. Exit")
    choice = int(input("Enter your choice: "))

    if choice == 1:
        value = int(input("Enter value to push: "))
        stack.append(value)
        print("Stack:", stack)
    elif choice == 2:
        if stack:
            print("Popped:", stack.pop())
        else:
            print("Stack is empty")
    elif choice == 3:
        print("Stack:", stack)
    elif choice == 4:
        break
    else:
        print("Invalid choice")
