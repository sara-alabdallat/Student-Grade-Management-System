#!/usr/bin/env python
# coding: utf-8

# In[3]:


# Merge Sort to sort students by grade (descending)
def merge_sort_grades(students):
    if len(students) <= 1:
        return students

    mid = len(students) // 2
    left = merge_sort_grades(students[:mid])
    right = merge_sort_grades(students[mid:])

    return merge_by_grade(left, right)


def merge_by_grade(left, right):
    sorted_list = []
    i = j = 0

    while i < len(left) and j < len(right):
        if left[i][1] > right[j][1]:   # sort by grade descending
            sorted_list.append(left[i])
            i += 1
        else:
            sorted_list.append(right[j])
            j += 1

    sorted_list.extend(left[i:])
    sorted_list.extend(right[j:])
    return sorted_list


# Merge Sort to sort students by name (ascending)
def merge_sort_names(students):
    if len(students) <= 1:
        return students

    mid = len(students) // 2
    left = merge_sort_names(students[:mid])
    right = merge_sort_names(students[mid:])

    return merge_by_name(left, right)


def merge_by_name(left, right):
    sorted_list = []
    i = j = 0

    while i < len(left) and j < len(right):
        if left[i][0].lower() < right[j][0].lower():
            sorted_list.append(left[i])
            i += 1
        else:
            sorted_list.append(right[j])
            j += 1

    sorted_list.extend(left[i:])
    sorted_list.extend(right[j:])
    return sorted_list


# Binary Search by name
def binary_search(students, target_name):
    low = 0
    high = len(students) - 1

    while low <= high:
        mid = (low + high) // 2
        mid_name = students[mid][0].lower()

        if mid_name == target_name.lower():
            return students[mid]
        elif target_name.lower() < mid_name:
            high = mid - 1
        else:
            low = mid + 1

    return None


# ================= MAIN PROGRAM =================

students = []

# Input loop
while True:
    name = input("Enter student name (or 'stop' to finish): ")
    if name.lower() == 'stop':
        break

    grade = float(input("Enter student grade: "))
    students.append((name, grade))


# Sort by grades (descending)
sorted_by_grade = merge_sort_grades(students)

print("\nStudents sorted by grade (high to low):")
for student in sorted_by_grade:
    print(student[0], "-", student[1])


# Sort by names for binary search
sorted_by_name = merge_sort_names(students)

# Search
search_name = input("\nEnter student name to search: ")
result = binary_search(sorted_by_name, search_name)

if result:
    print("Student found:")
    print("Name:", result[0])
    print("Grade:", result[1])
else:
    print("Student not found.")


# In[ ]:




