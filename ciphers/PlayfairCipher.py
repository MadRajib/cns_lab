class PlayFair:
    table = None
    row = 0
    col = 0
    def build_table(self, row=0, col=0):
        self.row = row
        self.col = col
        self.table = []
        for _ in range(row):
            r = []
            for _ in range(col):
                r.append('*')
            self.table.append(r)
        
    def print_table(self):
        for row in range(self.row):
            for col in range(self.col):
                print(self.table[row][col],end="")
            print("")

    # set all element as *
    def clear_table(self):
        for row in range(self.row):
            for col in range(self.col):
                self.table[row][col] = "*"

    def find_letter(self, letter):
        for row in range(self.row):
            for col in range(self.col):
                if (self.table[row][col] == letter):
                    return (row,col)
        return None
    
    def encode_pair(self, a, b):
        if a == b:
            print("ERROR: letters to encode_pair must be distinct")
            return
        a_r, a_c = self.find_letter(a)
        b_r, b_c = self.find_letter(b)

        h = abs(a_r - b_r)
        w = abs(a_c - b_c)

        # if box is rectangle
        if(w > 0 and h > 0):
            return self.table[a_r][b_c] + self.table[b_r][a_c]
        
        # if only one column
        if (w == 0):
            return self.table[(a_r+1) % self.row][a_c] + self.table[(b_r+1) % self.row][b_c]

        if (h == 0):
            return self.table[a_r][(a_c+1) % self.col] + self.table[b_r][(b_c+1) % self.col]

    def decode_pair(self, a, b):
        if a == b:
            print("ERROR: letters to encode_pair must be distinct")
            return
        a_r, a_c = self.find_letter(a)
        b_r, b_c = self.find_letter(b)

        h = abs(a_r - b_r)
        w = abs(a_c - b_c)

        # if box is rectangle
        if(w > 0 and h > 0):
            return self.table[a_r][b_c] + self.table[b_r][a_c]
        
        # if only one column
        if (w == 0):
            return self.table[(a_r-1) % self.row][a_c] + self.table[(b_r-1) % self.row][b_c]

        if (h == 0):
            return self.table[a_r][(a_c-1) % self.col] + self.table[b_r][(b_c-1) % self.col]
    
    
    def create_table(self, secret):
        self.clear_table()
        row = 0
        col = 0
        for ch in secret:
            self.table[row][col]  = ch.upper()
            col +=1
            if (col == self.col):
                col = 0
                row +=1 

    def create_pair(self, text):
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



if __name__ == "__main__":
    # s = input("Enter the secret key: ") 
    s = "abcdefghijklmnopqrstuvqxy"
    p = "Hidethegoldi"
    
    ply = PlayFair()
    ply.build_table(5,5)
    ply.print_table()
    ply.create_table(s)
    ply.print_table()

    pairs = ply.create_pair(p)
    print(pairs)
    encode_pairs_list = []
    for pair in pairs:
       encode_pairs_list.append(ply.encode_pair(pair[0],pair[1]))
    
    print(encode_pairs_list)

    pairs = []
    for pair in encode_pairs_list:
        pairs.append(ply.decode_pair(pair[0],pair[1]))

    print(pairs)