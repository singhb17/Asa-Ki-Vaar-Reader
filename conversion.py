# Script made to convert existing data format to format required by JS
# Nothing in relation to the actual reader project

# Get input from user via terminal
input_text = input("Paste your lines here (press Enter twice to finish):\n")

# Collect all input lines until an empty line is entered
lines = []
while input_text:
    lines.append(input_text.strip())
    input_text = input()

# Print the lines in the desired format
for i, line in enumerate(lines):
    if i < len(lines) - 1:
        print(f'"{line}",')
    else:
        print(f'"{line}"')