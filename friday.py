'''
LANG: PYTHON3
PROG: friday
'''

x = open("friday.in")
num = int(x.read())
x.close()


year = 1900
counter = {"mon":0, "tue":0, "wed":0, "thu":0, "fri":0, "sat":0, "sun":0}
days = ["mon","tue","wed","thu","fri","sat","sun","mon","tue","wed","thu","fri","sat","sun","mon","tue","wed","thu","fri","sat","sun","mon","tue","wed","thu","fri","sat","sun","mon","tue","wed","thu","fri","sat","sun","mon","tue","wed","thu","fri","sat","sun"]
months = ["jan","feb","mar","apr","may","jun","jul","aug","sep","oct","nov","dec"]
start = "mon"
for i in range(num):
    for x in months:
        if x == "jan" or x == "mar" or x == "may" or x == "jul" or x == "aug" or x == "oct" or x == "dec":
            index = days.index(start)
            counter[days[index+12]] += 1
            start = days[index+31]
        elif x == "feb":
            index = days.index(start)
            counter[days[index+12]] += 1
            if (1900 + i) % 100 == 0:
                if (1900 + i) % 400 == 0:
                    start = days[index+29]
                else:
                    start = days[index+28]
            elif (1900 + i) % 4 == 0:
                start = days[index+29]
            else:
                start = days[index+28]          

        elif x == "apr" or x == "jun" or x == "sep" or x == "nov":
            index = days.index(start)
            counter[days[index+12]] += 1
            start = days[index+30]
        
output = f"{counter['sat']} {counter['sun']} {counter['mon']} {counter['tue']} {counter['wed']} {counter['thu']} {counter['fri']}\n"

print(output)

x = open("friday.out","w")
x.write(output)
x.close()


