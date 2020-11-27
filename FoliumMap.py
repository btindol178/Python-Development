# pip install folium
# dir(folium)
#help(folium.map)
import folium

# location given in lat then lon in that order (list of coordinates [80,-100])
map = folium.Map(location=[80,-100])

# point to map object
map.save("Map1.html") # same map and open the file path in the browser

# do antoher coordinates
map = folium.Map(location=[38.58,-99.09],zoom_start =6)
map.save("Map1.html")

# tiles = "Stamen Terrain"
