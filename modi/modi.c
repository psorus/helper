#define PY_SSIZE_T_CLEAN
#include <Python.h>
#include <structmember.h>
/*#include "pycore_object.h"*/ /* _PyObject_Init()*/
#include "math.h"

long qmm(long alpha,long beta,long a,long b){
    long x=alpha;
    long mode=a*b;
    while(x%b!=beta){x=(x+a)%(mode);}
    return x;
}
typedef struct {
    PyObject_HEAD
    long value;
    long modulo;
    /* Type-specific fields go here. */
} ModiObject;



static void modi_dealloc(ModiObject *self){
    /*Py_XDECREF(self->value); dont need this, since it is c++ type?*/
    Py_TYPE(self)->tp_free((PyObject *) self);

}
static int modi_init(ModiObject *self, PyObject *args, PyObject *kwds)
{
    static char *kwlist[] = {"value","modulo", NULL};

    if (!PyArg_ParseTupleAndKeywords(args, kwds, "|ii", kwlist,&self->value,&self->modulo))
        return -1;

    return 0;
}


static PyMemberDef Modi_members[] = {
    {"value", T_INT, offsetof(ModiObject, value), 0,
     "value of this object, similar to a python int"},
    {"modulo", T_INT, offsetof(ModiObject, modulo), 0,
     "maximum possible value of value, after which it loops around"},
    {NULL}  /* Sentinel */
};

static PyMethodDef Modi_methods[] = {
    /*{"negate", (PyCFunction) modi_negate, METH_NOARGS,
     "Negate the probability"
    },*/
    {NULL}  /* Sentinel */
};


static PyTypeObject ModiType;
PyObject * Modi_Fromlong(long fval,long modu)
{
    ModiObject *ret;
    ret=PyObject_Malloc(sizeof(ModiObject));
    if(!ret){return PyErr_NoMemory();}
    PyObject_Init((PyObject*)ret,&ModiType);
    /*ModiObject* ret;*/
    ret->value=fval;
    ret->modulo=modu;
    return (PyObject *)ret;
    /*return (PyObject *)ret;
*//*
    struct _Py_float_state *state = get_float_state();
    PyFloatObject *op = state->free_list;
    if (op != NULL) {
#ifdef Py_DEBUG
        // PyFloat_FromDouble() must not be called after _PyFloat_Fini()
        assert(state->numfree != -1);
#endif
        state->free_list = (PyFloatObject *) Py_TYPE(op);
        state->numfree--;
    }
    else {
        op = PyObject_Malloc(sizeof(PyFloatObject));
        if (!op) {
            return PyErr_NoMemory();
        }
    }
    _PyObject_Init((PyObject*)op, &PyFloat_Type);
    op->ob_ival = fval;
    return (PyObject *) op;
*/
}
static PyObject * modi_add(PyObject *a, PyObject *b)
{
    /*
     * Combine add two values, respect moduli
    */
    long va;
    long modulo=-1;
    if(PyLong_Check(a)){
        va=PyLong_AsLong(a);
    }else if(PyFloat_Check(a)){
        va=(long)PyFloat_AsDouble(a);
    }else{
        va=((ModiObject *)a)->value;
        modulo=((ModiObject *)a)->modulo;
    }
    long vb;
    if(PyLong_Check(b)){
        vb=PyLong_AsLong(b);
    }else if(PyFloat_Check(b)){
        vb=(long)PyFloat_AsDouble(b);
    }else{
        vb=((ModiObject *)b)->value;
        modulo=((ModiObject *)b)->modulo;
    }
    return Modi_Fromlong((va+vb)%modulo,modulo);
}
static PyObject * modi_mult(PyObject *a, PyObject *b)
{
    /*
     * Multiply and respect moduli
    */
    long va;
    long modulo=-1;
    if(PyLong_Check(a)){
        va=PyLong_AsLong(a);
    }else if(PyFloat_Check(a)){
        va=(long)PyFloat_AsDouble(a);
    }else{
        va=((ModiObject *)a)->value;
        modulo=((ModiObject *)a)->modulo;
    }
    long vb;
    if(PyLong_Check(b)){
        vb=PyLong_AsLong(b);
    }else if(PyFloat_Check(b)){
        vb=(long)PyFloat_AsDouble(b);
    }else{
        vb=((ModiObject *)b)->value;
        modulo=((ModiObject *)b)->modulo;
    }
    return Modi_Fromlong((va*vb)%modulo,modulo);
}


