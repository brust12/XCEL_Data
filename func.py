#Module func.py
import urllib
import pandas as pd
from openpyxl import load_workbook

def DownloadXcelData(tickername,companyname):
        ###Download###
    url = f"https://stockrow.com/api/companies/{tickername}/financials.xlsx?dimension=Q&section=Income%20Statement&sort=desc"
    
    try:
        urllib.request.urlretrieve(url,f'c:/Users/Riley/Desktop/stockt/Sheets/{tickername}.xlsx')
        print(tickername + " " + companyname)
        return True
    except Exception:
        notfoundstring = tickername+" "+companyname+" " "\t!!DOES NOT EXIST!!"
        print(notfoundstring)
        # Lines.remove(Lines[x])
        return False
    return False


def append(filename,companyname):
          ###Append###
    # if os.path.exists("c:/Users/Riley/Desktop/stockt/Sheets/combined.xlsx"):
    #   os.remove("c:/Users/Riley/Desktop/stockt/Sheets/combined.xlsx")
    # else:
    #   print("The file does not exist")


    print("Appending files...")
    

    # # current = pd.read_excel('c:/Users/Riley/Desktop/stockt/Sheets/combined.xlsx',skipfooter=2)
    # pdtotal = pd.DataFrame(current)
    # # downloaded = pd.read_excel(f'c:/Users/Riley/Desktop/stockt/Sheets/{filename}.xlsx',skipfooter=2)
    # # name = pd.DataFrame([filename,filename])
    # name = pd.Series("Name")
    # # current = current.append(name, ignore_index=True)
    # newsheet = [current,downloaded]
    #   # appeded.append(pd.Series(name='NameOfNewRow'))
    # pdtotal = pdtotal.concat(downloaded,ignore_index=True)
    # current = current.append(downloaded,ignore_index=True)
    # df = pd.read_excel('c:/Users/Riley/Desktop/stockt/Sheets/combined.xlsx', sheet_name=None,skipfooter=1)
    # df = pd.concat(pd.read_excel(f'c:/Users/Riley/Desktop/stockt/Sheets/{filename}.xlsx', sheet_name=None), ignore_index=True)


    # df.to_excel("c:/Users/Riley/Desktop/stockt/Sheets/combined.xlsx")
 
   
    # Read excel file 
    # and store into a DataFrame 
    df1 = pd.read_excel("c:/Users/Riley/Desktop/stockt/Sheets/combined.xlsx") 
    tickname = pd.Series(filename)
    compname = pd.Series(companyname)
    df2 = pd.read_excel(f"c:/Users/Riley/Desktop/stockt/Sheets/{filename}.xlsx") 
    newdata =[df1,tickname,compname,df2]
    # concat both DataFrame into a single DataFrame 
    df = pd.concat(newdata) 
    
    # Export Dataframe into Excel file 
    df.to_excel("c:/Users/Riley/Desktop/stockt/Sheets/combined.xlsx", index=False) 
