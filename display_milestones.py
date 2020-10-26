import time
from colorama import init
from colorama import Fore, Back, Style
from datetime import date

today = date.today()
this_month = today.strftime("%b").lower()
this_date = int( today.strftime("%d") )

init(autoreset = True)

all_milestones_arr = []

months = ["jan","feb","mar","apr","may","jun","jul","aug","sept","oct","nov","dec"]


def month_to_number(month):
    for i in range(0,12):
        if month.lower() == months[i]:
            return i
    print(month)


def print_milestone(milestone_arr):
    group = milestone_arr[4]
    group = group[:-1]
    status = milestone_arr[3]
    month = months[milestone_arr[1]]
    date = milestone_arr[0]
    milestone = milestone_arr[2]
    if(status == "1"):
        print(Style.BRIGHT + Back.GREEN + str(date),month, milestone, group)
    else:
        if(date < this_date and month_to_number(month) <= month_to_number(this_month)):
            print(Back.RED + str(date),month, milestone, group)
        else:
            print(Back.YELLOW + str(date),month, milestone, group)

f = open("milestones.txt", "r")
for x in f:
    array = x.split()
    if(len(array) != 1):
        milestone_arr = []
        status = array[len(array)-1]
        month = array[len(array)-2]
        date = array[len(array)-3]
        milestone = ' '.join([str(elem) for elem in array[:len(array)-3]])
        milestone_arr.append(int(date))
        milestone_arr.append(month_to_number(month))
        milestone_arr.append(milestone)
        milestone_arr.append(status)
        milestone_arr.append(group)
        all_milestones_arr.append(milestone_arr)
    else:
        group = x

#Sort
all_milestones_arr.sort(key = lambda e: e[0] )
all_milestones_arr.sort(key = lambda e: e[1])

num_milestones =len( all_milestones_arr ) -1
for i in range(0, num_milestones):
    print_milestone(all_milestones_arr[i%num_milestones])
    if(i % 1 == 0):
        time.sleep(3)


    
    
