#include <Python.h>

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

        printf("[*] Size of the Python List = %zd\n", size);
        printf("[*] Allocated = %zd\n", allocated);

        for (i = 0; i < size; i++)
        {
                printf("Element %d: ", i);
                plo = PyList_GET_ITEM(p, i);
                printf("%s\n", plo->ob_type->tp_name);
        }
}

void print_python_bytes(PyObject *p)
{
        (void)p;
}
