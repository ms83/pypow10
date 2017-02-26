from timeit import timeit
import extpow10
import cythonpow10
import cffipow10

# Number of iterations
N = 1<<24

# Calculate max 64b number which power of 10 not cause overflow 
modulo = 0
while (modulo+1)**10 < (1<<63):
    modulo += 1

def run_test(f):
    total = 0
    for i in range(N):
        total += f(i%modulo)
    print total

def test_normal():
    run_test(lambda x: x**10)

def test_extension():
    run_test(extpow10.pow10)

def test_cython(N):
    run_test(cythonpow10.pow10)

def test_cffi(N):
    run_test(cffipow10.lib.powerof10)
 
 
if __name__ == '__main__':
    # 5.38 sec
    print(timeit('test_normal()', number=1, setup='from __main__ import test_normal'))

    # 3.93 sec
    print(timeit('test_extension()', number=1, setup='from __main__ import test_extension'))

    # 3.52 sec
    print(timeit('test_cython(1<<22)', number=1, setup='from __main__ import test_cython'))

    # 3.34
    print(timeit('test_cffi(1<<22)', number=1, setup='from __main__ import test_cffi'))
