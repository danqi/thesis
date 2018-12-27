import matplotlib
import matplotlib.pyplot as plt
import matplotlib.dates as mdates
import datetime as dt
matplotlib.rcParams['legend.handlelength'] = 0
matplotlib.rcParams['legend.numpoints'] = 1


def isfloat(value):
    try:
        float(value)
        return True
    except ValueError:
        return False


mapping = {'Jan': 1, 'Feb': 2, 'Mar': 3, 'Apr': 4, 'May': 5, 'Jun': 6,
           'Jul': 7, 'Aug': 8, 'Sep': 9, 'Oct': 10, 'Nov': 11, 'Dec': 12}


def get_month(s):
    assert s in mapping
    return mapping[s]


def earlier(date1, date2):
    if date1[0] != date2[0]:
        return date1[0] < date2[0]
    if date1[1] != date2[1]:
        return date1[1] < date2[1]
    return False


records = []
with open('squad_leaderboard.txt') as f:
    for line in f.readlines():
        sp = line.strip().split('\t')
        if len(sp) == 2 and ('2016' in sp[0] or '2017' in sp[0] or '2018' in sp[0]):
            date = sp[0]
            system = sp[1]
        if len(sp) >= 2 and isfloat(sp[-2]) and isfloat(sp[-1]):
            em = float(sp[-2])
            f1 = float(sp[-1])

            if 'ensemble' not in system:
                print('-' * 100)
                year = int(date.split(' ')[-1])
                month = get_month(date.split(' ')[0])
                date = int(date.split(' ')[1][:-1])

                print(year, month)
                print(system)
                print(em, f1)

                if len(records) == 0 or earlier((year, month), (records[-1][0], records[-1][1])):
                    records.append((year, month, date, f1))
print(records)
records.append((2016, 6, 16, 51.0))

x = []
y = []
for rec in records:
    x.append(dt.date(rec[0], rec[1], rec[2]))
    y.append(rec[3])

plt.gca().xaxis.set_major_formatter(mdates.DateFormatter('%Y-%m'))
plt.plot([x[-1], x[-2]], [y[-1], y[-2]], '-b', marker='v', label='non-neural', markevery=5)
plt.plot(x[:-1], y[:-1], '-b', marker='x', label='neural')
plt.gca().set_ylim([45.0, 100.0])
plt.gcf().autofmt_xdate()
plt.ylabel('F1')
plt.text(x[-1], 92.0, 'human: 91.2')
plt.legend(loc=4)
plt.axhline(y=91.221, color='r', linestyle='--')
plt.savefig('squad_progress.png')
