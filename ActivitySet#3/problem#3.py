
class Palindrome:
    def __init__(self, w: str):
        self.w = w
        self.palindromes = []
        self.find_palindromes()
    
    @staticmethod
    def is_palindrome(s: str):
        if False in (s[i] == s[j] for i, j in zip(range(0, len(s) // 2), range(len(s) - 1, len(s) // 2 - 1, -1))):
            return False
        return True
    
    def find_palindromes(self):
        i = 0
        j = 2
        l = len(self.w)
        while i <  l - 2:
            if Palindrome.is_palindrome(tmp := self.w[i: j + 1]):
                self.palindromes.append((i + 1, tmp))
            j += 1
            
            if j == l:
                i += 1
                j = i + 2
    

def input_pdromes():
    while True:
        try:
            n = int(input())
            assert n > 0
            break
        except:
            print("Enter a valid integer greater than 0")
            continue
        
    pdromes = []    
    for _ in range(n):
        while True:
            try:
                m = int(input())
                assert m > 0
                break
            except:
                print("Enter a valid length for the string")
                continue
            
        while True:
            s = input().strip()
            if len(s) != m:
                print("Length of the string should match")
                continue
            pdromes.append(Palindrome(s))
            break
    return pdromes
            
            
def output(pdromes):
    print('\n')
    for pdrome in pdromes:
        print(pdrome.w)
        for i, p in pdrome.palindromes:
            print(i, p)
        print("\n")
                
                
def main():
    pdromes = input_pdromes()
    output(pdromes)

if __name__ == "__main__":
    main()                