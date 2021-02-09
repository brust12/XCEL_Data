import urllib.request
import pandas as pd
import os
import func

# print('Beginning file download with urllib2...')

#Get ticker names
tick2 = open('tickers2.txt', 'r')
Lines = tick2.readlines()



# if os.path.exists("c:/Users/Riley/Desktop/stockt/Sheets/combined.xlsx"):
#     os.remove("c:/Users/Riley/Desktop/stockt/Sheets/combined.xlsx")
# else:
#     open("c:/Users/Riley/Desktop/stockt/Sheets/combined.xlsx",'w+')
    


success = 0
fail = 0 
listofdl = []
#Main loop, Download then append to file
for x in range(4,25):
    splitup = Lines[x].strip().split('\t')
    tickername = splitup[0]
    companyname = splitup[1]
    passed = func.DownloadXcelData(tickername, companyname)
    if passed:
        success+= 1
        listofdl.append(tickername)
        func.append(tickername,companyname)
    else: 
        fail += 1
print (listofdl)
#Prints files found
# print("\nFiles updated: ", success)
# print("Files not found: ", fail)
# for x in range(0,15):
#     splitup = Lines[x].strip().split('\t')
#     tickername = splitup[0]
#     print(tickername)

       
       
       
       
       
       
       
       
       
        ###Append###
# if os.path.exists("c:/Users/Riley/Desktop/stockt/Sheets/new.xlsx"):
#   os.remove("c:/Users/Riley/Desktop/stockt/Sheets/new.xlsx")
# else:
#   print("The file does not exist")


# print("Appending files...")
# apple = pd.read_excel("c:/Users/Riley/Desktop/stockt/Sheets/AAPL.xlsx")
# zy = pd.read_excel("c:/Users/Riley/Desktop/stockt/Sheets/ZYXL.xlsx")

# name = pd.Series("Name")
# # newapple = applesheet.append(name, ignore_index= True)
# newsheet = [apple,name,zy]
# # appeded.append(pd.Series(name='NameOfNewRow'))
# appeded = pd.concat(newsheet)



# appeded.to_excel("c:/Users/Riley/Desktop/stockt/Sheets/new.xlsx", index=False)




exit
