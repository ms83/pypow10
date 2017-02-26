#include <Python.h>

static PyObject *
extpow10_pow10(PyObject *self, PyObject *args)
{
    int x;

    if (!PyArg_ParseTuple(args, "i", &x))
        return NULL;

    long long x2 = x*x;
    long long x4 = x2*x2;
    long long x8 = x4*x4;

    return Py_BuildValue("L", x2*x8);
}

static PyMethodDef extpow10Methods[] = {
    {"pow10", extpow10_pow10, METH_VARARGS, "Calculate power of 10 of given argument."},
    {NULL, NULL, 0, NULL}  
};

PyMODINIT_FUNC
initextpow10(void)
{
    (void) Py_InitModule("extpow10", extpow10Methods);
}
