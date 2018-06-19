import matplotlib
import seaborn as sb
import matplotlib.pyplot as plt
import pandas as pd
file= 'task1.xlsx'
xl= pd.ExcelFile(file)
print("Available Trainers:", xl.sheet_names)
a= pd.read_excel('task1.xlsx', sheet_name='Abdul')
b= pd.read_excel('task1.xlsx', sheet_name='Amitabh bacchan')
c= pd.read_excel('task1.xlsx', sheet_name='Arjun Reddy')
d= pd.read_excel('task1.xlsx', sheet_name='Imran Khan')
# inp = "abdul"
inp = input ("Enter Trainer Name: ").lower()
if inp == "abdul":
        g= sb.factorplot(x="Batches", y="no_of_students",hue="Technology",col="Mode/Term",data=a,kind="bar",size=7, aspect=.9);
        (g.set_axis_labels("", "Number of Students").set_titles ("{col_name} {col_var}").despine(left=True))  
        h= sb.factorplot(x="Batches", y="no_of_students",hue= "Technology",col="Location",data=a,kind="bar",size=4,aspect=.6);
        (h.set_axis_labels("", "Number of Students") .set_titles("{col_name} {col_var}") .despine(left=True))  
elif inp == "amitabh bacchan" :
        g= sb.factorplot(x="Batches", y="no_of_students",hue="Technology",col="Mode/Term",data=b,kind="bar",size=7, aspect=.9);
        (g.set_axis_labels("", "Number of Students").set_titles ("{col_name} {col_var}").despine(left=True))  
        h= sb.factorplot(x="Batches", y="no_of_students",hue= "Technology",col="Location",data=b,kind="bar",size=7,aspect=.9);
        (h.set_axis_labels("", "Number of Students") .set_titles("{col_name} {col_var}") .despine(left=True))  
elif inp == 'arjun reddy':
        g= sb.factorplot(x="Batches", y="no_of_students",hue="Technology",col="Mode/Term",data=c,kind="bar",size=7, aspect=.9);
        (g.set_axis_labels("", "Number of Students").set_titles ("{col_name} {col_var}").despine(left=True))  
        h= sb.factorplot(x="Batches", y="no_of_students",hue= "Technology",col="Location",data=c,kind="bar",size=7,aspect=.9);
        (h.set_axis_labels("", "Number of Students") .set_titles("{col_name} {col_var}") .despine(left=True))  
elif inp == 'imran khan':
        g= sb.factorplot(x="Batches", y="no_of_students",hue="Technology",col="Mode/Term",data=d,kind="bar",size=7, aspect=.9);
        (g.set_axis_labels("", "Number of Students").set_titles ("{col_name} {col_var}").despine(left=True))  
        h= sb.factorplot(x="Batches", y="no_of_students",hue= "Technology",col="Location",data=d,kind="bar",size=7,aspect=.9);
        (h.set_axis_labels("", "Number of Students") .set_titles("{col_name} {col_var}") .despine(left=True))  
else :
	print("Invalid Name Entered")

plt.ion()
plt.show(block = True)
