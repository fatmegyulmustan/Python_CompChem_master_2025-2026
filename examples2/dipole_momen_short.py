import re

import re

log_file = "Conformes_1_MM_water.log"
output_file_name = "Dipole_moment_components.txt"
var = "    X=      "

result = []
with open(log_file, 'rt') as text_file:
    text = text_file.read()  # list of lines
    pattern = r"\s(X=)\s+(-*\d.\d+)\s+(Y=\s+)(-*\d.\d+)\s+(Z=\s+)(-*\d.\d+)"
    result = re.findall(pattern, text)
    print(result)
    print(f'Dipole moment components: \n X = {result[-1][1]} \n Y = {result[-1][3]} \n Z = {result[-1][5]}')

with open(output_file_name, "w") as output_file:
    print(f'Dipole moment components: \n X = {result[-1][1]} \n Y = {result[-1][3]} \n Z = {result[-1][5]}',
          file=output_file)
