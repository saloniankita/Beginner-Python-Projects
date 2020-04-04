shoplist= []
print("Enter Your List Items here :\nType DONE when finished.")
while True:
    item=input("->")
    if item=='DONE':
        break
    shoplist.append(item)
print("This is your final list :\n")
for x in shoplist:
    print(x)
