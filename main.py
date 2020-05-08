
#importing the files
import numpy as np
# import matplotlib.pyplot as plt
import pandas as pd
from sklearn.cluster import KMeans
from sklearn.tree import DecisionTreeClassifier # Import Decision Tree Classifier



State_list=['Manipur','Mizoram','Sikkim','Nagaland','Meghalaya','Assam','Tripura','Arunachal']
State_list_S=['Mizoram','Sikkim','Nagaland','Meghalaya','Assam']
State_list_S_Nassam= ['Mizoram','Sikkim','Nagaland','Meghalaya','Tripura','Arunachal']
df_list={}  #datafrmae list




#Reading the csv files
for state in State_list:
    df_list[state]=pd.read_csv(state+'.csv',encoding = "ISO-8859-1",error_bad_lines=False);



def K_means(no_cluster, data_arr):
	clusters = KMeans(no_cluster)  

	cluster=clusters.fit( data_arr )
	return cluster

def Decision_Tree(X,y):

	# Create Decision Tree classifer object
	ClasF = DecisionTreeClassifier()

	# # Train Decision Tree Classifer
	D_Tree = ClasF.fit(X,y)
	return D_Tree

def DT_training_data_gen():
	#For label 0 i.e very_high
	arr=[]
	for x in range(1,12):
	    for i in range(12-x,1,-1):
	        col1=12-i-x
	        if(col1==0):
	            temp_arr=[x,i,0,0,0]
	            arr.append(temp_arr)
	        for j in range(col1,0,-1):
	            col2=12-i-j-x
	            if(col1==1):
	                temp_arr=[x,i,j,0,0]
	                arr.append(temp_arr)
	                temp_arr=[x,i,0,j,0]
	                arr.append(temp_arr)            
	            for k in range(col2,0,-1):
	                if(i+j+k+x==12):
	                    temp_arr=[x,i,j,k,0]
	        #                 print(temp_arr)
	                    arr.append(temp_arr) 




	#For label 1 i.e high
	for i in range(12,0,-1):
	    col1=12-i
	    if(col1==0):
	        temp_arr=[0,i,0,0,1]
	        arr.append(temp_arr)
	    for j in range(col1,1,-1):
	        col2=12-i-j
	        if(col1==1):
	            temp_arr=[0,i,j,0,1]
	            arr.append(temp_arr)
	            temp_arr=[0,i,0,j,1]
	            arr.append(temp_arr)            
	        for k in range(col2,0,-1):
	            if(i+j+k==12):
	                temp_arr=[0,i,j,k,1]
	    #                 print(temp_arr)
	                arr.append(temp_arr)



	#For label 2 i.e low

	var=12
	x=var
	while(x!=0):
	    temp_arr=[0,0,x,var-x,2]
	    x=x-1
	    arr.append(temp_arr)




	#For label 3 i.e very_low

	for i in range(12,0,-1):
	    temp_arr=[0,0,0,i,3]
	    arr.append(temp_arr)



	return arr

def district_wise_pred(dataframe,district,D_Tree,cluster_index):
	#Selecting all the rows which has this distrct
	df_for_dist=dataframe[dataframe.DISTRICT == district]
	#Selecting the column containing cluster value
	df_for_dist=df_for_dist.Crime_clusters

	df_for_dist=df_for_dist.to_numpy()
	no_of_row=np.size(df_for_dist)

	DTree_pred=[[0,0,0,0]]
	for i in range(0,no_of_row):
	    cluster_value=df_for_dist[i]
	    index= np.where(cluster_index == cluster_value )
	    index=index[0][0]
	    DTree_pred[0][index]=DTree_pred[0][index]+1
	y_pred = D_Tree.predict(DTree_pred)
	return y_pred




def state_wise_pred(dataframe,state,D_Tree,cluster_index):
	#Selecting all the rows which has this distrct
	df_for_state=dataframe[dataframe.STATE == state]
	#Selecting the column containing cluster value
	df_for_state=df_for_state.Crime_clusters

	df_for_state=df_for_state.to_numpy()
	no_of_row=np.size(df_for_state)

	DTree_pred=[[0,0,0,0]]
	for i in range(0,no_of_row):
	    cluster_value=df_for_state[i]
	    index= np.where(cluster_index == cluster_value )
	    index=index[0][0]
	    DTree_pred[0][index]=DTree_pred[0][index]+1
	y_pred = D_Tree.predict(DTree_pred)
	return y_pred




