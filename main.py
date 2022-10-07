import random
import time

hist = [0] * 10
times = [0] * 100 

def main():
    for i in range(100):
        buffer = get_random_nums()
        start_time = time.time_ns()
        calc_gyst(histogram = buffer)
        times[i] = time.time_ns() - start_time
    
    times.sort()
    print(f"Gystogram time is: {round(times[49] / 1000000, 4)} ms.")


def get_random_nums():
    arr = [0] * 1000000
    for i in range(1000000):
        arr[i] = random.randint(0, 999)
    return arr


def calc_gyst(histogram):
    for i in histogram:
        hist[(i // 100)] += 1


main()