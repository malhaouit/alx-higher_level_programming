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

	int bytes;
	if (size < 10)
        {
                bytes = size + 1;
                printf("  first %d bytes: ", bytes);
        }
	else
	{
		bytes = 10;
		printf("  first %d bytes: ", bytes);
	}

	for (i = 0; i < bytes; ++i)
	{
		if (bytes == 10)
			printf("%02x ", (unsigned char)str[i]);
		else
		{
			if (i != bytes - 1)
				printf("%02x ", (unsigned char)str[i]);
			else
				printf("00");
	}
	printf("\n");
}
