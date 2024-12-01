# Disable possibility of running this file directly
if __name__ == '__main__':
    raise Exception("This file cannot be run directly")

# Rectangle edges coordinates
SIMULATION_AREA_Y = (49.95855025648944, 50.154564013341734)
SIMULATION_AREA_X = (19.688292482742394, 20.02470275868903)
SIMULATION_WIDTH = SIMULATION_AREA_X[1] - SIMULATION_AREA_X[0]
SIMULATION_HEIGHT = SIMULATION_AREA_Y[1] - SIMULATION_AREA_Y[0]