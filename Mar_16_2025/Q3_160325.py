#train question 
#arrival time 
#departure time 
#find minimum number of
#platforms needed? 

def merge(intervals):
    # Step 1: Sort intervals by the start value
    intervals.sort(key=lambda x: x[0])

    merged = []
    for interval in intervals:
        # If merged list is empty OR no overlap, add the interval
        if not merged or merged[-1][1] < interval[0]:
            merged.append(interval)
        else:
            # Merge intervals by updating the end time
            merged[-1][1] = max(merged[-1][1], interval[1])

    return merged


arr = [900,940,950,1100,1500,1800]
dip = []