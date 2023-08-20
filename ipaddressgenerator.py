def restore_ip_addresses(s):
    def backtrack(start, path):
        if start == len(s) and len(path) == 4:
            result.append('.'.join(path))
            return
        
        if len(path) >= 4:
            return
        
        for end in range(start + 1, min(start + 4, len(s) + 1)):
            segment = s[start:end]
            if (len(segment) > 1 and segment[0] == '0') or int(segment) > 255:
                continue
            
            backtrack(end, path + [segment])
    
    result = []
    backtrack(0, [])
    return result

# Example usage
input_string = "25525511135"
result = restore_ip_addresses(input_string)
print("Valid IP address combinations:", result)
# Output: ['255.255.11.135', '255.255.111.35']
