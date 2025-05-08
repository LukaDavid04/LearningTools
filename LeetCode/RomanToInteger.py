class Solution(object):
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        sum = 0
        special = ["I", "X", "C"] 
        # normal = ["V", "L", "D", "M"]
        # order = ["I", "V", "X", "L", "C", "D", "M"]
        # values = [1, 5, 10, 50, 100, 500, 1000]
        roman_dict = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000}
        for i in range(len(s)):
            if s[i] in special:
                if i + 1 != len(s):
                    if (s[i] == "I" and s[i + 1] == "V") or (s[i + 1] == "X" and s[i] == "I"):
                        add = roman_dict.get(s[i])
                        sum = sum - add
                    elif (s[i] == "X" and s[i + 1] == "L") or (s[i + 1] == "C" and s[i] == "X"):
                        add = roman_dict.get(s[i])
                        sum = sum - add
                    elif (s[i] == "C" and s[i + 1] == "D") or (s[i + 1] == "M" and s[i] == "C"):
                        add = roman_dict.get(s[i])
                        sum = sum - add
                    else:
                        add = roman_dict.get(s[i])
                        sum = sum + add 
                else:
                    add = roman_dict.get(s[i])
                    sum = sum + add 
            else:
                add = roman_dict.get(s[i])
                sum = sum + add
        return sum
    
s = Solution()
print(s.romanToInt("MCMXCIV"))