#include <Python.h>
#include <stdio.h>

void print_python_bytes(PyObject *p)
{
    PyBytesObject *bytes = (PyBytesObject *)p;
    Py_ssize_t size, i;
    char *str;

    printf("[.] bytes object info\n");
    if (!PyBytes_Check(p))
    {
        printf("  [ERROR] Invalid Bytes Object\n");
        return;
    }
    size = PyBytes_Size(p);
    str = PyBytes_AsString(p);
    printf("  size: %ld\n", size);
    printf("  trying string: %s\n", str);
    printf("  first %ld bytes: ", (size < 10) ? size : 10);
    for (i = 0; i < size && i < 10; i++)
    {
        printf("%02x", (unsigned char)str[i]);
        if (i < size - 1 && i < 9)
            printf(" ");
    }
    printf("\n");
}

void print_python_list(PyObject *p)
{
    PyListObject *list = (PyListObject *)p;
    Py_ssize_t size, i;
    PyObject *elem;

    printf("[*] Python list info\n");
    if (!PyList_Check(p))
    {
        printf("  [ERROR] Invalid Python List Object\n");
        return;
    }
    size = PyList_Size(p);
    printf("[*] Size of the Python List = %ld\n", size);
    printf("[*] Allocated = %ld\n", list->allocated);
    for (i = 0; i < size; i++)
    {
        elem = PyList_GetItem(p, i);
        printf("Element %ld: ", i);
        if (PyBytes_Check(elem))
            print_python_bytes(elem);
        else
            printf("%s\n", Py_TYPE(elem)->tp_name);
    }
}
