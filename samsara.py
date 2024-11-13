#%% 



# For now, no player-character or non-player-characters.
pc = None 
npcs = [None, None, None]



# An action has a name, a list of input names, and a list of requirement functions.
class Action:
    def __init__(self, 
                 name,                                  # Name of action, like 'eat_northern_object'.
                 input_names = [],                      # Names of inputs, like ['character', 'item'].
                 get_inputs=lambda character: {'character': character}, # Function which gets inputs based on character.
                                                        # Ex: If the action is 'eat_northern_object', the 'item' is the object one space to the north. 
                 requirement_funcs=[],                  # Functions which judge action's validity and maybe changing the action.  
                 perform_func=lambda character, inputs: None): # Function which performs action.         
        self.name = name
        input_names.sort()
        self.input_names = input_names
        self.get_inputs = get_inputs
        self.requirement_funcs = requirement_funcs
        self.perform_func = perform_func

    # Check if character and inputs are valid with this action. If not, return resulting action, maybe None. 
    def check_requirements(self, character, inputs):
        # If inputs do not match input_names, invalid action, so no action performed.
        input_keys = list(inputs.keys())
        input_keys.sort()
        if(input_keys != self.input_names):
            return(None, True)
        # Check if character and inputs satisfy requirements.
        valid = True                                                # Assume valid.
        for requirement_func in self.requirement_funcs:             # For each requirement...
            action, valid = requirement_func(character, inputs)     # see if valid.
            if(not valid):                                          # If not valid...
                return(action, valid)                               # another action may arise. Ex: action 'eat_norther_object' with item 'rock' may return 'choke' action. 
        return(action, valid)
    


# Some examples of actions and corresponding keys.
action_keys = {
    'w' : Action('go_up', input_names = ['character']), 
    'a' : Action('go_left', input_names = ['character']),
    's' : Action('go_down', input_names = ['character']),
    'd' : Action('go_right', input_names = ['character']),
    'e' : Action('eat_this', input_names = ['character', 'this'])
}



# Non-player-characters choose keys to perform actions. 
def get_keys(npc):
    return(None)



# Given a character and pressed keys, try performing a corresponding action. 
def do_action(character, keys):
    action = None                                       # Assume no action.
    for valid_keys, this_action in action_keys.items(): # Iterate over possible keys.
        if(keys == valid_keys):                         # If keys are valid...
            action = this_action                        # Select that action.
            break
    if(action == None):                                 # If no action, stop.
        return 
    
    valid = False                                       # If there is an action, assume action is invalid. 
    while(not valid):                                   # Loop until valid action found (maybe no action)
        inputs = action.get_inputs(character)           # Get inputs based on character.
        action, valid = \
            action.check_requirements(character, inputs)# If action valid, stop. If invalid, check validity of resulting action (maybe no action).
    if(action == None):                                 # If no action valid, stop.
        return 
    action.perform(character, inputs)                   # Perform the action.
        
    
    
# In each step, the actions of the player and all npcs are performed.
def one_step():
    pc_keys = None                  # Replace this with something finding player key-presses. 
    do_action(pc, pc_keys)          # Do corresponding action.
    for npc in npcs:                # For each non-player-character...
        npc_keys = get_keys(npc)    # Find what 'keys' are pressed
        do_action(npc, npc_keys)    # and perform the corresponding action.
        
        
        
if __name__ == "__main__":
    for i in range(100):
        one_step()



# %%


