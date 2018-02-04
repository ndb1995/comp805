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


print("\nFourth Function:\n")
print(lab2.filter_0_items({'pencil':10, 'pen':8, 'paper':7}))
print(lab2.filter_0_items({'pencil':0, 'pen':-3, 'paper':-11}))
print(lab2.filter_0_items({'pencil':0.5, 'pen':-3.2, 'paper':0.0}))

print("\nFifth Function:\n")
print(lab2.average_grades({'Michael' :[100, 78, 88, 900/10], 'Daniel':[80, 95, 77, 64.0], 'Josh':[99, 89, 94, 66]}))
print(lab2.average_grades({'Michael' :[5*20, 188 * .5, 88], 'Daniel':[80.5, .15, 66, 64.0], 'Josh':[99 + 1 * -2, 40/.5]}))
print(lab2.average_grades({'Michael' :[78], 'Daniel':[90], 'Josh':[900/-9]}))
