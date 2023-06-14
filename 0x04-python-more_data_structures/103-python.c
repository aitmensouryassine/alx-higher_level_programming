#include <Python.h>
#include <object.h>
#include <listobject.h>

/**
 * print_python_list - prints basic infos about python lists
 * @p: python object
 */
void print_python_list(PyObject *p)
{
	PyListObject *list = malloc(sizeof(PyObject *));
	Py_ssize_t size = PyList_Size(p), i = 0;

	list = (PyListObject *)p;

	printf("[*] Python list info\n");
	printf("[*] Size of the Python List = %d\n", (int)size);
	printf("[*] Allocated = %d\n", (int)list->allocated);

	while (i < size)
	{
		printf("Element %d: ", (int)i);
		if (PyFloat_Check(list->ob_item[i]))
		{
			printf("float\n");
		}
		else if (PyTuple_Check(list->ob_item[i]))
		{
			printf("tuple\n");
		}
		else if (PyList_Check(list->ob_item[i]))
		{
			printf("list\n");
		}
		else if (PyUnicode_Check(list->ob_item[i]))
		{
			printf("str\n");
		}
		else
		{
			printf("int\n");
		}
		i++;
	}
}

/**
 * print_python_bytes - prints basic infos about python bytes objects
 * @p: python object
 */
void print_python_bytes(PyObject *p)
{
	Py_ssize_t size = PyBytes_Size(p), size_to_print, i = 0;

	printf("[.] bytes object info\n");
	printf("  size: %d\n", (int)size);
	printf("  trying string: %s\n", PyBytes_AS_STRING(p));

	if (size >= 10)
		size_to_print = 10;
	else
		size_to_print = size + 1;

	printf("  first %d bytes: ", (int)size_to_print);
	for (i = 0; i < size_to_print; i++)
	{
		printf("%02x", (unsigned char)PyBytes_AS_STRING(p)[i]);
		if (i == size_to_print - 1)
			printf("\n");
		else
			printf(" ");
	}
}
