import geopy
import pandas
from geopy.geocoders import Nominatim

#create nominatim object
nom=Nominatim(scheme="http")

def geocoder(filename):
    filename=filename
    print(filename)
    df=pandas.read_csv("uploaded/"+filename)
    return df
    