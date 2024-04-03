#include <Python.h>

/**
 * print_python_list - prints info about Python lists
 * @p: PyObject list
 */
void print_python_list(PyObject *p)
{
    Py_ssize_t size, i;
    PyListObject *list;

    printf("[*] Python list info\n");
    printf("[*] Size of the Python List = %ld\n", PyList_Size(p));
    printf("[*] Allocated = %ld\n", ((PyListObject *)p)->allocated);

    size = PyList_Size(p);
    list = (PyListObject *)p;
    for (i = 0; i < size; i++)
    {
        printf("Element %ld: %s\n", i, Py_TYPE(list->ob_item[i])->tp_name);
    }
}

/**
 * print_python_bytes - prints info about Python bytes
 * @p: PyObject bytes
 */
void print_python_bytes(PyObject *p)
{
    Py_ssize_t size, i;
    unsigned char *string;
    char *bytes_str;

    printf("[.] bytes object info\n");
    if (!PyBytes_Check(p))
    {
        printf("  [ERROR] Invalid Bytes Object\n");
        return;
    }

    size = PyBytes_Size(p);
    string = (unsigned char *)PyBytes_AsString(p);
    bytes_str = (size > 10) ? "trying string" : "first";
    printf("  size: %ld\n", size);
    printf("  %s %ld bytes: ", bytes_str, size);
    for (i = 0; i < size && i < 10; i++)
    {
        printf("%02x%c", string[i], (i == size - 1 || i == 9) ? '\n' : ' ');
    }
}

/**
 * print_python_float - prints info about Python float
 * @p: PyObject float
 */
void print_python_float(PyObject *p)
{
    double value;

    printf("[.] float object info\n");
    if (!PyFloat_Check(p))
    {
        printf("  [ERROR] Invalid Float Object\n");
        return;
    }

    value = ((PyFloatObject *)p)->ob_fval;
    printf("  value: %.*g\n", 16, value);
}

