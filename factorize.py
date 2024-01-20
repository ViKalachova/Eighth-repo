import time
from multiprocessing import Pool, cpu_count


def factorize(*number):
    for n in number:
        i = 1
        divisors = []
        while i ** 2 <= n:
            if n % i == 0:
                divisors.append(i)
                if i != n // i:
                    divisors.append(n // i)
            i += 1
        divisors.sort()
        print(divisors)

def callback(divisors):
    print(divisors)



if __name__ == '__main__':
    start = time.time()
    a = factorize(128, 255, 99999, 10651060)
    end = time.time() - start
    print(a, end)

    start1 = time.time()
    with Pool(cpu_count()) as p:
        p.apply_async(factorize(128), callback=callback)
        p.apply_async(factorize(255), callback=callback)
        p.apply_async(factorize(99999), callback=callback)
        p.apply_async(factorize(10651060), callback=callback)
        p.close()
        p.join()
    end2 = time.time() - start1
    print(end2)
