################################################################################
# GPIO Manipulator
################################################################################

################################################################################
# IMPORTS
################################################################################

################################################################################
# CLASSES
################################################################################
class gpio():
    class Direction():
        Input = "in"
        Output = "out"

    def __init__(self, pin):
        self.path = "/sys/class/gpio/gpio" + str(pin) + "/"
        try:
            with open("/sys/class/gpio/export", "w") as f:
                f.write(str(pin))
        except IOError:
            pass
    
    def set_direction(self, dir):
        if dir != self.Direction.Input and dir != self.Direction.Output:
            return
        with open(self.path + "direction", "w") as dir_f:
            dir_f.write(dir)

    def set_value(self, val):
        with open(self.path + "value", "w") as value_f:
            value_f.write(str(val))



################################################################################
# VARIABLES
################################################################################


################################################################################
# FUNCTIONS
################################################################################

