for i in range(1,6):
    mark = int(input(f"Enter Mark Of Subject {i} :- "))
    if mark <= 100:
        ttl = mark + mark + mark + mark + mark
    else:
        print("Enter Valid Marks....")

print(f"Total Marks :- {ttl}")
avg = ttl/5
print(f"Percentage :- {avg}")

if(avg >= 70):
    print("Distinction")
elif(avg >= 60 and avg < 70):
    print("First Class")
elif(avg >= 50 and avg < 60):
    print("Second Class")
elif(avg >= 40 and avg < 50):
    print("Third Class")
elif(avg >= 33):
    print("Pass Class")
else:
    print("Sorry! Bad luck Try Next Time...")