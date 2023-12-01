#include <stdlib.h>
#include <stdio.h>
#include <Python.h>
/**
 * print_python_list_info -  function that prints size Python lists
 * @p: python list and also acts as parameter.
 */
void print_python_list_info(PyObject *p)
{
	int listindex;

	printf("[*] Size of the Python List = %lu\n", Py_SIZE(p));
	printf("[*] Allocated = %lu\n", ((PyListObject *)p)->allocated);
	for (listindex = 0; listindex < Py_SIZE(p); listindex++)
		printf("Element %d: %s\n", listindex, Py_TYPE(PyList_GetItem(p, listindex))->tp_name);
}
