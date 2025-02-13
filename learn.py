def outer(var):
    rem = "remembered"
    def inner():
        print(var, rem)
    return inner

my_inner = outer("hello")
my_inner2 = outer("hi")

my_inner(), my_inner2()

