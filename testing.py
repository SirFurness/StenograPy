with open("data.jpeg", "r+b") as f:
    byte = f.read(1)
    encoded_zero = byte[0] & b'\xfe'[0]
    encoded_one = byte[0] | b'\xff'[0]
    decode = encoded_zero & b'\x01'[0]
    decode_one = encoded_one & b'\x01'[0]
    print(decode)
    print(decode_one)
    while byte:
        byte = f.read(1)
