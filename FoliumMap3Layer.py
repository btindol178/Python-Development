#import folium
#map = folium.Map(location=[38.58,-99.09],zoom_start =6, tiles = "Stamen Terrain") # tiles stamen changes background
#map = folium.Map(location=[38.58,-99.09],zoom_start =6) # tiles stamen changes background

# add marker!
#map.add_child(folium.Marker(location =[38.2,-99.1], popup="Hi I am blake",icon = folium.Icon(color='green'))) # gives you marker
#map.save("Map1.html")

##################################################################################
# instead of doing individually as above make fg a variable to add multiple things in
# make fg feature group for multiple points
# fg = folium.FeatureGroup(name= "My Map")
# fg.add_child(folium.Marker(location =[38.2,-99.1], popup="Hi I am blake",icon = folium.Icon(color='green'))) # gives you marker
# fg.add_child(folium.Marker(location =[37.2,-97.1], popup="Hi I am blake",icon = folium.Icon(color='green'))) # gives you marker
#
# map.add_child(fg) # add fg to map
#
# map.save("Map1.html")
#######################################################################################
# add multiple coordinates
# for coordinates in [[38.2,-99.1],[37.2,-97.1]]:
#     fg.add_child(folium.Marker(location =coordinates, popup="Hi I am blake",icon = folium.Icon(color='green'))) # gives you marker
# map.add_child(fg) # add fg to map
# map.save("Map1.html")
##########################################################################
# for i,j in zip([1,2,3], [4,5,6]):
#     print(i, "and", j)
########################################################################################
# Add multiple coordinates from fil`e first install pandas to load data
# pip install pandas
import pandas
import folium

data = pandas.read_csv("Volcanoes.txt") # dataframe
# data.columns (to see column names)

# make 2 lists to pass to plotting loop!
lat = list(data["LAT"]) # make the column lat into list for the plotting loop
lon = list(data["LON"])
elev = list(data["ELEV"]) # for the popup float number of elevation so need to use str() to convert
#len(lat) length of the columns

# Funciton to change color  in loop dynamically
def color_producer(elevation):
    if elevation < 1000:
        return "green"
    elif 1000 <= elevation < 3000:
        return "orange"
    else:
        return "red"



 # put html link in the html part
# html = """
# Volcano name:<br>
# <a href="https://www.google.com/search?q=%%22%s%%22" target="_blank">%s</a><br>
# Height: %s m
# """
# html for the icon when clicked
html = """<h4>Volcano information:</h4>
Height: %s m
"""

map = folium.Map(location=[38.58,-99.09],zoom_start =6)
# Make map variable
fgv = folium.FeatureGroup(name= "Volcanoes")


for lt, ln, el in zip(lat,lon,elev):
    iframe = folium.IFrame(html=html % str(el), width=200, height=100)
    # This is one way to do it
    #fg.add_child(folium.Marker(location = [lt,ln], popup= folium.Popup(iframe) ,parse_html = True, icon = folium.Icon(color=color_producer(el)))) # gives you marker ( i like this way better)
    # fg.add_child(folium.Marker(location = [lt,ln], popup= str(el)+ " meters" ,parse_html = True, icon = folium.Icon(color='green'))) # gives you marker
    fgv.add_child(folium.CircleMarker(location = [lt,ln], radius = 6, popup= folium.Popup(iframe) ,parse_html = True, fill_color = color_producer(el), color ='gray', fill=True, fill_opacity = 0.7)) # gives you marker

# feature group for population for layer control
fgp = folium.FeatureGroup(name= "Population")

# add coropleth structor layer
# open the world json file # read because folium needs aa string instead of file
# style_function expects lambda function
fgp.add_child(folium.GeoJson(data=(open("world.json","r", encoding = 'utf-8-sig').read()),style_function=lambda x: {'fillColor':'yellow' if x['properties']['POP2005'] < 10000000 else 'orange' if 10000000 <= x['properties']['POP2005'] < 20000000 else 'red'}))
#fg.add_child(folium.GeoJson(data=open("world.json","r", encoding = 'utf-8-sig'),style_function=lambda x: {'fillColor':'yellow'})) # old way

map.add_child(fgv) # add fg volcanoes
map.add_child(fgp) # add fg to map
map.add_child(folium.LayerControl()) # gives you layer toggle
map.save("Map1.html")
