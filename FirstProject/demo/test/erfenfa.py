#-*- conding:utf-8 -*-

def bisection_method(que,num,left=0,right=0):
    if left == right:
        assert num == que[left]
        return left
    else:
        middle = (right+left) // 2
        if num > que[middle]:
            return bisection_method(que,num,middle+1,right)
        else:
            return bisection_method(que,num,left,middle)


list_test = range(1,100)
print bisection_method(list_test,99,left=0,right=len(list_test)-1)
