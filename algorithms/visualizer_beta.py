import tkinter as tk
import random


def generate_random_list():
    return [random.randint(1, 400) for _ in range(100)]


class SortVisualizer:
    def __init__(self, root):
        self.root = root
        self.array = generate_random_list()
        self.canvas = tk.Canvas(root, width=600, height=400)
        self.canvas.pack()
        self.bar_width = 600 / len(self.array)
        self.draw_array()

        self.reset_button = tk.Button(root, text="Reset", command=self.reset)
        self.reset_button.pack(side=tk.LEFT)

        self.sort_button = tk.Button(root, text="Sort", command=self.start_sort)
        self.sort_button.pack(side=tk.RIGHT)

        self.sort_algorithm = "bubble"

        self.algorithm_selection = tk.StringVar(value=self.sort_algorithm)
        self.dropdown = tk.OptionMenu(
            root, self.algorithm_selection, "bubble", "merge", "quicksort"
        )
        self.dropdown.pack(side=tk.TOP)

    def draw_array(self, color_array=None):
        self.canvas.delete("all")
        if color_array is None:
            color_array = ["blue"] * len(self.array)
        for i, val in enumerate(self.array):
            x0 = i * self.bar_width
            y0 = 400 - val
            x1 = (i + 1) * self.bar_width
            y1 = 400
            self.canvas.create_rectangle(x0, y0, x1, y1, fill=color_array[i])
        self.root.update_idletasks()

    def start_sort(self):
        selected_algorithm = self.algorithm_selection.get()
        if selected_algorithm == "bubble":
            self.bubble_sort(0, 0)
        elif selected_algorithm == "merge":
            self.merge_sort(self.array)
        elif selected_algorithm == "quicksort":
            self.quicksort(self.array)

    def bubble_sort(self, i, j):
        n = len(self.array)
        if i < n:
            if j < n - i - 1:
                if self.array[j] > self.array[j + 1]:
                    self.array[j], self.array[j + 1] = self.array[j + 1], self.array[j]
                    self.draw_array(
                        [
                            "red" if x == j or x == j + 1 else "blue"
                            for x in range(len(self.array))
                        ]
                    )
                self.root.after(1, self.bubble_sort, i, j + 1)
            else:
                self.root.after(1, self.bubble_sort, i + 1, 0)
        else:
            self.draw_array(["green"] * len(self.array))

    def merge_sort(self, array, left=0, right=None):
        if right is None:
            right = len(array)

        if right - left > 1:
            mid = (left + right) // 2
            self.merge_sort(array, left, mid)
            self.merge_sort(array, mid, right)
            self.merge(array, left, mid, right)
            self.draw_array()
            self.root.after(50)

    def merge(self, array, left, mid, right):
        left_part = array[left:mid]
        right_part = array[mid:right]

        i = j = 0
        k = left
        while i < len(left_part) and j < len(right_part):
            # Color the current elements being compared red
            self.draw_array(
                [
                    "red" if x == k or x == left + i or x == mid + j else "blue"
                    for x in range(len(array))
                ]
            )
            self.root.update_idletasks()
            self.root.after(10)

            if left_part[i] <= right_part[j]:
                array[k] = left_part[i]
                i += 1
            else:
                array[k] = right_part[j]
                j += 1
            k += 1

        while i < len(left_part):
            array[k] = left_part[i]
            i += 1
            k += 1

        while j < len(right_part):
            array[k] = right_part[j]
            j += 1
            k += 1

    def quicksort(self, arr, low=0, high=None):
        if high is None:
            high = len(arr) - 1

        if low < high:
            pivot_index = self.partition(arr, low, high)
            self.draw_array()
            self.root.after(10)

            # Recursively sort left and right parts
            self.quicksort(arr, low, pivot_index - 1)
            self.quicksort(arr, pivot_index + 1, high)

    def partition(self, arr, low, high):
        pivot = arr[high]
        i = low - 1

        for j in range(low, high):
            if arr[j] < pivot:
                i += 1
                arr[i], arr[j] = arr[j], arr[i]
                self.draw_array(
                    ["red" if x == i or x == j else "blue" for x in range(len(arr))]
                )
                self.root.update_idletasks()
                self.root.after(20)

        arr[i + 1], arr[high] = arr[high], arr[i + 1]
        return i + 1

    def reset(self):
        self.array = generate_random_list()
        self.draw_array()


if __name__ == "__main__":
    root = tk.Tk()
    root.title("Sorting Visualizer")
    visualizer = SortVisualizer(root)
    root.mainloop()
