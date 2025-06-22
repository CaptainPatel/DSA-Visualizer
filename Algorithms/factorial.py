from graphviz import Digraph

def factorial(n):
    # to create a graph object named ....
    graph = Digraph(comment='Factorial Recursion Tree')
    graph.attr(rankdir='TB', bgcolor='white')  # Top to Bottom layout

    # this is the main recursive func
    def add_nodes(curr):
        # base case
        if curr == 0 or curr == 1:
            label = f"{curr}! = 1" # 0! = 1  /  1! = 1
            # first parameter is the node name
            graph.node(str(curr), label=label, shape='box', style='filled', color='lightgreen', fontname='Helvetica')
            return 1
        else:
            label = f"{curr}! = {curr} * ({curr-1})!"
            graph.node(str(curr), label=label, shape='ellipse', style='filled', color='lightblue', fontname='Helvetica')
            graph.edge(str(curr), str(curr - 1), color='gray', style='dashed')
            return curr * add_nodes(curr - 1)

    result = add_nodes(n)
    #cleanup = true to remove any intermediate products like dot files
    graph.render('factorial_graph', format='png', view=True, cleanup=True)

    return result, graph