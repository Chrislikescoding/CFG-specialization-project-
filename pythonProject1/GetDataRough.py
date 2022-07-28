import json
import datetime
import csv
# f = open('2019_MARCH.json', 'r')
# data = json.load(f)


with open("2019_MARCH.json", "r") as read_file:
    read_content = json.load(read_file)
    access=read_content['timelineObjects']
   # print(type(access))
    f= open('first.csv', 'w',newline='')
    writer = csv.writer(f)
  #  writer = csv.writer(csvfile, delimiter=' ',
    #                    quotechar='|', quoting=csv.QUOTE_MINIMAL)
for element in access:
  # print(element)

   try:
    # print(type(element['placeVisit']))
     #  print(type(element['placeVisit']['location']['latitudeE7']))
         if element.get('placeVisit', 'nokey') != 'nokey':
             start1 = element['placeVisit']['location']['latitudeE7']
             address1 = element['placeVisit']['location']['address']
             name = element['placeVisit']['location']['name']

             print(start1)
             print(address1)

             header = ['start', 'address']


             # with open('first.csv', 'w') as f:
             #     writer = csv.writer(f)
             #
             #     # write the header
             #     writer.writerow(header)
             #
             #     # write the data
             #     writer.writerow(data)
             #     f.close()

         elif  element.get('activitySegment', 'nokey') != 'nokey':
             start2=element['activitySegment']['startLocation']['latitudeE7']
             activity_type=element['activitySegment']['activityType']
             timestampfr=element['activitySegment']['duration']['startTimestamp']

             timestampto = element['activitySegment']['duration']['endTimestamp']
             time_to = timestampto[12:19]
             time_from = timestampfr[12:19]

             distance = element['activitySegment']['waypointPath']['distanceMeters']

             data2 = [name,address1, time_from, time_to, distance]
             print(data2)
             if activity_type == 'IN_PASSENGER_VEHICLE' and data2 != '' :
                writer.writerow(data2)


                 # write the header
         #        writer.writerow(header)

                 # write the data

     #print(type)
#print(distance)
   except KeyError:
        print("there was an error")

 #   print('*******************************************************')


      # print(type(element['activitySegment']['distance']))
      # print(element['activitySegment']['activityType'])
        #    parkingEvent =element['activitySegment']['parkingEvent']
      #  print(end + ' ' + parkingEvent)



