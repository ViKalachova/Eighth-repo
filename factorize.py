import time
import logging
from multiprocessing import Pool, cpu_count


def factorize(number):
    i = 1
    divisors = []
    while i ** 2 <= number:
        if number % i == 0:
            divisors.append(i)
            if i != number // i:
                divisors.append(number // i)
        i += 1
    divisors.sort()
    return divisors

def sinhron_factorize(*numbers):
    start = time.time()
    result = []
    for number in numbers:
        result.append(factorize(number))
    end = time.time()
    logging.debug(f"Usual execution time: {end - start} seconds")
    print(result)
    return result

def parallel_factorize(*numbers):
    start = time.time()
    with Pool(cpu_count()) as p:
        result = p.map_async(factorize, numbers)
    end = time.time()
    logging.debug(f"Parallel execution time: {end - start} seconds")
    return result


if __name__ == '__main__':
    logging.basicConfig(level=logging.DEBUG, format='%(levelname)s: %(message)s')
    sinhron_factorize(128, 255, 99999, 10651060)
    parallel_factorize(128, 255, 99999, 10651060)