def State_Analyz(State_df):
	
	#Removing the total row 
	State_df=State_df[State_df.DISTRICT != "TOTAL"]
	

	#Selecting the required columns
	data_frame=State_df.iloc[:,1:]
	# data=data_frame.iloc[:,2:]

	# Adding all the crime and storing it on a new column called TOTAL
	data_frame["TOTAL"]= data_frame.iloc[:,2:].sum(axis=1)


	#Selecting the columns for clustering
	data_arr = data_frame.iloc[:,2:-1] 
	data_arr = np.array(data_arr) #Converting to array



	#Applying KMeans
	clusters=K_means(4,data_arr)
	clusters.cluster_centers_
	clusters.labels_


	#Placing the cluster value to the dataset by creating new column name Crime_cluster
	data_frame['Crime_clusters'] = clusters.labels_ 
	# print(data_frame.sort_values(by=['TOTAL'],ascending = True)) #Sorting the dataframe w.r.t label



	#Adding the feature centers for getting each cluster centers
	centers = np.array(clusters.cluster_centers_)
	center_sum =np.sum(centers,axis=1)



	#Sorting the clusters w.r.t crime numbers  
	cluster_index = []
	cluster_index_name = ['V_High', 'High','Low','V_Low']
	
	#Ascending color intensity i.e red=v_high yellow=low
	cluster_intens=['red','brown','orange','yellow']
	cluster_color=['red','brown','orange','yellow']
	for i in range(0,4):
	    index= np.argmax(center_sum) #FInds the max element fron the array
	    center_sum[index]=0;
	    
	    cluster_index.append(index)
	    cluster_color[index]=cluster_intens[i]
    



	#Training data
	print(cluster_color)
	print(cluster_index)

	arr=DT_training_data_gen() 
	#Placing the data array to data frame 
	# DTree_df= pd.read_csv("DTreeT.csv")
	DTree_df=pd.DataFrame(columns=['V_High', 'High','Low','V_Low','O_Label'])
	x,y = np.shape(arr)
	for i in range(0,x):
	    df2=pd.DataFrame([arr[i][:]],columns=['V_High', 'High','Low','V_Low','O_Label'])
	    DTree_df=DTree_df.append(df2,ignore_index=True)
	    


	#Selecting the features for X and Y value for Desision tree
	feature_cols = ['V_High', 'High', 'Low', 'V_Low']
	X = DTree_df[feature_cols] # Features
	y = DTree_df.O_Label # Target variable
	X=X.to_numpy()
	X=X.astype(np.int)
	y=y.to_numpy()
	y=y.astype(np.int)


	#Decision Tree training
	D_Tree = Decision_Tree(X,y)


	#Gettin All the unique districts	
	unique_districts=data_frame.DISTRICT.unique()
	# district=unique_districts[1]
	District_Clusters={}
	for district in unique_districts:
		D_Tree_Pred=district_wise_pred(data_frame,district,D_Tree,cluster_index)
		print(D_Tree_Pred)
		# index= np.where(cluster_index == D_Tree_Pred[0] )
		index=D_Tree_Pred[0]
		cluster_name= cluster_index_name[index]
		print(cluster_name)
		District_Clusters[district]=cluster_name


	return District_Clusters
	


