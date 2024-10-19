import heapq

def min_fuel_cost(F, U, K, M, stations):
    # Sort stations by their distance
    stations.sort()
    
    # Add a pseudo-station at the destination with 0 price to handle the end case
    stations.append((M, 0))
    
    total_cost = 0  # Total cost spent on fuel
    current_fuel = K  # Current fuel in the car
    current_position = 0  # Start from position 0
    
    # Priority queue to keep track of the cheapest fuel prices
    pq = []
    heapq.heappush(pq, stations[0][1])
    print(stations, pq)
    i = 1
    for j in range(0, len(stations)-1):
        distance=stations[j][0]
        price=stations[j][1]
        print("distance: ",distance, price)
        # Calculate the distance to the next station
        distance_to_next_station = distance - current_position
        print("distance_to_next_station: ",distance_to_next_station)

        # Use up the fuel to reach the next station
        current_fuel -= distance_to_next_station
        current_position = distance
       
        print ("current_fuel: ", current_fuel, current_position)
        # If we don't have enough fuel to reach this station, buy fuel from the cheapest stations
        while current_fuel < stations[j+1][0]-current_position and pq:
            print(i, pq)
            cheapest_price = heapq.heappop(pq)
            fuel_needed = min(-current_fuel, U - K)  # How much fuel we can buy
            total_cost += fuel_needed * cheapest_price
            current_fuel += fuel_needed
            i+=1
        
        # If we still can't reach the station, return -1 (journey not possible)
        if current_fuel < 0:
            return -1
        
        # Add the current station's fuel price to the heap
        heapq.heappush(pq, price)
        print(i, pq)
    return total_cost

# Input and output processing
def main():
    test_cases = int(input())
    
    for _ in range(test_cases):
        F, U, K, M = map(int, input().split())
        stations = [tuple(map(int, input().split())) for _ in range(F)]
        result = min_fuel_cost(F, U, K, M, stations)
        print(result)

if __name__ == "__main__":
    main()
