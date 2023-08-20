"""Reverse words in an Array"""
class Solution:
    def reverseWords(self, s):
        words = s.split(' ')
        reversed_words = []
        for word in words:
            word1=word[::-1]
            reversed_words.append(word1)
        reversed_sentence = ' '.join(reversed_words)
        print(reversed_sentence)

obj = Solution()
obj.reverseWords("i like this program very much")
