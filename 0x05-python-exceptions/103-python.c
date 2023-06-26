#include <Python.h>

void print_python_bytes(PyObject *p);
void print_python_float(PyObject *p);
void print_python_bytes(PyObject *p);

/**
 * print_python_list - print some basic info about Python lists
 * @p: python list
 */
void print_python_list(PyObject *p)
{
	PyListObject *list;
	Py_ssize_t  size, i;

	fflush(stdout);
	printf("[*] Python list info\n");

	if (!PyList_Check(p))
	{
		printf("  [ERROR] Invalid List Object\n");
		return;
	}

	list = (PyListObject *)p;
	size = PyList_GET_SIZE(p);

	printf("[*] Size of the Python List = %ld\n", size);
	printf("[*] Allocated = %ld\n", list->allocated);

	for (i = 0; i < size; i++)
	{
		printf("Element %ld: %s\n", i, list->ob_item[i]->ob_type->tp_name);
		if (PyBytes_Check(list->ob_item[i]))
			print_python_bytes(list->ob_item[i]);
		else if (PyFloat_Check(list->ob_item[i]))
			print_python_float(list->ob_item[i]);
	}
}

/**
 * print_python_bytes - print some basic info about Python bytes
 * @p: python list
 */
void print_python_bytes(PyObject *p)
{
	PyBytesObject *b;
	PyVarObject *v;
	Py_ssize_t size, size_to_print, i;
	char *str;

	fflush(stdout);
	printf("[.] bytes object info\n");

	if (!PyBytes_Check(p))
	{
		printf("  [ERROR] Invalid Bytes Object\n");
		return;
	}

	b = (PyBytesObject *)p, str = b->ob_sval;
	v = (PyVarObject *)(p), size = v->ob_size;

	if (size >= 10)
		size_to_print = 10;
	else
		size_to_print = size + 1;

	printf("  size: %ld\n", size);
	printf("  trying string: %s\n", str);
	printf("  first %ld bytes: ", size_to_print);
	for (i = 0; i < size_to_print; i++)
	{
		printf("%02x", (unsigned char)str[i]);
		if (i == size_to_print - 1)
			printf("\n");
		else
			printf(" ");
	}
}


/**
 * print_python_float - print some basic info about Python float object
 * @p: python list
 */
void print_python_float(PyObject *p)
{
	PyFloatObject *f;

	fflush(stdout);
	printf("[.] float object info\n");

	if (!PyFloat_Check(p))
	{
		printf("  [ERROR] Invalid Float Object\n");
		return;
	}

	f = (PyFloatObject *)p;

	printf("  value: %s\n",
	       PyOS_double_to_string(f->ob_fval, 'r',
				     0, Py_DTSF_ADD_DOT_0, NULL));
}
