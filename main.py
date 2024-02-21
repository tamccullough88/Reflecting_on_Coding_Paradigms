'''
Implement a function that will flatten and sort an array of integers in ascending order, and which adheres to a functional programming paradigm.
'''
array = ["5","7","3","4","2","9","0","1","6"]

# function to flatten the sorted items. 
def flatten_and_sort(a):
    new_array = []
    for item in a:
        for i in item:
            new_array.append(i)
    return sorted(new_array)

print(flatten_and_sort(array))

'''
How does this solution ensure data immutability?
It does not since an array can be updated at any time. 


Is this solution a pure function? Why or why not? 
No, this function changes the array from it's original state. 

Is this solution a higher order function? Why or why not?
yes, it takes in the "sorted()" function as an argument

Would it have been easier to solve this problem using a different programming style?
Maybe. We could have tried to solve it with a lambda function. 

Why in particular is functional programming a helpful paradigm when solving this problem?
we created the solution using the code using a function

'''

#I accidently did this first, even after reading the prompt and seeing array and not dictionary. I went ahead and left it for you to check over and see if I did it right. Thank you!

'''
Implement a function that will flatten and sort an array of integers in ascending order, and which adheres to a functional programming paradigm.
'''
item = {'c': 1, 'b': {'y': 2, 'x': 3}, 'a': 4}


# function to flatten the sorted items. 
def flatten_and_sort(a):
    result = dict()
    for i in a.keys():
        if type(a[i]) == dict:
            for k,v in a[i].items():
                new_key = i + "." + k
                result[new_key] = v
                
        else: 
            result[i] = a[i]

    sort_items = {key: val for key, val in sorted(result.items(), key = lambda ele: ele[0])}
    return sort_items

print(flatten_and_sort(item))

