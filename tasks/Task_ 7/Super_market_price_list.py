ittems = ["pen","book","table"] # list of items
print(ittems)
itm_1 = float(input("Enter price: ")) # collects input
itm_2 = float(input("Enter price: ")) # collects input
itm_3 = float(input("Enter price: ")) # collects input

dic = {}
dic[ittems[0]] = itm_1
dic[ittems[1]] = itm_2
dic[ittems[2]] = itm_3

print(dic) 
change_itm = input("Enter item: ")
change_price = float(input("Enter price: "))
dic.update({change_itm:change_price})
print(dic)


