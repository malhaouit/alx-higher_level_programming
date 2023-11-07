#include <stdio.h>
#include <Python.h>

/**
 * print_python_list_info - Prints some basic info about Python lists
 * @p: Python object
 *
 * Return: Nothing
 */
void print_python_list_info(PyObject *p)
{
	int i;
	PyListObject *plo = (PyListObject *)p;

	printf("[*] Size of the Python List = %d\n", Py_SIZE(plo));
	printf("[*] Allocated = %d\n", plo->allocated);

	for (i = 0; i < Py_SIZE(plo); i++)
	{
		printf("Element %d: %s\n", i, Py_TYPE(PyList_GET_ITEM(p, i))->tp_name);
	}
}
