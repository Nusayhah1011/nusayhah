#create a list of five items
tasks = ["login your application","insert your password"," check your account","transfer money","receive receipt"]
#access the first and last items by index,
print(tasks[0])
print(tasks[4])
# use len() to check the length
print(len(tasks))
#append and check length again
tasks.append("close your application")
print(len(tasks))

#print(tasks[7]) >> error message "IndexError: list index out of range"