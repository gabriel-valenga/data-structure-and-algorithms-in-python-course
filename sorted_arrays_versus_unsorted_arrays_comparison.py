from random import random
import timeit
from chapter4_unsorted_arrays import UnsortedArray
from chapter5_sorted_arrrays import SortedArray
from general_use import functions_comparison


class CompareSortedAndUnsortedArrays:

    def __init__(self):
        self.list_of_values = []
        self.sorted_array = None
        self.unsorted_array = None
        self.fill_list_of_values()
        self.insert_a_list_of_values_in_sorted_array()
        self.insert_a_list_of_values_in_unsorted_array()


    def fill_list_of_values(self):
        for i in range(1000):
            self.list_of_values.append(round(random()*1000, 4))


    def insert_a_list_of_values(self, array:SortedArray|UnsortedArray):
        for value in self.list_of_values:
            array.insert(value)
        return array


    def insert_a_list_of_values_in_sorted_array(self) -> SortedArray:
        self.sorted_array = SortedArray(len(self.list_of_values))
        return self.insert_a_list_of_values(self.sorted_array)


    def insert_a_list_of_values_in_unsorted_array(self) -> UnsortedArray:
        self.unsorted_array = UnsortedArray(len(self.list_of_values))
        return self.insert_a_list_of_values(self.unsorted_array)
    

    def search_a_list_of_values_in_sorted_array_using_binary_search(self, list_of_values_to_search:list):
        for value in list_of_values_to_search:
            self.sorted_array.binary_search(value)
        return self.sorted_array
    

    def search_a_list_of_values_in_unsorted_array_using_linear_search(self, list_of_values_to_search:list):
        for value in list_of_values_to_search:
            self.unsorted_array.search(value)
        return self.unsorted_array

    

comparison = CompareSortedAndUnsortedArrays()
comparison.fill_list_of_values()
# functions_comparison(comparison.insert_a_list_of_values_in_sorted_array, comparison.insert_a_list_of_values_in_unsorted_array)
list_of_values_to_search = [round(random()*1000, 4) for _ in range(100)]
functions_comparison(
    comparison.search_a_list_of_values_in_sorted_array_using_binary_search, 
    comparison.search_a_list_of_values_in_unsorted_array_using_linear_search,
    list_of_values_to_search
)