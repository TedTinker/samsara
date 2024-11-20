#%%
from pyvis_plotter import create_interactive_network_html



# node: (name, color, size, shape)
def make_node(name, color = (128, 128, 128), size = 15, shape = "dot"):
    return((name, color, size, shape))

nodes = [
    make_node("Anything", size = 25, shape = "square"),     # A, any other characters
    make_node("Hungry Ghost"),                              # H, large character which eats anything
    make_node("Rat"),                                       # R, small character which eats potato
    make_node("Farmer"),                                    # F, character which grows potatoes
    make_node("Warrior"),                                   # W. character which fights
    make_node("King"),                                      # K, giant character which collects gold for deities
    make_node("Deity"),                                     # D, giant character which makes gold into weather
    make_node("Potato Plant", (0, 180, 0), 10, "triangle"), # PP, object which makes potatoes when given water
    make_node("Potato", (128, 128, 0), 10, "triangle"),     # P, object which gives health
    make_node("Gold", (200, 200, 0), 10, "triangle"),       # G, object to flow up to deity or to hungry ghost
    make_node("Water", (0, 0, 255), 10, "triangle")]        # Wa, object which makes potato plants make potatoes



# edge: (source, destination, color, width, arrows, length, label)
# label: "character (karma impact) action/object/character (karma impact)/etc"
# karma impact: + for good karma, - for bad karma
def make_edge(source, destination, color = "black", width = 3, arrows = None, length = 300, label = ""):
    return((source, destination, color, width, arrows, length, label))


edges = [
    
    make_edge("Anything", "Anything", length = 150, label = 
"""A (-1) hits on-color A"""),
    
    make_edge("Anything", "Hungry Ghost", label = 
"""A (+1) gives G to H
H (-1) eats A except G or R"""),
    
#    make_edge("Anything", "Rat", label = 
#""" """),
    
    make_edge("Anything", "Farmer", label = 
"""F (-1) hits A except R"""),
    
#    make_edge("Anything", "Warrior", label = 
#""" """),

#    make_edge("Anything", "King", label = 
#""" """),

#    make_edge("Anything", "Deity", label = 
#""" """),
    
    
    
    make_edge("Hungry Ghost", "Gold", label = 
"""H (+1) eats G"""),
    
#    make_edge("Hungry Ghost", "Hungry Ghost", length = 150, label = 
#""" """),
    
    make_edge("Hungry Ghost", "Rat", label = 
"""H (+1) eats R (+1)"""),
    
#    make_edge("Hungry Ghost", "Farmer", label = 
#""" """),

#    make_edge("Hungry Ghost", "Warrior", label = 
#""" """),

#    make_edge("Hungry Ghost", "King", label = 
#""" """),

#    make_edge("Hungry Ghost", "Deity", label = 
#""" """),
    
    
    
    make_edge("Rat", "Potato", label = 
"""R (-1) takes P"""),

    make_edge("Rat", "Rat", length = 150, label = 
"""R (+1) gives P to injured R"""),

    make_edge("Rat", "Farmer", label = 
"""F (-1) hits R wo P
F (+1) hits R w P"""),

    make_edge("Rat", "Warrior", label = 
"""W (+1) hits R"""),

#    make_edge("Rat", "King", label = 
#""" """),

    make_edge("Rat", "Deity", label = 
"""D (-1) contains R"""),
    
    
    
    make_edge("Farmer", "Potato Plant", label = 
"""F (+1) gives Wa to PP"""),
    
    make_edge("Farmer", "Farmer", length = 150, label = 
"""F (+1) gives P to injured on-color F
F (+1) gives P to on-color W"""),
    
    make_edge("Farmer", "Warrior", label = 
"""W (+1) hits off-color F"""),

#    make_edge("Farmer", "King", label = 
#""" """),

#    make_edge("Farmer", "Deity", label = 
#""" """),
    

    
    make_edge("Warrior", "Warrior", length = 150, label = 
"""W (+1) hits off-color W
W (-1) hits on-color W"""),    
    
    make_edge("Warrior", "King", label = 
"""K (+1) contains on-color W (+1)
W (+1) gives G to on-color K"""),

#    make_edge("Warrior", "Deity", label = 
#""" """),
    
    
    
#    make_edge("King", "King", length = 150, label = 
#""" """),
    
    make_edge("King", "Deity", label = 
"""K (+1) gives G to on-color D"""),
    
    
    
    make_edge("Deity", "Potato Plant", label = 
"""D (+1) contains PP"""),
    
    make_edge("Deity", "Water", label = 
"""D (+1) contains W"""),
    
#    make_edge("Deity", "Deity", length = 150, label = 
#""" """),
    
    ]

create_interactive_network_html(nodes, edges, "samsara_characters.html")

# %%
