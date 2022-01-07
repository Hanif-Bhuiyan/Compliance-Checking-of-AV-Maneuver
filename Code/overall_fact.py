

overall_true_atom = []
overall_false_atom = []
overall_action = []


class overall_mapping_for_atom:

    def overall_mapping_true(self, true_atom_list):

        self.true_atom_list = true_atom_list

        for atom in true_atom_list:
            if atom not in overall_true_atom:  # not a duplicate
                overall_true_atom.append(atom)

        return overall_true_atom
        overall_true_atom.clear()

    def overall_mapping_false(self, false_atom_list):

        self.false_atom_list = false_atom_list


        for atom in false_atom_list:
            if atom not in overall_false_atom:  # not a duplicate
                overall_false_atom.append(atom)

        return overall_false_atom
        overall_false_atom.clear()

    def overall_mapping_illegal_action(self, illegal_action_list):

        self.illegal_action_list = illegal_action_list

#        print("From overall fact")

        for action in illegal_action_list:
            #print(action)
            if action not in overall_action:  # not a duplicate
                overall_action.append(action)

        #print()
        #print(overall_action)
        return overall_action
        overall_action.clear()