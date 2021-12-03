def merge_sort_(array, last):
	merge_sort(array, 0, last)


def merge(array, first, mid, last):
	index_first_half = mid - first + 1
	index_second_half = last - mid

	first_half = [0] * index_first_half
	second_half = [0] * index_second_half

	for index_first in range(0, index_first_half):
		first_half[index_first] = array[first + index_first]

	for index_second in range(0, index_second_half):
		second_half[index_second] = array[mid + 1 + index_second]

	index_first = 0
	index_second = 0
	merged_index = first

	while index_first < index_first_half and index_second < index_second_half:
		if first_half[index_first] <= second_half[index_second]:
			array[merged_index] = first_half[index_first]
			index_first += 1
		else:
			array[merged_index] = second_half[index_second]
			index_second += 1
		merged_index += 1

	while index_first < index_first_half:
		array[merged_index] = first_half[index_first]
		index_first += 1
		merged_index += 1

	while index_second < index_second_half:
		array[merged_index] = second_half[index_second]
		index_second += 1
		merged_index += 1


def merge_sort(array, first, last):
	if first < last:
		mid = first + (last - first)//2
		merge_sort(array, first, mid)
		merge_sort(array, mid + 1, last)
		merge(array, first, mid, last)
