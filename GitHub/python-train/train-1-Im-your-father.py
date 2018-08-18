import time
d=" Father.I am sorry.I failed you.I didn't know how to win.I had to invent new rules.I thought you would want me to stay alive.Now you are not sure.if you think I have lost my way.maybe I should die.I will not suffer.If I do not survive.thank you.for creating me."

d=d.lstrip()  #去除字符串前后的空格
d=d.lower()   #大写转换为小写
d=d.upper()   #小写转换为大写
new_d=d.split(".") #按照括号内的字符分割，默认为空格
for x in new_d:
    print(x)
    time.sleep(1)  #延时1秒
    print()        #换行