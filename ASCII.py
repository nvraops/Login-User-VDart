print("*****Welcome to Binary Converter*****")
print(" Here you are requested to Enter your Name and your Name is converted into Binary Values using ASCII")

# This function changes each letter in a name into a custom binary code
def simple_binary_converter(name):
    output = []  # This will hold final results

    for ch in name:
        # Step 1: Get number for the letter
        num = ord(ch)

        # Step 2: Convert number to 8-digit binary string
        bin_str = format(num, '08b')

        # Step 3: Split binary into first 4 and last 4 bits
        first = bin_str[:4]
        last = bin_str[4:]

        # Step 4: Count how many 1s are in first part
        count_1s_first = first.count('1')

        # Step 5: Add 1 or 0 at the start based on how many 1s
        if count_1s_first % 2 == 1:
            first = '1' + first
        else:
            first = '0' + first

        # Step 6: Count 1s in second part
        count_1s_last = last.count('1')

        # Step 7: Add 1 or 0 at the end based on how many 1s
        if count_1s_last % 2 == 1:
            last = last + '1'
        else:
            last = last + '0'

        # Step 8: Combine both parts to make final binary
        final = first + last

        # Step 9: Save the result
        output.append((ch, final))

    return output

# Get input from user
name_input = input("Type your name: ")

# Call the function
final_result = simple_binary_converter(name_input)

# Show the results
print("\nCustom binary output:")
for letter, binary in final_result:
    print(letter, "=>", binary)
