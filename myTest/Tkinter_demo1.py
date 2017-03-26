#-*- coding:utf-8 -*-
from Tkinter import *
import tkMessageBox

top = Tk()
top.title("计算总数量")
top.geometry('300x600')

baseNum = Label(top,text='基数：')
baseNum.pack()
base_text = StringVar()
base = Entry(top, textvariable = base_text)
base_text.set(" ")
base.pack()


growthRate = Label(top,text='增长率：')
growthRate.pack()
growth_text = StringVar()
growth = Entry(top, textvariable = growth_text)
growth_text.set('0.0115')
growth.pack()


useTime = Label(top,text='时间（天）：')
useTime.pack()
time_text = StringVar()
times = Entry(top, textvariable = time_text)
time_text.set(" ")
times.pack()

#定义求总和函数
def sum_test(baseNum,growthRate,time):
    return baseNum * (1+growthRate)**(time)

#定义增长函数
def add_sum (baseNum,growthRate,time):
    return baseNum * (1+growthRate)**(time) - baseNum


#定义第N天增长数函数
def add_num (baseNum,growthRate,time):
    return baseNum *growthRate* (1+growthRate)**(time-1)


#定义显示结果函数

def on_show(re_sum,re_add,add_Num,times):
    show_top = Tk()
    show_top.title("计算结果显示")
    show_top.geometry('300x600')
    print "+++++++++"
    print (re_add)
    print(re_sum)
    print(add_Num)

    # 显示第N天增长数
    addNum1 = Label(show_top, text='第%d天增长数：' % times)
    addNum1.pack()
    num_text1 = StringVar()
    add_Nums1 = Entry(show_top, textvariable=num_text1)
    num_text1.set('22')
    add_Nums1.pack()

    # 显示增长数
    add_Sums = Label(show_top, text='增长总数：')
    add_Sums.pack()
    add_text = StringVar()
    adds = Entry(show_top, textvariable=add_text)
    add_text.set(re_add)
    adds.pack()
    # 显示总数
    Sums = Label(show_top, text='总数：')
    Sums.pack()
    sum_text = StringVar()
    sums = Entry(show_top, textvariable=sum_text)
    sum_text.set(re_sum)
    sums.pack()

    show_top.mainloop()



def on_click():
    #获取输入信息
    if base_text.get().strip() == '':
        tkMessageBox.showinfo(title='基数', message='基数为空，请输入有效的数值！')
    else:
        base_Num = float(base_text.get())

    if growth_text.get().strip() == '':
        tkMessageBox.showinfo(title='增长率', message='增长率为空，请输入有效的数值！')
    else:
        growth_Rate = float(growth_text.get())

    if time_text.get().strip() == '':
        tkMessageBox.showinfo(title='时间', message='时间为空，请输入有效的数值！')
    elif float(time_text.get()) < 1:
        tkMessageBox.showinfo(title='时间', message='时间小于1，请输入大于或等于1的数值！')
    else:
        temp_time = float(time_text.get())
        times = int(temp_time)

    #print(growth_Rate)
    #print(times)
    re_sum = sum_test(base_Num,growth_Rate,times)
    #四舍五入保留小数点后两位
    re_sum = round(re_sum,2)
    #print type(re_sum)
    re_add = add_sum(base_Num,growth_Rate,times)
    #四舍五入保留小数点后两位
    re_add = round(re_add, 2)

    add_Num = add_num(base_Num,growth_Rate,times)
    add_Num = round(add_Num, 2)

    print (re_add)
    print(re_sum)
    print(add_Num)

    # 显示第N天增长数
    addNum = Label(top, text='第%d天增长数：' % times)
    addNum.pack()
    num_text = StringVar()
    add_Nums = Entry(top, textvariable=num_text)
    num_text.set(add_Num)
    add_Nums.pack()

    # 显示增长数
    add_Sums = Label(top, text='增长总数：')
    add_Sums.pack()
    add_text = StringVar()
    adds = Entry(top, textvariable=add_text)
    add_text.set(re_add)
    adds.pack()
    # 显示总数
    Sums = Label(top, text='总数：')
    Sums.pack()
    sum_text = StringVar()
    sums = Entry(top, textvariable=sum_text)
    sum_text.set(re_sum)
    sums.pack()

#调用显示函数
    on_show(re_sum,re_add,add_Num,times)



    #string = str("基数是：%s 增长率是：%s 时间是:%s 天" %(base_Num,times,growth_Rate))
    #print("基数是：%s 增长率是：%s 时间是:%s 天" %(base_Num,times,growth_Rate))
    #python 3  是 messagebox
    #messagebox.showinfo(title='测试', message = string)

Button(top,text="计算",command = on_click).pack()


top.mainloop()

if __name__ == '__main__':
    pass