def Single_Crime_Analyz(State_df,crime):

	#Removing the total row 
	State_df=State_df[State_df.DISTRICT != "TOTAL"]
		

	#Selecting the required columns
	data_frame=State_df.loc[:,['DISTRICT',crime]]


	#Selecting the columns for clustering
	data_arr = data_frame.iloc[:,1:] 
	data_arr = np.array(data_arr) #Converting to array


	#Applying KMeans
	clusters=K_means(4,data_arr)
	clusters.cluster_centers_
	clusters.labels_



	#Placing the cluster value to the dataset by creating new column name Crime_cluster
	data_frame['Crime_clusters'] = clusters.labels_ 




	#Adding the feature centers for getting each cluster centers
	centers = np.array(clusters.cluster_centers_)
	center_sum =np.sum(centers,axis=1)



	#Sorting the clusters w.r.t crime numbers  
	cluster_index = []
	cluster_index_name = ['V_High', 'High','Low','V_Low']
	
	#Ascending color intensity i.e red=v_high yellow=low
	cluster_intens=['red','brown','orange','yellow']
	cluster_color=['red','brown','orange','yellow']
	for i in range(0,4):
	    index= np.argmax(center_sum) #FInds the max element fron the array
	    center_sum[index]=0;
	    
	    cluster_index.append(index)
	    cluster_color[index]=cluster_intens[i]
    



	#Training data
	print(cluster_color)
	print(cluster_index)

	arr=DT_training_data_gen() 
	#Placing the data array to data frame 
	DTree_df=pd.DataFrame(columns=['V_High', 'High','Low','V_Low','O_Label'])
	x,y = np.shape(arr)
	for i in range(0,x):
	    df2=pd.DataFrame([arr[i][:]],columns=['V_High', 'High','Low','V_Low','O_Label'])
	    DTree_df=DTree_df.append(df2,ignore_index=True)
	    


	#Selecting the features for X and Y value for Desision tree
	feature_cols = ['V_High', 'High', 'Low', 'V_Low']
	X = DTree_df[feature_cols] # Features
	y = DTree_df.O_Label # Target variable
	X=X.to_numpy()
	X=X.astype(np.int)
	y=y.to_numpy()
	y=y.astype(np.int)


	#Decision Tree training
	D_Tree = Decision_Tree(X,y)


	#Gettin All the unique districts	
	unique_districts=data_frame.DISTRICT.unique()
	# district=unique_districts[1]
	District_Clusters={}
	for district in unique_districts:
		D_Tree_Pred=district_wise_pred(data_frame,district,D_Tree,cluster_index)
		print(D_Tree_Pred)
		# index= np.where(cluster_index == D_Tree_Pred[0] )
		index=D_Tree_Pred[0]
		cluster_name= cluster_index_name[index]
		print(cluster_name)
		District_Clusters[district]=cluster_name




	return District_Clusters
	










def Regional_Analyz():
	State_df=df_list[State_list[0]]


	#Joining all the state file to one file

	for state in State_list_S:
		State_df=State_df.append(df_list[state])





	#Removing the total row 
	State_df=State_df[State_df.DISTRICT == "TOTAL"]
		

	#Selecting the required columns
	data_frame=State_df.drop('DISTRICT',axis=1)


	# Adding all the crime and storing it on a new column called TOTAL
	data_frame["TOTAL"]= data_frame.iloc[:,2:].sum(axis=1)


	#Selecting the columns for clustering
	data_arr = data_frame.iloc[:,-1:] 
	data_arr = np.array(data_arr) #Converting to array


	#Applying KMeans
	clusters=K_means(4,data_arr)
	clusters.cluster_centers_
	clusters.labels_



	#Placing the cluster value to the dataset by creating new column name Crime_cluster
	data_frame['Crime_clusters'] = clusters.labels_ 




	#Adding the feature centers for getting each cluster centers
	centers = np.array(clusters.cluster_centers_)
	center_sum =np.sum(centers,axis=1)



	#Sorting the clusters w.r.t crime numbers  
	cluster_index = []
	cluster_index_name = ['V_High', 'High','Low','V_Low']

	#Ascending color intensity i.e red=v_high yellow=low
	cluster_intens=['red','brown','orange','yellow']
	cluster_color=['red','brown','orange','yellow']
	for i in range(0,4):
	    index= np.argmax(center_sum) #FInds the max element fron the array
	    center_sum[index]=0;
	    
	    cluster_index.append(index)
	    cluster_color[index]=cluster_intens[i]




	#Training data

	arr=DT_training_data_gen() 
	#Placing the data array to data frame 
	DTree_df=pd.DataFrame(columns=['V_High', 'High','Low','V_Low','O_Label'])
	x,y = np.shape(arr)
	for i in range(0,x):
	    df2=pd.DataFrame([arr[i][:]],columns=['V_High', 'High','Low','V_Low','O_Label'])
	    DTree_df=DTree_df.append(df2,ignore_index=True)
	    


	#Selecting the features for X and Y value for Desision tree
	feature_cols = ['V_High', 'High', 'Low', 'V_Low']
	X = DTree_df[feature_cols] # Features
	y = DTree_df.O_Label # Target variable
	X=X.to_numpy()
	X=X.astype(np.int)
	y=y.to_numpy()
	y=y.astype(np.int)


	#Decision Tree training
	D_Tree = Decision_Tree(X,y)


	#Gettin All the unique States	
	unique_states=data_frame.STATE.unique()
	# district=unique_districts[1]
	State_Clusters={}
	for state in unique_states:
		D_Tree_Pred=state_wise_pred(data_frame,state,D_Tree,cluster_index)
		print(D_Tree_Pred)
		# index= np.where(cluster_index == D_Tree_Pred[0] )
		index=D_Tree_Pred[0]
		cluster_name= cluster_index_name[index]
		State_Clusters[state]=cluster_name

	print(State_Clusters)
	return State_Clusters





