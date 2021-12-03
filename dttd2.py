import random
import pandas as pd

class People(object):

    def __init__(self,speed):
        self.speed = speed

    def me(self):
        if self.speed>1:
            return "I'm speed man"
        else:
            return "I'm normal man"

def create_people(speed_per=3.0,acc_speed=2):
    seed = random.uniform(1.0,10.0)
    return People(acc_speed) if seed<=speed_per else People(1)

# 并行，单侧1个/s，同时2个/s
def lift1_load(time:int,peoples) -> (int,int):
    load_people = 0
    use_time = time
    for i in range(time):
        if load_people < len(peoples):
            load_people +=2
        else:
            load_people = len(peoples)
            use_time = i
            break
    return use_time, load_people

# 并行，单侧1个/s，同时2个/s
def lift2_load(time:int,peoples) -> (int,int):
    load_people = 0
    use_time = time
    for i in range(time):
        people = peoples[load_people]
        load_people += 1
        maybe_num = 3 if people.speed>1 else 2
        for j in range(load_people, min(load_people + maybe_num, len(peoples))):
            people = peoples[j]
            if people.speed < 2:
                break
            load_people += 1

        if load_people >= len(peoples):
            use_time = i
            break
    return use_time, load_people

def on_left_vs(time:int,per):
    data_arrays = []
    speed_peoples = [create_people(per) for j in range(100)]
    for t in range(10,time,2):
       print("-------------%d-------------" % t)
       print("normal: time: %d, peoples: %d" % lift1_load(t, normal_peoples))
       print("rand: time: %d, peoples: %d" % lift2_load(t, speed_peoples))
       data_arrays.append(['normal',*lift1_load(t, normal_peoples)])
       data_arrays.append(['rand', *lift2_load(t, speed_peoples)])
    with pd.ExcelWriter('dttd'+str(per)+'.xlsx') as writer:
        pd.DataFrame(data_arrays,columns=['测试类型','使用时间','荷载人数']).to_excel(writer)

if __name__ == '__main__':

    normal_peoples = [create_people(0) for i in range(100)]

    for i in [5.6]:
        on_left_vs(60,i)


