#!/usr/local/bin/python3
import dis

# https://opensource.com/article/18/4/introduction-python-bytecode
# http://www.goldsborough.me/python/low-level/2016/10/04/00-31-30-disassembling_python_bytecode/
# Hacking bytecode: http://www.bravegnu.org/blog/python-byte-code-hacks.html
# Patching bytecode: https://rushter.com/blog/python-bytecode-patch/
# Python .pyc internals: https://nedbatchelder.com/blog/200804/the_structure_of_pyc_files.html
# Python 30K ft view: https://leanpub.com/insidethepythonvirtualmachine/read
# UC Irvine: https://www.ics.uci.edu/~brgallar/week9_3.html

foo=15

def hello(n=3):
    global foo
    
    user="bob"
    print("world", user, 255)
    print("foo: ", foo)
    foo +=1
    print("foo:", foo)
    return foo

# Run it.
print("execution:","*"*10)
hello()
print()





# This code inspects function above.
print("Disassembly of hello")
print()
print("LINENO       OP OP_NAME                  IDX RESOLVED")
print("="*50)
dis.dis(hello)

print("")
print("")

# Note: most of __code__ is immutable so hacking it, requires new objects.
print("code internals:")
print(hello.__code__)

# tuple of any literals that occur in function body.
print("__code__.co_consts:")
for i, val in enumerate(hello.__code__.co_consts):
    print(str(i)+": ",val)
print()

# tuple of names of local vars in func body.
print("__code__.co_varnames:")
for i, val in enumerate(hello.__code__.co_varnames):
    print(str(i)+": ",val)
print()

# tuple of non-local names referenced in func body.
print("__code__.co_names")
for i, val in enumerate(hello.__code__.co_names):
    print(str(i)+": ",val)
print()

# Actual binary opcode instructions for func.
print("__code__.co_code")
# Raw bytes.
# print(hello.__code__.co_code)
# As integers
print(list(hello.__code__.co_code))

#for i, ch in enumerate(hello.__code__.co_code):
#    print("%d: %02X".format(i, ord(ch))

# Dumps all co_* fields in a single shot.
def all_co(obj):
    for attr in dir(obj.__code__):
        if attr.startswith('co_'):
            print("  %s = %s" % (attr, obj.__code__.__getattribute__(attr)))

#all_co(hello)

