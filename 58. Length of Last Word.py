def lengthOfLastWord(s: str) -> int:
        words = s.split()
        return len(words[len(words)-1])

print(lengthOfLastWord("Hello World"))                
                
