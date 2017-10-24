import folium
import pandas

data = pandas.read_csv("beepop.txt")
lat=list(data["LAT"])
lon=list(data["LON"])
pop=list(data["POPULATION"])


def color_producer(population):
    if population <10000:
        return 'red'
    elif population <= population < 100000:
        return 'orange'
    else:
        return 'green'


data = pandas.read_csv("state_pop.txt")
la=list(data["LAT"])
lo=list(data["LON"])
popu=list(data["POPULATION"])

def color_fill(population):
    if population <900000:
        return 'blue'
    elif population <= population < 1005000:
        return 'green'
    else:
        return 'red'



map = folium.Map(location=[40.6976701,-74.2598712], zoom_start=9, tiles="Mapbox Bright")


fgb=folium.FeatureGroup(name="Bee Population")

for lt,ln,p, in zip(lat,lon,pop):
    fgb.add_child(folium.CircleMarker(location=[lt,ln],radius=6,popup=str(p)+' bees',
    fill_color=color_producer(p),fill=True, color='grey', fill_opacity=0.7))

fgs=folium.FeatureGroup(name="State Population")

for lt,ln,p, in zip(la,lo,popu):
    fgs.add_child(folium.CircleMarker(location=[lt,ln],radius=6,popup=str(p)+' people',
    fill_color=color_fill(p),fill=True, color='grey', fill_opacity=0.7))

fgh=folium.FeatureGroup(name="Human Population")

fgh.add_child(folium.GeoJson(data=open('world.json','r', encoding='utf-8-sig').read(),
style_function=lambda x:{'fillColor':'green' if x['properties']['POP2005'] < 10000000
else 'orange' if 10000000 <= x['properties']['POP2005'] < 200000000 else 'red'}))

map.add_child(fgb)
map.add_child(fgs)
map.add_child(fgh)
map.add_child(folium.LayerControl())

map.save("InteractiveMap.html")
