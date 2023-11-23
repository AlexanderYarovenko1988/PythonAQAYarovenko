class ArrayIntersection:
    def __init__(self, array1, array2):
        self.array1 = array1
        self.array2 = array2

    def find_intersection(self):
        intersection = list(filter(lambda x: x in self.array1, self.array2))
        return intersection


array1 = [1, 2, 3, 4, 5]
array2 = [3, 4, 5, 6, 7]

array_intersection_obj = ArrayIntersection(array1, array2)
result = array_intersection_obj.find_intersection()

print(f"Перетин масивів:{result}")
