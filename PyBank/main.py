import os


import csv

csvFilePath = os.path.join("..", "Resources", "budget_data.csv")

analysiscsv = os.path.join("analysis.txt")
print()
print("Financial Analysis")
print()
print("---------------------------------------------------") 
print()

## Declaring Variable ##

rowcount = 0
total = 0
change_list = []
netChange = 0
preVal = 0
length = 0
avg = 0
great_Inc =0
great_IncDate = ""
great_Dec = 99999999999
great_DecDate = ""
month = ""
month_list =[]
listrow = -1
output =""

with open(csvFilePath, newline='') as csvfile:
    
    data = csv.reader(csvfile)
    headings =  next(data)
  
    for row in data:


      ## Calculating number of rows## 
        rowcount += 1
      ## Calulating the sum of total ##  
      ## if not str(row[1]).startswith('P'):
        total = total + int(row[1])
        
        if rowcount == 1:  
    
          preVal = int(row[1])
    
        else: 
             ##calculating net change## 
         netChange = (int(row[1])) - preVal
         month = row[0]
         preVal = int(row[1])
         change_list.append(netChange)
         month_list.append(month)

## calculating highest increase % decrease in net change##

for chg in change_list:
  listrow += 1
## print(float(chg[0]))
  if float(chg)>great_Inc:
       great_Inc = chg
      ## print("test")
       great_IncDate = month_list[listrow]
  ##     great_IncDate = chg[1]

  if float(chg)<great_Dec:
       great_Dec = chg
       great_DecDate = month_list[listrow]
       #great_DecDate = row[0]

print ("Total Months:" , rowcount,)
print()
print ("Total " , "${:.0f}".format(total))
print()
avg = round(sum(change_list)/len(change_list),2)
print ("Change in Average :", "${:.2f}".format(avg))
print()
print("Greatest Increase in Profits:" ,great_IncDate,"(","${:.0f}".format(great_Inc),")")
print()
print("Greatest Decrease in Profits:" ,great_DecDate,"(","${:.0f}".format(great_Dec),")")
print()

rowcount = str(rowcount)

with open(analysiscsv,"w") as textfile:
 
 
  output += "Financial Analysis \n"
 
  output += "--------------------------------------------------- \n"
 
  output += f"Total Months: \t\t\t {rowcount}\n"
  
  output += f"Total: \t\t\t {total}\n"

  output += f"Change in Average: \t\t\t{avg}\n"
  
  output +=f"Greatest Increase in Profits: \t\t\t {great_IncDate} \t{great_Inc} \n"

  output +=f"Greatest Decrease in Profits: \t\t\t{great_DecDate} \t{great_Dec}"
 

  textfile.write(output)

   