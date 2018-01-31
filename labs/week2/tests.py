import lab2
print("\nFirst Function:\n")
print(lab2.squared_nums([1,2,3]))
print(lab2.squared_nums([]))
print(lab2.squared_nums([-1,-2,-3]))
print(lab2.squared_nums([1,0]))

print("\nSecond Function:\n")
print(lab2.check_title(['Hello World','Hello_world','Title']))
print(lab2.check_title(['Hello_World', 'A great 3 Days', 'hello World']))
print(lab2.check_title([10, 11, 12]))

print("\nThird Function:\n")
print(lab2.restock_inventory({'pencil':10, 'pen':8, 'paper':7}))
print(lab2.restock_inventory({'pencil':0, 'pen':-3, 'paper':-11}))
print(lab2.restock_inventory({'pencil':0.5, 'pen':-3.2, 'paper':11.0}))
