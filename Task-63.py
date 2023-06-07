class Robot:
    def __init__(self, name, speed):
        self.name = name
        self.speed = speed

    def motion(self):
        motion_time = int(input('Введите время, в часах: '))
        way = motion_time * self.speed

        print(self.name, ' проехал: ', way, ' за: ', motion_time, ' со скоростью: ', self.speed)


# roboto = Robot('test', 150)
# roboto.motion()

class CrawlerRobot(Robot):
    def __init__(self, name, speed, territory):
        Robot.__init__(self, name, speed)
        self.territory = territory


class WheelsRobot(Robot):
    def __init__(self, name, speed, car_brand):
        Robot.__init__(self, name, speed)
        self.car_brand = car_brand

