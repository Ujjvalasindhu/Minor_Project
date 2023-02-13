from flask  import Flask, render_template, request
import pickle,pandas
app=Flask(__name__)
@app.route('/', methods=['GET', 'POST'])
def predict():
	html='cropprediction.html'
	if request.method == 'GET':
		return render_template(html)
	else:
		model=pickle.load(open('model.pkl','rb'))
		cropslist=list(pickle.load(open('crop.pkl','rb')))
		distlist=list(pickle.load(open('dist.pkl','rb')))
		seasonlist=list(pickle.load(open('season.pkl','rb')))
		dist=request.form['dist']
		crpyr=request.form['crpyr']
		season=request.form['season']
		crop=request.form['crop']
		area=request.form['area']
		dist_test=distlist.index(dist.upper())
		crpyr_test=int(crpyr)
		season_test=seasonlist.index(season.capitalize())
		crop_test=cropslist.index(crop.capitalize())
		area_test=float(area)
		input=pandas.DataFrame(columns=['District_Name', 'Crop_Year', 'Season', 'Crop', 'Area'])
		input.loc[0]=[dist_test, crpyr_test, season_test, crop_test, area_test]
		return render_template(html, result=model.predict(input)[0])
if __name__ == '__main__':
	app.run(debug=True)