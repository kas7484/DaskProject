import time
import random


from dask.distributed import Client, wait, progress, as_completed

def logic(b):
    subtotal = 0
    for i in range(b):
        x = random.uniform(-1, 1)
        y = random.uniform(-1, 1)
        if x*x + y*y <= 1:
            subtotal = subtotal + 1 
    return subtotal
    
    
def pi(n):
    with Client(n_workers=4) as c:
        start = time.perf_counter()
        workers_results = c.map(logic, [n]*n)
        total = c.gather(workers_results)
        pi = 4 * sum(total) / (n * n)
        end = time.perf_counter()
        total_time = end - start
        print(f"The estimate for pi is {pi} in {total_time} time")
