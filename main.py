total_sum = 0
while True:
    try:
        tickets_count = int(input("Введите количество билетов: "))
        if tickets_count <= 0:
            print("Количество билетов не может быть нулем или отрицательным!")
            continue
        break
    except ValueError:
        print("Введите целое число!")

for i in range(tickets_count):
    while True:
        try:
            age = int(input(f"Введите возраст посетителя для билета №{i + 1}: "))
            if age < 0:
                print("Возраст не может быть отрицательным!")
                continue
            break
        except ValueError:
            print("Введите целое число!")
    if age < 18:
        price = 0
    elif 18 <= age <= 25:
        price = 990
    else:
        price = 1390

    total_sum += price

if tickets_count > 3:
    total_sum *= 0.9

print("Сумма к оплате: ", total_sum)