def vigenere_cipher(message, key, mode):
    table = []
    for i in range(26):
        table.append([chr((i+j)%26 + ord('A')) for j in range(26)])

    key = "".join(key.split()).upper()
    
    message_len = len(message)
    key_len = len(key)
    
    key_repeat = key * (message_len // key_len) + key[:message_len % key_len]
    
    result = ""
    for i in range(message_len):
        row = ord(message[i]) - ord('A')
        col = ord(key_repeat[i]) - ord('A')
        if mode == "encrypt":
            result += table[row][col]
        else:
            result += chr(table[col].index(message[i]) + ord('A'))
    
    return result