#include <Python.h>

void print_python_list(PyObject *p);
void print_python_bytes(PyObject *p);

/**
 * print_python_list - Prints some basic info about Python lists
 * @p: Python object
 *
 * Return: Nothing
 */
void print_python_list(PyObject *p)
{
        int i;
        Py_ssize_t size, allocated;
        PyObject *plo;

        size = PyList_Size(p);
        allocated = ((PyListObject *)p)->allocated;

        printf("[*] Python list info\n");
        printf("[*] Size of the Python List = %zd\n", size);
        printf("[*] Allocated = %zd\n", allocated);

        for (i = 0; i < size; i++)
        {
                printf("Element %d: ", i);
                plo = PyList_GET_ITEM(p, i);
                printf("%s\n", plo->ob_type->tp_name);
                if (strcmp(plo->ob_type->tp_name, "bytes") == 0)
                        print_python_bytes(plo);

        }
}

/**
 * print_python_bytes - Prints some basic info about Python bytes objects
 * @p: Python object
 *
 * Return: Nothing
 */
void print_python_bytes(PyObject *p)
{
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

        printf("  size: %zd\n", size);
        printf("  trying string: %s\n", str);

        if (size < 10)
        {
                size = size + 1;
        }
        else
        {
                size = 10;
        }
        printf("  first %zd bytes: ", size);
        for (i = 0; i < size; ++i)
        {
                printf("%02hhx", (unsigned char)str[i]);
                if (i == (size - 1))
                        printf("\n");
                else
                        printf(" ");
        }
}
