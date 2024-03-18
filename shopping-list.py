def add_item_to_list(item, list):
    list.append(item)
    return list
my_list = ['apple', 'banana', 'cherry']
add_item_to_list('dragonfruit', my_list)
print(my_list)  # Output: ['apple', 'banana', 'cherry', 'dragonfruit']

def remove_item(item,list):
    if item in list:
        list.remove(item)
my_list = [ 'apple', 'banana', 'cherry']
remove_item('apple', my_list)
print(my_list)

