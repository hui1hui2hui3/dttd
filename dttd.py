"""
电梯难题1：轨道电梯

电梯正常情况下可以一次同行2人，速度为1；但由于上班族早晚高峰，导致一侧速度为2，一侧速度为1
假如现在有50人要上电梯，
策略1：同时2人，上电梯不加速
策略2: 1侧加速，1侧不加速正常上电梯，
请计算那种策略下，通过的时间最短

结论：
1. 和人数无关
2. 决定因素为 参与加速人员比率 和  参与的人员速度
关键点：
当30%的人参与，速度达到其他人员4.5倍时，第二种更加省时
加速耗时 比率：0.30，速度：4.5，耗时：48.8
加速耗时 比率：0.50，速度：3.5，耗时：44.4
加速耗时 比率：0.60，速度：3.0，耗时：45.5
加速耗时 比率：0.70，速度：3.0，耗时：41.7

线下观测：
1. 现实下加速速度为多少
2. 现实中参与比例为多少
"""
# 并行，速度1
def on_lift1(people:int) -> float:
    return on_lift2(people, 0, 0)/2

# 异步，速度1+2
def on_lift2(people:int,acc_per=0.3,acc_speed:float=2.0) -> float:
    return people/(acc_per*acc_speed+(1-acc_per)*1)

def on_left_vs(people:int):
    print("+++++++++++%d+++++++++++" % people)
    t1 = on_lift1(people)
    print("并行耗时 比率：%.2f，速度：%.1f，耗时：%.1f" % (1, 1, t1))
    for per in [int((x/10+0.3)*10)/10 for x in range(7)]:
        for speed in [x/10+2.5 for x in range(5,40,5)]:
            t2 = on_lift2(people, per, speed)
            if t2 < t1:
                print("加速耗时 比率：%.2f，速度：%.1f，耗时：%.1f" % (per, speed ,t2))
                break

on_left_vs(100)