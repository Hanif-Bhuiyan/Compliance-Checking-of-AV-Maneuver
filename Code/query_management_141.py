from owlready2 import *
import os
import math
from query_check_for_av_b import *
from query_check_for_av_e import *
from primary_checking_of_av_tv_position import *
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

tv_ahead_of_av = tv_availability()
primary_checking = primary_checking_of_av_tv()

class query_mapping_141:

    def mapping_141(self, atom_check, atom_filename, av, tv, av_lane, tv_lane, flag_141):

        print("From Rule 141")

        self.atom_check = atom_check
        self.atom_filename = atom_filename
        self.av= av
        self.tv=tv
        self.av_lane = av_lane
        self.tv_lane = tv_lane
        self.flag_141 = flag_141

        true_atom.clear()
        false_atom.clear()


        def modify(a):
            answer3 = float(a)
            answer4 = round(answer3, 1)
            return answer4

        def query_triggering(q_d1, q_d2, at, a_n, a_v, t_v):

            list_of_answer = []

            #print(q_d1)
            #print(q_d2)

            for sparql_query_file in q_d2:
                sparql_check = os.path.join(q_d1, sparql_query_file)
                #print(sparql_check)

                atom_name_for_matching = a_n + "_"

                if (sparql_query_file.startswith(atom_name_for_matching)):
                    for sparql_line in open(sparql_check, "r"):
                        sparql_line.strip()
                        #print(atom_name_for_matching)
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


        def driver_Of_bicyle(q_d1, q_d2, at,a_n, a_v, t_v): #141_1

            #list_of_answer = [at]
            false_atom.append(at)
            print(at)


        def driver_IsDrivingOn_MultiLaneRoad(q_d1, q_d2, at,a_n, a_v, t_v): #141_2
            list_of_answer = []
            list_of_answer = query_triggering(q_d1, q_d2, at, a_n, a_v, t_v)
            #print(list_of_answer)
            if (list_of_answer[0] > 1.0):

                true_atom.append(at)
            else:

                false_atom.append(at)
                print(at)

        def vehicle_CanBeSafelyOvertakenIn_markedLane(at, which_av, which_tv, which_av_lane, which_tv_lane): #141_3

            av_behind_tv = tv_ahead_of_av.tv_distance(which_av, which_tv)

            if (which_av_lane == which_tv_lane and av_behind_tv):

                sdc = safe_distance_check()
                safe_distance = sdc.safety(which_av, which_tv)

                if (safe_distance):

                    true_atom.append(at) #141_3
                    true_atom.append("IsSafeToOvertakeToTheLeftOf_vehicle")  # 141_7
                    true_atom.append("driver_OvertakeToTheLeftOf_vehicle")  # 141_13

                else:

                    false_atom.append(at)
                    print(at)
                    violate_action.append("safe distance from target vehicle")

            else:
                true_atom.append(at)  # 141_3
                true_atom.append("IsSafeToOvertakeToTheLeftOf_vehicle")  # 141_7
                true_atom.append("driver_OvertakeToTheLeftOf_vehicle")  # 141_13


        def markedLane_IsToTheLeftOf_vehicle(q_d1, q_d2, at,a_n, a_v, t_v): #141_4
            list_of_answer = []
            list_of_answer = query_triggering(q_d1, q_d2, at, a_n, a_v, t_v)
            #print("\n")
            #print(list_of_answer[0])
            #print(list_of_answer[1])
            #print("\n")
            #if (list_of_answer[0] == 1.0 and list_of_answer[1] > 1.0 and list_of_answer[2] == 1.0):
            if (list_of_answer[0] == 1.0 and list_of_answer[1] > 1.0):

                true_atom.append(at)
            else:

                false_atom.append(at)
                print(at)


        '''
        def vehicle_IsTurningRight(q_d1, q_d2, at, a_n, a_v, t_v): #141_5
            list_of_answer = []
            list_of_answer = query_triggering(q_d1, q_d2, at, a_n, a_v, t_v)
            print(list_of_answer)
            #if (list_of_answer[0] == 1.0 and list_of_answer[1] == list_of_answer[2]):
            #print(list_of_answer[0])
            #rint(list_of_answer[1])
            #print(list_of_answer[2])
            #print(list_of_answer[3])

            if (list_of_answer[0] == 1.0 and ((list_of_answer[1] == list_of_answer[2]) or (list_of_answer[1] == list_of_answer[2] - 1.0)) and list_of_answer[3] == 1):
            #if (list_of_answer[0] == 1.0 and ((list_of_answer[1] == list_of_answer[2]) or (list_of_answer[2] - 1== list_of_answer[1])) and list_of_answer[3] == 1):
            #if (list_of_answer[0] == 1.0 and ((list_of_answer[1] == list_of_answer[2]) or (list_of_answer[1] == list_of_answer[2] - 1.0)) and list_of_answer[3] == 1):
            #if (((list_of_answer[0] == 1.0 and list_of_answer[3] == 1) and (list_of_answer[1] == list_of_answer[2])) or ((list_of_answer[0] == 1.0 and list_of_answer[3] == 1) and (list_of_answer[1] == list_of_answer[2] - 1.0))):

                true_atom.append(at)
            else:

                false_atom.append(at)
                print(at)
        '''
        def vehicle_IsTurningRight(q_d1, q_d2, at, a_n, a_v, t_v):  #141_5
            list_of_answer = []
            list_of_answer = query_triggering(q_d1, q_d2, at, a_n, a_v, t_v)

            if (list_of_answer[0] == 1.0 and ((list_of_answer[1] == list_of_answer[2]) or (list_of_answer[1] == list_of_answer[2] - 1.0)) and list_of_answer[3] == 1):

                true_atom.append(at)
                #violate_action.append("Target Vehicle intended to turn right")
            else:

                false_atom.append(at)
                print(at)
        def vehicle_IsGivingRightChangeOfDirectionSignal(q_d1, q_d2, at,a_n, a_v, t_v): #141_6
            list_of_answer = []
            list_of_answer = query_triggering(q_d1, q_d2, at, a_n, a_v, t_v)
            #print(list_of_answer)
            if (list_of_answer[0] == 1.0):

                true_atom.append(at)
            else:

                false_atom.append(at)
                print(at)

        def vehicle_IsMakingUturn(q_d1, q_d2, at,a_n, a_v, t_v): #141_8
            list_of_answer = []
            list_of_answer = query_triggering(q_d1, q_d2, at, a_n, a_v, t_v)
            #print(list_of_answer)
            if (list_of_answer[2] == 1.0 and (list_of_answer[1] == list_of_answer[0] or list_of_answer[1] == list_of_answer[0] - 1.0) and list_of_answer[3] == 1):

                true_atom.append(at)
            else:

                false_atom.append(at)
                print(at)

        def vehicle_IsOn_centreOfRoad(q_d1, q_d2, at,a_n, a_v, t_v): #141_9
            list_of_answer = []
            list_of_answer = query_triggering(q_d1, q_d2, at, a_n, a_v, t_v)
            #print("Information for vehicle is on center of road, total lane, target vehicle lane number",list_of_answer)
            #if((list_of_answer[1] > math.ceil(list_of_answer[1]/list_of_answer[0])) and (list_of_answer[0] > math.ceil(list_of_answer[1]/list_of_answer[0]))):
            if ((list_of_answer[1] >= math.floor(list_of_answer[0] / list_of_answer[1])) and (list_of_answer[1] < list_of_answer[0])):
                true_atom.append(at)
            else:
                false_atom.append(at)
                print(at)

        def vehicle_IsStationary(q_d1, q_d2, at,a_n, a_v, t_v): #141_10
            list_of_answer = []
            list_of_answer = query_triggering(q_d1, q_d2, at, a_n, a_v, t_v)
            #print("Vehicle is stationary")
            #print(list_of_answer)
            #print(list_of_answer)
            if (list_of_answer[0] == 0.0):

                true_atom.append(at)
            else:

                false_atom.append(at)
                print(at)

        def driver_IsLawfullyLaneFiltering(q_d1, q_d2, at,a_n, a_v, t_v): #141_11

            #list_of_answer = [at]
            false_atom.append("driver_IsLawfullyLaneFiltering")
            print(at)

        def driver_IsLawfullyEdgeFiltering(q_d1, q_d2, at,a_n, a_v, t_v): #141_12

            #list_of_answer = [at]
            false_atom.append("driver_IsLawfullyEdgeFiltering")
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

            # For rule 141

            '''
            if (self.flag_141 == 0 and self.safety_of_primary == 0):

                print("here")
                prinmary_check = primary_checking.checking_of_av_tv(self.av, self.tv)

                if (self.av_lane == self.tv_lane and prinmary_check):
                    self.safety_of_primary =1
                    safety_of_primary_check = safety_border_tv.safety_check_for_target_vehicle(self.tv)

                    print(prinmary_check)
                    print(safety_of_primary_check)

                    if (prinmary_check >= safety_of_primary_check):
                        self.flag_141 == 1
            '''

            # if (self.flag_140 == 1 or prinmary_check >= safety_of_primary_check):

            if (self.flag_141 == 1):

                false_atom.append("driver_Of_bicyle")
                true_atom.append("driver_IsDrivingOn_MultiLaneRoad")
                true_atom.append("vehicle_CanBeSafelyOvertakenIn_markedLane")
                true_atom.append("IsSafeToOvertakeToTheLeftOf_vehicle")
                true_atom.append("driver_OvertakeToTheLeftOf_vehicle")
                true_atom.append("markedLane_IsToTheLeftOf_vehicle")
                false_atom.append("vehicle_IsTurningRight")
                false_atom.append("vehicle_IsGivingRightChangeOfDirectionSignal")
                false_atom.append("vehicle_IsMakingUturn")
                true_atom.append("vehicle_IsOn_centreOfRoad")
                false_atom.append("vehicle_IsStationary")
                false_atom.append("driver_IsLawfullyLaneFiltering")
                false_atom.append("driver_IsLawfullyEdgeFiltering")

            else:

                if ("driver_Of_bicyle" in line):  #141_1
                    driver_Of_bicyle(query_dir1, query_dir2, atom, atom_name, self.av, self.tv)

                if ("driver_IsDrivingOn_MultiLaneRoad" in line):  #141_2
                    driver_IsDrivingOn_MultiLaneRoad(query_dir1, query_dir2, atom, atom_name, self.av, self.tv)

                if ("vehicle_CanBeSafelyOvertakenIn_markedLane" in line):  #141_3
                    vehicle_CanBeSafelyOvertakenIn_markedLane(atom, self.av, self.tv, self.av_lane, self.tv_lane)

                if ("markedLane_IsToTheLeftOf_vehicle" in line):  #141_4
                    markedLane_IsToTheLeftOf_vehicle(query_dir1, query_dir2, atom, atom_name, self.av, self.tv)

                if ("vehicle_IsTurningRight" in line): #141_5
                    vehicle_IsTurningRight(query_dir1, query_dir2, atom, atom_name, self.av, self.tv)

                if ("vehicle_IsGivingRightChangeOfDirectionSignal" in line):  #141_6
                    vehicle_IsGivingRightChangeOfDirectionSignal(query_dir1, query_dir2, atom, atom_name, self.av, self.tv)

                if ("vehicle_IsMakingUturn" in line):  #141_8
                    vehicle_IsMakingUturn(query_dir1, query_dir2, atom, atom_name, self.av, self.tv)

                if ("vehicle_IsOn_centreOfRoad" in line):  #141_9
                    vehicle_IsOn_centreOfRoad(query_dir1, query_dir2, atom, atom_name, self.av, self.tv)

                if ("vehicle_IsStationary" in line):  #141_10
                    vehicle_IsStationary(query_dir1, query_dir2, atom, atom_name, self.av, self.tv)

                if ("driver_IsLawfullyLaneFiltering" in line):  #141_11
                    driver_IsLawfullyLaneFiltering(query_dir1, query_dir2, atom, atom_name, self.av, self.tv)

                if ("driver_IsLawfullyEdgeFiltering" in line):  #141_12
                    driver_IsLawfullyEdgeFiltering(query_dir1, query_dir2, atom, atom_name, self.av, self.tv)


        converted_list_true_fact = []
        converted_list_true_fact.clear()

        for element in true_atom:
            converted_list_true_fact.append(element.strip())

        converted_list_false_fact = []
        converted_list_false_fact.clear()

        for element in false_atom:
            converted_list_false_fact.append(element.strip())


        return converted_list_true_fact, converted_list_false_fact, violate_action























