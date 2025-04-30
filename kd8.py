queue = []

while True:
    print("\nQueue Operations:\n1. Enqueue\n2. Dequeue\n3. Display\n4. Exit")
    choice = int(input("Enter your choice: "))

    if choice == 1:
        value = int(input("Enter value to enqueue: "))
        queue.append(value)
        print("Queue:", queue)
    elif choice == 2:
        if queue:
            print("Dequeued:", queue.pop(0))
        else:
            print("Queue is empty")
    elif choice == 3:
        print("Queue:", queue)
    elif choice == 4:
        break
    else:
        print("Invalid choice")
