def factor(n, m):
    if (n == 0 or m == 0):
        return 0, 0

    if (n > 0 and m > 0):
        x1 = 1
        x2 = n - x1

        while (x2 > x1):
            if x1 * x2 == m:
                return x1, x2
            x1 += 1
            x2 = n - x1

    elif (n > 0 and m < 0):
        x1 = 0
        x2 = n
        r = 0

        while(r >= m):
            r = x1 * x2
            if r == m:
                return x1, x2
            x1 -= 1
            x2 += 1

            

    elif (n < 0 and m > 0):
        
        x2 = -1
        x1 = n - x2

        while (x2 >= x1):
            if (x1 * x2 == m):
                return x1, x2
            x2 -= 1
            x1 = n - x2
    elif (n < 0 and m < 0):
        x2 = 1
        x1 = n - x2
        

        while (x1 * x2 <= m):

            if ((x1 * x2) == m):
                return x1, x2
            x2 += 1
            x1 = n - x2


    
    return 0, 0



# For n > 0, m > 0
assert factor(6, 5) == (1, 5)
assert factor(6, 8) == (2, 4)

# For n > 0, m < 0
assert factor(5, -6) == (-1, 6)
assert factor(5, -14) == (-2, 7) 


# For n < 0, m > 0
assert factor(-4, 3) == (-3, -1)
assert factor(-6, 9) == (-3, -3)


# for n < 0, m < 0

assert factor(-6, 5) == (-5, -1)
assert factor(-4, 3) == (-3, -1)
assert factor(-4, 4) == (-2, -2)
assert factor(-6, 8) == (-4, -2)
assert factor(-6, 9) == (-3, -3)