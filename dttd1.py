"""
电梯难题1：轨道电梯

电梯正常情况下可以一次同行2人，速度为1；但由于上班族早晚高峰，导致一侧速度为2，一侧速度为1
假如现在有50人要上电梯，
策略1：同时2人，上电梯不加速
策略2: 1侧加速，1侧不加速正常上电梯，
请计算那种策略下，通过的时间最短

线下观测：
1. 现实下加速速度为多少  2倍
2. 现实中参与比例为多少  40%
"""
# 并行，单侧1个/s，同时2个/s
def lift1_load(time:int) -> float:
    return lift2_load(time, 0.5, 1)

# 异步，一次1个/s，另一次2个/s
def lift2_load(time:int,acc_per=0.3,acc_speed:float=2.0) -> float:
    return time*(acc_per*acc_speed+(1-acc_per)*1)

def on_left_vs(time:int,start_per=0.1, start_speed=0.5):
    print("+++++++++++%d+++++++++++" % time)
    load1 = lift1_load(time)
    print("并行耗时 比率：%.2f，速度：%.1f，运载量：%.1f" % (1, 1, load1))
    for per in [int((x / 10 + start_per) * 10) / 10 for x in range(5)]:
        for speed in [x / 10 + start_speed for x in range(5, 40, 5)]:
            load2 = lift2_load(time, per, speed)
            if load2 > load1:
                print("加速耗时 比率：%.2f，速度：%.1f，运载量：%.1f，倍率：%.2f" % (per, speed, load2, (load2-load1)/load1))
                break

on_left_vs(60, 0.4,1.5)