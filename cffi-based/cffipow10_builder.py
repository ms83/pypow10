from cffi import FFI
ffibuilder = FFI()

ffibuilder.cdef("long long powerof10(long long);")

ffibuilder.set_source("cffipow10",
r"""
    static long long powerof10(long long x)
    {
        long long x2 = x*x;
        long long x4 = x2*x2;
        long long x8 = x4*x4;
        return x2*x8;
    }
""")

if __name__ == "__main__":
    ffibuilder.compile(verbose=True)
