def load_rgb_matrix_from_file(file_path, img_width, img_height):
    with open(file_path, 'r') as file:
        data = file.read().split(',')

    data = list(map(int, data))
    pixels = [data[i:i+3] for i in range(0, len(data), 3)]

    matrix = []
    for i in range(img_height):
        row = pixels[i * img_width:(i + 1) * img_width]
        matrix.append(row)

    return matrix


def extract_nth_bit_from_rgb(rgb_value, n):
    r_nth_bit = (rgb_value[0] >> (n - 1)) & 1
    g_nth_bit = (rgb_value[1] >> (n - 1)) & 1
    b_nth_bit = (rgb_value[2] >> (n - 1)) & 1
    
    # next bit
    # r1_nth_bit = (rgb_value[0] >> (n)) & 1
    # g1_nth_bit = (rgb_value[1] >> (n)) & 1
    # b1_nth_bit = (rgb_value[2] >> (n)) & 1

    # next bit
    # r2_nth_bit = (rgb_value[0] >> (n + 1)) & 1
    # g2_nth_bit = (rgb_value[1] >> (n + 1)) & 1
    # b2_nth_bit = (rgb_value[2] >> (n + 1)) & 1

    return [r_nth_bit, g_nth_bit, b_nth_bit]


def diagonal_traverse_lsb(matrix):
    rows = len(matrix)
    cols = len(matrix[0])

    bits = []

    for d in range(rows + cols - 1):
        if d < cols:
            row = 0
            col = d
        else:
            row = d - cols + 1
            col = cols - 1

        diagonal = []
        while row < rows and col >= 0:
            lsb_values = extract_nth_bit_from_rgb(matrix[row][col], 1)
            diagonal.extend(lsb_values) 
            row += 1
            col -= 1

        if d % 2 == 0:
            bits.extend(diagonal)
        else:
            bits.extend(diagonal[::-1])

    return bits


def bitstream_to_ascii(bitstream):
    ascii_string = ''
    
    for i in range(0, len(bitstream), 8):
        byte = bitstream[i:i + 8]

        if len(byte) < 8:
            break

        byte_str = ''.join(map(str, byte))
        byte_value = int(byte_str, 2)
        ascii_string += chr(byte_value)
    
    return ascii_string


# Main Program
if __name__ == "__main__":
    # Image dimensions
    img_width = 2280
    img_height = 1282
    # test_img_width = 3
    # test_img_height = 3

    file_path = "input.txt" 
    rgb_matrix = load_rgb_matrix_from_file(file_path, img_width, img_height)

    diagonal_lsb_values = diagonal_traverse_lsb(rgb_matrix)
    ascii_string = bitstream_to_ascii(diagonal_lsb_values)

    print(ascii_string[:100])
