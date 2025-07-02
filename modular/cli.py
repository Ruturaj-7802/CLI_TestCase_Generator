import argparse
from modular.generators.array_generators import generate_array_unique_elements

def main_cli():
    parser = argparse.ArgumentParser(description="Test Case Generator CLI")
    parser.add_argument('--type', required=True, choices=['array_unique'], help="Type of test case to generate")
    parser.add_argument('--testcases', type=int, required=True, help="Number of testcases")
    parser.add_argument('--size_min', type=int, required=True, help="Minimum number of elements")
    parser.add_argument('--size_max', type=int, required=True, help="Maximum number of elements")
    parser.add_argument('--min', type=int, required=True, help="Minimum element value")
    parser.add_argument('--max', type=int, required=True, help="Maximum element value")
    parser.add_argument('--output', required=True, help="Output file name with extension (.txt)")

    args = parser.parse_args()
    output_filename = args.output
    if output_filename[-4:] != '.txt':
        output_filename = output_filename + '.txt'

    if args.type == 'array_unique':
        generate_array_unique_elements(
            file_name = output_filename, 
            tc = args.testcases, 
            sz_min = args.size_min, 
            sz_max = args.size_max, 
            low = args.min, 
            high = args.max)