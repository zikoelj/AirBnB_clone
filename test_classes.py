#!/usr/bin/python3
from models import storage
from models.state import State
from models.city import City
from models.place import Place
from models.review import Review
from models.amenity import Amenity

def main():
    """Chargement des objets depuis le stockage"""
    all_objs = storage.all()

    """Affichage des objets rechargés"""
    print("-- Reloaded objects --")
    for obj_id in all_objs.keys():
        obj = all_objs[obj_id]
        print(obj)

    """ Création d'un nouvel État"""
    print("-- Create a new State --")
    new_state = State()
    new_state.name = "California"
    new_state.save()
    print(new_state)

    """Création d'une nouvelle Ville"""
    print("-- Create a new City --")
    new_city = City()
    new_city.state_id = new_state.id
    new_city.name = "Los Angeles"
    new_city.save()
    print(new_city)

    """ Création d'un nouvel Aménité"""
    print("-- Create a new Amenity --")
    new_amenity = Amenity()
    new_amenity.name = "Wifi"
    new_amenity.save()
    print(new_amenity)
    
    """Création d'une nouvelle Place"""
    print("-- Create a new Place --")
    new_place = Place()
    new_place.city_id = new_city.id
    new_place.user_id = "d780baa2-fda1-4189-aa15-415d8322ee02"  
    new_place.name = "Cozy Apartment"
    new_place.description = "A cozy apartment in the heart of the city."
    new_place.number_rooms = 2
    new_place.number_bathrooms = 1
    new_place.max_guest = 4
    new_place.price_by_night = 100
    new_place.latitude = 34.052235
    new_place.longitude = -118.243683
    new_place.amenity_ids = [new_amenity.id]
    new_place.save()
    print(new_place)

    """Création d'une nouvelle Review"""
    print("-- Create a new Review --")
    new_review = Review()
    new_review.place_id = new_place.id
    new_review.user_id = "d780baa2-fda1-4189-aa15-415d8322ee02"  
    new_review.text = "Great place to stay!"
    new_review.save()
    print(new_review)

if __name__ == "__main__":
    main()
