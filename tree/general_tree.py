# example pt 1
#
#           None             <--- parent = None (GPU is a root node)
#             |              
#           'GPU'            <--- data = 'GPU'
#           /   \
#       'Nvidia'   'AMD'     <--- children = ['Nvidia', 'AMD'] (data)

# example pt 2
#
#           'GPU'            <--- parent = 'GPU'
#             |
#           'Nvidia'         <--- data = 'Nvidia
#           /   \
#       '3060'  '1660 Super' <--- children = ['3060', '1660 Super']

class TreeNode:
    def __init__(self, data):
        self.data = data
        self.children = []
        self.parent = None

