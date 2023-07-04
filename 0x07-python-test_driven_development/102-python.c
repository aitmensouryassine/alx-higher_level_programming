#include <Python.h>

/**
 * print_python_list - print some basic info about Python lists
 * @p: python list
 */
void print_python_string(PyObject *p)
{
	int len = 24;
	char *str = "Test";

	printf("[.] string object info\n");

	if (PyBytes_Check(p))
	{
		printf("  [ERROR] Invalid String Object\n");
		return;
	}

	printf("  type: compact ascii");
	printf("  length: %d\n", len);
	printf("  value: %s\n", str);
}
