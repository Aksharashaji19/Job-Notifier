a= input("Enter name to Encrypt :")
key = int(input("Enter the key value :"))

c = " "
for i in a:
    if i ==" ":
        c = c+"#"
    else:
        c= c + chr(ord(i)+key)
print(c)

for i in a:
    frequency = a.count(i)
    print(str(i) + ": " + str(frequency), end=", ")
