from datetime import datetime

user_input = input("enter your goal with a deadline separated by a colon\n")
input_list = user_input.split(":")

goal = input_list[0]
deadline = input_list[1]

deadline_date = datetime.strptime(deadline, "%d.%m.%Y")
today_data = datetime.today()
time_till = deadline_date - today_data

print(f"Dear user ! Time remaining for you goal : {goal} is {time_till.days} days")