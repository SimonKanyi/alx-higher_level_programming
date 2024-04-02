#include <Python.h>

/**
 * print_python_bytes - Prints info about Python bytes objects
 * @p: PyObject
 */
void print_python_bytes(PyObject *p)
{
    PyBytesObject *bytes = (PyBytesObject *)p;
    Py_ssize_t size, i;
    char *string;

    printf("[.] bytes object info\n");
    if (!PyBytes_Check(p))
    {
        printf("  [ERROR] Invalid Bytes Object\n");
        fflush(stdout);
        return;
    }
    size = PyBytes_Size(p);
    printf("  size: %ld\n", size);
    string = PyBytes_AsString(p);
    if (size > 10)
        size = 10;
    else
        size++;
    printf("  trying string: %s\n", string);
    printf("  first %ld bytes: ", size);
    for (i = 0; i < size; i++)
    {
        printf("%02hhx", string[i]);
        if (i < size - 1)
            printf(" ");
    }
    printf("\n");
    fflush(stdout);
}

/**
 * print_python_list - Prints info about Python list objects
 * @p: PyObject
 */
void print_python_list(PyObject *p)
{
    PyListObject *list = (PyListObject *)p;
    Py_ssize_t size, i;
    PyObject *item;

    printf("[*] Python list info\n");
    if (!PyList_Check(p))
    {
        printf("  [ERROR] Invalid List Object\n");
        fflush(stdout);
        return;
    }
    size = PyList_Size(p);
    printf("[*] Size of the Python List = %ld\n", size);
    printf("[*] Allocated = %ld\n", list->allocated);
    for (i = 0; i < size; i++)
    {
        item = PyList_GetItem(p, i);
        printf("Element %ld: %s\n", i, Py_TYPE(item)->tp_name);
        if (PyBytes_Check(item))
            print_python_bytes(item);
    }
    fflush(stdout);
}

/**
 * print_python_float - Prints info about Python float objects
 * @p: PyObject
 */
void print_python_float(PyObject *p)
{
    PyFloatObject *f = (PyFloatObject *)p;
    double value;

    printf("[.] float object info\n");
    if (!PyFloat_Check(p))
    {
        printf("  [ERROR] Invalid Float Object\n");
        fflush(stdout);
        return;
    }
    value = f->ob_fval;
    printf("  value: %f\n", value);
    fflush(stdout);
}
