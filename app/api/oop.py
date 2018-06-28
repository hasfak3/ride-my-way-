from flask import Flask, jsonify, Blueprint
from flask_restful import reqparse
from .rideModel import rides, RideAPI

app = Flask(__name__)
blue_print_rides = Blueprint('blue_print_rides', __name__)


@blue_print_rides.route('/api/v1/rides', methods=['GET'])
def get_rides():

    return jsonify({"Rides": Rides}), 200


@blue_print_rides.route('/api/v1/rides/<int:ride_id>', methods=['GET'])
def get_ride(ride_id):
    ride = RideAPI.get_ride(ride_id)

    return jsonify({"ride": ride}), 200


@blue_print_rides.route('/api/v1/rides/create', methods=['POST'])
def create_ride():
    parser = reqparse.RequestParser()

    parser.add_argument("ref_no")
    parser.add_argument("date")
    parser.add_argument("time")
    parser.add_argument("fro")
    parser.add_argument("destination")
    parser.add_argument("fare")
    arguments = parser.parse_args()

    ride_instance = RideAPI(arguments["ref_no"], arguments["date"], arguments["time"], arguments["fro"], arguments["destination"], arguments["fare"])

    created_ride = RideAPI.create_ride(ride_instance)

return jsonify({"ride": created_ride}), "Ride was created successfully"
