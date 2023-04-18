initial_velocity = float(input("Введите начальную скорость (в м/с): "))
acceleration = float(input("Введите ускорение (в м/c^2): "))
time = float(input("Введите время движения (в секундах): "))

distance = initial_velocity * time + (0.5 * acceleration * time ** 2)

print("Расстояние, которое пройдет объект: ", distance, "м")
