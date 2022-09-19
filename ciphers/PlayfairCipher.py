# Initialize a 6 by 6 table of stars
from glob import glob


table = [['*', '*', '*', '*', '*', '*'],
         ['*', '*', '*', '*', '*', '*'],
         ['*', '*', '*', '*', '*', '*'],
         ['*', '*', '*', '*', '*', '*'],
         ['*', '*', '*', '*', '*', '*'],
         ['*', '*', '*', '*', '*', '*']]

def print_table():
    for row in range(6):
        for col in range(6):
            print(table[row][col],end="")
        print("")

def clear_table():
    for row in range(6):
        for col in range(6):
            table[row][col] = "*"

def find_letter(letter):
    for row in range(6):
        for col in range(6):
            if (table[row][col] == letter):
                return (row,col)
    return None
    
def encode_pair(a, b):
    if a == b:
        print("ERROR: letters to encode_pair must be distinct")
        return
    a_r, a_c = find_letter(a)
    b_r, b_c = find_letter(b)

    h = abs(a_r - b_r)
    w = abs(a_c - b_c)

    # if box is rectangle
    if(w > 0 and h > 0):
        return table[a_r][b_c] + table[b_r][a_c]
    
    # if only one column
    if (w == 0):
        return table[(a_r+1) % 6][a_c] + table[(b_r+1) % 6][b_c]

    if (h == 0):
        return table[a_r][(a_c+1) % 6] + table[b_r][(b_c+1) % 6]

def decode_pair(a, b):
    if a == b:
        print("ERROR: letters to encode_pair must be distinct")
        return
    a_r, a_c = find_letter(a)
    b_r, b_c = find_letter(b)

    h = abs(a_r - b_r)
    w = abs(a_c - b_c)

    # if box is rectangle
    if(w > 0 and h > 0):
        return table[a_r][b_c] + table[b_r][a_c]
    
    # if only one column
    if (w == 0):
        return table[(a_r-1) % 6][a_c] + table[(b_r-1) % 6][b_c]

    if (h == 0):
        return table[a_r][(a_c-1) % 6] + table[b_r][(b_c-1) % 6]
    
    
def create_table(secret):
    clear_table()
    global table
    row = 0
    col = 0
    for ch in secret:
        table[row][col]  = ch.upper()
        col +=1
        if (col == 6):
            col = 0
            row +=1 

def create_pair(text):
    pair_list = []
    i = 0
    while i < len(text):
        a = text[i].upper()
        i += 1
        b = text[i].upper()
        
        if(a == b ):
            pair_list.append(a+'X') # if we have same
            continue
        i+=1

        pair_list.append(a+b)    

    return pair_list

def playfair(key, plaintext):
    create_table(key)
    print_table()
    pairs = create_pair(plaintext)
    print(pairs)
    encode_pairs_list = []
    for pair in pairs:
       encode_pairs_list.append(encode_pair(pair[0],pair[1]))
    
    print(encode_pairs_list)
    pairs = []
    for pair in encode_pairs_list:
        pairs.append(decode_pair(pair[0],pair[1]))

    print(pairs)



if __name__ == "__main__":
    # s = input("Enter the secret key: ") 
    s = "abcdefghijklmnopqrstuvqxyz0123456789"
    p = "Hidethegoldi"
    print(playfair(s, p))