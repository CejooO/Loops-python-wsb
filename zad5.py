#6
list = [1,2,3,4,5,6,7,8,9]

counter_odd = 0;
counter_even = 0;

for i in list:
    if(i%2==0):
        counter_odd +=1
    if not i%2==0:
        counter_even+=1

print("Number of odd numbers" , counter_odd)
print("Number of even numbers" , counter_even)
