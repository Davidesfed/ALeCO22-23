from statespacetree import StateSpaceTree
from livenodeslist import LiveNodesList

def generate_permutations(symbols):
    tree = StateSpaceTree(len(symbols), symbols, mode="perm no rep")
    live_nodes = LiveNodesList(tree.root, strategy="FIFO")
    iteration = 0
    while not live_nodes.empty():
        e_node = live_nodes.select()
        new_nodes = tree.expand(e_node)
        for node in new_nodes:
            live_nodes.insert(node)
        iteration += 1
    return tree.get_leaves()

if __name__ == "__main__":
    print([str(x) for x in generate_permutations(["a", "b", "c"])])