def District_Year_Analyz(state,district):
	crime_cat_names=['MURDER','RAPE','KIDNAPPING & ABDUCTION','DACOITY','ROBBERY','BURGLARY','THEFT','AUTO THEFT','CHEATING','HURT/GREVIOUS HURT']
	top_crime_col_index=[]
	total={}
	top_crime={}
	second_top_crime={}
	top_crime_list={}

	data_frame=state[state.DISTRICT == district]

	#Removing the State column	
	data_frame=data_frame.iloc[:,1:]


	data_frame["TOTAL"]= data_frame.iloc[:,2:].sum(axis=1)


	#Selecting the crime category column and converting to array
	data_frame_with_year_and_total=data_frame.iloc[:,1:]
	data_frame=np.array(data_frame_with_year_and_total.iloc[:,1:-1])
	data_frame_with_year_and_total=np.array(data_frame_with_year_and_total)
	data_row=data_frame[:1,:]
	crime_cat_len=len(data_row[0])






	#Finding avg crimate rate for each crime category in the district
	crime_col_avg=[]
	no_of_year=0
	for i in range(0,crime_cat_len):
	    data_col=data_frame[:,i:i+1]
	    no_of_year=len(data_col)
	    col_total=data_col.sum(axis=0)
	    col_avg=col_total/no_of_year
	    crime_col_avg.append(col_avg[0])






	#Finding topmost and second topmost crime in the district
	for i in range(0,2):
	    col_index = np.argmax(crime_col_avg)
	    top_crime_col_index.append(col_index)
	    crime_col_avg[col_index]=0



	#filing the top,total and second top crime list on year basis
	for i in range(0,no_of_year):
	    year=data_frame_with_year_and_total[i][0]
	    top_crime[str(year)]=int(data_frame[i][top_crime_col_index[0]])
	    second_top_crime[str(year)]=int(data_frame[i][top_crime_col_index[1]])
	    total[str(year)]=int(data_frame_with_year_and_total[i][-1])



	#Category name of the top 2 crime
	top_crime_list["top"]=crime_cat_names[top_crime_col_index[0]]
	top_crime_list["Second_top"]=crime_cat_names[top_crime_col_index[1]]



	composition_data_obj={"top_crime_list":top_crime_list,"total":total,"top_crime":top_crime,"second_top_crime":second_top_crime}
	return composition_data_obj






def State_Year_Analyz(state):
	crime_cat_names=['MURDER','RAPE','KIDNAPPING & ABDUCTION','DACOITY','ROBBERY','BURGLARY','THEFT','AUTO THEFT','CHEATING','HURT/GREVIOUS HURT']
	top_crime_col_index=[]
	total={}
	top_crime={}
	second_top_crime={}
	top_crime_list={}

	data_frame=state[state.DISTRICT == "TOTAL"]
	

	#Removing the State column	
	data_frame=data_frame.iloc[:,1:]
	

	data_frame["TOTAL"]= data_frame.iloc[:,2:].sum(axis=1)
	print(data_frame)

	#Selecting the crime category column and converting to array
	data_frame_with_year_and_total=data_frame.iloc[:,1:]
	data_frame=np.array(data_frame_with_year_and_total.iloc[:,1:-1])
	data_frame_with_year_and_total=np.array(data_frame_with_year_and_total)
	data_row=data_frame[:1,:]
	crime_cat_len=len(data_row[0])

	print(data_frame,crime_cat_len)




	#Finding avg crimate rate for each crime category in the district
	crime_col_avg=[]
	no_of_year=0
	for i in range(0,crime_cat_len):
	    data_col=data_frame[:,i:i+1]
	    no_of_year=len(data_col)
	    col_total=data_col.sum(axis=0)
	    col_avg=col_total/no_of_year
	    crime_col_avg.append(col_avg[0])





	print(crime_col_avg,no_of_year)
	#Finding topmost and second topmost crime in the district
	for i in range(0,2):
	    col_index = np.argmax(crime_col_avg)
	    top_crime_col_index.append(col_index)
	    crime_col_avg[col_index]=0


	print(top_crime_col_index)
	#filing the top,total and second top crime list on year basis
	for i in range(0,no_of_year):
	    year=data_frame_with_year_and_total[i][0]
	    top_crime[str(year)]=int(data_frame[i][top_crime_col_index[0]])
	    second_top_crime[str(year)]=int(data_frame[i][top_crime_col_index[1]])
	    total[str(year)]=int(data_frame_with_year_and_total[i][-1])



	#Category name of the top 2 crime
	top_crime_list["top"]=crime_cat_names[top_crime_col_index[0]]
	top_crime_list["Second_top"]=crime_cat_names[top_crime_col_index[1]]



	composition_data_obj={"top_crime_list":top_crime_list,"total":total,"top_crime":top_crime,"second_top_crime":second_top_crime}
	return composition_data_obj













































