import pyspark
print("Done")

def myFun(arg1, *argv):
    print("First argument :", arg1)
    print(type(argv))
    # argv(1) = "from"
    argv = list(argv)
    argv[1] = "from"
    print(type(argv))
    for arg in argv:
        print("Next argument through *argv :", arg)