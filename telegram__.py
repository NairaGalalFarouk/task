fileData = open(r"E:\python sql\telegramData.txt","w")
fileData.write("buy :9000 \n")
fileData.write("sell:1000 \n")
fileData.write("stop: 8800 \n")
file = open(r"E:\python sql\telegram.txt","w")
file.write("buy between :9000\n")
file.write("targets:1000 \n")
file.write("stop loss: 8800 \n")
file = open(r"E:\python sql\telegram.txt","r")
fileData = open(r"E:\python sql\telegramData.txt","r")
print(file.readline()+file.readline()+file.readline())
