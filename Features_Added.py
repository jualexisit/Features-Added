


file = open('sizes.txt',"r")
content = file.readlines()
file.close()
print(content)

total = 0


for i in list(content):
    #print(i)

    if "MiB" in i:
        #print(float(i[:-4]) * 1000 * 1000)
        total += float(i[:-4]) * 1000 *1000
    elif "KiB" in i:
        #print(float(i[:-4]) * 1000)
        total += float(i[:-4]) * 1000
    elif "B" in i:
        #print(float(i[:-2]))
        total += float(i[:-2])
    else:
        pass
    #print(total)

print("the total amoung of data is: " + str(total) + "Bytes or " + str(total / 1000 / 1000) + " MegaBytes")

