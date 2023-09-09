import time
import functools

def time_it(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        start_time = time.time()
        result = func(*args, **kwargs)
        end_time = time.time()
        print(f"{func.__name__} took {end_time - start_time:.6f} seconds to execute")
        return result
    return wrapper

@time_it
def say_hello(name: str) -> str:
    return "Hello " + name + "!"

print(say_hello("John")) # -> Output:
                         # say_hello took 0.000002 seconds to execute 
                         # Hello John!



