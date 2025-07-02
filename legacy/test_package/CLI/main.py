import argparse
import inquirer
from yaspin import yaspin
import numpy as nm
import string
import random

tc = 1

def generate_array_unique_elements(ml = 0, mh=0,kl=0,kh=0):
    # Logic to generate test cases for 'Array with unique elements'
    with open(file_name, 'w') as file:
        file.write(str(tc) + "\n")      
    print("Enter range of size of array as space seperated integers: ", end="")
    nl, nh = map(int, input().split())    
    print("Enter range of values of elements as space seperated integers: ", end="")
    p, q = map(int, input().split())

    while((nh - nl) > (q-p+1)):
        print("Enter range of size of array as space seperated integers: ", end="")
        nl, nh = map(int, input().split())    
        print("Enter range of values of elements as space seperated integers: ", end="")
        p, q = map(int, input().split())

    for i in range(0, tc):
        res = []      
        n1 = nm.random.randint(nl, nh+1)
        m1 = nm.random.randint(ml, mh+1)
        k1 = nm.random.randint(kl, kh+1)
        unique_elements = set()

        while len(unique_elements) < n1:
            unique_elements.add(str(nm.random.randint(p, q+1)))   

        res = list(unique_elements) 
        file_content = ' '.join(res)  # Convert the list to a string separated by spaces   

        with open(file_name, 'a') as file:
            file.write(str(n1))
            if m1 != 0: 
                file.write(" " +str(m1))
                if k1 != 0:
                    file.write(" " + str(k1))
            file.write("\n"+ file_content + "\n")
        file_content=""
        res = []
    return "Test cases generated for Array with unique elements."

def generate_array_duplicates(ml =0, mh=0,kl= 0,kh=0):
    # Logic to generate test cases for 'Array with duplicates'
    with open(file_name, 'w') as file:
        file.write(str(tc) + "\n")  
    print("Enter range of size of array as space seperated integers: ", end="")
    nl, nh = map(int, input().split())    
    print("Enter range of values of elements as space seperated integers: ", end="")
    p, q = map(int, input().split())
    for i in range(0, tc):
        res = []  
        n1 = nm.random.randint(nl, nh+1)
        m1 = nm.random.randint(ml, mh+1)
        k1 = nm.random.randint(kl, kh+1)
        for j in range(n1):
            res.append(str(nm.random.randint(p, q+1)))  # Append random integers as strings
        
        file_content = ' '.join(res)  # Convert the list to a string separated by spaces        
        with open(file_name, 'a') as file:
            file.write(str(n1))
            if(m1 != 0): 
                file.write(" " + str(m1))
                if(k1 != 0):
                    file.write(" " + str(k1))
            file.write("\n" + file_content + "\n")
        file_content=""
        res = []
    return "Test cases generated for Array with duplicates."

def generate_permutation_array(ml =0,mh=0, kl=0, kh=0):
    # Logic to generate test cases for 'Permutation Array'
    with open(file_name, 'w') as file:
        file.write(str(tc) + "\n")  
    print("Enter range of size of array as space seperated integers: ", end="")
    nl, nh = map(int, input().split())
    for i in range(0, tc):
        res = []  
        n1 = nm.random.randint(nl, nh+1)
        m1 = nm.random.randint(ml, mh+1)
        k1 = nm.random.randint(kl, kh+1)
        unique_elements = set()
        while len(unique_elements) < n1:            
            unique_elements.add(str(nm.random.randint(1, n1+1)))        
        res = list(unique_elements) 

        file_content = ' '.join(res)  # Convert the list to a string separated by spaces        
        with open(file_name, 'a') as file:
            file.write(str(n1))
            if(m1 != 0): 
                file.write(" " + str(m1))
                if(k1 != 0):
                    file.write(" " + str(k1))
            file.write("\n" + file_content + "\n")
        file_content=""
        res = []
    return "Test cases generated for Permutation Array."