static PyObject * modi_float(PyObject *v)
{
    return PyFloat_FromDouble((double)(((ModiObject *)v)->value));
}
static PyObject * modi_long(PyObject *v)
{
    return PyLong_FromLong((((ModiObject *)v)->value));
}




static PyNumberMethods modi_as_number = {
    modi_add,          /* nb_add */
    0,          /* nb_subtract */
    modi_mult,          /* nb_multiply */
    0,          /* nb_remainder */
    0,       /* nb_divmod */
    0,          /* nb_power */
    0, /* nb_negative */
    0,        /* nb_positive */
    0, /* nb_absolute */
    0, /* nb_bool */
    0,                  /* nb_invert */
    0,                  /* nb_lshift */
    0,                  /* nb_rshift */
    0,                  /* nb_and */
    0,                  /* nb_xor */
    0,                  /* nb_or */
    modi_long, /* nb_int */
    0,                  /* nb_reserved */
    modi_float,        /* nb_float */
    0,                  /* nb_inplace_add */
    0,                  /* nb_inplace_subtract */
    0,                  /* nb_inplace_multiply */
    0,                  /* nb_inplace_remainder */
    0,                  /* nb_inplace_power */
    0,                  /* nb_inplace_lshift */
    0,                  /* nb_inplace_rshift */
    0,                  /* nb_inplace_and */
    0,                  /* nb_inplace_xor */
    0,                  /* nb_inplace_or */
    0,    /* nb_floor_divide */
    0,          /* nb_true_divide */
    0,                  /* nb_inplace_floor_divide */
    0,                  /* nb_inplace_true_divide */
};

static PyObject * modi_repr(PyObject * self){
   return PyUnicode_FromFormat("%ld modulo %ld",((ModiObject *)self)->value,((ModiObject *)self)->modulo);
}


static PyObject * gmmpy(PyObject *self, PyObject *args)
{
    ModiObject *a;
    ModiObject *b;
    if (!PyArg_ParseTuple(args, "OO", &a,&b))
        return NULL;
    int ret=qmm(a->value,b->value,a->modulo,b->modulo);
    return Modi_Fromlong(ret,a->modulo*b->modulo);
    /*return PyFloat_FromDouble(val);*/
}






static PyMethodDef ModiMethods[] = {
    {"merge",gmmpy,METH_VARARGS,"Combine a modular object (alpha modulo a) with another one (beta modulo b) into one (gamma modulo a*b)"},
    /*{"sigmoid",  sigmoid_function, METH_VARARGS,"Evaluate a sigmoid function into a modi probability"},
    {"heaviside",  heaviside_function, METH_VARARGS,"Evaluate a heaviside function into a modi probability"},*/
    {NULL, NULL, 0, NULL}        /* Sentinel */
};



static PyTypeObject ModiType = {
    PyVarObject_HEAD_INIT(NULL, 0)
    .tp_name = "modi.Modi",
    .tp_doc = "Modi objects",
    .tp_basicsize = sizeof(ModiObject),
    .tp_itemsize = 0,
    .tp_flags = Py_TPFLAGS_DEFAULT | Py_TPFLAGS_BASETYPE,
    .tp_new = PyType_GenericNew,
    .tp_dealloc=(destructor) modi_dealloc,
    .tp_init= (initproc) modi_init,
    .tp_members=Modi_members,
    .tp_methods=Modi_methods,
    .tp_as_number=&modi_as_number,
    .tp_repr=modi_repr,
};




static PyModuleDef modimodule = {
    PyModuleDef_HEAD_INIT,
    .m_name = "modi",
    .m_doc = "Example module that creates an extension type, which allows for integer manipulation with respect to a modulo.",
    .m_size = -1,
    ModiMethods
};

PyMODINIT_FUNC
PyInit_modi(void)
{
    PyObject *m;
    if (PyType_Ready(&ModiType) < 0)
        return NULL;

    m = PyModule_Create(&modimodule);
    if (m == NULL)
        return NULL;

    Py_INCREF(&ModiType);
    if (PyModule_AddObject(m, "Modi", (PyObject *) &ModiType) < 0) {
        Py_DECREF(&ModiType);
        Py_DECREF(m);
        return NULL;
    }

    return m;
}
