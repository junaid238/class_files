from fuzzywuzzy import fuzz
from fuzzywuzzy import process
tech_unique =['DS+P', 'Anguar', 'bliockchain', 'Angular', 'DM', 'Devops', 'Devops+AWS', 'AWS', 'AZURE', 'DS', 'Unity 3D', 'DevOps', 'Java', 'Backend+html+css js', 'BD+DS', 'fullstack', 'PY+DS', 'Python', 'Hadoop', 'Digital Marketing', 'Py+DS', 'FullStack', 'DevOps+AWS', 'Front end till Angular', 'bolck chain', 'devops', 'Photoshop', 'Android', 'DATA SCIENCE', 'Azure + AWS', 'Azure', 'Andorid', 'Python + Django', 'DevOps+AWS+PY', 'azure', 'DS + DA', 'PY + DS', 'Data SCIENCE', 'Devops + AWS', 'DEVOPS', 'SQL Azure', 'PY+Django', 'Full Stack', 'PY + DS + Daya Analysis', 'Data SCIENCE + Tablue', 'Block Chain', 'Cyber Security', 'PY+DS+PD', 'Blockchain', 'DA+DS+BD', 'Android+DevOps+Python+DA', 'Python+DS', 'Python + Datascience', 'Angular JS', 'nan']
all_tech = ['DS+P', 'Anguar', 'bliockchain', 'Angular', 'Angular', 'DM', 'DM', 'Devops', 'Devops', 'DS+P', 'Devops+AWS', 'DM', 'AWS', 'AZURE', 'DS', 'AWS', 'Unity 3D', 'DevOps', 'Java', 'AWS', 'Backend+html+css js', 'BD+DS', 'fullstack', 'fullstack', 'PY+DS', 'AZURE', 'Python', 'AZURE', 'fullstack', 'Python', 'DM', 'Hadoop', 'Devops', 'Digital Marketing', 'Py+DS', 'FullStack', 'DevOps+AWS', 'DevOps+AWS', 'DevOps+AWS', 'Front end till Angular', 'bolck chain', 'devops', 'Photoshop', 'Android', 'DATA SCIENCE', 'Azure + AWS', 'Azure + AWS', 'Azure', 'PY+DS', 'Andorid', 'AWS', 'Python + Django', 'Python', 'DevOps+AWS', 'DevOps+AWS+PY', 'azure', 'DS + DA', 'PY + DS', 'PY + DS', 'Data SCIENCE', 'Devops + AWS', 'AWS', 'Angular', 'DevOps+AWS', 'AWS', 'FullStack', 'DevOps', 'DevOps+AWS', 'DevOps+AWS', 'Photoshop', 'DEVOPS', 'SQL Azure', 'DevOps', 'PY+Django', 'PY+DS', 'AWS', 'PY+DS', 'PY + DS', 'AWS', 'AWS', 'Devops', 'Full Stack', 'AWS', 'Azure', 'Python', 'Python', 'PY + DS + Daya Analysis', 'Data SCIENCE + Tablue', 'Block Chain', 'PY + DS', 'Devops', 'Cyber Security', 'PY+DS+PD', 'Digital Marketing', 'Blockchain', 'DA+DS+BD', 'Android+DevOps+Python+DA', 'Python+DS', 'DA+DS+BD', 'Python + Datascience', 'Angular JS', 'nan', 'nan']
tech_count = {"cloudops":0 , "datahub" : 0}

datahub = "DS+P DS  BD+DS DataPython+DS DA+DS+BDPython + Datascience SCIENCE Hadoop PY + DS Python DATA SCIENCE PY+Django PY+DS+PD Datascience "
cloudops = "Devops AWS AZURE DEVOPS DevOps+AWS Devops+AWS"
fullstack = "Front end back end Angular JS Full Stack html css  "
count_dh = 0
count_co = 0

for i in all_tech:
	obj = datahub.lower().find(i.lower())
	obj2 = cloudops.lower().find(i.lower())
	# print(obj)
	if (obj != -1):
		# print(i)
		count_dh = count_dh + 1
	elif(obj2 != -1):
		# print(i)
		count_co = count_co + 1
	# else:
		# print(i)
tech_count["datahub"] = count_dh
tech_count["cloudops"] = count_co
# print(tech_count)
dh_list = datahub.split()
dv_list = cloudops.split()
# print(dh_list)
# print(dv_list)

# def course_cat(name):
# 	if(datahub.lower().find(name.lower()) != -1):
# 		obj = "data_obj"
# 	elif(cloudops.lower().find(name.lower())!= -1):
# 		obj =  "cloud_obj"
# 	else:
# 		obj = name
# 	return obj
data_count = 0
cloud_count = 0
fs_count = 0 
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
for i in all_tech:
	print(i + "---->" + course_cat(i))

print("%s %d " %("DataHub Walkins" , data_count))
print("%s %d " %("Full Stack Walkins" , fs_count))
print("%s %d " %("CloudOps Walkins" , cloud_count))
