count_w_s=7
count_w_m=6
count_w_l=2
count_b_s=8
count_b_m=5
count_b_l=2
def available(color,size):
    global count_w_s
    global count_w_m
    global count_w_l
    global count_b_s
    global count_b_m
    global count_b_l
    if color=="white":
        if size=="s" and count_w_s != 0:
            count_w_s-=1
            print("white small size")
            print("order confirm white shirt small size")
        elif size=="m" and count_w_m != 0:
            count_w_m-=1
            print("white medium")
            print("order confirm white shirt medium size")
        elif size=="l" and count_w_l != 0:
            count_w_l
            count_w_l -= 1
            print(count_w_l)
            print("white large")
            print("order confirm white shirt large size")
        else:
            print("required stock is unavailable at the moment")
    elif color=="blue":
        if size=="s" and count_b_s != 0:
            count_b_s-=1
            print("blue small size")
            print("order confirm blue shirt small size")
        elif size=="m" and count_b_m != 0:
            count_b_m-=1
            print("blue medium")
            print("order confirm blue shirt medium size")
        elif size=="l" and count_b_l != 0:
            count_b_l-=1
            print("blue large")
            print("order confirm blue shirt large size")
        else:
            print("required stock is unavailable at the moment")
    else:
        print("color or size invalid")
while True:
    available(input("enter color"),input("enter size"))
