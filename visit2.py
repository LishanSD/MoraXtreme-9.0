import sys
import heapq

# Structure to represent a fuel station
class Station:
    def __init__(self, distance, price):
        self.distance = distance
        self.price = price

def min_cost_trip(F, U, K, M, stations):

    stations.sort(key=lambda x: x.distance)
    dp = [[float('inf')] * (U + 1) for _ in range(F + 1)]

    dp[0][K] = 0

    for i in range(F):
        for fuel in range(U + 1):
            if dp[i][fuel] == float('inf'):
                continue  # Skip impossible states


            next_distance = (M - stations[i].distance) if i == F - 1 else stations[i + 1].distance - stations[i].distance


            if fuel >= next_distance:
                dp[i + 1][fuel - next_distance] = min(dp[i + 1][fuel - next_distance], dp[i][fuel])

            for buy in range(U - fuel + 1):
                cost = buy * stations[i].price
                if fuel + buy >= next_distance:  # Can reach next station after buying fuel
                    dp[i + 1][fuel + buy - next_distance] = min(dp[i + 1][fuel + buy - next_distance], dp[i][fuel] + cost)


    min_cost = min(dp[F][fuel] for fuel in range(M - stations[F - 1].distance + 1) if dp[F][fuel] != float('inf'))

    return -1 if min_cost == float('inf') else min_cost

def main():
    input = sys.stdin.read
    data = input().splitlines()
    
    idx = 0
    T = int(data[idx])
    idx += 1
    results = []
    
    for _ in range(T):
        # Read F, U, K, M
        F, U, K, M = map(int, data[idx].split())
        idx += 1
        
        stations = []
        for i in range(F):
            A, P = map(int, data[idx].split())
            stations.append(Station(A, P))
            idx += 1
        
        # Get the result for this test case
        result = min_cost_trip(F, U, K, M, stations)
        results.append(result)
    
    # Print all results
    sys.stdout.write("\n".join(map(str, results)) + "\n")

if __name__ == "__main__":
    main()
