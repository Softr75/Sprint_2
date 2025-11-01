class PointsForPlace:
    def get_points_for_place(self, place=0):
        if place > 100:
            print('Баллы начисляются только первым 100 участникам')
            return None
        elif place < 1:
            print('Спортсмен не может занять нулевое или отрицательное место')
            return None
        else:
            self.points = 101 - place
            return self.points

class PointsForMeters:
    @staticmethod
    def get_points_for_meters(meters):
        if meters % 1 != 0 or meters < 0:
            print('Количество метров не может быть отрицательным или дробным')
            return None
        else:
            points = meters * 0.5
            return points

class TotalPoints(PointsForPlace, PointsForMeters):
    def get_total_points(self, place=0, meters=0):
        points_place = PointsForPlace.get_points_for_place(self, place)
        points_distance = PointsForMeters.get_points_for_meters(meters)
        total = points_place + points_distance
        return total
    
points_for_place = PointsForPlace()
print(points_for_place.get_points_for_place(10))

points_for_meters = PointsForMeters()
print(points_for_meters.get_points_for_meters(10))

total_points = TotalPoints()
print(total_points.get_points_for_place(10))
print(total_points.get_points_for_meters(10))
print(total_points.get_total_points(100, 10))