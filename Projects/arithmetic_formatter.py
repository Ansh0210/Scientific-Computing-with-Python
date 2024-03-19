def arithmetic_arranger(problems, show_answers=False):
    
    # each problem in problems split at whitespace
    split_probs = [prob.split() for prob in problems]

    # index for each item in split probs
    num1_i = 0
    num2_i = 2
    
    all_num1 = [prob[num1_i] for prob in split_probs]
    all_num2 = [prob[num2_i] for prob in split_probs]
    all_ops = [ops[1] for ops in split_probs]
    
    # checks for the len of the problems given and checks if more than 5
    if len(problems) > 5:
        return 'Error: Too many problems.'
    
    for item in split_probs:
        # check to see if + or - is in the problem, if not returns error
        if "+" not in item and "-" not in item:
            return "Error: Operator must be '+' or '-'." 
        
        # check to see if num1 and num2 are digits 
        if not item[num1_i].isdigit() or not item[num2_i].isdigit():
            return "Error: Numbers must only contain digits." 
        
        # check to see if num1 and num2 are more than 4 digits
        if len(item[num1_i]) > 4 or len(item[num2_i]) > 4:
            return "Error: Numbers cannot be more than four digits."
    
    top_row = []
    middle_row = []
    bottom_row = []
    result_row = []
    
    for n1, n2 in zip(all_num1, all_num2):
        # append dashes for the bottom row 
        bottom_row.append("-" * (max(len(n1), len(n2))+2))        
    
    # top row and middle row logic 
    for dash, num1, num2, ops in zip(bottom_row, all_num1, all_num2, all_ops):
        # top logic
        space_top = len(dash) - len(num1)
        top_row.append(f'{space_top * " "}{num1}')    
        
        # bottom logic
        space_middle = len(dash) - len(num2) - 1
        middle_row.append(f'{ops}{space_middle * " "}{num2}')

        # result logic 
        if ops == '+':
            solution = int(num1) + int(num2)
        elif ops == '-':
            solution = int(num1) - int(num2)
        
        if len(str(solution)) > max(len(num1), len(num2)):    
            result_row.append(f'{" "}{solution}')
        else:
            result_row.append(f'{" "*2}{solution}')
    
    #conversion of rows of list into string
    top_str = f"{'    '.join(top_row)}"
    bottom_str = f"{'    '.join(bottom_row)}"
    middle_str = f"{'    '.join(middle_row)}"
    result_str = f"{'    '.join(result_row)}"
    
    # show answer logic
    if show_answers:
        final_sol = f"{top_str}\n{middle_str}\n{bottom_str}\n{result_str}"
        return final_sol
    else:
        final_sol = f"{top_str}\n{middle_str}\n{bottom_str}"
        return final_sol

# check for final solution
print(f'\n{arithmetic_arranger(["2 + 3", "32 + 698", "3801 - 2", "45 + 43", "123 + 49"], True)}')