def Regional_Analyz_Nassam():
	State_df=df_list[State_list[0]]


	#Joining all the state file to one file

	for state in State_list_S_Nassam:
		State_df=State_df.append(df_list[state])





	#Removing the total row 
	State_df=State_df[State_df.DISTRICT == "TOTAL"]
		

	#Selecting the required columns
	data_frame=State_df.drop('DISTRICT',axis=1)


	# Adding all the crime and storing it on a new column called TOTAL
	data_frame["TOTAL"]= data_frame.iloc[:,2:].sum(axis=1)


	#Selecting the columns for clustering
	data_arr = data_frame.iloc[:,-1:] 
	data_arr = np.array(data_arr) #Converting to array


	#Applying KMeans
	clusters=K_means(4,data_arr)
	clusters.cluster_centers_
	clusters.labels_



	#Placing the cluster value to the dataset by creating new column name Crime_cluster
	data_frame['Crime_clusters'] = clusters.labels_ 




	#Adding the feature centers for getting each cluster centers
	centers = np.array(clusters.cluster_centers_)
	center_sum =np.sum(centers,axis=1)



	#Sorting the clusters w.r.t crime numbers  
	cluster_index = []
	cluster_index_name = ['V_High', 'High','Low','V_Low']

	#Ascending color intensity i.e red=v_high yellow=low
	cluster_intens=['red','brown','orange','yellow']
	cluster_color=['red','brown','orange','yellow']
	for i in range(0,4):
	    index= np.argmax(center_sum) #FInds the max element fron the array
	    center_sum[index]=0;
	    
	    cluster_index.append(index)
	    cluster_color[index]=cluster_intens[i]




	#Training data

	arr=DT_training_data_gen() 
	#Placing the data array to data frame 
	DTree_df=pd.DataFrame(columns=['V_High', 'High','Low','V_Low','O_Label'])
	x,y = np.shape(arr)
	for i in range(0,x):
	    df2=pd.DataFrame([arr[i][:]],columns=['V_High', 'High','Low','V_Low','O_Label'])
	    DTree_df=DTree_df.append(df2,ignore_index=True)
	    


	#Selecting the features for X and Y value for Desision tree
	feature_cols = ['V_High', 'High', 'Low', 'V_Low']
	X = DTree_df[feature_cols] # Features
	y = DTree_df.O_Label # Target variable
	X=X.to_numpy()
	X=X.astype(np.int)
	y=y.to_numpy()
	y=y.astype(np.int)


	#Decision Tree training
	D_Tree = Decision_Tree(X,y)


	#Gettin All the unique States	
	unique_states=data_frame.STATE.unique()
	# district=unique_districts[1]
	State_Clusters={}
	for state in unique_states:
		D_Tree_Pred=state_wise_pred(data_frame,state,D_Tree,cluster_index)
		print(D_Tree_Pred)
		# index= np.where(cluster_index == D_Tree_Pred[0] )
		index=D_Tree_Pred[0]
		cluster_name= cluster_index_name[index]
		State_Clusters[state]=cluster_name

	print(State_Clusters)
	return State_Clusters









