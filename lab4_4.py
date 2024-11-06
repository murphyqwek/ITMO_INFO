import time

main, dop1, dop2, dop3 = 0, 0, 0, 0

start_time = time.perf_counter()
for i in range(100):
    import lab4
end_time = time.perf_counter()

main = end_time - start_time

start_time = time.perf_counter()
for i in range(100):
    import lab4_1
end_time = time.perf_counter()

dop1 = end_time - start_time

start_time = time.perf_counter()
for i in range(100):
    import lab4_2
end_time = time.perf_counter()

dop2 = end_time - start_time

start_time = time.perf_counter()
for i in range(100):
    import lab4_3
end_time = time.perf_counter()

dop3 = end_time - start_time


print("\n\n\n\n\n\n\n")

print(f"Основное задание - {main}")

print(f"Дополнительное задание 1 - {dop1}")

print(f"Дополнительное задание 2 - {dop2} ")

print(f"Дополнительное задание 3 - {dop3} ")