def generate_binary_string():
    # Logic to generate test cases for 'Binary String'
    with open(file_name, 'w') as file:
        file.write(str(tc) + "\n")  
    print("Enter range of size of array as space seperated integers: ", end="")
    nl, nh = map(int, input().split())
    for i in range(0, tc):
        res = []  
        n1 = nm.random.randint(nl, nh+1)
        for j in range(n1):
            res.append(str(nm.random.randint(0, 2)))

        file_content = ''.join(res)  # Convert the list to a string separated by spaces        
        with open(file_name, 'a') as file:
            file.write(str(n1))
            file.write("\n" + file_content + "\n")
        file_content=""
        res = []
    return "Test cases generated for Binary String."

def generate_array_nm():
    # Logic to generate test cases for 'Array with n, m'
    
    questions2 = [
    inquirer.List('choice', message="Enter the test cases you want:",
                  choices=[
                    '1. Array with unique elements',
                    '2. Array with duplicates',
                    '3. Permutation Array',
                      # Add other choices here...
                  ]),
    ]
    answers2 = inquirer.prompt(questions2)
    selected_choice2 = int(answers2['choice'].split('.')[0])
    print("Enter range of 'm' as space seperated integers: ", end="")
    ml, mh = map(int, input().split()) 
    # m1 = nm.random.randint(ml, mh+1)
    if selected_choice2 in [1,2,3]:
        test_cases = choice_functions[selected_choice2](ml, mh)  # Call the selected function
    else:
        print("Invalid choice")

    return "Test cases generated for Array with n, m."

def generate_array_nmk():
    # Logic to generate test cases for 'Array with n, m, k'
    questions2 = [
    inquirer.List('choice', message="Enter the test cases you want:",
                  choices=[
                    '1. Array with unique elements',
                    '2. Array with duplicates',
                    '3. Permutation Array',
                      # Add other choices here...
                  ]),
    ]
    answers2 = inquirer.prompt(questions2)
    selected_choice2 = int(answers2['choice'].split('.')[0])
    print("Enter range of 'm' as space seperated integers: ", end="")
    ml, mh = map(int, input().split()) 
    # m1 = nm.random.randint(ml, mh+1)
    print("Enter range of 'k' as space seperated integers: ", end="")
    kl, kh = map(int, input().split()) 
    # k1 = nm.random.randint(kl, kh+1)
    if selected_choice2 in [1,2,3]:
        test_cases = choice_functions[selected_choice2](ml,mh,kl,kh)  # Call the selected function
    else:
        print("Invalid choice")

    return "Test cases generated for Array with n, m, k."

def generate_two_array():
    # Logic to generate test cases for 'two arrays with n, m'
    questions2 = [
    inquirer.List('choice', message="Enter the test cases you want:",
                  choices=[
                    '1. Array with unique elements',
                    '2. Array with duplicates',
                    '3. Permutation Array',
                      # Add other choices here...
                  ]),
    ]
    answers2 = inquirer.prompt(questions2)
    selected_choice2 = int(answers2['choice'].split('.')[0])
    print("Enter range of 'm' as space seperated integers: ", end="")
    ml, mh = map(int, input().split()) 
    # m1 = nm.random.randint(ml, mh+1)
    if selected_choice2 in [1,2,3]:
        test_cases = choice_functions[selected_choice2](ml, mh)  # Call the selected function
    else:
        print("Invalid choice")
    return "Test cases generated for two arrays with n, m."

def generate_nmk():
    # Logic to generate test cases for 'n, m, k'
    with open(file_name, 'w') as file:
        file.write(str(tc) + "\n")     
    print("Enter range of 'n' as space seperated integers: ", end="")
    nl, nh = map(int, input().split())    
    print("Enter range of 'm' as space seperated integers: ", end="")
    ml, mh = map(int, input().split())    
    print("Enter range of 'k' as space seperated integers: ", end="")
    kl, kh = map(int, input().split())    

    for i in range(0, tc):
        n1 = nm.random.randint(nl, nh+1)
        m1 = nm.random.randint(ml, mh+1)
        k1 = nm.random.randint(kl, kh+1)
     
        with open(file_name, 'a') as file:
            file.write(str(n1) + " " + str(m1) + " " + str(k1) + "\n")
    return "Test cases generated for n, m, k."

