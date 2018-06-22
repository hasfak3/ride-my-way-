Rides = []
class allRides:
    def __init__(self, date, licenseNo, fro,destination,category,time,route,fare):
        self.ride_id = self.generate_id(Rides)
        self.date = Date
        self.LicenseNo = License Number
        self.fro = pickup
		self.destination = destination
		self.category = Car category
		self.time = Time
		self.route = Route
		self.fare = Fare

    def get_Rides():

        global Rides
        if Rides:
            return Rides
        return "No ride Found"

    def get_ride(ride_id):
        global Rides
        for ride in Rides:
            if ride.get('id') == ride_id:
                return ride
            continue

        return "That ride is not found"

    def create_ride(self):

        ride = {
            "id": self.ride_id,
            "ref_no": self.ref_no,
            "date": self.date,
            "time": self.time
			"Date": self.date,
			"License Number": self.LicenseNo, 
			"pickup": self.fro,
			"pickup":self.destination,
			"Car category":self.category,
			"Time": self.time,
			"Route": self.route, 
			"Fare": self.fare
        }

        Rides.append(ride)

        return ride

    def generate_id(_list):
        if _list:
            return _list[-1].get("id") + 1
return 1