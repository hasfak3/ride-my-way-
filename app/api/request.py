from ..Rides.rideModel import RideAPI

requests = []

class RequestModel:

    def __init__(self, user_id, ride_id):
        self.request_id = RideAPI.generate_id(requests)
        self.user_id = user_id
        self.ride_id = ride_id
        self.status = "pending"

    def CreateRequest(self):

        request = {

            "id": self.request_id,
            "user_id": self.user_id,
            "ride_id": self.ride_id,
            "status": "pending"
        }
        requests.append(request)

        return request

    def GetRequest(request_id):
        global requests
        for request in requests:
            if request.get("id") == request_id:
                return request
            continue
        return "sorry request not found"
