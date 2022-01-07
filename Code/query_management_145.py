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

class query_mapping_145:

    def mapping_145(self, atom_check, atom_filename, av, tv, av_lane, tv_lane, flag_145, trigger_lane):

        print("From Rule 145")

        self.atom_check = atom_check
        self.atom_filename = atom_filename
        self.av= av
        self.tv=tv
        self.av_lane = av_lane
        self.tv_lane = tv_lane
        self.flag_145 = flag_145
        self.trigger_lane = trigger_lane

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


        def driver_IsOvertakingByCrossingADividingLine_anotherDriver(at, which_av, which_tv, which_av_lane, which_tv_lane): #145_1

            av_behind_tv = tv_ahead_of_av.tv_distance(which_av, which_tv)

            if(which_av_lane == which_tv_lane and av_behind_tv):

                sdc = safe_distance_check()
                safe_distance = sdc.safety(which_av, which_tv)

                if (safe_distance):

                    true_atom.append(at)
                    true_atom.append("driver_IsOvertakingByCrossingToTheRightOfTheCentreOfTheRoad_anotherDriver")  #145_5
                    true_atom.append("driver_IsAtASufficientDistanceToAvoidACollisionInFrontOf_anotherDriver")  # 145_10
                    true_atom.append("driver_HasPassed_anotherDriver") # 145_3
                    true_atom.append("anotherDriver_IncreaseTheSpeed") # 145_4

                else:

                    false_atom.append(at)
                    print(at)
                    violate_action.append("safe distance from target vehicle")

            else:

                true_atom.append(at)
                true_atom.append("driver_IsOvertakingByCrossingToTheRightOfTheCentreOfTheRoad_anotherDriver")  # 145_5
                true_atom.append("driver_IsAtASufficientDistanceToAvoidACollisionInFrontOf_anotherDriver")  # 145_10

                true_atom.append("driver_HasPassed_anotherDriver")  # 145_3
                true_atom.append("anotherDriver_IncreaseTheSpeed")  # 145_4



        def driver_isDrivingOn_twoWayRoad(q_d1, q_d2, at,a_n, a_v, t_v): #145_2
            #print("Yes Checking here")
            list_of_answer = []
            list_of_answer = query_triggering(q_d1, q_d2, at, a_n, a_v, t_v)
            #print(list_of_answer)
            if (list_of_answer[0] == 1.0):

                true_atom.append(at)
            else:

                false_atom.append(at)
                print(at)


        def anotherDriver_IsDrivingOn_markedLane(q_d1, q_d2, at,a_n, a_v, t_v, trigger_for_lane): #145_6
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

                true_atom.append(at) #145_6
                true_atom.append("driver_HasReturnedTo_markedLane")  #145_7
                true_atom.append("anotherDriver_IsDrivingOn_lineOfTraffic") #145_8
                true_atom.append("driver_HasReturnedTo_lineOfTraffic") #145_9


                #if (list_of_answer[2] == 1.0 and trigger_for_lane == 1):
                if (list_of_answer[2] == 1.0 and trigger_for_lane == 1 and speed_of_tv > 1):
                    violate_action.append("crossed solid line")

            else:

                false_atom.append(at)
                print(at)
                #violate_action.append("crossing solid line")

                #if (list_of_answer[2] == 1.0 and trigger_for_lane == 1):
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

            # For rule 145

            '''
            if (self.flag_145 == 0):

                prinmary_check = primary_checking.checking_of_av_tv(self.av, self.tv)

                safety_of_primary_check = safety_border_tv.safety_check_for_target_vehicle(self.tv)
                #print(safety_of_primary_check)

                if (prinmary_check >= safety_of_primary_check):
                    self.flag_145 == 1
            '''

            # if (self.flag_140 == 1 or prinmary_check >= safety_of_primary_check):

            if (self.flag_145 == 1):

                true_atom.append("driver_IsOvertakingByCrossingADividingLine_anotherDriver")
                true_atom.append("driver_IsOvertakingByCrossingToTheRightOfTheCentreOfTheRoad_anotherDriver")
                true_atom.append("driver_IsAtASufficientDistanceToAvoidACollisionInFrontOf_anotherDriver")
                true_atom.append("driver_HasPassed_anotherDriver")
                true_atom.append("anotherDriver_IncreaseTheSpeed")
                true_atom.append("anotherDriver_IsDrivingOn_markedLane")
                #true_atom.append("driver_HasReturnedTo_markedLane")
                #true_atom.append("anotherDriver_IsDrivingOn_lineOfTraffic")
                #true_atom.append("driver_HasReturnedTo_lineOfTraffic")
                false_atom.append("driver_isDrivingOn_twoWayRoad")

                if ("anotherDriver_IsDrivingOn_markedLane" in line):  # 145_6
                    anotherDriver_IsDrivingOn_markedLane(query_dir1, query_dir2, atom, atom_name, self.av, self.tv,self.trigger_lane)


            else:

                if ("driver_IsOvertakingByCrossingADividingLine_anotherDriver" in line):  # 145_1
                    driver_IsOvertakingByCrossingADividingLine_anotherDriver(atom,self.av,self.tv, self.av_lane, self.tv_lane)

                if ("driver_isDrivingOn_twoWayRoad" in line):  #145_2
                    driver_isDrivingOn_twoWayRoad(query_dir1, query_dir2, atom, atom_name, self.av, self.tv)

                if("anotherDriver_IsDrivingOn_markedLane" in line): #145_6
                    anotherDriver_IsDrivingOn_markedLane(query_dir1, query_dir2, atom, atom_name, self.av, self.tv, self.trigger_lane)




        converted_list_true_fact = []
        converted_list_true_fact.clear()

        for element in true_atom:
            converted_list_true_fact.append(element.strip())


        converted_list_false_fact = []
        converted_list_false_fact.clear()

        for element in false_atom:
            converted_list_false_fact.append(element.strip())


        return converted_list_true_fact, converted_list_false_fact, violate_action























