strings = ['ab', 'ab','abc']
queries = ['ab', 'abc', 'bc']
count = []

def matchingStrings(strings, queries):
    # Write your code here
    for string in queries:
        # counting queries in strings
        list = strings.count(string)
        # append list to count
        count.append(list)
    # print count items each on a seperate line
    for x in count:
        print(x)


matchingStrings(strings, queries)
            