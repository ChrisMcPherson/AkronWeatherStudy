from urllib.request import urlopen
import os.path
import csv

path = 'C:\\Users\\Chris\\Desktop\\AkronWeatherData.csv'
headers = ['EST','Max TemperatureF','Mean TemperatureF','Min TemperatureF','Max Dew PointF','MeanDew PointF','Min DewpointF','Max Humidity', 'Mean Humidity', 'Min Humidity', 'Max Sea Level PressureIn', 'Mean Sea Level PressureIn', 'Min Sea Level PressureIn', 'Max VisibilityMiles', 'Mean VisibilityMiles', 'Min VisibilityMiles', 'Max Wind SpeedMPH', 'Mean Wind SpeedMPH', 'Max Gust SpeedMPH','PrecipitationIn', 'CloudCover', 'Events', 'WindDirDegrees']

with open(path, 'a', newline='') as myfile:
    wr = csv.writer(myfile, quoting=csv.QUOTE_ALL)
    wr.writerow(headers)

    startingYear = 1973
    while (startingYear < 2016):
        #weatherApi = 'https://www.wunderground.com/history/airport/KAKR/{}/1/1/CustomHistory.html?dayend=31&monthend=12&yearend={}&req_city=&req_state=&req_statename=&reqdb.zip=&reqdb.magic=&reqdb.wmo=&format=1'.format(startingYear, startingYear)
        weatherApi = 'https://www.wunderground.com/history/airport/KBKL/{}/1/1/CustomHistory.html?dayend=31&monthend=12&yearend={}&req_city=&req_state=&req_statename=&reqdb.zip=&reqdb.magic=&reqdb.wmo=&format=1'.format(startingYear, startingYear)
        response = urlopen(weatherApi) #Get csv from API
        responseDecoded = response.read().decode('utf-8')
        responseFixed = responseDecoded.replace("\n","",1)
        csvFile = csv.reader(responseFixed.splitlines())

        next(csvFile, None) #skip header
        for row in csvFile:
           wr.writerow(row)

        startingYear = startingYear + 1