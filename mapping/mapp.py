import folium
import pandas as pd
map = folium.Map(location=[29.1492, 75.7217], tiles="OpenStreetMap", default_zoom_start=15)



data = pd.DataFrame({
   'lon':[75.645, 76.453, 75.452, 75.23, 75.03, 73.57, 75.82, 78.5],
   'lat':[28.123, 28.3243, 28.32, 28.93, 28.33, 19.52, 19.29, 72.97],
   'name':['A', 'B', 'C', 'D', 'E', 'f', 'g', 'H'],
   'value':[10, 12, 40, 70, 23, 43, 100, 43]
}, dtype=str)
folium.Marker(
    location=[29.0815, 75.3733],
    popup='oh i located <b>Bhirani</b>',
    tooltip = "Click for more"
).add_to(map)

for i in range(0,len(data)):
   folium.Marker(
      location=[data.iloc[i]['lat'], data.iloc[i]['lon']],
      popup=data.iloc[i]['name'],
   ).add_to(map)
map.save('mymap.html')