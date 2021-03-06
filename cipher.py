##############################################################################
# COMPONENT:
#    CIPHER01
# Author:
#    Br. Helfrich, Kyle Mueller, <your name here if you made a change>
# Summary:
#    Implement your cipher here. You can view 'example.py' to see the
#    completed Caesar Cipher example.
##############################################################################


##############################################################################
# CIPHER
##############################################################################
class Cipher:
    def __init__(self):
        # TODO: Insert anything you need for your cipher here
        pass

    def get_author(self):
        # TODO: Return your name
        return "Chase A. Switzer"

    def get_cipher_name(self):
        # TODO: Return the cipher name
        return "Playfair Cipher"

    ##########################################################################
    # GET CIPHER CITATION
    # Returns the citation from which we learned about the cipher
    ##########################################################################
    def get_cipher_citation(self):
        # TODO: This function should return your citation(s)
        citations = """
        1. https://learning.oreilly.com/library/view/express-learning-cryptography/9788131764527/chap03.xhtml
            * ITL Education Solutions Limited
            * Express Learning: Cryptography and Network Security
            * Jan 2012
        2. https://www.youtube.com/watch?v=-KjFbTK1IIw 
            * Videos By Kevin
            * Playfair Cipher 
            * Mar 18, 2018
        3. https://justcryptography.com/playfair-implementation/
            * Just Cryptography (Rafael)
            * How to implement the Playfair cipher in python? 
            * N/A
        4. https://www.geeksforgeeks.org/playfair-cipher-with-examples/ 
            * Geeksforgeeks (AbhayBhat) 
            * Playfair Cipher with Examples 
            * Dec 24, 2021
        5. https://dev.to/karanmunjani/encryption-using-playfair-cipher-in-python-24l4
            * Karan-Munjani
            * Playfair Cipher Encryption Program in Python
            * Oct 3, 2021
        """
        return citations

    ##########################################################################
    # GET PSEUDOCODE
    # Returns the pseudocode as a string to be used by the caller
    ##########################################################################
    def get_pseudocode(self):
        # TODO: This function should return your psuedocode, neatly formatted

        # The encrypt pseudocode
        pc = """
            encrypt(plaintext, password)
                ciphertext <- ""
                matrix <- generate_matrix(uppercase password)
                message <- separate_dup_char(plaintext)
                ciphertext_list <- playfair(uppercase message, matrix)
                FOR element IN ciphertext_list
                    append element to string ciphertext
                RETURN ciphertext
        """

        # The decrypt pseudocode
        pc += """
            decrypt()
                plaintext = ""
                matrix = self.generate_matrix(uppercase password)
                encrypted_message = separate_dup_chars(ciphertext)
                plaintext_list = playfair_reverse(uppercase encrypted_message, matrix)
                FOR element IN plaintext_list:
                    append element to string plaintext
                RETURN plaintext
        """

        # The generate matrix psuedocode, responsible for encoding and decoding a message
        pc += """
            generate_matrix(password)
                key <- password
                matrix <- [
                    [0, 0, 0, 0, 0]
                    [0, 0, 0, 0, 0]
                    [0, 0, 0, 0, 0]
                    [0, 0, 0, 0, 0]
                    [0, 0, 0, 0, 0]
                ]

                added_letters <- []
                row_index <- 0
                col_index <- 0

                FOR letter IN key:
                    IF letter NOT IN added_letters
                        matrix[row_index][col_index] <- letter
                        append letter TO added_letters
                        row_index <- row_index add 1 if col_index IS 4 ELSE row_index
                        col_index <- col_index add 1 if col_index IS NOT 4 else 0
                    else:
                        continue
            
                remaining_letters <- []
                FOR num IN range(65(A), 91(Z))
                    IF chr value of num IS 'J'
                        continue
                    ELSE IF chr value of num NOT IN added_letters
                        append chr value of num TO remaining_letters

                index <- 0
                FOR i IN range(5)
                    FOR j IN range(5)
                        IF matrix[i][j] IS NOT 0
                            continue
                        ELSE
                            matrix[i][j] <- remaining_letters[index]
                            index add 1

                return matrix
        """

        pc += """
            separate_dup_chars(plaintext)
                FOR index IN range(0, length of plaintext - 1, 2)
                IF index < length of plaintext
                    IF plaintext[index] == plaintext[index + 1]
                        plaintext <- plaintext[index] + "X" + plaintext[index plus 1]
        
                IF length of plaintext modulo 2 IS NOT 0
                    plaintext <- append "X" at end of plaintext
                RETURN plaintext
        """

        pc += """
            return_index(letter, matrix)
                IF letter EQUALS J
                    LETTER <- 'I'
                FOR row IN range(5)
                    FOR col IN range(5)
                        IF matrix[row][col] IS letter
                            RETURN (row, col)
        """

        pc += """
            playfair(message, matrix)
                ciphertext <- []
                FOR index IN range(0, length of message minus 1, 2)
                    row1, col1 <- 0, 0
                    row2, col2 <- 0, 0
                    IF index < length of message
                        row1, col1 <- return_index(message[index], matrix)
                        row2, col2 <- return_index(message[index + 1], matrix)

                    IF row1 EQUALS row2
                        append matrix[row1][(col1 + 1) % 5] TO ciphertext
                        append matrix[row2][(col2 + 1) % 5] TO ciphertext
                    ELSE IF col1 EQUALS col2
                        append matrix[(row1 + 1) % 5][col1] TO ciphertext
                        append matrix[(row2 + 1) % 5][col2] TO ciphertext
                    ELSE
                        append matrix[row1][col2] TO ciphertext
                        append matrix[row2][col1] TO ciphertext
                RETURN ciphertext
        """

        pc += """
            playfair_reverse(self, message, matrix):
                plaintext <- []
                FOR index IN range(0, length of message minus 1, 2)
                    row1, col1 <- 0, 0
                    row2, col2 <- 0, 0
                    
                    IF index < length of message
                        row1, col1 <- return_index(message[index], matrix)
                        row2, col2 <- return_index(message[index + 1], matrix)
            
                    IF row1 EQUALS row2
                        col1 <- col1 minus 1 if col1 ABOVE 0 ELSE 4
                        col2 <- col2 minus 1 if col2 ABOVE 0 ELSE 4
                        append matrix[row1][col1] TO plaintext
                        append matrix[row2][col2] TO plaintext
    
                    ELSE IF col1 EQUALS col2
                        row1 <- row1 minus 1 if row1 ABOVE 0 ELSE 4
                        row2 <- row2 minus 1 if row2 ABOVE 0 ELSE 4
                        append matrix[row1][col1] TO plaintext
                        append matrix[row2][col2] tTO plaintext
                    
                    ELSE
                        append matrix[row1][col2] TO plaintext
                        append matrix[row2][col1] TO plaintext
                RETURN plaintext
        """
        return pc

    ##########################################################################
    # ENCRYPT
    # TODO: ADD description
    ##########################################################################
    def encrypt(self, plaintext, password):
        ciphertext = ""
        
        matrix = self.generate_matrix(password.upper())
        message = self.separate_dup_chars(plaintext)
        ciphertext_list = self.playfair(message.upper(), matrix)

        for ele in ciphertext_list:
            ciphertext += ele

        return ciphertext

    # generates the matrix key used to encode the message
    def generate_matrix(self, password):
        key = password
        matrix = [[0 for i in range(5)] for j in range(5)]

        added_letters = []
        row_index = 0
        col_index = 0

        # add all letters from password to matrix
        for letter in key:
            if letter not in added_letters:
                matrix[row_index][col_index] = letter
                added_letters.append(letter)
                row_index = row_index + 1 if col_index == 4 else row_index
                col_index = col_index + 1 if col_index != 4 else 0
            else:
                continue
            
        # find characters not yet added to the matrix
        remaining_letters = []
        for num in range(65, 91):
            if chr(num) == 'J':
                continue # J usually omitted from the 25 characters
            elif chr(num) not in added_letters:
                remaining_letters.append(chr(num))

        # add remaining characters to the matrix
        index = 0
        for i in range(5):
            for j in range(5):
                if matrix[i][j] != 0:
                    continue
                else:
                    matrix[i][j] = remaining_letters[index]
                    index += 1
        
        return matrix

    # break message elements into pairs to be encrypted by the key matrix
    def separate_dup_chars(self, plaintext):
        for index in range(0, len(plaintext) - 1, 2): # -1 to avoid memory errors
            if index < len(plaintext):
                if plaintext[index] == plaintext[index + 1]:
                    plaintext = plaintext[:index + 1] + "X" + plaintext[index + 1:]
        
        # if plaintext has odd num of characters, append an X at the end
        if len(plaintext) % 2 != 0:
            plaintext = plaintext[:] + "X"
        return plaintext

    # return index of current letter
    def return_index(self, letter, matrix):
        # remember: J is not part of the list
        if letter == 'J':
            letter = 'I'
        for row in range(5):
            for col in range(5):
                if matrix[row][col] == letter:
                    return (row, col)
    
    def playfair(self, message, matrix):
        ciphertext = []
        for index in range(0, len(message) - 1, 2):
            row1, col1 = 0, 0
            row2, col2 = 0, 0
            # don't reach into memory we don't have
            if index < len(message) + 1:
                row1, col1 = self.return_index(message[index], matrix)
                row2, col2 = self.return_index(message[index + 1], matrix)
            
            # If two letters are in the same row, replace them with values to the right
            if row1 == row2:
                ciphertext.append(matrix[row1][(col1 + 1) % 5])
                ciphertext.append(matrix[row2][(col2 + 1) % 5])
            # If two letters are in the same column, replace them with values below
            elif col1 == col2:
                ciphertext.append(matrix[(row1 + 1) % 5][col1])
                ciphertext.append(matrix[(row2 + 1) % 5][col2])
            # If two letters are not in the same row or col, form a box and 
            # replace the values with those horizontally on the opposite side of the box
            else:
                ciphertext.append(matrix[row1][col2])
                ciphertext.append(matrix[row2][col1])
        return ciphertext
    
    ##########################################################################
    # DECRYPT
    # TODO: ADD description
    ##########################################################################
    def decrypt(self, ciphertext, password):
        # use the same matrix as above to decrypt the message
        plaintext = ""

        matrix = self.generate_matrix(password.upper())
        message = self.separate_dup_chars(ciphertext)
        plaintext_list = self.playfair_reverse(message.upper(), matrix)
        for ele in plaintext_list:
            plaintext += ele

        return plaintext

    # Identical process to playfair function, but reverse previous operations
    def playfair_reverse(self, message, matrix):
        plaintext = []
        for index in range(0, len(message) - 1, 2):
            row1, col1 = 0, 0
            row2, col2 = 0, 0
            # don't reach into memory we don't have
            if index < len(message):
                row1, col1 = self.return_index(message[index], matrix)
                row2, col2 = self.return_index(message[index + 1], matrix)
            
            # If two letters are in the same row, replace them with values to the left
            if row1 == row2:
                col1 = col1 - 1 if col1 > 0 else 4
                col2 = col2 - 1 if col2 > 0 else 4
                plaintext.append(matrix[row1][col1])
                plaintext.append(matrix[row2][col2])
            # If two letters are in the same column, replace them with values above
            elif col1 == col2:
                row1 = row1 - 1 if row1 > 0 else 4
                row2 = row2 - 1 if row2 > 0 else 4
                plaintext.append(matrix[row1][col1])
                plaintext.append(matrix[row2][col2])
            # If two letters are not in the same row or col, form a box and 
            # replace the values with those horizontally on the opposite side of the box
            else:
                plaintext.append(matrix[row1][col2])
                plaintext.append(matrix[row2][col1])
        return plaintext