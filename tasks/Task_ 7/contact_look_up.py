print("\nContact Quicq lookup")
names = ("Ayomide","Ayodele","Ayoposi") # a tuple containing names
phne_num = ("0810980","09045678","09045678")
contac_info = dict(zip(names, phne_num))
name = input("Enter a name: ")
print(contac_info.get(name, "Name not found"))
