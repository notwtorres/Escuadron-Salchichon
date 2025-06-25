from flask import Flask, request, render_template
import time
from dataclasses import dataclass

app = Flask(__name__)

@dataclass
class Person:
    _id_counter: int = 0
    
    def __init__(self, name: str, age: int):
        Person._id_counter += 1
        self.id = Person._id_counter
        self.name = name
        self.age = age

people = []

def binarySearch(arr, target, key):
    left, right = 0, len(arr) - 1
    while left <= right:
        mid = (left + right) // 2
        if arr[mid].__dict__[key] == target:
            return f"{key} {target} found for {arr[mid].name} at index {mid}"
        elif arr[mid].__dict__[key] < target:
            left = mid + 1
        else:
            right = mid - 1
    return f"{key} {target} not found in the array"

def bubblesort(my_array, key):
    n = len(my_array)
    for i in range(n-1):
        for j in range(n-i-1):
            if my_array[j].__dict__[key] > my_array[j+1].__dict__[key]:
                my_array[j], my_array[j+1] = my_array[j+1], my_array[j]
    return my_array

def insertionsort(my_array, key):
    n = len(my_array)
    for i in range(1, n):
        insert_index = i
        current_value = my_array.pop(i)
        for j in range(i-1, -1, -1):
            if my_array[j].__dict__[key] > current_value.__dict__[key]:
                insert_index = j
        my_array.insert(insert_index, current_value)
    return my_array

def partition(array, low, high, key):
    pivot = array[high].__dict__[key]
    i = low - 1
    for j in range(low, high):
        if array[j].__dict__[key] <= pivot:
            i += 1
            array[i], array[j] = array[j], array[i]
    array[i+1], array[high] = array[high], array[i+1]
    return i+1

def quicksort(array, key, low=0, high=None):
    if high is None:
        high = len(array) - 1
    if low < high:
        pivot_index = partition(array, low, high, key)
        quicksort(array, key, low, pivot_index-1)
        quicksort(array, key, pivot_index+1, high)
    return array

def linearSearch(arr, target, key):
    for i in range(len(arr)):
        if arr[i].__dict__[key] == target:
            return f"{key} {target} found for {arr[i].name} at index {i}"
    return f"{key} {target} not found in the array"

@app.route('/', methods=['GET', 'POST'])
def index():
    result = ""
    time_taken = 0
    
    if request.method == 'POST':
        action = request.form.get('action')
        
        if action == 'add':
            name = request.form.get('name')
            age = int(request.form.get('age'))
            people.append(Person(name, age))
            result = f"Added {name} with age {age} and ID {people[-1].id}"
        
        elif action == 'sort':
            sort_key = 'age'  
            algorithm = request.form.get('algorithm')
            people_copy = people.copy()
            
            start_time = time.time()
            if algorithm == 'bubble':
                sorted_people = bubblesort(people_copy, sort_key)
            elif algorithm == 'insertion':
                sorted_people = insertionsort(people_copy, sort_key)
            else:  # quicksort
                sorted_people = quicksort(people_copy, sort_key)
            time_taken = (time.time() - start_time) * 1000  
            
            result = f"Sorted by {sort_key} using {algorithm} sort in {time_taken:.3f} ms\n"
            result += "\n".join([f"ID: {p.id}, Name: {p.name}, Age: {p.age}" for p in sorted_people])
        
        elif action == 'search':
            search_key = request.form.get('search_key')
            target = int(request.form.get('target'))
            algorithm = request.form.get('search_algorithm')
            people_copy = quicksort(people.copy(), search_key)
            
            start_time = time.time()
            if algorithm == 'binary':
                result = binarySearch(people_copy, target, search_key)
            else:  # linear
                result = linearSearch(people_copy, target, search_key)
            time_taken = (time.time() - start_time) * 1000  
            result += f"\nSearch completed in {time_taken:.3f} ms"
    
    return render_template('index.html', people=people, result=result)

if __name__ == '__main__':
    app.run(debug=True)