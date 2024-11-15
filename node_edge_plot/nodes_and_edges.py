#%%
from pyvis_plotter import create_interactive_network_html



# node: (name, color, size, shape)
def make_node(name, color = (128, 128, 128), size = 15, shape = "dot"):
    return((name, color, size, shape))

nodes = [
    make_node("Hungry Ghost"),
    make_node("Rat"),
    make_node("Farmer"),
    make_node("Warrior"),
    make_node("King"),
    make_node("Deity"),
    make_node("Potato Plant", (0, 180, 0), 10, "triangle"),
    make_node("Potato", (128, 128, 0), 10, "triangle"),
    make_node("Gold", (200, 200, 0), 10, "triangle"),
    make_node("Water", (0, 0, 255), 10, "triangle")]



# edge: (source, destination, color, width, arrows, length, label)
def make_edge(source, destination, color = "black", width = 3, arrows = None, length = 500, label = ""):
    return((source, destination, color, width, arrows, length, label))


edges = [
    make_edge("Hungry Ghost", "Rat", label = 
"""H (+1) eats R (+1)"""),
    
    make_edge("Hungry Ghost", "Gold", label = 
"""H (+1) eats G"""),
    
    
    
    make_edge("Rat", "Potato", label = 
"""R (-1) takes P"""),

    make_edge("Rat", "Rat", length = 150, label = 
"""R (+1) gives P to hurt R"""),
    
    
    
    make_edge("Farmer", "Potato Plant", label = 
"""F (+1) gives Wa to PP"""),
    
    make_edge("Farmer", "Rat", label = 
"""F (-1) hits R"""),
    
    
    
    make_edge("Warrior", "Farmer", label = 
"""W (+1) hits off-color F
W (-1) hits on-color F"""),    
    
    
    
    make_edge("King", "Warrior", label = 
"""K (+1) contains W (+1)"""),
    
    ]

create_interactive_network_html(nodes, edges, "samsara_characters.html")

# %%
