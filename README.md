# Bitmap Parser

This is simple bitmap (string) parser. It creates a C++ std::array of variable size. It is a simple tool used aid creating images/digits/drawings on small OLED displayes (e.g. OLEDs with the SSD1327 controller)

## Usage

- Create a bitmap string with 0's and 1's. All lines must be of equal size.
- Set the right size for lines and rows.
- Name the outcome.
- Select the size of the hexadecimal output.
- Run the script.

## Future updates

- Get rid of all manual tweaks and use arguments.
- Get bitmap(s) from file.
- Get the size of lines and rows automatically.
- Allow line lengths where size%!=0.
- Output to file.
- Output to different languages.
- UI for drawing bitmap.