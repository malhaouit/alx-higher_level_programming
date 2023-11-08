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
	PyObject *plo;

	printf("[*] Size of the Python List = %d\n", (int)Py_SIZE(p));
	printf("[*] Allocated = %d\n", (int)((PyListObject *)p)->allocated);

	for (i = 0; i < Py_SIZE(p); i++)
	{
		printf("Element %d: ", i);
		plo = PyList_GetItem(p, i);
		printf("%s\n", Py_TYPE(plo)->tp_name);
	}
}
