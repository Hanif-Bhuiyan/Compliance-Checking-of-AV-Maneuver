from overall_fact import *


fully_final_illegal_action = ['Target Vehicle intended to go right', 'Target vehicle had do not overtake sign', 'safe distance from target vehicle', 'safe distance from other vehicles', 'not clear view of approaching traffic', 'Target vehicle intended to turn right', 'Target vehicle intended to make U-Turn', 'Target Vehicle intended to turn right', 'Target Vehicle intended to make U-Turn']
b = []

of = overall_mapping_for_atom()

if("Target vehicle intended to turn right" or "Target Vehicle intended to make U-Turn" in fully_final_illegal_action):
    for i, item in enumerate(fully_final_illegal_action):
        if (item == "Target Vehicle intended to make U-Turn" or item == "Target Vehicle intended to go right"):
            fully_final_illegal_action[i] = "Target vehicle intended to turn right"

b = of.overall_mapping_illegal_action(fully_final_illegal_action)

print(b)