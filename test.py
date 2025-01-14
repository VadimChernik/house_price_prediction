import requests

# Here is your API url:
url = 'http://localhost:9696/predict'

# Here are your house characteristics, in a dict:
house = {
    "lotarea": 11475,
    "masvnrarea": 0.0,
    "bsmtfinsf1": 550,
    "bsmtunfsf": 163,
    "totalbsmtsf": 713,
    "1stflrsf": 811,
    "2ndflrsf": 741,
    "grlivarea": 1552,
    "bsmtfullbath": 1,
    "fullbath": 2,
    "halfbath": 1,
    "bedroomabvgr": 3,
    "totrmsabvgrd": 6,
    "fireplaces": 1,
    "garagecars": 2,
    "garagearea": 434,
    "wooddecksf": 209,
    "openporchsf": 208,
    "age": 50,
    "totalsf": 2265,
    "mszoning": "RL",
    "lotshape": "Reg",
    "landcontour": "Lvl",
    "lotconfig": "Inside",
    "neighborhood": "NWAmes",
    "condition1": "RRAn",
    "bldgtype": "1Fam",
    "housestyle": "2Story",
    "overallqual": "6",
    "overallcond": "6",
    "yearbuilt": "1975",
    "yearremodadd": "1975",
    "roofstyle": "Gable",
    "exterior1st": "VinylSd",
    "exterior2nd": "VinylSd",
    "exterqual": "TA",
    "extercond": "TA",
    "foundation": "CBlock",
    "bsmtqual": "Gd",
    "bsmtcond": "TA",
    "bsmtexposure": "No",
    "bsmtfintype1": "ALQ",
    "bsmtfintype2": "Unf",
    "heatingqc": "TA",
    "electrical": "SBrkr",
    "kitchenqual": "TA",
    "functional": "Typ",
    "garagetype": "Attchd",
    "garageyrblt": "1975.0",
    "garagefinish": "RFn",
    "garagequal": "TA",
    "paveddrive": "Y",
    "mosold": "2",
    "yrsold": "2006",
    "saletype": "WD",
    "salecondition": "Normal"
}

# Here your get your response from your API using the customer above
response = requests.post(url, json=house).json()
print(response)