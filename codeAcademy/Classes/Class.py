# Define the DriveBot class here!
class DriveBot:
    def __init__(self):
        self.motor_speed = 0
        self.direction = 0
        self.sensor_range = 0

# Create an object from the class
robot_1 = DriveBot()

# Set the instance variables
robot_1.motor_speed = 5
robot_1.direction = 90
robot_1.sensor_range = 10

# Use print statements to check your work
print(robot_1.motor_speed)  # Output: 5
print(robot_1.direction)    # Output: 90
print(robot_1.sensor_range) # Output: 10

class DriveBot:
    def __init__(self):
        self.motor_speed = 0
        self.direction = 0
        self.sensor_range = 0

    def control_bot(self, new_speed, new_direction):
        self.motor_speed = new_speed
        self.direction = new_direction

    def adjust_sensor(self, new_sensor_range):
        self.sensor_range = new_sensor_range

# Create an object from the class
robot_1 = DriveBot()

# Use the methods here
robot_1.control_bot(10, 180)
robot_1.adjust_sensor(20)

# Use print statements to check your work
print(robot_1.motor_speed)  # Output: 10
print(robot_1.direction)    # Output: 180
print(robot_1.sensor_range) # Output: 20
