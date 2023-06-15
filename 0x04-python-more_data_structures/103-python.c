#include <Python.h>
#include <object.h>
#include <listobject.h>

void print_python_bytes(PyObject *p);

/**
 * print_python_list - prints basic infos about python lists
 * @p: python object
 */
void print_python_list(PyObject *p)
{
	PyListObject *list;
	Py_ssize_t size = PyList_Size(p), i = 0;

	list = (PyListObject *)p;

	printf("[*] Python list info\n");
	printf("[*] Size of the Python List = %d\n", (int)size);
	printf("[*] Allocated = %d\n", (int)list->allocated);

	while (i < size)
	{
		printf("Element %d: %s\n", (int)i, ((list->ob_item[i])->ob_type)->tp_name);
		if (PyBytes_Check(list->ob_item[i]))
			print_python_bytes(list->ob_item[i]);
		i++;
	}
}

/**
 * print_python_bytes - prints basic infos about python bytes objects
 * @p: python object
 */
void print_python_bytes(PyObject *p)
{
	Py_ssize_t size, size_to_print, i = 0;
	char *pybyte_as_str;

	printf("[.] bytes object info\n");
	if (!PyBytes_Check(p))
	{
		printf("  [ERROR] Invalid Bytes Object\n");
		return;
	}

	size = ((PyVarObject *)(p))->ob_size;
	pybyte_as_str = ((PyBytesObject *)p)->ob_sval;

	printf("  size: %d\n", (int)size);
	printf("  trying string: %s\n", pybyte_as_str);

	if (size >= 10)
		size_to_print = 10;
	else
		size_to_print = size + 1;

	printf("  first %d bytes: ", (int)size_to_print);
	for (i = 0; i < size_to_print; i++)
	{
		printf("%02x", (unsigned char)pybyte_as_str[i]);
		if (i == size_to_print - 1)
			printf("\n");
		else
			printf(" ");
	}
}
