# -*- coding: utf-8 -*-
import time
def main():
    ReadlinesCount = 0
    studentOnLine = {"jupyter":0,"test":"0"}
    studentWriting = {"jupyter": 0,"test":"0"}
    while True:
        tStart = time.time()
        readArray = []
        log_ip_file = open("/var/log/jupyter_screen.log", 'r')
        log_op_file = open("/var/log/jupyter.log", 'a+')
        for readline in log_ip_file.readlines():
            readArray.append(readline)
        for i in range(ReadlinesCount, len(readArray), +1):
            if "User logged in:" in readArray[i]:
                log_op_file.writelines(readArray[i]) # 登入次數
                temp = readArray[i].split("|")
		user = temp[4].split(" ")
                studentOnLine[user[3]] = 1    #將學生上線的信號改為1

            elif "Saving file at" in readArray[i]:  # 送出作業的次數
                log_op_file.writelines(readArray[i])

            elif "Creating new notebook in" in readArray[i]:  # 創了幾個新的資料
                log_op_file.writelines(readArray[i])

            elif "User logged out" in readArray[i]: # 將學生上線化為0
                temp = readArray[i].split("|")
                user = temp[4].split(" ")
                studentOnLine[user[3]] = 0
		print("logged out",studentOnLine[user[3]])
            elif "Kernel started" in readArray[i]:
                temp = readArray[i].split(" ")
                studentWriting[temp[3]] = 1

            elif "Kernel shutdown"in readArray[i]:
                temp = readArray[i].split(" ")
                studentWriting[temp[3]] = 0
		print("K shut",studentWriting[temp[3]])
        for i in studentOnLine:
            if studentOnLine[i] == 1:
                log_op_file.writelines("onlinestudent|"+i+"\n")

        for i in studentWriting:
            if studentWriting[i] == 1:
                log_op_file.writelines("writingstudent|"+i+"\n")

        log_ip_file.close()
        log_op_file.close()
        ReadlinesCount = len(readArray)
        tEnd = time.time()
        print tEnd - tStart
        time.sleep(60-(tEnd-tStart))
if __name__ == "__main__":
    main()
