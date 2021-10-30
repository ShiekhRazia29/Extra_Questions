a = 6.30 
raw_time =float(input("Enter a time"))
if raw_time >=6.30 and raw_time <=7.30:
    print("Exercise")
elif raw_time >= 9.00 and raw_time <= 10.00:
    print("Refreshment time")
elif raw_time >10.00 and raw_time <= 13.00 :
    print("Study time")
elif raw_time >13.00 and raw_time <= 14.30:
    print("Lunch Break")
elif raw_time > 14.30 and raw_time <= 16.30:
    print("Cultural activities")
elif raw_time > 16.30  and raw_time <= 18.00:
    print("Dance class")
elif raw_time > 18.00 and raw_time <= 18.30:
    print("Snacks break")
elif raw_time > 18.30 and raw_time <= 21.00:
    print("Second study")
elif raw_time > 21.00 and raw_time <= 22.30:
    print("Dinner time")
elif raw_time > 22.30 and raw_time <= 23.30:
    print("Task completion")
else:
    print("Lights off")
