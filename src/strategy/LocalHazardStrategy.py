from .Strategy import Strategy

# Class definition
class LocalHazardStrategy(Strategy):
    # Method for handling strategy
    def execute(self):
        print(f"{self.event.color}Handling LocalHazard event in location: {self.event.location}{self.event.color_end}")
        vehicles_sent = 0
        while vehicles_sent < self.event.vehicles_needed:
            station = self.choose_nearest_station()
            if not station:
                if self.event.handled or vehicles_sent == 1:
                    break
                self.calculate_distances()
                continue
            print(f"{self.event.color}Asking station: {station.name} - {station.location} for vehicle{self.event.color}")

            vehicle = station.send_vehicle(self.event)
            if vehicle:
                vehicles_sent += 1
                print(f"{self.event.color}Vehicle {vehicle.number} sent from station {station.name}{self.event.color_end}")
            else:
                self.distances.pop(station)
                print(f"{self.event.color}Station {station.name} has no available vehicles{self.event.color_end}")

        print(f"{self.event.color}Finished handling LocalHazard\nSent {vehicles_sent} vehicles{self.event.color_end}")