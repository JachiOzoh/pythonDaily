# To display the average of a list of 10 (or less) ages
count=0
total=0
while True:
    age=input('Type in your age: ')
    if age.lower() == "done":
        print('All Done!!')
        break
    else:
        pass
# In case of non numeric input, use try and except statement
    try:
        iage=int(age)
    except:
        print('Not A Valid Character')
        quit
    count = count + 1
    total=total+iage
# To calculate the sum and average of the ages
print("SUM: ",total," AVG: ", total/count)
