class ListAnalyzer:
    def __init__(self, lists):
        self.lists = lists

    def find_max_min_length_lists(self):
        sorted_lists = sorted(self.lists, key=lambda x: len(x))
        min_length_list = sorted_lists[0]
        max_length_list = sorted_lists[-1]

        return min_length_list, max_length_list


lists_to_analyze = [[1, 2, 3], [4, 5], [6, 7, 8, 9], [10]]
analyzer = ListAnalyzer(lists_to_analyze)
min_length_list, max_length_list = analyzer.find_max_min_length_lists()

print(f"Список з мінімальною довжиною: {min_length_list}")
print(f"Список з максимальною довжиною: {max_length_list}")
