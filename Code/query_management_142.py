from owlready2 import *
import os
import math
from query_check_for_av_b import *
from query_check_for_av_e import *
from safe_distance02 import *

from safety_border_check import *
from primary_checking_of_av_tv_position import *
primary_checking = primary_checking_of_av_tv()
safety_border_tv = safety_border_check_for_target_vehicle()


true_atom = []
false_atom = []
violate_action = []

qb = query_behaviour()
qe = query_environment()

class query_mapping_142:

    def mapping_142(self, atom_check, atom_filename, av, tv, av_lane, tv_lane, flag_142):

        print("From Rule 142")

        self.atom_check = atom_check
        self.atom_filename = atom_filename
        self.av= av
        self.tv=tv
        self.av_lane = av_lane
        self.tv_lane = tv_lane
        self.flag_142 = flag_142

        true_atom.clear()
        false_atom.clear()

        def modify(a):
            answer3 = float(a)
            answer4 = round(answer3, 1)
            return answer4

        def query_triggering(q_d1, q_d2, at, a_n, a_v, t_v):

            list_of_answer = []

            for sparql_query_file in q_d2:
                sparql_check = os.path.join(q_d1, sparql_query_file)

                atom_name_for_matching = a_n + "_"

                if (sparql_query_file.startswith(atom_name_for_matching)):
                    for sparql_line in open(sparql_check, "r"):
                        sparql_line.strip()
                        #print(sparql_line)




                    ## Now have to trigger the query in ontology with vehicle name

                    query_for_which_vehicle = t_v

                    if ("ab" in sparql_line):
                        if ("vehicle" in at):
                            answer = qb.query_trigger_for_behaviour(sparql_line, query_for_which_vehicle)
                            answer2 = modify(answer[0])
                        else:
                            answer = qb.query_trigger_for_behaviour(sparql_line, a_v)
                            answer2 = modify(answer[0])
                    elif ("ae" in sparql_line):
                        answer = qe.query_trigger_for_environment(sparql_line)
                        answer2 = modify(answer[0])
                        # print(answer2)
                    else:
                        print("answer could not found for this query")

                    list_of_answer.append(answer2)
            return list_of_answer
            # print(list_of_answer)


        def driver_OvertakeToTheRightOf_vehicle(at, which_av, which_tv, which_av_lane, which_tv_lane): #142_1

            av_behind_tv = tv_ahead_of_av.tv_distance(which_av, which_tv)

            if (which_av_lane == which_tv_lane and av_behind_tv):

                sdc = safe_distance_check()
                safe_distance = sdc.safety(which_av, which_tv)

                if (safe_distance):

                    true_atom.append(at)

                else:

                    false_atom.append(at)
                    print(at)
            else:

                true_atom.append(at)


        def vehicle_IsTurningRight(q_d1, q_d2, at, a_n, a_v, t_v):  # 142_2
            list_of_answer = []
            list_of_answer = query_triggering(q_d1, q_d2, at, a_n, a_v, t_v)
            #print(list_of_answer)
            #if (list_of_answer[0] == 1.0 and list_of_answer[1] == list_of_answer[2]):
            #if (list_of_answer[0] == 1.0):
            if (list_of_answer[0] == 1.0 and ((list_of_answer[1] == list_of_answer[2]) or (list_of_answer[1] == list_of_answer[2] - 1.0)) and list_of_answer[3] == 1):

                true_atom.append(at)
                violate_action.append("Target Vehicle intended to turn right")
            else:

                false_atom.append(at)
                print(at)

        def vehicle_IsGivingRightChangeOfDirectionSignal(q_d1, q_d2, at,a_n, a_v, t_v): #142_3
            list_of_answer = []
            list_of_answer = query_triggering(q_d1, q_d2, at, a_n, a_v, t_v)
            #print(list_of_answer)
            if (list_of_answer[0] == 1.0):

                true_atom.append(at)
                violate_action.append("Target Vehicle intended to go right")
            else:

                false_atom.append(at)
                print(at)

        def vehicle_IsMakingUturn(q_d1, q_d2, at,a_n, a_v, t_v): #142_4
            list_of_answer = []
            list_of_answer = query_triggering(q_d1, q_d2, at, a_n, a_v, t_v)
            #print(list_of_answer)
            #if (list_of_answer[0] == list_of_answer[1] and list_of_answer[2] == 1):
            #if (list_of_answer[2] == 1.0 and (list_of_answer[1] == list_of_answer[0] or list_of_answer[1] == list_of_answer[0] - 1.0)):
            if (list_of_answer[2] == 1.0 and (list_of_answer[1] == list_of_answer[0] or list_of_answer[1] == list_of_answer[0] - 1.0) and list_of_answer[3] == 1):

                true_atom.append(at)
                violate_action.append("Target Vehicle intended to make U-Turn")
            else:

                false_atom.append(at)
                print(at)


        def vehicle_IsOn_centreOfRoad(q_d1, q_d2, at,a_n, a_v, t_v): #142_5
            list_of_answer = []
            list_of_answer = query_triggering(q_d1, q_d2, at, a_n, a_v, t_v)
            #print("Information for vehicle is on center of road, total lane, target vehicle lane number",list_of_answer)
            #if(list_of_answer[1] > math.ceil(list_of_answer[1]/list_of_answer[0]) and list_of_answer[0] > math.ceil(list_of_answer[1]/list_of_answer[0])):
            if ((list_of_answer[1] >= math.floor(list_of_answer[0] / list_of_answer[1])) and (list_of_answer[1] < list_of_answer[0])):
                true_atom.append(at)
            else:
                false_atom.append(at)
                print(at)


        for line in open(self.atom_check, "r"): ## Now start reading inside of every line of file (c, r_142, ...), first start reading c file
            line.strip()
            atom_name1 = line.split(":")
            atom_name = atom_name1[0] # c_1
            #print(atom_name)
            atom = atom_name1[-1] #vehicle_IsTurningLeft
            #print(atom)

            # Now based on atom, reading queries

            query_dir = "C:/Users/bhuiyanh/PycharmProjects/Code-Complaince-Checking/query/"  # query path
            query_dir1 = query_dir + self.atom_filename  # now based on atom, making query path to find queries
            #print(query_dir1)

            query_dir2 = os.listdir(query_dir1)  # in this query how many query files, it is reading all
            #print(query_dir2)

            # For rule 142
            '''
            if (self.flag_142 == 0):

                prinmary_check = primary_checking.checking_of_av_tv(self.av, self.tv)

                safety_of_primary_check = safety_border_tv.safety_check_for_target_vehicle(self.tv)

                if (prinmary_check >= safety_of_primary_check):
                    self.flag_142 == 1

            # if (self.flag_140 == 1 or prinmary_check >= safety_of_primary_check):
            
            '''

            if (self.flag_142 == 1):

                true_atom.append("driver_OvertakeToTheRightOf_vehicle")
                false_atom.append("vehicle_IsTurningRight")
                false_atom.append("vehicle_IsGivingRightChangeOfDirectionSignal")
                false_atom.append("vehicle_IsMakingUturn")
                true_atom.append("vehicle_IsOn_centreOfRoad")

            else:

                if ("driver_OvertakeToTheRightOf_vehicle" in line):  #142_1
                    driver_OvertakeToTheRightOf_vehicle(atom, self.av, self.tv, self.av_lane, self.tv_lane)

                if ("vehicle_IsTurningRight" in line): #142_2
                    vehicle_IsTurningRight(query_dir1, query_dir2, atom, atom_name, self.av, self.tv)

                if ("vehicle_IsGivingRightChangeOfDirectionSignal" in line):  #142_3
                    vehicle_IsGivingRightChangeOfDirectionSignal(query_dir1, query_dir2, atom, atom_name, self.av, self.tv)

                if ("vehicle_IsMakingUturn" in line):  #142_4
                    vehicle_IsMakingUturn(query_dir1, query_dir2, atom, atom_name, self.av, self.tv)

                if ("vehicle_IsOn_centreOfRoad" in line):  #142_5
                    vehicle_IsOn_centreOfRoad(query_dir1, query_dir2, atom, atom_name, self.av, self.tv)


        converted_list_true_fact = []
        converted_list_true_fact.clear()

        for element in true_atom:
            converted_list_true_fact.append(element.strip())

        converted_list_false_fact = []
        converted_list_false_fact.clear()

        for element in false_atom:
            converted_list_false_fact.append(element.strip())

        return converted_list_true_fact, converted_list_false_fact, violate_action
