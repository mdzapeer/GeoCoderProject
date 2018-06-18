import geopy
import pandas
from geopy.geocoders import Nominatim

#create nominatim object
nom=Nominatim(scheme="http")

def geocoder(filename):
    df=pandas.read_csv("uploaded/"+filename)
    df.set_index("ID")
    df.columns=df.columns.str.lower()
    df["latitude"]=df["address"].apply(nom.geocode).apply(lambda x: x.latitude if x != None else None)
    df["longitude"]=df["address"].apply(nom.geocode).apply(lambda x: x.longitude if x != None else None)    
    return df
    