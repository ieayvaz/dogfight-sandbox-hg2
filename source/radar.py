import harfang as hg
import math
import matplotlib.pyplot as plt
def is_within_radar(aircraft_loc: hg.Vec3, radar_loc: hg.Vec3, heading: hg.Vec3, range: float, field_of_view: float):
    distance = hg.Dist(aircraft_loc, radar_loc)
    if distance > range:
        return False
    
    distance_vec = aircraft_loc - radar_loc
    angle_to_object = (math.degrees(math.atan2(distance_vec.x,distance_vec.z)) + 360) % 360
    radar_angle = heading
    #print(f"Radar rotation: {rotation.x}/{rotation.y}, Dist angle: {angle_to_object}, Radar angle: {radar_angle}")
    angle_diffrence = min(abs(angle_to_object-radar_angle),(angle_to_object+radar_angle)%360)
    if angle_diffrence > field_of_view:
        return False

    return True
