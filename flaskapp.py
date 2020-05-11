from main import *
from flask import Flask, render_template, request, jsonify
from flask import request


app = Flask(__name__)


@app.route('/')
def index():
	return render_template('index.html')


@app.route('/backend/Entire', methods=['POST'])
def process():
	
	name = request.form["name"]
	state = request.form["state"] 

	if name and state!= 'selected disabled':
		District_Clusters=State_Analyz(df_list[state])
		return jsonify(District_Clusters)
	else:
		return jsonify({'err' : 'Error Occured!'})



@app.route('/backend/Individual', methods=['POST'])
def process2():
	
	name = request.form["name"]
	crime = request.form["crime"]
	state = request.form["state"] 

	if name and state!= 'selected disabled' and crime!= 'selected disabled':
		District_Clusters=Single_Crime_Analyz(df_list[state],crime)
		return jsonify(District_Clusters)
	else:
		return jsonify({'err' : 'Error Occured!'})




@app.route('/backend/Entire_NE', methods=['POST'])
def process3():
	
	name = request.form["name"]

	if name:
		State_Clusters=Regional_Analyz()
		return jsonify(State_Clusters)
	else:
		return jsonify({'err' : 'Error Occured!'})




@app.route('/backend/Entire/year', methods=['POST'])
def process4():
	
	district = request.form["district"]
	state = request.form["state"]

	if district and state:
		Year_Analysis=District_Year_Analyz(df_list[state],district)
		return jsonify(Year_Analysis)
	else:
		return jsonify({'err' : 'Error Occured!'})






@app.route('/backend/Entire_NE/year', methods=['POST'])
def process5():
	
	state = request.form["state"]

	if state:
		Year_Analysis=State_Year_Analyz(df_list[state])
		return jsonify(Year_Analysis)
	else:
		return jsonify({'err' : 'Error Occured!'})

































@app.route('/NE/N_Assam')
def process10():
	State_Clusters=Regional_Analyz_Nassam()
	return jsonify(State_Clusters)




@app.route('/StateYear')
def process11():
	# State_Clusters=Regional_Analyz_Nassam()
	state=request.args.get('state')
	Year=request.args.get('year')
	print("hdskjhgfdghdjshgjdhk",Year,type(int(Year)))
	District_Clusters=State_Analyz_for_a_year(df_list[state],int(Year))
	return jsonify(District_Clusters)







@app.route('/NEYear')
def process12():
	# State_Clusters=Regional_Analyz_Nassam()
	Year=request.args.get('year')
	State_Clusters= Regional_Analyz_for_a_year(int(Year))
	return jsonify(State_Clusters)





@app.route('/StateCrimeYear')
def process13():
	# State_Clusters=Regional_Analyz_Nassam()
	state=request.args.get('state')
	crime=request.args.get('crime')
	Year=request.args.get('year')
	State_Clusters= Single_Crime_Analyz_State_for_a_year(df_list[state],crime,int(Year))
	return jsonify(State_Clusters)



@app.route('/NECrimeYear')
def process14():
	# State_Clusters=Regional_Analyz_Nassam()
	crime=request.args.get('crime')
	Year=request.args.get('year')
	State_Clusters= Regional_Analyz_for_a_year_Single_Crime(int(Year),crime)
	return jsonify(State_Clusters)


@app.route('/NECrimeYearNotAssam')
def process15():
	# State_Clusters=Regional_Analyz_Nassam()
	crime=request.args.get('crime')
	Year=request.args.get('year')
	State_Clusters= Regional_Analyz_for_a_year_Single_Crime_NAssam(int(Year),crime)
	return jsonify(State_Clusters)



if __name__ == '__main__':
	app.run(host= '0.0.0.0',port=8080)

























	