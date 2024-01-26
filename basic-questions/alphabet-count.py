#input: "aaabbccdd"
#output: a3b2c3d2
# Program to count the no of alphabets and print the occurences with them


def alpha_count(str1):
    count = 1
    previous = str1[0] #set first char for comparing with the next
    new_str = ""
    
    for i in str1[1:]:
        if i == previous:
            count += 1
            previous = i
        else:
            new_str = new_str + previous + str(count)       #when a different char is found, 
                                                            #concat the previous char and its count, then reinitialise count 
            previous = i
            count = 1
            
    new_str = new_str + previous + str(count)
    print(new_str)

str1 = "aaabbccdd"
alpha_count(str1)
