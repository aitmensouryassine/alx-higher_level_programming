#include <Python.h>
#include <object.h>
#include <listobject.h>

/**
 * print_python_list_info - prints some basic info about Python lists.
 * @p: Python Object
 */
void print_python_list_info(PyObject *p)
{
	Py_ssize_t size = PyList_Size(p), i = 0;
	PyObject *iter = PyObject_GetIter(p), *item;

	printf("[*] Size of the Python List = %d\n", (int)size);
	printf("[*] Allocated = %d\n", (int)Py_SIZE(p));

	while (i < size)
	{
		item = PyIter_Next(iter);

		printf("Element %d: ", (int)i);
		if (PyFloat_Check(item))
		{
			printf("float\n");
		}
		else if (PyTuple_Check(item))
		{
			printf("tuple\n");
		}
		else if (PyList_Check(item))
		{
			printf("list\n");
		}
		else if (PyUnicode_Check(item))
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
