from ride import RideSharing
from users import Rider, Driver

GoBro = RideSharing("GoBro")
kashem = Rider("Kashem", "kashem@gmail.com", 1234, "Mohakhali", 1200)
GoBro.add_rider(kashem)
ratan = Driver("Ratan", "kolim@gmail.com", 5678, "Gulshan")
GoBro.add_driver(ratan)
kashem.request_ride(GoBro, "Uttara", "car")
ratan.reach_destination(kashem.current_ride)
kashem.show_current_ride()