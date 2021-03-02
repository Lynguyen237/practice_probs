# Create a script that returns the day of the week,s is a string that represents the day of the week, 
# and k is an int that returns the day of the week that is K days later.
# eg s = "Wed", k = 2, then return "Fri"

def day_of_the_week(s,k):
    days = ["Mon", "Tue", "Wed", "Thr", "Fri", "Sat", "Sun"]

    k = k % 7

    s_idx = days.index(s)

    result_day_idx = s_idx + k
    
    if s_idx + k > 6:
        result_day_idx = (s_idx + k - 7)
    
    
    return days[result_day_idx]

print (day_of_the_week("Wed",2)) #Fri
print (day_of_the_week("Wed",4)) #Sun
print (day_of_the_week("Wed",5)) #Mon
print (day_of_the_week("Wed",500)) #Sat