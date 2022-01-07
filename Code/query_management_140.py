from owlready2 import *
import os
import math

from primary_checking_info import *
from query_check_for_av_b import *
from query_check_for_av_e import *
from safe_distance02 import *
from tv_availability_check import *
from other_vehicle_safe_distance_check import *
from primary_checking_info import *

from safety_border_check import *
from primary_checking_of_av_tv_position import *
primary_checking = primary_checking_of_av_tv()
safety_border_tv = safety_border_check_for_target_vehicle()

true_atom = []
false_atom = []

violate_action = []

qb = query_behaviour()
qe = query_environment()
qbn = query_mapping_lane()
tv_behind = av_after_tv()

qbn = query_mapping_lane()
av_distance = 0
tv_distance = 0

#one_time_check = 0

#converted_list_true_fact = []
#converted_list_false_fact = []


def tv_av_distance(measure_av_distance, measure_tv_distance):

    true_atom.clear()
    false_atom.clear()

    onto = get_ontology("C:/Users/bhuiyanh/OneDrive - Queensland University of Technology/Ontology- Protege/av_info_behaviour.owl")
    onto.load()

    ## Modifying query return from ontology ##

    def modify(a):
        answer3 = float(a)
        answer4 = round(answer3, 2)
        return answer4

    sparql_x = "SELECT ?is_positionx WHERE {ab:vehicle ab:is_positionx ?is_positionx.}"
    sparql_y = "SELECT ?is_positiony WHERE {ab:vehicle ab:is_positiony ?is_positiony.}"

    answer_av_x = qb.query_trigger_for_behaviour(sparql_x, measure_av_distance)
    answer2_av_x = modify(answer_av_x[0])
    position_x_of_av = answer2_av_x

    answer_av_y = qb.query_trigger_for_behaviour(sparql_y, measure_av_distance)
    answer2_av_y = modify(answer_av_y[0])
    position_y_of_av = answer2_av_y

    av_position_calc = (position_x_of_av * position_x_of_av) + (position_y_of_av * position_y_of_av)
    av_position = math.sqrt(av_position_calc)
    #av_position = abs(av_position)

    answer_tv_x = qb.query_trigger_for_behaviour(sparql_x, measure_tv_distance)
    answer2_tv_x = modify(answer_tv_x[0])
    position_x_of_tv = answer2_tv_x

    answer_tv_y = qb.query_trigger_for_behaviour(sparql_y, measure_tv_distance)
    answer2_tv_y = modify(answer_tv_y[0])
    position_y_of_tv = answer2_tv_y

    tv_position_calc = (position_x_of_tv * position_x_of_tv) + (position_y_of_tv * position_y_of_tv)
    tv_position = math.sqrt(tv_position_calc)
    #tv_position = abs(tv_position)

    distance = tv_position - av_position
    return distance

'''
    if (position_x_of_av > 0):

        distance = tv_position - av_position
        return distance
    else:
        distance = av_position - tv_position
        return distance
        
'''


