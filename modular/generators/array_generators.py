import random
import sys

def generate_array_unique_elements(file_name: str, tc:int, sz_min: int, sz_max: int, low: int, high: int):
    
    if (high < low) or (sz_max < sz_min):
        print(f"\n WARNING! \n\n Cannot generate arrays as ranges provided are incorrect!\n")
        sys.exit(1)
        
    total_unique_elements = high - low + 1
    
    if total_unique_elements < sz_min:
        print(f"\n WARNING! \n\n Cannot generate arrays as {sz_min} size. \n {sz_min} > total unique elements in {low} and {high}.\n")
        sys.exit(1)

    effective_sz_max = min(sz_max, total_unique_elements)
    valid_sizes = list(range(sz_min, effective_sz_max + 1))

    with open(file_name, 'w') as f:
        f.write(f"{tc}\n")
        for _ in range(tc):
            size = random.choice(valid_sizes)
            unique_elements = random.sample(range(low, high + 1), size)
            f.write(f"{size}\n")
            f.write(" ".join(map(str, unique_elements)) + "\n")

    print("\n\nWriting to file...")
    print(f"✔ Successfully wrote to {file_name}\n")