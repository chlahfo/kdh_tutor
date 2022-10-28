import random
all_nums=list(range(1, 46))
for i in range(6):
    a = random.randint(1, 45) 
    pic_num=all_nums.pop(a)
    print(pic_num)
    