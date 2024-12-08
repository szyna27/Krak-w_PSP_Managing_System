from .Strategy import Strategy

# Class definition
class FireHazardStrategy(Strategy):
    # Method for handling strategy
    def execute(self):
        print(f"{self.event.color}Handling FireHazard event in location: {self.event.location}{self.event.color_end}")
        vehicles_sent = 0
        while vehicles_sent < self.event.vehicles_needed:
            station = self.choose_nearest_station()
            if not station:
                if self.event.handled:
                    break
                self.calculate_distances()
                continue

            vehicle = station.send_vehicle(self.event)
            if vehicle:
                vehicles_sent += 1
            else:
                self.distances.pop(station)

        print(f"{self.event.color}Finished handling FireHazard\nSent {vehicles_sent} vehicles{self.event.color_end}")

        
