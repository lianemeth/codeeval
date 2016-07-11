import sys

ONE_TO_19 = ("", "One", "Two", "Three", "Four", "Five", "Six", "Seven",
"Eight", "Nine", "Ten", "Eleven", "Twelve", "Thirteen", "Fourteen", "Fifteen",
"Sixteen", "Seventeen", "Eighteen", "Nineteen")
TENS = ("Twenty", "Thirty", "Forty", "Fifty", "Sixty", "Seventy", "Eighty",
"Ninety")
LARGE_SCALE = ("Billion", "Million", "Thousand", "Hundred")

def small_value(n):
    if n <= 19:
        return ONE_TO_19[n]
    out = ""
    out += TENS[(n / 10) - 2]
    if n % 10:
        out += ONE_TO_19[n % 10]
    return out

def big_values(n):
    out = ""
    i = 0
    m = 1000000000
    while i < len(LARGE_SCALE):
        units = n / m
        n = n % m
        if units > 0:
            if units >= 100:
                btext, _ = big_values(units)
                out += btext + LARGE_SCALE[i]
            else:
                out += small_value(units) + LARGE_SCALE[i]
        i += 1
        if m > 1000:
            m = m / 1000
        else:
            m = 100
    return out, n 

def convert_to_text(n):
    if n == 0:
        return "ZeroDollars"
    if n == 1:
        return "OneDollar"
    big_number, m = big_values(n)
    small_number =  small_value(m)
    return big_number + small_number + "Dollars"

if __name__ == "__main__":
    with open(sys.argv[1], 'r') as test_cases:
        for test in test_cases:
            n = int(test.replace("/n",""))
            print convert_to_text(n)

