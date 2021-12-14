from typing import List


def change_period(period: str):
    if period == "PM":
        return "AM", 1
    else:
        return "PM", 0


def new_day(days: List, day: str, day_pass: str):
    newday = int(days.index(day)+day_pass) % 7
    return days[newday]


def add_time(t1: str, t2: str, day: str = ""):

    t1, period = t1.split(" ")
    t1_h, t1_m = t1.split(":")
    t2_h, t2_m = t2.split(":")
    t1_h = int(t1_h)
    t2_h = int(t2_h)
    t1_m = int(t1_m)
    t2_m = int(t2_m)
    day_pass = 0
    day_names = ["Monday", "Tuesday", "Wednesday",
                 "Thursday", "Friday", "Saturday", "Sunday"]

    if day != "":
        day = day.lower()
        day = day.capitalize()

    h_n = t2_h + t1_h
    m_n = t1_m + t2_m

    if (h_n - 12 > 0 and m_n - 60 > 0) or (not h_n - 12 > 0 and m_n - 60 > 0):
        while 1:
            m_n = m_n-60
            h_n = h_n + 1
            if m_n - 60 > 0:
                continue
            else:
                if m_n < 10:
                    m_n = "0" + str(m_n)
                break
        while 1:
            h_n = h_n - 12
            period, result = change_period(period)
            day_pass = day_pass + result
            if h_n - 12 > 0:
                continue
            elif h_n == 12 and int(m_n) > 0 :
                period, result = change_period(period)
                day_pass = day_pass + result
                break
            else:
                break
        if h_n == 0 or h_n == "00" or h_n == 0 or h_n == "0":
            h_n = 12
        if day != "":

            if day_pass == 1:
                day_name = new_day(day_names, day, day_pass)
                print(f"{h_n}:{m_n} {period} next day, {day_name}")
                return f"{h_n}:{m_n} {period} next day"
            elif day_pass > 0:
                day_name = new_day(day_names, day, day_pass)
                print(f"{h_n}:{m_n} {period}, {day_name} ({day_pass} days later)")
                return f"{h_n}:{m_n} {period}, {day_name} ({day_pass} days later)"
            else:
                print(f"{h_n}:{m_n} {period}, {day}")
                return f"{h_n}:{m_n} {period}, {day}"
        else:
            if day_pass == 1:
                print(f"{h_n}:{m_n} {period} (next day)")
                return f"{h_n}:{m_n} {period} (next day)"
            elif day_pass > 0:
                print(f"{h_n}:{m_n} {period} ({day_pass} days later)")
                return f"{h_n}:{m_n} {period} ({day_pass} days later)"
            else:
                print(f"{h_n}:{m_n} {period}")
                return f"{h_n}:{m_n} {period}"

    elif h_n - 12 > 0 and not m_n - 60 > 0:
        while 1:
            h_n = h_n - 12
            period, result = change_period(period)
            day_pass = day_pass + result
            if h_n - 12 > 0:
                continue
            elif h_n == 12 and int(m_n) > 0 :
                period, result = change_period(period)
                day_pass = day_pass + result
                break
            else:
                break
        if day != "":
            if day_pass == 1:
                day_name = new_day(day_names, day, day_pass)
                print(f"{h_n}:{m_n} {period}, {day_name} (next day)")
                return f"{h_n}:{m_n} {period}, {day_name} (next day)"
            elif day_pass > 0:
                day_name = new_day(day_names, day, day_pass)
                print(f"{h_n}:{m_n} {period}, {day_name} ({day_pass} days later)")
                return f"{h_n}:{m_n} {period}, {day_name} ({day_pass} days later)"
            else:
                print(f"{h_n}:{m_n} {period}, {day}")
                return f"{h_n}:{m_n} {period}, {day}"
        else:
            if day_pass == 1:
                print(f"{h_n}:{m_n} {period} (next day)")
                return f"{h_n}:{m_n} {period} (next day)"
            elif day_pass > 0:
                print(f"{h_n}:{m_n} {period} ({day_pass} days later)")
                return f"{h_n}:{m_n} {period} ({day_pass} days later)"
            else:
                print(f"{h_n}:{m_n} {period}")
                return f"{h_n}:{m_n} {period}"
        
        
    else:
        if m_n < 10:
            m_n = "0" + str(m_n)   
        if day != "":
            print(f"{h_n}:{m_n} {period}, {day}")
            return f"{h_n}:{m_n} {period}, {day}"
        else:
            print(f"{h_n}:{m_n} {period}")
            return f"{h_n}:{m_n} {period}"  


if __name__ == "__main__":
    add_time("11:40 AM", "0:25")