def State_Analyz_for_a_year(State_df,year):
	


	#Removing the total row 
	State_df=State_df[State_df.DISTRICT != "TOTAL"]
	
	


	#Selecting the required columns
	data_frame=State_df.iloc[:,1:]
	# data=data_frame.iloc[:,2:]


	# Adding all the crime and storing it on a new column called TOTAL
	data_frame["TOTAL"]= data_frame.iloc[:,2:].sum(axis=1)


	#Selecting the columns for clustering
	data_arr = data_frame.iloc[:,2:-1] 
	data_arr = np.array(data_arr) #Converting to array



	#Applying KMeans
	clusters=K_means(4,data_arr)
	clusters.cluster_centers_
	clusters.labels_


	#Placing the cluster value to the dataset by creating new column name Crime_cluster
	data_frame['Crime_clusters'] = clusters.labels_ 
	# print(data_frame.sort_values(by=['TOTAL'],ascending = True)) #Sorting the dataframe w.r.t label

	#Select the rows for the current year
	State_df=State_df[State_df.YEAR == year]



	#Adding the feature centers for getting each cluster centers
	centers = np.array(clusters.cluster_centers_)
	center_sum =np.sum(centers,axis=1)



	#Sorting the clusters w.r.t crime numbers  
	cluster_index = []
	cluster_index_name = ['V_High', 'High','Low','V_Low']
	
	#Ascending color intensity i.e red=v_high yellow=low
	cluster_intens=['red','brown','orange','yellow']
	cluster_color=['red','brown','orange','yellow']
	for i in range(0,4):
	    index= np.argmax(center_sum) #FInds the max element fron the array
	    center_sum[index]=0;
	    
	    cluster_index.append(index)
	    cluster_color[index]=cluster_intens[i]
    



	Result ={}
	# data_frameArr=np.array(data_frame);
	for i in range(0,len(data_frame)):
		cluster_value=data_frame.iloc[i].Crime_clusters
		index=np.where(cluster_index==cluster_value)
		index=index[0][0]
		Result[data_frame.iloc[i].DISTRICT]=cluster_index_name[index]

	
	return Result









def Regional_Analyz_for_a_year(year):
	State_df=df_list[State_list[0]]


	#Joining all the state file to one file

	for state in State_list_S:
		State_df=State_df.append(df_list[state])



	print(State_df)

	#Removing the total row 
	State_df=State_df[State_df.DISTRICT == "TOTAL"]

	
		

	#Selecting the required columns
	data_frame=State_df.drop('DISTRICT',axis=1)


	# Adding all the crime and storing it on a new column called TOTAL
	data_frame["TOTAL"]= data_frame.iloc[:,2:].sum(axis=1)


	#Selecting the columns for clustering
	data_arr = data_frame.iloc[:,-1:] 
	data_arr = np.array(data_arr) #Converting to array


	#Applying KMeans
	clusters=K_means(4,data_arr)
	clusters.cluster_centers_
	clusters.labels_



	#Placing the cluster value to the dataset by creating new column name Crime_cluster
	data_frame['Crime_clusters'] = clusters.labels_ 

	#Select the rows for the current year
	State_df=State_df[State_df.YEAR == year]



	#Adding the feature centers for getting each cluster centers
	centers = np.array(clusters.cluster_centers_)
	center_sum =np.sum(centers,axis=1)



	#Sorting the clusters w.r.t crime numbers  
	cluster_index = []
	cluster_index_name = ['V_High', 'High','Low','V_Low']

	#Ascending color intensity i.e red=v_high yellow=low
	cluster_intens=['red','brown','orange','yellow']
	cluster_color=['red','brown','orange','yellow']
	for i in range(0,4):
	    index= np.argmax(center_sum) #FInds the max element fron the array
	    center_sum[index]=0;
	    
	    cluster_index.append(index)
	    cluster_color[index]=cluster_intens[i]



	Result ={}
	# data_frameArr=np.array(data_frame);
	for i in range(0,len(data_frame)):
		cluster_value=data_frame.iloc[i].Crime_clusters
		index=np.where(cluster_index==cluster_value)
		index=index[0][0]
		Result[data_frame.iloc[i].STATE]=cluster_index_name[index]

	return Result













	# #Gettin All the unique districts	
	# unique_districts=data_frame.DISTRICT.unique()
	# # district=unique_districts[1]
	# District_Clusters={}
	# for district in unique_districts:
	# 	D_Tree_Pred=district_wise_pred(data_frame,district,D_Tree,cluster_index)
	# 	print(D_Tree_Pred)
	# 	# index= np.where(cluster_index == D_Tree_Pred[0] )
	# 	index=D_Tree_Pred[0]
	# 	cluster_name= cluster_index_name[index]
	# 	print(cluster_name)
	# 	District_Clusters[district]=cluster_name


	# return District_Clusters

# District_Clusters=State_Analyz(df_list['Manipur'])

# print(District_Clusters)

# Single_Crime_Analyz(df_list['Manipur_Major_Data'],'RAPE')
# Regional_Analyz()

# print(District_Year_Analyz(df_list['Manipur'],"IMPHAL_WEST"))

# print(State_Year_Analyz(df_list['Manipur']))
# Regional_Analyz_for_a_year(2001)