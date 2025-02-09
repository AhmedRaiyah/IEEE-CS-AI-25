
def common_elements(set1, set2):
    result = set()

    for element in set1:
        if element in set2:
            result.add(element) 
        
    return result


set_a = set(map(int, input().split()))
set_b = set(map(int, input().split()))

print(common_elements(set_a, set_b))
