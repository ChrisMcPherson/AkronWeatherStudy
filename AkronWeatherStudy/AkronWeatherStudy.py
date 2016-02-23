from urllib.request import urlopen
import os.path
import csv


headers = ['EST','Max TemperatureF','Mean TemperatureF','Min TemperatureF','Max Dew PointF','MeanDew PointF','Min DewpointF','Max Humidity', 'Mean Humidity', 'Min Humidity', 'Max Sea Level PressureIn', 'Mean Sea Level PressureIn', 'Min Sea Level PressureIn', 'Max VisibilityMiles', 'Mean VisibilityMiles', 'Min VisibilityMiles', 'Max Wind SpeedMPH', 'Mean Wind SpeedMPH', 'Max Gust SpeedMPH','PrecipitationIn', 'CloudCover', 'Events', 'WindDirDegrees']
fileExists = False

if os.path.isfile(path):
    fileExists = True
else:
    forecastFile = open(path, 'w')
    dataSet.append(headers)

startingYear = 1987
while (1987 < 2016):
    weatherAPI = 'https://www.wunderground.com/history/airport/KAKR/{}/1/1/CustomHistory.html?dayend=31&monthend=12&yearend={}&req_city=&req_state=&req_statename=&reqdb.zip=&reqdb.magic=&reqdb.wmo=&format=1'.format(startingYear, startingYear)
    path = 'C:\\Users\\Chris\\Desktop\\ForecastData.csv'

    response = urlopen(weatherAPI) #Get csv from API
    rawData = csv.reader(response)

    with open(path, 'a', newline='') as myfile:
        wr = csv.writer(myfile, quoting=csv.QUOTE_ALL)
        next(rawData, None) #skip header
        for row in rawData:
            wr.writerow(row)

    startingYear = startingYear + 1

