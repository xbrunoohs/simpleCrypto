#setting the encrypt matrix
ENCRYPT_TABLE = [[1, 2], [1, 3]]

#inicializing the decryption matrix
DECRYPT_TABLE = [[0, 0], [0, 0]]

#computing the inverted matrix
def invert_matrix() -> None:
    determinant = 1 / ((ENCRYPT_TABLE[0][0] * ENCRYPT_TABLE[1][1]) - (ENCRYPT_TABLE[0][1] * ENCRYPT_TABLE[1][0]))
    DECRYPT_TABLE[0][0] = int(determinant * ENCRYPT_TABLE[1][1])
    DECRYPT_TABLE[0][1] = int(-(determinant * ENCRYPT_TABLE[0][1]))
    DECRYPT_TABLE[1][0] = int(-(determinant * ENCRYPT_TABLE[1][0]))
    DECRYPT_TABLE[1][1] = int(determinant * ENCRYPT_TABLE[0][0])

#multiplying the matrix by a vector of dimention 2 
def multiply_matrix(vec: list[int], mat: list[list[int]]) -> list[int]:
    result = [0, 0]
    result[0] = mat[0][0] * vec[0] + mat[0][1] * vec[1]
    result[1] = mat[1][0] * vec[0] + mat[1][1] * vec[1]
    return result

#function to encrypt the message
def encrypt(s: str) -> str:
    buffer = str()
    for i in range(0, len(s), 2):
        vec1 = ord(s[i])
        vec2 = 0
        if (i + 1) < len(s):
            vec2 = ord(s[i + 1])
        result = multiply_matrix([vec1, vec2], ENCRYPT_TABLE)
        buffer += str(result[0]) + " " + str(result[1]) + " "
    return buffer

#function to decrypt the message
def decod(s: str) -> str:
    s = s.split()
    buffer = str()
    for i in range(0, len(s), 2):
        vec1 = int(s[i])
        vec2 = int(s[i + 1])
        result = multiply_matrix([vec1, vec2], DECRYPT_TABLE)
        buffer += str(chr(result[0])) + str(chr(result[1]))
    return buffer

#messages to test the application
def frase(s: str) -> None:
    print("Building cypher matrixes...")
    invert_matrix()
    print("String to be encrypted: " + s)
    frasecod = encrypt(s)
    print("Encrypted string: " + frasecod)
    print("Running decrypted function...")
    print(decod(frasecod))

#test to run the 
if __name__ == "__main__":
    frase("ESTUDAR PARA TRANSFORMAR O MUNDO!")
