def prefix_to_subnet_mask(prefix_length):
    # Validate prefix length
    if prefix_length < 0 or prefix_length > 32:
        raise ValueError("Prefix length must be between 0 and 32.")
    
    # Generate subnet mask from prefix length
    mask = (0xFFFFFFFF << (32 - prefix_length)) & 0xFFFFFFFF
    return f"{(mask >> 24) & 255}.{(mask >> 16) & 255}.{(mask >> 8) & 255}.{mask & 255}"

def is_valid_subnet_mask(subnet_mask):
    # Split the subnet mask into its octets
    octets = subnet_mask.split('.')
    
    # Check if there are 4 octets
    if len(octets) != 4:
        return False
    
    # Check if each octet is in the range 0-255
    for octet in octets:
        if not octet.isdigit() or not (0 <= int(octet) <= 255):
            return False

    # Convert octets to binary and check if they are contiguous
    binary = ''.join(format(int(octet), '08b') for octet in octets)
    return '01' not in binary  # valid if there's no '01' in binary representation
