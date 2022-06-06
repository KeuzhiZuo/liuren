import borax
from datetime import timedelta
from borax.calendars import LunarDate

dict_list = ['大安','留连','速喜','赤口','小吉','空亡']
dict = {
    '大安':"大安事事昌，求财在坤方，失物去不远，宅舍保安康\n行人身未动，病者主无妨，将军回田野，仔细更推详。",
    '留连':"留连事难成，求谋日未明，官事凡宜缓，去者未回程\n失物南方见，急讨方心称，更须防口舌，人口且平平。",
    '速喜':"速喜喜来临，求财向南行，失物申未午，逢人路上寻\n官事有福德，病者无祸侵，田宅六畜吉，行人有信音。",
    '赤口':"赤口主口舌，官非切宜防，失物速速讨，行人有惊慌\n六畜多作怪，病者出西方，更须防咀咒，诚恐染瘟皇。",
    '小吉':"小吉最吉昌，路上好商量，阴人来报喜，失物在坤方\n行人即便至，交关甚是强，凡事皆和合，病者叩穷苍。",
    '空亡':"空亡事不祥，阴人多乖张，求财无利益，行人有灾殃\n失物寻一见，官事有刑伤，病人逢暗鬼，解禳保安康。"
    }

print("请按照提示输入您想算的日期和时间")
input_year = int(input("请输入年："))
input_month = int(input("请输入月："))
input_day = int(input("请输入日："))
input_time = int(input("请输入时间,请只输入24小时制进位后的小时数:  \n(如23：35，只需输入23，如果是1：00请输入1)\n"))

time_list = ['子时','丑时','寅时','卯时','辰时','巳时','午时','未时','申时','酉时','戌时','亥时']

if input_time >= 23 or input_time < 1:
    lunar_time_int = 1
elif input_time >= 1 and input_time < 3:
    lunar_time_int = 2
elif input_time >= 3 and input_time < 5:
    lunar_time_int = 3
elif input_time >= 5 and input_time < 7:
    lunar_time_int = 4
elif input_time >= 7 and input_time < 9:
    lunar_time_int = 5
elif input_time >= 9 and input_time < 11:
    lunar_time_int = 6
elif input_time >= 11 and input_time < 13:
    lunar_time_int = 7
elif input_time >= 13 and input_time < 15:
    lunar_time_int = 8
elif input_time >= 15 and input_time < 17:
    lunar_time_int = 9
elif input_time >= 17 and input_time < 19:
    lunar_time_int = 10
elif input_time >= 19 and input_time < 21:
    lunar_time_int = 11
elif input_time >= 21 and input_time < 23:
    lunar_time_int = 12

# calculate the lunar date and time
ld = LunarDate.from_solar_date(input_year, input_month, input_day)
lunar_time = time_list[(lunar_time_int-1)]

print(ld.strftime('您输入的日期农历为：%Y年%L%M月%D，干支表示法为：%G')) 
print("您输入的时间为:",lunar_time)

lunar_month = ld.month
lunar_day = ld.day

month_f = dict_list[(lunar_month-1) % 6]
print("本月整体运势为:", month_f)

day_f = dict_list[(lunar_month+lunar_day-2) % 6]
print("本日整体运势为:",day_f)    

time_f = dict_list[(lunar_month+lunar_day+lunar_time_int-3) % 6]
print("本日本时辰运势为: {};".format(time_f),"曰:", dict[time_f])
