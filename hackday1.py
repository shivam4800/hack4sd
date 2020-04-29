from googleplaces import GooglePlaces, types, lang 
import requests 
import json
global city,loca1,loca,l1,l2,data,res
res = requests.get('https://ipinfo.io/')
data = res.json()

city = data['city']
loca1=data['loc']
loca=loca1.split(",")
print(loca)

l1=str(loca[0])
l2=str(loca[1])
print(l1)
print(l2)
print(city)
print(data) 

def hospitals():
    
    API_KEY = 'AIzaSyCtOBNxN2ppCKdrhDOWnqp207YIg3lLYWIgoogle_places = GooglePlaces(API_KEY)'
      

    query_result = google_places.nearby_search(  
            lat_lng ={'lat': l1, 'lng': l2}, 
            radius = 5000, 
           
            types =[types.hospital]) 
      
     
    if query_result.has_attributions: 
        print (query_result.html_attributions) 
      
      

    for place in query_result.places: 
        # print(type(place)) 
        # place.get_details()
        print(place)
        print (place.name) 
        print("Latitude", place.geo_location['lat']) 
        print("Longitude", place.geo_location['lng']) 
        print()
def covid():
    states=[]
    users=input("enter state name: ")
    users=users.lower()
    
    res1 = requests.get('https://api.rootnet.in/covid19-in/stats/latest')
    data1 = res1.json()
    for i in range(0,32):
        
        state=(data1['data']['regional'][i]['loc'])
        state=state.lower()
        states.append(state)
    if users in states:
            o=states.index(users)
            print(data1['data']['regional'][o]['deaths'])
    else:
            print("state not found")
    

covid()
    


