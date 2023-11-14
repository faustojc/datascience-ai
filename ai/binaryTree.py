def generate_tree(arr):
    if not arr:
        return None
    
    mid = len(arr) // 2
    root = {'val': arr[mid], 'left': None, 'right': None}
    
    root['left'] = generate_tree(arr[:mid])
    root['right'] = generate_tree(arr[mid+1:])
    
    return root

def print_tree(root, level=0):
    if root:
        print_tree(root['right'], level+1)
        print(' ' * 4 * level + '->', root['val'])
        print_tree(root['left'], level+1)

arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
root = generate_tree(arr)

print_tree(root)

