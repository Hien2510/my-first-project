tasks = []

while True:
    print("\n===== TODO LIST =====")
    print("1. Xem công việc")
    print("2. Thêm công việc")
    print("3. Thoát")

    choice = input("Chọn: ")

    if choice == "1":
        if len(tasks) == 0:
            print("Chưa có công việc nào.")
        else:
            print("\nDanh sách công việc:")
            for i, task in enumerate(tasks, start=1):
                print(f"{i}. {task}")

    elif choice == "2":
        task = input("Nhập công việc mới: ")
        tasks.append(task)
        print("Đã thêm công việc!")

    elif choice == "3":
        print("Tạm biệt!")
        break

    else:
        print("Lựa chọn không hợp lệ.")