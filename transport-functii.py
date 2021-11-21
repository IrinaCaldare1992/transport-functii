#### CONTEXT ####

####   USER  ####
user_departure_name      = "Chisinau"
user_departure_km        = 0
user_destination_name    = "Balti"
user_destination_km      = 120
user_road_max_duration_h = 60


#### TRANSPORTATION OPTIONS ####
# - walking
transport_walk_speed_km_h = 10

# - bike
transport_bike_speed_km_h = 40

# - car
transport_car_speed_km_h  = 120

# - bus
transport_bus_speed_km_h  = 60

#### HELPER FUNCTIONS ####
def calcDistance(u_dep, u_des):
    distance_km = abs(u_des- u_dep)
    return distance_km

def calcDuration(dist, t_speed):
    duration_h = dist / t_speed
    return duration_h


def evaluateTransport(u_dep, u_des, u_max_dur, t_speed):
    distance_km = calcDistance(u_dep, u_des)
    duration_h  = calcDuration(distance_km, t_speed)
    answer      = duration_h <= u_max_dur
    return answer

def printResult(u_dep_name, u_des_name, dist, dur):
    result = (" The distance between", u_dep_name, "and", u_des_name, "is: ", dist, "km and The estimated duration is:", dur)
    return result

#### DECISION MAKING ####

################# BUS ##################
answer_b = evaluateTransport(
    user_departure_km,
    user_destination_km,
    user_road_max_duration_h,
    transport_bus_speed_km_h
)

distance_km = calcDistance(
    user_departure_km, 
    user_destination_km,
    )

duration_h = calcDuration(
    distance_km,
    transport_bus_speed_km_h
)

result_b = printResult(user_departure_name, user_destination_km, distance_km, duration_h)


################# BUS ##################

################# WALK ##################
answer_w = evaluateTransport(
    user_departure_km,
    user_destination_km,
    user_road_max_duration_h,
    transport_walk_speed_km_h
)

distance_km = calcDistance(
    user_departure_km, 
    user_destination_km,
    )

duration_h = calcDuration(
    distance_km,
    transport_walk_speed_km_h
)
result_w = printResult(user_departure_name, user_destination_km, distance_km, duration_h)

################# WALK ##################

################# BIKE ##################
answer_bi = evaluateTransport(
    user_departure_km,
    user_destination_km,
    user_road_max_duration_h,
    transport_bike_speed_km_h
)

distance_km = calcDistance(
    user_departure_km, 
    user_destination_km,
    )

duration_h = calcDuration(
    distance_km,
    transport_bike_speed_km_h
)
result_bi = printResult(user_departure_name, user_destination_km, distance_km, duration_h)

################# BIKE ##################

################# CAR ##################
answer_c = evaluateTransport(
    user_departure_km,
    user_destination_km,
    user_road_max_duration_h,
    transport_car_speed_km_h
)

distance_km = calcDistance(
    user_departure_km, 
    user_destination_km,
    )

duration_h = calcDuration(
    distance_km,
    transport_car_speed_km_h
)
result_c = printResult(user_departure_name, user_destination_km, distance_km, duration_h)

################# CAR ##################

if answer_c == True:
    print("Car is okay")
elif answer_b == True:
    print("Bus is okay")
elif answer_bi == True:
    print("Bike is okay")
elif answer_w == True:
    print("Walk is okay")
else:
    print("No solution") 



###### IF - ELSE  / Concurrent/ Independent


