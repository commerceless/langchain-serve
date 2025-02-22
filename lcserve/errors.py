class InvalidInstanceError(ValueError):
    def __init__(self, instance):
        super().__init__("Invalid instance: {}".format(instance))
        self.instance = instance


class InvalidAutoscaleMinError(ValueError):
    def __init__(self, min):
        super().__init__("Invalid autoscale.min: {}".format(min))
        self.min = min
