import concurrent.futures
import time

def calc_cube(numbers):
    print("calculate cube of numbers")
    for n in numbers:
        time.sleep(0.2)
        print('cube:',n*n*n)

arr = [2,3,8,9]
if _name_ == "_main_":
    with concurrent.futures.ThreadPoolExecutor() as executor:
        start_time = time.perf_counter()
        result = list(executor.map(calc_cube, arr))
        finish_time = time.perf_counter()
    print(f"Program finished in {finish_time-start_time} seconds")
    print(result)
