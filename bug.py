
# I could have watched 4 episodes of anime instead of doing this 😭

import random
import re
import pyperclip

def swap_operators(line):
    # this one is pure evil, vscode or the compiler wont detect it.
    swap_map = {
        "=="  : "=",
        ">=" : "+=",
        "*=" : "+=",
        "+"  : "-",
        "-"  : "*",
        "|" : "||",
        "*" : "/",
        "/" : "-",
        ">>": "<<",        
        "&&" : "&",
    }
    
    print("____________________________")
    for operator, replacement in swap_map.items():
        RNG = random.random() 
        if operator in line and RNG < 0.8:
            line = line.replace(operator, replacement, 1)
            
    return line
    
    
def add_off_by_one_error(line):
    # this is what drives people to commit crimes
    
    match = re.search(r'(for|while)\s*\(([^)]+)\)', line)
    if match:
        print("Match")
        # print("Old: ", line)
        RNG = random.random()
        condition = match.group(2)
        if '<' in condition or '>' in condition:
            # print(lambda x: str(int(x.group(1))+1))
            line = re.sub(r'(\d+)(?!.*\d)', lambda x: str(int(x.group(1))+1), line)
            # print("New: ", line)
        
    return line 
            
    ...
    
def change_data_type(line):
    # happens
    data_types = ['int', 'float', 'double', 'char', 'long', 'short', 'unsigned']
    
    def choose_alternate_type(current_type, data_types):
        print("choosing")
        index = data_types.index(current_type)
            
        # making sure new index is not the same as old index by modular arithemetic     
        new_index = ((index+random.randint(1, len(data_types)-1))%len(data_types))
        return data_types[new_index]
    
    condition = random.random() > 0.2 # 20% chance 
    if condition: 
        for data_type in data_types:
            line = re.sub(r'\b' + re.escape(data_type) + r'\b', lambda m: choose_alternate_type(m.group(0), data_types), line)
        
    return line
    ...
    
def mess_up_order_of_operations(line):
    # happens
    if random.random() < 0.2:
        line = re.sub(r'\b(\w+)\s*([+\-*/])\s*(\w+)\b', r'(\1 \2 \3)', line)  # Add parentheses around simple expressions
        
        line = re.sub(r'\((\w+ \+ \w+)\)', r'\1', line)  # Remove parentheses around simple addition expressions
        line = re.sub(r'\((\w+ - \w+)\)', r'\1', line) 
    
    return line
    
    
def change_semicolons(line):
    if random.random() < 0.1:
        line =  re.sub(r";", ":", line, count=1)
    
    return line
    # happens
    ...
    
def shadow_variable_in_deeper_scope(line):
    # vscode will detect this but ok.
    ...
    

input_file = """using namespace std;

int main ()

{

    int num;
    num = 0
    num = (num + 1) + 3;

    cout << "Enter the number to be checked : ";

    cin >> num;

    if (num % 2 == 0)

        cout << num << " is Even.";

    else

        cout << num << " is Not Even ";
        
    for(int i = 0; i < 10; i++);
    
    while(int j = 5; j > 15; j++);

    return 0;

}
"""



def main():
    
    def get_multiline_input():
        
        lines = []
        while True:
            line = input()
            if not line:
                break
            lines.append(line)
        return '\n'.join(lines) 
    
    input_file = pyperclip.paste()
        
    for line in input_file.split('\n'):
        line = swap_operators(line)
        
        line = add_off_by_one_error(line)
        line = change_data_type(line)
        line = mess_up_order_of_operations(line)
        line = change_semicolons(line)
        
        print(line)
    
    
if __name__ == "__main__":
    
    main()
    
    

    
    













