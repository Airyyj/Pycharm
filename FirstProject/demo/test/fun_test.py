#-*-coding:utf-8-*-
def fun_test(name,greeting):
    '在函数的开头注释部分即是函数的文档函数 ————关键字参数，调用时，关键字必须与参数名相同'
    print '%s,%s!' % (greeting,name)

fun_test(name="杨要军",greeting='Hello')

fun_test(greeting='Hello',name="杨要军")

'以下是查看文档函数的方法'

print fun_test.__doc__

print help(fun_test)