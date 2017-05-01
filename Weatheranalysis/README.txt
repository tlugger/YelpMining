processweather.py modifies these csv files in this order(uses many csv files because doesnt do file modifications in place)
pitt2016->edit->dates->filleddates->avgweather
avgweather.csv will contain one row with the weather rating for that hour

createdailyaverages.py will create the daily average for every day
ive taken average weather and pasted it into avgthis.csv in the DAILYSunset row for convinience
it will use csv files in this order
avgthis->avgdailyweather
