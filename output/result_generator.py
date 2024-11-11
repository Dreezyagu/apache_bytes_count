import ast

total_cost = 0

for i in range(0,5):
    with open(f'part-0000{i}', 'r') as file:
        data = file.read().strip()
        data_dict = ast.literal_eval(data)
        total_cost+=data_dict["Total cost"]


# Open the file in write mode
with open('result.txt', 'w') as file:
    # Write each tuple in a readable format
    file.write(f"Total cost: {total_cost} euros")
    


