from django.shortcuts import render
from django.http import HttpResponse
import googlemaps, json, requests
import geopy.distance

from hotelfindernyc.models import Hotel
gmaps = googlemaps.Client(key='AIzaSyAvKZFY2i0mbC74TrJ_KT6k6lcURZNf6wY')
api_key = "AIzaSyAvKZFY2i0mbC74TrJ_KT6k6lcURZNf6wY"
# Create your views here.
def home(request):
    return render(request, 'main.html')

def about_us(request):
    return render(request, 'About_Us.html')

def report(request):
    return render(request, 'hotel_analysis_2.html')

def search_by_address(request):
    if request.method == 'POST':
        address = request.POST.get('address')
        anemity = request.POST.getlist("amenity_filter")
        star = request.POST.getlist("star_filter")
        price_range = request.POST.getlist("price_filter")
        query_dict = {}
        for i in range(len(anemity)):
            query_dict[anemity[i]] = '1'
        if star:
            query_dict['star__in'] = []
            for i in range(len(star)):
                if star[i] == '2':
                    query_dict['star__in'] += ['1.0','2.0']
                else:
                    query_dict['star__in'] += [star[i]]

        hotels = Hotel.objects.filter(**query_dict)

        if price_range:
            hotels = Hotel.objects.exclude(price__lte = 1)
            if "200" not in price_range:
                hotels = hotels.exclude(price__lte = 200)
            if "300" not in price_range:
                hotels = hotels.exclude(price__lte=300, price__gte=200)
            if "400" not in price_range:
                hotels = hotels.exclude(price__lte=400, price__gte=300)
            if "500" not in price_range:
                hotels = hotels.exclude(price__lte=500, price__gte=400)
            if "600" not in price_range:
                hotels = hotels.exclude(price__gte=500)

        hotels = hotels.values()

        if address:
            geo_location = get_location(address, api_key)
            target_hotels = []
            for hotel in hotels:
                lat,lon = hotel['latitude'], hotel['longitude']
                distance = geopy.distance.vincenty(geo_location, (lat,lon)).km
                if distance < 1:
                    hotel_info = {"Name":hotel['name'], "Rating": hotel["rating"],
                                  "Location":hotel["street_address"],"Price":hotel['price'],
                                  "Tel": hotel["phone"], "Web":hotel["web"], "Address":hotel['address'],"Lon":lon, "Lat":lat,
                                  "rating_distribution":[hotel["five_star_rating"], hotel["four_star_rating"],
                                                         hotel["three_star_rating"], hotel["two_star_rating"],
                                                         hotel["one_star_rating"]],
                                  "price_data":[hotel['p1'], hotel['p2'],hotel['p3'],hotel['p4'],hotel['p5'],
                                                hotel['p6'],hotel['p7'],hotel['p8'],hotel['p9'],hotel['p10']],
                                  "nearby_hotel":[hotel['n1'],hotel['n2'],hotel['n3'],hotel['n4'],hotel['n5'],
                                                  hotel['n6'],hotel['n7'],hotel['n8'],hotel['n9'],hotel['n10']]}
                    target_hotels.append(hotel_info)
        else:
            target_hotels = []
            for hotel in hotels:
                hotel_info = {"Name": hotel['name'], "Rating": hotel["rating"],
                              "Location": hotel["street_address"], "Price": hotel['price'],
                              "Tel": hotel["phone"], "Web": hotel["web"], "Address": hotel['address'], "Lon": hotel['longitude'],
                              "Lat": hotel['latitude'],
                              "rating_distribution": [hotel["five_star_rating"], hotel["four_star_rating"],
                                                      hotel["three_star_rating"], hotel["two_star_rating"],
                                                      hotel["one_star_rating"]],
                              "price_data": [hotel['p1'], hotel['p2'], hotel['p3'], hotel['p4'], hotel['p5'],
                                             hotel['p6'], hotel['p7'], hotel['p8'], hotel['p9'], hotel['p10']],
                              "nearby_hotel": [hotel['n1'], hotel['n2'], hotel['n3'], hotel['n4'], hotel['n5'],
                                               hotel['n6'], hotel['n7'], hotel['n8'], hotel['n9'], hotel['n10']]}
                target_hotels.append(hotel_info)

        return render(request, 'main.html', {'hotels': target_hotels})

    return render(request, 'main.html')


def get_location(address, api_key):
    api_response = requests.get('https://maps.googleapis.com/maps/api/geocode/json?address={0}&key={1}'.format(address, api_key))
    api_response_dict = api_response.json()
    if api_response_dict['status'] == 'OK':
        latitude = api_response_dict['results'][0]['geometry']['location']['lat']
        longitude = api_response_dict['results'][0]['geometry']['location']['lng']
    return (latitude, longitude)

