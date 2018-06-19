import gspread
from oauth2client.service_account import ServiceAccountCredentials
import pandas as pd
import seaborn as sns
import matplotlib as plt
from pandas.tools.plotting import scatter_matrix
from matplotlib import cm
import datetime

now = datetime.datetime.now()
nw = now.strftime("%d-%m-%Y")
print(now.strftime("%d-%m-%Y"))
def timeData():
	scope = ['https://spreadsheets.google.com/feeds', 'https://www.googleapis.com/auth/drive']
	creds = ServiceAccountCredentials.from_json_keyfile_name('/Users/junaid/Downloads/client_secret.json', scope)
	client = gspread.authorize(creds)
	data_dict = {}


	sheet = 	client.open("Walkins_may15").sheet1
	
	list_of_hashes = sheet.get_all_records()
	list_of_values = sheet.get_all_values()
	# print(type(list_of_hashes))
	# print(list_of_values)
	headers = list_of_values[0]
	dates = []
	courses = []
	responders = []
	pds = []

	for i in range(1,len(list_of_values)):
		dates.append(list_of_values[i][1].upper())
		courses.append(list_of_values[i][5].upper())
		responders.append(list_of_values[i][6].upper())
		if(len(list_of_values[i][13]) >3):
			pds.append(list_of_values[i][13])
		else:
			pds.append("not registered")
	data_dict[headers[1]] = dates
	data_dict[headers[5]] = courses
	data_dict[headers[6]] = responders
	data_dict[headers[13]] = pds
	df = pd.DataFrame(data=data_dict)
	count = 0
	for i in dates :
		if nw == i:
			count +=1
	print(df.head())
	print(pds)
	fig, ((ax1, ax2), (ax3, ax4)) =plt.pyplot.subplots(nrows=2, ncols=2)
	plt.pyplot.title('date wise walkins')
	ss = sns.countplot(df['Date'], ax=ax1)
	ss.set_xticklabels(ss.get_xticklabels(), rotation=40, ha="right")
	plt.pyplot.tight_layout()
	plt.pyplot.title('walkins per PD')
	ss = sns.countplot(df['Designated_pd'], ax=ax2)
	ss.set_xticklabels(ss.get_xticklabels(), rotation=40, ha="right")
	plt.pyplot.tight_layout()
	plt.pyplot.title('Course status')
	ss = sns.countplot(df['Course'], ax=ax3)
	ss.set_xticklabels(ss.get_xticklabels(), rotation=40, ha="right")
	plt.pyplot.tight_layout()
	plt.pyplot.title('Responder status')
	ss = sns.countplot(df['Responder'], ax=ax4)
	ss.set_xticklabels(ss.get_xticklabels(), rotation=40, ha="right")
	plt.pyplot.tight_layout()
	plt.pyplot.show()
timeData()
