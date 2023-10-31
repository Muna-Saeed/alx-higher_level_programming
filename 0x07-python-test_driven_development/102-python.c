#include <Python.h>

void print_python_string(PyObject *p) {
    Py_ssize_t length;
    const char *value;

    if (!PyUnicode_Check(p)) {
        fprintf(stderr, "[ERROR] Invalid String Object\n");
        return;
    }

    length = PyUnicode_GET_LENGTH(p);
    value = PyUnicode_AsUTF8AndSize(p, &length);

    printf("[.] string object info\n");
    printf("  type: %s\n", PyUnicode_IS_COMPACT_ASCII(p) ? "compact ascii" : "compact unicode object");
    printf("  length: %ld\n", length);
    printf("  value: %s\n", value);
}
