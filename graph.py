import matplotlib.pyplot as plt

# Dataset sizes
dataset_sizes = [10, 100, 1000, 10000, 50000]

# Execution times (in seconds) from analysis
insertion_sort_times = [0.000012, 0.000789, 0.056721, 1.347812, 32.687123]
merge_sort_times = [0.000005, 0.000345, 0.004213, 0.052183, 0.356124]
heapsort_times = [0.000008, 0.000410, 0.006128, 0.078134, 0.498761]
quicksort_times = [0.000007, 0.000297, 0.003897, 0.045678, 0.298453]

# Create the plot
plt.figure(figsize=(10, 6))

plt.plot(dataset_sizes, insertion_sort_times, marker='o', linestyle='-', label='Insertion Sort', color='red')
plt.plot(dataset_sizes, merge_sort_times, marker='s', linestyle='-', label='Merge Sort', color='blue')
plt.plot(dataset_sizes, heapsort_times, marker='^', linestyle='-', label='Heapsort', color='green')
plt.plot(dataset_sizes, quicksort_times, marker='d', linestyle='-', label='Quicksort', color='purple')

# Labels, title, and grid
plt.xlabel("Dataset Size (Number of Elements)")
plt.ylabel("Execution Time (Seconds)")
plt.title("Sorting Algorithm Performance Analysis")
plt.xscale("log")  # Log scale for better visualization
plt.yscale("log")  # Log scale for better time comparison
plt.legend()
plt.grid(True, which="both", linestyle="--", linewidth=0.5)

# Save and show the plot
plt.savefig("sorting_performance.png")
plt.show()
