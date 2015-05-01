import os
from json import Feature, Point, FeatureCollection


def get_bike_data():

	bike_file = open("./201408_rebalancing_data.csv")

	for line in bike_file:
		line.strip()
		line = line.split(',')
		print line

  #       location = poi.title
  #       lng = poi.lng
  #       lat = poi.lat
  #       info = poi.info

  #       # Functions from the geojson library create geoson objects with the
  #       # details specified
  #       data_point = Feature(geometry=Point((lng, lat)), properties={
  #                            "title": title, "longitude": lng, "lat": lat, "info": info, "marker-color": "#B0A600"})
  #       coordinates.append(my_point)

  #   # We return all this geojson as a feature collection
  #   new_coords = FeatureCollection(coordinates)
  #   return new_coords

		# if '2014-03-01' in line[3]: 
		# 	print line




get_bike_data();