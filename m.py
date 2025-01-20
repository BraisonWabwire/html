# Initialize the car queue
car_queue = 5  # Example: 5 cars in the queue

# Function to simulate the traffic light logic
def traffic_light_simulation(car_queue):
    print("Traffic light simulation started.")
    
    while car_queue > 0:
        # Set traffic light to red
        print("Traffic light is RED. Cars are waiting.")
        
        # Turn light green and let one car pass
        print("Traffic light turns GREEN.")
        print("A car passes through the intersection.")
        car_queue -= 1
        
        # Turn light back to red
        print("Traffic light turns RED again.")
        print(f"Cars remaining in queue: {car_queue}")
        print("-" * 30)
    
    print("All cars have passed. Traffic light simulation ended.")

# Run the simulation
traffic_light_simulation(car_queue)
