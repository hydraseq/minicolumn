from minicolumn import MiniColumn

source_files = ['example.0.txt', 'example.1.txt', 'example.2.txt']
data_dir = 'dexample'
mcol = MiniColumn(source_files, data_dir)


def get_successors(tree, node, level):
    #print("level:", level)
    if level < -len(tree):
        #print("returning nada")
        return []
    return tree[level][node['start']:node['end']]

def process_sentence(sentence):
    trees = mcol.evaluate(sentence)
    
    def print_tree(tree1):
        snodes =  tree1[-1][0]
        
        runnodes = snodes[:]
        
        def print_path(tree, node):
            fringe = []
            fringe.append(node)
            path = []
            level = -1 
            #print("init fringe", fringe)
            while fringe:
                cnode = fringe.pop()
                path.append(cnode)
                level -= 1
                for n in get_successors(tree1, cnode, level):
                    #print("n", n)
                    fringe.append(n)
            
            print("========")
            for n in path:
                if n['convo'][0].startswith('0_'):
                    print(n['convo'], n['words'])
                else:
                    print(n['convo'])
        
        for nn in runnodes:
            print_path(tree1, nn)
    
    for tree in trees:
        print_tree(tree)

process_sentence("start pomodoro")
