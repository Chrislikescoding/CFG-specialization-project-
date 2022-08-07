import json
import csv
from copy import deepcopy

f = open('../2019_MARCH.json', 'r')
with open("../2019_MARCH.json", "r") as read_file:
    read_content = json.load(read_file)
    access=read_content['timelineObjects']
f.close()
data_dict={"from postcode":" ",
           "from place":"",
           "to place":"",
           "distance":0 ,
           "activity type":"",
           "date":"",
            "time":""}

data_to_csv=[]

for key,element in enumerate(access):
    activity_type=' '
    second_row = False
    save_place = ' '
    try:
        if element.get('placeVisit', 'nokey') != 'nokey':
            second_row = False
            data_dict["from postcode"]= element['placeVisit']['location']['address']
            data_dict["from place"]= element['placeVisit']['location']['name']

        elif element.get('activitySegment', 'nokey') != 'nokey':
             second_row = True
             activity_type=element['activitySegment']['activityType']
             timestampfr = element['activitySegment']['duration']['startTimestamp']
             time_from = timestampfr[12:19]
             data_dict["time"]=timestampfr[12:19]
             date_from = timestampfr[0:10]
             data_dict["date"] = timestampfr[0:10]
             distance_flt = element['activitySegment']['waypointPath']['distanceMeters']
             data_dict["distance"] = int(distance_flt)
             data_dict["activity type"]=element['activitySegment']['activityType']
    except KeyError:
        print("there was an error")
    finally:
        if activity_type == 'IN_PASSENGER_VEHICLE':
            data_to_csv.append(deepcopy(data_dict))
for index,diction in enumerate(data_to_csv):
     if index >0:
        data_to_csv[index-1]["to place"]=data_to_csv[index]["from place"]
        print(data_to_csv[index-1]["to place"])
fieldnames=[{'from place':1, 'from postcode':2, 'to place':3, 'distance':4,'time'   :5,'date':6,'activity type':7}]
keys = fieldnames[0].keys()
with open('../first.csv', 'a', newline='') as output_file:
    dict_writer = csv.DictWriter(output_file, keys)
    dict_writer.writeheader()
    dict_writer.writerows(data_to_csv)