def generate_string():
    # Logic to generate test cases for 'String'
    with open(file_name, 'w') as file:
        file.write(str(tc) + "\n")     
    print("Enter range of length of string as space seperated integers: ", end="")
    nl, nh = map(int, input().split())  
    for i in range(0, tc):
        res = []  
        n1 = nm.random.randint(nl, nh+1)

        random_string = ''.join(random.choice(string.ascii_lowercase) for _ in range(n1))
        res.append(random_string)

        file_content = ' '.join(res)  # Convert the list to a string separated by spaces        
        with open(file_name, 'a') as file:
            file.write(str(n1))
            file.write("\n" + file_content + "\n")
        file_content=""
        res = []
    return "Test cases generated for String."

def generate_grid():

    with open(file_name, 'w') as file:
        file.write(str(tc) + "\n")    
    print("Enter range of number of rows 'n' as space seperated integers: ", end="")
    nl, nh = map(int, input().split())
    print("Enter range of number of columns 'm' as space seperated integers: ", end="")
    ml, mh = map(int, input().split()) 
    print("Enter range of grid elements 'k' as space seperated integers: ", end="")
    kl, kh = map(int, input().split())
    
    for i in range(0, tc):
        res = []      
        n1 = nm.random.randint(nl, nh+1)
        m1 = nm.random.randint(ml, mh+1)

        for j in range(0, n1):
            row = []
            for k in range(0, m1):                
                k1 = nm.random.randint(kl, kh+1)
                if (k1 not in row):
                    row.append(str(k1))
                else:
                    k-=1
                    continue
            res.append(row)
            file_content = '\n'.join([' '.join(row) for row in res])  # Convert the list of lists to a string with newline separation     

        with open(file_name, 'a') as file:
            file.write(str(n1))
            if m1 != 0: 
                file.write(" " +str(m1))
            file.write("\n"+ file_content + "\n")
        file_content=""
        res = []
    return "Test cases generated for Grid."