class query_mapping_140:

    def mapping_140(self, atom_check, atom_filename, av, tv, av_lane, tv_lane, lo_flag, ro_flag, main_target_vehicle, flag_140, flag_140_safety):

        print("From Rule 140")

        self.atom_check = atom_check
        self.atom_filename = atom_filename
        self.av= av
        self.tv=tv
        self.av_lane = av_lane
        self.tv_lane = tv_lane
        self.lo_flag = lo_flag
        self.ro_flag = ro_flag
        self.main_target_vehicle = main_target_vehicle
        self.flag_140 = flag_140
        self.flag_140_safety = flag_140_safety
        #print(self.flag_140_safety)
        #self.safety_of_primary = safety_of_primary
        #one_time_check = self.flag_140_safety
        abc= 0

        true_atom.clear()
        false_atom.clear()
        violate_action.clear()
        #abc = 0
        #converted_list_true_fact.clear()
        #converted_list_false_fact.clear()

        def modify(a):
            answer3 = float(a)
            answer4 = round(answer3, 2)
            return answer4


        def driver_HasClearViewOf_approachingTraffic(at, which_av, which_tv, main_target_vehicle_id, one_time_check): #140

            #0print(one_time_check)
            ov_not_safe = 0
            onto = get_ontology("C:/Users/bhuiyanh/OneDrive - Queensland University of Technology/Ontology- Protege/av_info_behaviour.owl")
            onto.load()

            vehicle_instance = onto.vehicle.instances()
            vehicle_number = len(vehicle_instance)

            vehicle = []

            target_vehicle = []
            #print(one_time_check)

            if(vehicle_number > 1):

                for i in range(0, len(vehicle_instance)):
                    # print(vehicle_instance[i])
                    vehicle_instance1 = str(vehicle_instance[i]).split(".")
                    vehicle_instance2 = vehicle_instance1[-1]
                    vehicle.append(vehicle_instance2)

                av_lane = qbn.mapping_av_lane(which_av)

                for i in range(1, len(vehicle)):
                    target_vehicle.append(vehicle[i])

                #main_target_vehicle_lane = qbn.mapping_av_lane(target_vehicle[main_target_vehicle_id])
                main_target_vehicle_lane = qbn.mapping_av_lane(which_tv)

                is_av_cross_tv_already = primary_checking.checking_of_av_tv(which_av, which_tv)

                #print(is_av_cross_tv_already)

                sfaety_border = safety_border_tv.safety_check_for_target_vehicle(which_tv)
                #print(sfaety_border)

                if (av_lane == main_target_vehicle_lane and is_av_cross_tv_already > 0 and is_av_cross_tv_already < sfaety_border):
                    #print("Yuppppppppppppppppppppppppppp")
                    ov_not_safe = ov_not_safe + 1
                    #false_atom.append(at)
                    #print(at)
                    violate_action.append("not clear view of target vehicle")
                    #print("Ollleee got it*******************************************")

                if(av_lane == main_target_vehicle_lane and (is_av_cross_tv_already > sfaety_border or is_av_cross_tv_already < 0)):

                    ov_not_safe = 0
                    print("Yup from here")

                else:

                    #ov_not_safe = 0
                    print("yes checking")

                    for i in range(len(target_vehicle)):

                        if (one_time_check < 1 and target_vehicle[i] != which_tv):

                            tv_lane = qbn.mapping_tv_lane(target_vehicle[i])

                            sfaety_border_for_approaching_traffic = safety_border_tv.safety_check_for_target_vehicle(target_vehicle[i])

                            #print(tv_lane)
                            #print(main_target_vehicle_lane)
                            if (self.lo_flag == 1 and tv_lane == main_target_vehicle_lane - 1): # I dont care who is behind me I care when I am going to take action am i keeping safe diatance or not

                                av_cross_tv = primary_checking.checking_of_av_tv(which_av, target_vehicle[i])

                                #print(av_cross_tv)

                                if (av_cross_tv > 0 and av_cross_tv < sfaety_border_for_approaching_traffic):
                                    print("Approaching traffic not safe")
                                    ov_not_safe = ov_not_safe + 1
                                    violate_action.append("not clear view of approaching traffic")
                                    one_time_check = 1
                                    print("gottttttttttttttttttttttttttttttttttttttttttt 1 ")


                            if (self.ro_flag == 1 and tv_lane == main_target_vehicle_lane + 1):

                                av_cross_tv = primary_checking.checking_of_av_tv(which_av, target_vehicle[i])

                                #print(av_cross_tv)

                                if (av_cross_tv > 0 and av_cross_tv < sfaety_border_for_approaching_traffic):
                                    print("Approaching traffic not safe")
                                    ov_not_safe = ov_not_safe + 1
                                    violate_action.append("not clear view of approaching traffic")
                                    one_time_check = 1
                                    print("gottttttttttttttttttttttttttttttttttttttttttt 2 ")


            if (ov_not_safe == 0):
                true_atom.append(at)
                #true_atom.append('driver_Overtake_vehicle')

            else:
                false_atom.append(at)
                false_atom.append('driver_Overtake_vehicle')
                #false_atom.append('driver_CanSafelyOvertake_vehicle')
                print(at)
                #violate_action.append("not clear view of approaching traffic")

            #print(one_time_check)
            return one_time_check



        def driver_CanSafelyOvertake_vehicle(at, which_av, which_tv, which_av_lane, which_tv_lane):

            flag_ov_not_safe_target_vehicle = 0
            flag_ov_not_safe_other_vehicle = 0

            av_behind_tv = tv_ahead_of_av.tv_distance(which_av, which_tv)

            if (which_av_lane == which_tv_lane and av_behind_tv):

                sdc = safe_distance_check()
                safe_distance = sdc.safety(which_av, which_tv)
                #print(safe_distance)

                if (safe_distance):

                    #true_atom.append(at)
                    #true_atom.append('driver_Overtake_vehicle')  # 11
                    flag_ov_not_safe_target_vehicle = 0

                else:

                    #false_atom.append(at)
                    #print(at)
                    #violate_action.append("safe distance from target vehicle")
                    flag_ov_not_safe_target_vehicle = 1


            else:

                #print("I am here")
                onto = get_ontology("C:/Users/bhuiyanh/OneDrive - Queensland University of Technology/Ontology- Protege/av_info_behaviour.owl")
                onto.load()

                vehicle_instance = onto.vehicle.instances()
                vehicle_number = len(vehicle_instance)
                # print(vehicle_number)
                # print(type(vehicle_number))

                vehicle = []

                target_vehicle = []

                #if (vehicle_number > 1):

                for i in range(0, len(vehicle_instance)):
                    # print(vehicle_instance[i])
                    vehicle_instance1 = str(vehicle_instance[i]).split(".")
                    vehicle_instance2 = vehicle_instance1[-1]
                    vehicle.append(vehicle_instance2)

                av_when_consider_other_vehicle = vehicle[0]
                avlane_when_consider_other_vehicle = qbn.mapping_av_lane(av_when_consider_other_vehicle)

                #av_lane = qbn.mapping_av_lane(which_av)

                for i in range(1, len(vehicle)):
                    target_vehicle.append(vehicle[i])

                #print(target_vehicle)

                list_check = []
                for i in range(len(target_vehicle)):

                    tv_when_consider_other_vehicle = target_vehicle[i]
                    #print(tv_when_consider_other_vehicle)

                    av_behind_tv = tv_ahead_of_av.tv_distance(av_when_consider_other_vehicle, tv_when_consider_other_vehicle)

                    # print("AV Lane number",av_lane)

                    # TV lane count
                    tvlane_when_consider_other_vehicle = qbn.mapping_tv_lane(tv_when_consider_other_vehicle)
                    # print("Target vehicle lane number", tv_lane)

                    if(av_behind_tv and avlane_when_consider_other_vehicle == tvlane_when_consider_other_vehicle):

                        print("Other Vehicle Checking start")


                        sdc = safe_distance_check()
                        safe_distance = sdc.safety(av_when_consider_other_vehicle, tv_when_consider_other_vehicle)


                        if (safe_distance):

                            flag_ov_not_safe_other_vehicle = 0

                        else:
                            print("gotta", tv_when_consider_other_vehicle)
                            flag_ov_not_safe_other_vehicle = 1

            #print("shjdhdshdsdsdhsjdhsadjshdhsajdh",flag_ov_not_safe)

            if(flag_ov_not_safe_target_vehicle == 0 and flag_ov_not_safe_other_vehicle == 0):
                #print("from here")
                true_atom.append(at)
                true_atom.append('driver_Overtake_vehicle')
                #true_atom.append('driver_Overtake_vehicle')  # 11
            else:
                false_atom.append(at)
                false_atom.append('driver_Overtake_vehicle')
                print(at)
                #print("driver_Overtake_vehicle")
                if(flag_ov_not_safe_other_vehicle == 1):
                    violate_action.append("safe distance from other vehicles")
                if (flag_ov_not_safe_target_vehicle == 1):
                    violate_action.append("safe distance from target vehicle")


        '''
        if (self.flag_140 == 0 and  self.safety_of_primary == 0):

            print("here")
            prinmary_check = primary_checking.checking_of_av_tv(self.av, self.tv)

            if (self.av_lane == self.tv_lane and prinmary_check):

                safety_of_primary_check = safety_border_tv.safety_check_for_target_vehicle(self.tv)


                print(prinmary_check)
                print(safety_of_primary_check)

                if(prinmary_check >= safety_of_primary_check):
                    self.flag_140 == 1


        #if (self.flag_140 == 1 or prinmary_check >= safety_of_primary_check):
        print(self.flag_140)
        '''

        if (self.flag_140 == 1):

            print("now start")

            true_atom.append("driver_HasClearViewOf_approachingTraffic")
            true_atom.append("driver_CanSafelyOvertake_vehicle")


        else:

            for line in open(self.atom_check, "r"): ## Now start reading inside of every line of file (c, r_142, ...), first start reading c file
                line.strip()
                atom_name1 = line.split(":")
                atom_name = atom_name1[0] # c_1
                #print(atom_name)
                atom = atom_name1[-1] #vehicle_IsTurningLeft
                #print(atom)

                # Now based on atom, reading queries

                query_dir = "C:/Users/bhuiyanh/PycharmProjects/Practise22/query/"  # query path
                query_dir1 = query_dir + self.atom_filename  # now based on atom, making query path to find queries
                #print(query_dir1)

                query_dir2 = os.listdir(query_dir1)  # in this query how many query files, it is reading all
                #print(query_dir2)

                # For rule 142

                if ("driver_HasClearViewOf_approachingTraffic" in line):  #140_1
                    abc = driver_HasClearViewOf_approachingTraffic(atom, self.av, self.tv, self.main_target_vehicle,self.flag_140_safety)

                #if ("driver_HasClearViewOf_approachingTraffic" in line):  #140_1
                    #driver_HasClearViewOf_approachingTraffic(atom)

                if ("driver_CanSafelyOvertake_vehicle" in line):  #140_2
                    driver_CanSafelyOvertake_vehicle(atom, self.av, self.tv, self.av_lane, self.tv_lane)


        converted_list_true_fact = []
        converted_list_true_fact.clear()


        for element in true_atom:
            converted_list_true_fact.append(element.strip())


        converted_list_false_fact = []
        converted_list_false_fact.clear()

        for element in false_atom:
            converted_list_false_fact.append(element.strip())

        #print(converted_list_false_fact)
        #print(violate_action)

        #print("ABC value is",abc)
        return converted_list_true_fact, converted_list_false_fact, violate_action, abc
