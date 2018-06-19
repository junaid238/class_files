import numpy as np
import pandas as pd 
import matplotlib.pyplot as plt
import seaborn as sns
import xlrd
from matplotlib.gridspec import GridSpec
from fuzzywuzzy import fuzz
from fuzzywuzzy import process
# get_ipython().run_line_magic('matplotlib', 'inline')

datahub = "DS+P DS  BD+DS DataPython+DS DA+DS+BDPython + Datascience SCIENCE Hadoop PY + DS Python DATA SCIENCE PY+Django PY+DS+PD Datascience"
cloudops = "Devops AWS AZURE DEVOPS DevOps+AWS Devops+AWS"
fullstack = "Front end back end Angular JS Full Stack html css  "
positive = "visited registered joined "
get_back = " get back in will visit tomorrow call back follow EOD "
negative = " dead lead not interested somewhere"


walkins = pd.ExcelFile('walkinsGB.xlsx')
dfs = pd.read_excel('walkinsGB.xlsx')
print(dfs.shape)
dfs.head(3)

data_count = 0
cloud_count = 0
fs_count = 0 
pos_count= 0 
neg_count= 0 
follow_count= 0 

def status_cat(status):
    global pos_count
    global neg_count
    global follow_count

    if(fuzz.partial_ratio(positive.lower(), status.lower()) > 50):
        obj = "positive"
        pos_count = pos_count+ 1
    elif(fuzz.partial_ratio(negative.lower(), status.lower()) > 50):
        obj =  "negative"
        neg_count = neg_count+1
    elif(fuzz.partial_ratio(get_back.lower(), status.lower()) > 50):
        obj =  "get_back"
        follow_count = follow_count+1
    else:
        obj = "Others"
    return obj

def course_cat(name):
	global data_count 
	global cloud_count 
	global fs_count
	if(fuzz.partial_ratio(datahub.lower(), name.lower()) > 50):
		obj = "data_obj"
		data_count = data_count+ 1
	elif(fuzz.partial_ratio(cloudops.lower(), name.lower()) > 50):
		obj =  "cloud_obj"
		cloud_count = cloud_count+1
	elif(fuzz.partial_ratio(fullstack.lower(), name.lower()) > 50):
		obj =  "fs_obj"
		fs_count = fs_count+1
	else:
		obj = "Others"
	return obj

for i in range(0 ,len(dfs['Status'])):
    dfs['Status'][i] = status_cat(str(dfs['Status'][i]))

for i in range(0 ,len(dfs['Technology'])):
    dfs['Technology'][i] = course_cat(str(dfs['Technology'][i]))

sns.set(style="darkgrid")
fig, axs = plt.subplots(ncols=2)
sns.countplot(dfs.Technology, ax=axs[0])
sns.countplot(dfs.Status, ax=axs[1])
plt.show()
