# tee ratkaisu tänne
# Write your solution here
import math
def get_station_data(filename: str) -> dict:
    location_data = {}
    with open(filename, 'r') as f:
        for line in f:
            line = line.strip().split(';')
            if line[0] != 'Longitude':
                location_data[line[3]] = tuple(float(coord) for coord in line[:2])
    return location_data

def distance(stations: dict, station1: str, station2: str) -> float:
    lng = (stations.get(station1)[0] - stations.get(station2)[0]) * 55.26
    lat = (stations.get(station1)[1] - stations.get(station2)[1]) * 111.2
    return math.sqrt(lng**2 + lat**2)

def greatest_distance(stations: dict) -> tuple:
    station_dist_pairs = []
    stations_list = list(stations.keys())
    for i in range(len(stations_list) - 1):
        for j in range(i+1, len(stations_list)):
            station_dist_pairs.append([stations_list[i], 
            stations_list[j],
            distance(stations, stations_list[i], stations_list[j])])

    
    return tuple(sorted(station_dist_pairs, key=lambda x: x[2], reverse=True)[0])

if __name__ == "__main__":
    stations = get_station_data('stations1.csv')
    # print(distance(stations, "Designmuseo", "Hietalahdentori"))
    station1, station2, greatest = greatest_distance(stations)
    print(station1, station2, greatest)

