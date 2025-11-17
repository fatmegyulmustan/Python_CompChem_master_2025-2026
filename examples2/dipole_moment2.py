import re

log_file = "Conformes_1_MM_water.log"
output_file_name = "Dipole_moment_components.xlsx"

with open(log_file, 'rt') as text_file:
    text_file_lines = text_file.readlines()  # list of lines
    var = " Dipole moment"

    var_indexes = []
    component_indexes = []
    for i in range(len(text_file_lines)):
        if str(text_file_lines[i]).startswith(var):
            var_index = i
            var_indexes.append(var_index)
            component_indexes.append(var_index + 1)
            components = text_file_lines[component_indexes[-1]]
    pattern = r"\s(X=)\s+(-*\d.\d+)\s+(Y=\s+)(-*\d.\d+)\s+(Z=\s+)(-*\d.\d+)"
    result = re.findall(pattern, components)


with open(output_file_name, "w") as output_file:
    print(f'Dipole moment components: \n X = {result[0][1]} \n Y = {result[0][3]} \n Z = {result[0][5]}', file=output_file)




