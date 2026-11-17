class Solution:
    def numberToWords(self, num: int) -> str:
        digits = {
            0: "Zero",
            1: "One",
            2: "Two",
            3: "Three",
            4: "Four",
            5: "Five",
            6: "Six",
            7: "Seven",
            8: "Eight", 
            9: "Nine"
        }
        tens = {
            2: "Twenty",
            3: "Thirty",
            4: "Forty",
            5: "Fifty",
            6: "Sixty",
            7: "Seventy",
            8: "Eighty",
            9: "Ninety"
        }
        teens = {
            0: "Ten",
            1: "Eleven",
            2: "Twelve",
            3: "Thirteen",
            4: "Fourteen",
            5: "Fifteen",
            6: "Sixteen",
            7: "Seventeen",
            8: "Eighteen",
            9: "Nineteen"
        }
        big = {
            0: "Hundred",
            1: "Thousand",
            2: "Million",
            3: "Billion",
            4: "Trillion"
        }

        if num == 0:
            return digits[0]

        def formHundred(num):
            if int(num) == 0:
                return ""
            
            number = ""
            for ch in num:
                number = ch + number

            length = len(number)

            res = ""
            if int(number[0]) != 0:
                res = digits[int(number[0])]
            if length > 1 and int(number[1]) != 0:
                if int(number[1]) == 1:
                    res = teens[int(number[0])]
                else:
                    temp = res
                    res = tens[int(number[1])]
                    if temp:
                        res = res + " " + temp
            if length > 2 and int(number[2]) != 0:
                temp = res
                res = digits[int(number[2])] + " " + big[0]
                if temp:
                    res = res + " " + temp
            
            return res

        numStr = str(num)
        parts = []
        results = []

        for i in range(len(numStr)-1, -1, -3):
            if i-2 >= 0:
                parts.append(numStr[i-2:i+1])
            else:
                parts.append(numStr[0:i+1])

        for i in range(len(parts)):
            res = formHundred(parts[i])
            if res and res != digits[0] and i != 0:
                res = res + " " + big[i]
            results.append(res)

        finalRes = ""
        for res in results:
            if res != "":
                finalRes = res + " " + finalRes

        return finalRes.strip()