#!/usr/bin/env python

"""bitmap_parses.py: Parses bitmap strings to C++ std::arrays."""

# todo: as external file
bitmap = """
00000000000000000000000000000000
00000000000000010000000000000000
00000000000000111000000000000000
00000000000001111100000000000000
00000000000011111110000000000000
00000000000111111111000000000000
00000000001111111111100000000000
00000000011111111111110000000000
00000001111111111111111100000000
00000011111111111111111110000000
00001111111111111111111111100000
00001111111111111111001111100000
00011111111111111110000111110000
00011111111111111111001111110000
00011111111111111111111111110000
00001111111111111111111111100000
00001111111111111111111111100000
00000111111111111111111111000000
00000011111111111111111110000000
00000000111111111111111000000000
00000000001111111111100000000000
00000000000000100000000000000000
00000000000000000000000000000000
"""

# todo: as arguments
lines = 23
rows = 32
array_name = "drop"
hex_char_size = 2

# todo: it's not always uint8_t
generated_string = "constexpr std::array<std::array<uint8_t," + str(rows//8) +\
    ">, + " + str(lines) + "> array" + array_name + "{{"

for i in range(lines):
    generated_string += "\n\t{"
    hex_array = []

    for j in range(rows//4):
        # future update: what if %4!=0?
        val = 0
        ex = 0
        slice_start = (i * rows) + (i + 1) + (j * 4)
        for bit in bitmap[slice_start:slice_start+4]:
            val += pow(2, 3-ex) if bit == '1' else 0
            ex += 1
        hex_array.append(val)

    for k in range(rows//4//hex_char_size):
        hex_string = "0x"
        for hex_values in hex_array[k*hex_char_size:k*hex_char_size +
                                    hex_char_size]:
            hex_string += str(hex(hex_values).lstrip("0x").rstrip("L"))
            if hex_values == 0:
                hex_string += "0"
        while len(hex_string) is not (2+hex_char_size):
            hex_string += "0"
        generated_string += hex_string + ","

    # remove extra comma
    generated_string = generated_string[:-1]
    generated_string += "},"

# remove extra comma
generated_string = generated_string[:-1]
generated_string += "\n}};"
print(generated_string)
