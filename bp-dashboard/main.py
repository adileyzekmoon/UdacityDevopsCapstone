from flask import Flask, render_template
import json

app = Flask(__name__)

@app.route('/index.html', methods = ['GET'])
@app.route('/', methods = ['GET'])
def home():

    
    with open("clientListFull.json", "r") as jsonFile:
        clientData = json.load(jsonFile)

    male = {"12 and under": 0,
            "13 - 18": 0,
            "19 - 24": 0,
            "25 - 30": 0,
            "31 - 39": 0,
            "40 - 49": 0,
            "50 and above": 0}
    female = {"12 and under": 0,
            "13 - 18": 0,
            "19 - 24": 0,
            "25 - 30": 0,
            "31 - 39": 0,
            "40 - 49": 0,
            "50 and above": 0}
    
    for each in clientData:
        if each["BirthDate"]:
            birthYear = int(each["BirthDate"][0:4])
            age = 2021 - birthYear
        if each["Gender"] == "Male":
            if age < 13:
                male["12 and under"] += 1
            elif (13 <= age <= 18):
                male["13 - 18"] += 1
            elif (19 <= age <= 24):
                male["19 - 24"] += 1
            elif (25 <= age <= 30):
                male["25 - 30"] += 1
            elif (31 <= age <= 39):
                male["31 - 39"] += 1
            elif (40 <= age <= 49):
                male["40 - 49"] += 1
            elif 50<= age:
                male["50 and above"] += 1
        elif each["Gender"] == "Female":
            if age < 13:
                female["12 and under"] += 1
            elif (13 <= age <= 18):
                female["13 - 18"] += 1
            elif (19 <= age <= 24):
                female["19 - 24"] += 1
            elif (25 <= age <= 30):
                female["25 - 30"] += 1
            elif (31 <= age <= 39):
                female["31 - 39"] += 1
            elif (40 <= age <= 49):
                female["40 - 49"] += 1
            elif 50 <= age:
                female["50 and above"] += 1

    with open("visitMap.json", "r") as jsonFile:
        visitData = json.load(jsonFile)
    
    passUsageData = {}
    for date in visitData:
        for classPass in visitData[date]:
            if classPass in passUsageData.keys():
                passUsageData[classPass] += visitData[date][classPass]
            else:
                passUsageData[classPass] = visitData[date][classPass]
    
    print(passUsageData)
    topFive = [k for k,x in sorted(passUsageData.items(), key=lambda item: item[1], reverse=True)][0:5]
    print(topFive)
    for each in visitData:
        visitData[each] = sum([visitData[each][key] for key in visitData[each]])
    print(visitData)
                
    
    
    return render_template('index.html', male=male, female=female, visitData=visitData, passUsageData=passUsageData, topFive=topFive)
    
    
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=80, debug=True)