def generate_tree(selected_choice1 = 0, selected_choice2 = 0, selected_choice3 = 0, v1 =0):
    # Logic to generate test cases for 'Tree'
    with open(file_name, 'w') as file:
        file.write(str(tc) + "\n")      
    if(selected_choice1 == 0) :
        vl, vh = map(int, input("Enter range of number of vertices 'V' as space seperated integers : ").split())   
    if(selected_choice1 == 0):
        questions1 = [
        inquirer.List('choice', message="Enter the test cases you want:",
                    choices=[
                        '1. Connected Tree',
                        '2. Not connected Tree',
                        # Add other choices here...
                    ]),
        ]
        answers1 = inquirer.prompt(questions1)
        selected_choice1 = int(answers1['choice'].split('.')[0])
    if(selected_choice2 == 0):
        questions2 = [
        inquirer.List('choice', message="Enter the test cases you want:",
                    choices=[
                        '1. Directed Tree',
                        '2. Un-directed Tree',
                        # Add other choices here...
                    ]),
        ]
        answers2 = inquirer.prompt(questions2)
        selected_choice2 = int(answers2['choice'].split('.')[0])
    if(selected_choice3 == 0):
        questions3 = [
        inquirer.List('choice', message="Enter the test cases you want:",
                    choices=[
                        '1. Weighted Tree',
                        '2. Un-weighted Tree',
                        # Add other choices here...
                    ]),
        ]
        answers3 = inquirer.prompt(questions3)
        selected_choice3 = int(answers3['choice'].split('.')[0])
    if(selected_choice3 == 1):
        wl, wh = map(int,input("Enter range of weight to edges as space seperated integers : ").split())
    edges = []
    for j in range(0, tc):
    ## Using Prufer Code
        while True:
            v1 = random.randint(vl, vh)
            if v1 != 1:
                break
        pruferCode = []
        for i in range(v1-2):
            element = random.randint(1, v1)
            pruferCode.append(element)
        # edges = []
        edges.clear()
        freqCount = {}

        for i in range(1, v1+1):
            freqCount[i] = 0
        for i in pruferCode:
            freqCount[i] = freqCount[i] + 1
        
        for i in pruferCode:
            edge1 = i
            for j in range(1, v1+1):
                if freqCount[j] == 0:
                    edge2 = j
                    break    
            if(selected_choice3 == 1): 
                w1 = random.randint(wl, wh)   
                edges.append([edge1, edge2, w1])
            else:
                edges.append([edge1, edge2])
            freqCount[edge1]-=1
            freqCount[edge2]-=1

        cnt =0
        for i in range(1, v1+1):
            if(freqCount[i] == 0):
                if(cnt == 0):
                    edge1 = i
                    cnt+=1
                elif(cnt == 1):
                    edge2 = i
                    break
        if(selected_choice3 == 1):
            w1 = random.randint(wl, wh)
            edges.append([edge1, edge2, w1])
        else:
            edges.append([edge1, edge2])

        if(selected_choice1 == 2):
            x = random.randint(1, (len(edges)//2)+1)
            random_items = random.sample(edges, x)
            for item in random_items:
                edges.remove(item)        

        file_content = ""
        for iii in range(len(edges)):
            if(selected_choice3 == 1):
                file_content += str(edges[iii][0]) + " " + str(edges[iii][1]) + " " + str(edges[iii][2])
            else:
                file_content += str(edges[iii][0]) + " " + str(edges[iii][1])
            if iii != len(edges)-1:
                file_content += "\n"
        with open(file_name, 'a') as file:
            if v1 <= len(edges):
                file.write(str(v1)+" 0\n" )
            else:
                file.write(str(v1)+" "+str(len(edges)))
                if(len(edges) != 0):
                    file.write("\n"+ file_content + "\n")
                else:
                    file.write("\n")
        file_content=""        
    return "Test cases generated for Tree."
def tree_to_cyclic_graph(tree_edge_list):
    def find_non_leaf_nodes(tree_edges):
        nodes = set()
        for edge in tree_edges:
            nodes.add(edge[0])
            nodes.add(edge[1])
        return nodes

    def add_extra_edge(tree_edges, non_leaf_nodes):
        # Choose two non-leaf nodes randomly and add an edge between them
        u, v = map(random.choices(non_leaf_nodes, k = 2))
        w = random.randint(1, 10)  # Adjust the weight range as needed
        tree_edges.append([u, v, w])

    graph = {}
    non_leaf_nodes = find_non_leaf_nodes(tree_edge_list)

    for edge in tree_edge_list:
        u, v = edge[:2]  # Extract the first two elements, assuming u, v, w format
        w = edge[2] if len(edge) > 2 else 1  # Use provided weight if available, else default to 1
        graph.setdefault(u, []).append((v, w))
        graph.setdefault(v, []).append((u, w))

    add_extra_edge(tree_edge_list, non_leaf_nodes)
    return graph

def generate_graph():
    with open(file_name, 'w') as file:
        file.write(str(tc) + "\n")      
    vl, vh = map(int, input("Enter range of number of vertices 'V' as space seperated integers : ").split()) 
    v1 = random.randint(vl ,vh)  
    questions1 = [
    inquirer.List('choice', message="Enter the test cases you want:",
                  choices=[
                    '1. Connected Graph',
                    '2. Not connected Graph',
                      # Add other choices here...
                  ]),
    ]
    answers1 = inquirer.prompt(questions1)
    selected_choice1 = int(answers1['choice'].split('.')[0])
    questions2 = [
    inquirer.List('choice', message="Enter the test cases you want:",
                  choices=[
                    '1. Directed Graph',
                    '2. Un-directed Graph',
                      # Add other choices here...
                  ]),
    ]
    answers2 = inquirer.prompt(questions2)
    selected_choice2 = int(answers2['choice'].split('.')[0])
    questions3 = [
    inquirer.List('choice', message="Enter the test cases you want:",
                  choices=[
                    '1. Weighted Graph',
                    '2. Un-weighted Graph',
                      # Add other choices here...
                  ]),
    ]
    answers3 = inquirer.prompt(questions3)
    selected_choice3 = int(answers3['choice'].split('.')[0])
    if(selected_choice3 == 1):
        wl, wh = map(int,input("Enter range of weight to edges as space seperated integers : ").split())
    for j in range(0, tc):
    ## Using Prufer Code
        while True:
            v1 = random.randint(vl, vh)
            if v1 != 1:
                break
        pruferCode = []
        for i in range(v1-2):
            element = random.randint(1, v1)
            pruferCode.append(element)
        edges = []
        edges.clear()
        freqCount = {}

        for i in range(1, v1+1):
            freqCount[i] = 0
        for i in pruferCode:
            freqCount[i] = freqCount[i] + 1
        
        for i in pruferCode:
            edge1 = i
            for j in range(1, v1+1):
                if freqCount[j] == 0:
                    edge2 = j
                    break    
            if(selected_choice3 == 1): 
                w1 = random.randint(wl, wh)   
                edges.append([edge1, edge2, w1])
            else:
                edges.append([edge1, edge2])
            freqCount[edge1]-=1
            freqCount[edge2]-=1

        cnt =0
        for i in range(1, v1+1):
            if(freqCount[i] == 0):
                if(cnt == 0):
                    edge1 = i
                    cnt+=1
                elif(cnt == 1):
                    edge2 = i
                    break
        if(selected_choice3 == 1):
            w1 = random.randint(wl, wh)
            edges.append([edge1, edge2, w1])
        else:
            edges.append([edge1, edge2])

        if(selected_choice1 == 2):
            x = random.randint(1, (len(edges)//2)+1)
            random_items = random.sample(edges, x)
            for item in random_items:
                edges.remove(item)       

    graph = tree_to_cyclic_graph(edges)


    
    file_content = ""
    for iii in range(len(graph)):
        if(selected_choice3 == 1):
            file_content += str(graph[iii][0]) + " " + str(graph[iii][1]) + " " + str(graph[iii][2])
        else:
            file_content += str(graph[iii][0]) + " " + str(graph[iii][1])
        if iii != len(graph)-1:
            file_content += "\n"
    with open(file_name, 'a') as file:
        if v1 <= len(graph):
            file.write(str(v1)+" 0\n" )
        else:
            file.write(str(v1)+" "+str(len(graph)))
            if(len(graph) != 0):
                file.write("\n"+ file_content + "\n")
            else:
                file.write("\n")
        file_content=""    

    return "Test cases generated for Graph."


# Define functions for generating test cases for other choices...

# Mapping function names to their respective choices
choice_functions = {
    1: generate_array_unique_elements,
    2: generate_array_duplicates,
    3: generate_permutation_array,
    4: generate_binary_string,
    5: generate_array_nm,
    6: generate_array_nmk,
    7: generate_two_array,
    8: generate_nmk,
    9: generate_string,
    10: generate_grid,
    11: generate_graph,
    12: generate_tree,
    # Map other choices to their respective functions...
}

parser = argparse.ArgumentParser(description='Write content to a file')
parser.add_argument('--content', help='Content to write to the file')
args = parser.parse_args()

questions = [
    inquirer.Text('file_name', message="Enter the file name (without .txt)"),
    inquirer.List('choice', message="Enter the test cases you want:",
                  choices=[
                    '1. n; Array with unique elements',
                    '2. n; Array with duplicates',
                    '3. n; Permutation Array',
                    '4. n; Binary String',
                    '5. n, m; Integer Array',
                    '6. n, m, k; Integer Array',
                    '7. n, m; Integer Array-1; Integer Array-2',
                    '8. n, m, k',
                    '9. n; String',
                    '10. n, m; Grid',
                    # '11. n, m; Graph',
                    '11. n, m; Tree'
                      # Add other choices here...
                  ]),
    inquirer.Text('tc_num', message="Number of test cases: "),
]

answers = inquirer.prompt(questions)

file_name = answers['file_name'] + ".txt"
selected_choice = int(answers['choice'].split('.')[0])  # Extracting the selected choice number
tc = int(answers['tc_num'])

if selected_choice in choice_functions:
    test_cases = choice_functions[selected_choice]()  # Call the selected function
else:
    print("Invalid choice")

with yaspin(text="Writing to file...", color="cyan") as spinner:
    try:
        # with open(file_name + ".txt", 'w') as file:
        #     file.write(test_cases)
        spinner.ok("✔")
        print(f"Successfully written test cases to {file_name}.")
    except Exception as e:
        spinner.fail("✘")
        print(f"Failed to write to {file_name}. Error: {str(e)}")
