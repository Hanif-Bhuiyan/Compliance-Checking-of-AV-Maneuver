from owlready2 import *
import os
import math
from query_check_for_av_b import *
from query_check_for_av_e import *
from tv_availability_check import *
from safe_distance02 import *
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

class query_mapping_144:

    def mapping_144(self, atom_check, atom_filename, av, tv, av_lane, tv_lane, flag_144, safety_of_primary, safety_of_primary_check, trigger_lane):

        print("From Rule 144")

        self.atom_check = atom_check
        self.atom_filename = atom_filename
        self.av= av
        self.tv=tv
        self.av_lane = av_lane
        self.tv_lane = tv_lane
        self.flag_144 = flag_144
        self.safety_of_primary = safety_of_primary
        self.safety_of_primary_check = safety_of_primary_check
        self.trigger_lane = trigger_lane
        #self.receive_timestamp = receive_timestamp
        #previous_timestamp = self.receive_timestamp - 0.05

        true_atom.clear()
        false_atom.clear()

        def modify(a):
            answer3 = float(a)
            answer4 = round(answer3, 1)
            return answer4


        def query_triggering(q_d1, q_d2, at,a_n, a_v, t_v):

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


        def driver_IsOvertaking_vehicle(at, which_av, which_tv,which_av_lane, which_tv_lane): #144_1

            av_behind_tv = tv_ahead_of_av.tv_distance(which_av, which_tv)

            if(which_av_lane == which_tv_lane and av_behind_tv):

                sdc = safe_distance_check()
                safe_distance = sdc.safety(which_av, which_tv)

                if (safe_distance):

                    true_atom.append(at)
                    true_atom.append("driver_PassAtSufficientDistanceToAvoidCollisionWith_vehicle")  #144_2
                    true_atom.append("driver_PassAtSufficientDistanceToAvoidObstructingThePathOf_vehicle")  #144_3
                    true_atom.append("driver_IsAtSufficientDistancePastToAvoidCollisionWith_vehicle")  # 144_4
                    true_atom.append("driver_IsAtSufficientDistancePastToAvoidObstructingThePathOf_vehicle")  # 144_5

                else:

                    false_atom.append(at)
                    violate_action.append("safe distance from target vehicle")
                    print(at)
            else:

                true_atom.append(at)
                true_atom.append("driver_PassAtSufficientDistanceToAvoidCollisionWith_vehicle")  # 144_2
                true_atom.append("driver_PassAtSufficientDistanceToAvoidObstructingThePathOf_vehicle")  # 144_3
                true_atom.append("driver_IsAtSufficientDistancePastToAvoidCollisionWith_vehicle")  # 144_4
                true_atom.append("driver_IsAtSufficientDistancePastToAvoidObstructingThePathOf_vehicle")  # 144_5


        def vehicle_IsTravellingOn_markedLane(q_d1, q_d2, at,a_n, a_v, t_v, trigger_for_lane): #144_6
            list_of_answer = []
            list_of_answer = query_triggering(q_d1, q_d2, at, a_n, a_v, t_v)

            ## Tv is stationary or not checking ####
            sparql = "SELECT ?is_speed WHERE {ab:vehicle ab:is_speed ?is_speed.}"

            answer_tv = qb.query_trigger_for_behaviour(sparql, t_v)
            answer2_tv = modify(answer_tv[0])
            speed_of_tv = answer2_tv

            ### Tv is stationary or not checking
            #print(list_of_answer)
            if (list_of_answer[0] == 1.0):

                true_atom.append(at) #144_6
                true_atom.append("vehicle_IsTravellingOn_lineOfTraffic")#144_7
                true_atom.append("driver_ReturnTo_markedLane") #144_8

                #print(trigger_for_lane)



                if (list_of_answer[2] == 1.0 and trigger_for_lane == 1 and speed_of_tv > 1):
                    violate_action.append("crossed solid line")

            else:

                false_atom.append(at)
                print(at)
                #violate_action.append("crossed solid line")
                violate_action.append("safe distance from target vehicle")

                #if (list_of_answer[2] == 1.0 and self.trigger_lane == 1):
                if (list_of_answer[2] == 1.0 and trigger_for_lane == 1 and speed_of_tv > 1):
                    violate_action.append("crossed solid line")



        ## Now read atom file (c, 141, 142, amd 142)
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

            # For rule 144

            prinmary_check = primary_checking.checking_of_av_tv(self.av, self.tv)
            #print(prinmary_check)

            #safety_of_primary_check = 0
            if (self.safety_of_primary < 1 and self.av_lane == self.tv_lane and prinmary_check > 0):

                #print("lokkkssssss")
                self.safety_of_primary_check = safety_border_tv.safety_check_for_target_vehicle(self.tv)
                print("Here is the considering speed")
                print(self.safety_of_primary_check)
                self.safety_of_primary = 1


            if (self.flag_144 < 1 and self.safety_of_primary > 0):

                #print("checkinggggggggggggggggggggggggggggggggggg")
                if (prinmary_check > self.safety_of_primary_check):
                    self.flag_144 = 1
                    #print(prinmary_check)
                    #print(self.safety_of_primary_check)
                    print("Yahpoooo got it bosss")
                    #print(self.flag_144)


            # if (self.flag_140 == 1 or prinmary_check >= safety_of_primary_check):

            if (self.flag_144 == 1):

                true_atom.append("driver_IsOvertaking_vehicle")
                true_atom.append("driver_PassAtSufficientDistanceToAvoidCollisionWith_vehicle")
                true_atom.append("driver_PassAtSufficientDistanceToAvoidObstructingThePathOf_vehicle")
                true_atom.append("driver_IsAtSufficientDistancePastToAvoidCollisionWith_vehicle")
                true_atom.append("driver_IsAtSufficientDistancePastToAvoidObstructingThePathOf_vehicle")
                #true_atom.append("vehicle_IsTravellingOn_markedLane")
                #true_atom.append("vehicle_IsTravellingOn_lineOfTraffic")
                #true_atom.append("driver_ReturnTo_markedLane")

                if ("vehicle_IsTravellingOn_markedLane" in line):  # 144_6
                    vehicle_IsTravellingOn_markedLane(query_dir1, query_dir2, atom, atom_name, self.av, self.tv,self.trigger_lane)

            else:

                if ("driver_IsOvertaking_vehicle" in line):  # 144_1
                    driver_IsOvertaking_vehicle(atom,self.av,self.tv, self.av_lane, self.tv_lane)

                if("vehicle_IsTravellingOn_markedLane" in line): #144_6
                    vehicle_IsTravellingOn_markedLane(query_dir1, query_dir2, atom, atom_name, self.av, self.tv, self.trigger_lane)




        #print(violate_action)

        converted_list_true_fact = []
        converted_list_true_fact.clear()

        for element in true_atom:
            converted_list_true_fact.append(element.strip())

        converted_list_false_fact = []
        converted_list_false_fact.clear()

        for element in false_atom:
            converted_list_false_fact.append(element.strip())

        return converted_list_true_fact, converted_list_false_fact, violate_action, self.flag_144, self.safety_of_primary, self.safety_of_primary_check























