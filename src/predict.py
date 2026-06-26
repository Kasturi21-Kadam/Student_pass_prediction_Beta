import joblib

model = joblib.load("model/model.pkl")

hours = [[6]]

prediction = model.predict(hours)

if prediction[0] == 1:
	print("Pass")
else:
	print("Fail")