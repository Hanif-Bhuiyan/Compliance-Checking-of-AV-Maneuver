from builtins import print
import os

import bold as bold
from owlready2 import *
from six import print_

import overall_fact
from query_management_145 import *
from query_management_144 import *
from query_management_141 import *
from query_management_142 import *
from query_management_140 import *
from query_management_143_left import *
from query_management_143_right import *
from primary_checking_info import *
from overall_fact import *
from tv_availability_check import *
from safe_distance02 import *
from other_vehicle_safe_distance_check import *
from plotting import *
from position_finding import *
import time

import pandas as pd
from av_b import *
from av_e import *
#from quer_check02 import *
from query_check_for_av_e import *
from query_check_for_av_b import *

from av_b import behaviour
from av_e import environment


#############making exel file for plotting########


import xlsxwriter


workbook = xlsxwriter.Workbook('output.xlsx') # This is the output file
worksheet_data = workbook.add_worksheet('data')

'''
path1 = 'C:/Users/bhuiyanh/PycharmProjects/Code-Complaince-Checking/final_output.txt'

isExist1 = os.path.exists(path1)

if (isExist1):
    os.remove("final_output.txt")

'''
################################################

flag_145 = 0
flag_144 = 0
flag_144_safety = 0
flag_140_safety = 0
flag_143_l = 0
flag_143_r = 0
flag_142 = 0
flag_141 = 0
flag_140 = 0

primary_145 = 0
primary_144 = 0
primary_143_l = 0
primary_143_r = 0
primary_142 = 0
primary_141 = 0
primary_140 = 0


data1 = pd.read_excel("Ex_1_menu_1_behaviour.xlsx")
data2 = pd.read_excel("Ex_1_menu_1_environment.xlsx")


true_fact_145 = []
false_fact_145 = []

true_fact_144 = []
false_fact_144 = []

true_fact_143 = []
false_fact_143 = []

true_fact_141 = []
false_fact_141 = []

true_fact_140 = []
false_fact_140 = []

overall_true_fact = []
overall_false_fact = []

illegal_action_140 = []
illegal_action_141 = []
illegal_action_142 = []
illegal_action_143 = []
illegal_action_144 = []
illegal_action_145 = []

illegal_action = []
final_illegal_action1 = []
final_illegal_action2 = []
final_illegal_action3 = []
final_illegal_action4 = []
fully_final_illegal_action = []
last_fully_final_illegal_action = []

last_fully_final_illegal_action.clear()

last = overall_mapping_for_atom()


final_true_fact = []
final_false_fact = []

position_x_of_av = []
position_y_of_av = []
position_x_of_tv = []
position_y_of_tv = []

plot_timestamp = []

plot_time = []

plot_decision = []

plot_decision.clear()

#fully_final_violate_action = []

onto = get_ontology("C:/Users/bhuiyanh/OneDrive - Queensland University of Technology/Ontology- Protege/av_info_behaviour.owl")
onto.load()

vehicle_instance = onto.vehicle.instances()
vehicle_number = len(vehicle_instance)

print("There are" +" "+str(vehicle_number-1) + " "+"target vehicles")

vehicle = []

target_vehicle = []

timestamp_dict = []
av_lane_number_dict = []
send_trigger_lane_change = 0

for i in range(0, len(vehicle_instance)):
    #print(vehicle_instance[i])

    vehicle_instance1 = str(vehicle_instance[i]).split(".")
    vehicle_instance2 = vehicle_instance1[-1]
    vehicle.append(vehicle_instance2)

av = vehicle[0]

for i in range(1, len(vehicle)):
    target_vehicle.append(vehicle[i])
    target_vehicle_lane_number = qbn.mapping_tv_lane(vehicle[i])
    print("target vehicle-",i,"lane number is",target_vehicle_lane_number)
            # print("Target vehicle lane number", tv_lane)


ro = 0
lo = 0

print("Target vehicles name are in sequential order.. like closest vehicle is target vehicle-1.. next vehicle is target vehicle-2.. like this..")
print("So.. for which target vehicle you want to validate the overtaking maneuover action.. ")

user_require_tv_number = int(input("Please input 0, 1, 2... which one you want..but only one at a time"))

print(user_require_tv_number)
print(target_vehicle)
tv = target_vehicle[user_require_tv_number]
print(tv)

print("You are validating for Target Vehicle-", user_require_tv_number)

print("Now...Which overtaking you want to validate? Left Overtaking or Right Overtaking")

print("Type l for Left overtaking validation or type r for Right Overtaking validation")

overtaking_type = input("Give the input l/r :")


if(overtaking_type == "l" or overtaking_type == "L"):

    lo = 1

    print("What time range you want to validate")

    start = int(input("Please give the start range"))
    end = int(input("Please give the end range"))

    start_time = time.time()

    plot_decision.clear()
    av_lane_number_dict.clear()
    send_trigger_lane_change = 0

    for timestamp in range(start, end):
        # print("For which timestamp you want to validate")

        # val = int(input("Which timestamp you want to validate"))
        print("For timestamp", timestamp)
        plot_timestamp.append(timestamp)

        val = timestamp
        locate = val - 2
        #print(locate)

        #print("Creating Ontology")

        ## Behaviour Ontology Functions

        a: behaviour = behaviour()

        what_time = a.create_ontology_behaviour(data1, locate)
        plot_time.append(what_time)


        ## Environment Ontology Functions

        b: environment = environment()

        b.create_ontology_en(data2, locate)

        qbn = query_mapping_lane()
        qm_144 = query_mapping_144()
        qm_145 = query_mapping_145()
        qm_141 = query_mapping_141()
        qm_142 = query_mapping_142()
        qm_140 = query_mapping_140()
        qm_143_left = query_mapping_143_left()
        of = overall_mapping_for_atom()
        tv_ahead_of_av = tv_availability()
        position_find=av_tv_postion()

        atom_path = "C:/Users/bhuiyanh/PycharmProjects/Code-Complaince-Checking/atoms"
        atom_dirs = os.listdir(atom_path)  # Reading all in this directory

        if ("vehicle" in av): # checking for vehicle

            true_fact_145.clear()
            false_fact_145.clear()
            true_fact_144.clear()
            false_fact_144.clear()
            true_fact_143.clear()
            false_fact_143.clear()
            true_fact_141.clear()
            false_fact_141.clear()
            true_fact_140.clear()
            false_fact_140.clear()
            overall_true_fact.clear()
            overall_false_fact.clear()

            #illegal_action.clear()
            illegal_action_140.clear()
            illegal_action_141.clear()
            illegal_action_142.clear()
            illegal_action_143.clear()
            illegal_action_144.clear()
            illegal_action_145.clear()


            #final_illegal_action1.clear()
            #final_illegal_action2.clear()
            #final_illegal_action3.clear()
            #final_illegal_action4.clear()
            #fully_final_illegal_action.clear()
            final_true_fact.clear()
            final_false_fact.clear()



            # Lane Number count
            tn = "totallane"

            total_lane = qbn.mapping_lane(tn)
            # print("Total Lane",total_lane)

            # Bicycle Lane count

            bn = "bicycle"
            bicycle_lane = qbn.mapping_lane(bn)
            # print("Bicycle Lane",bicycle_lane)

            # AV lane number identify

            av_lane = qbn.mapping_av_lane(av)
            # print("AV Lane number",av_lane)

            av_lane_number_dict.append(av_lane)
            # print(av_lane_number_dict)
            length = len(av_lane_number_dict)
            # print(length)

            if (locate > 5):

                # print(av_lane_number_dict[length-1])
                # print(av_lane_number_dict[length-2])

                if (av_lane_number_dict and length > 2):

                    if (av_lane_number_dict[length - 1] != av_lane_number_dict[length - 2]):
                        send_trigger_lane_change = 1
                    else:
                        send_trigger_lane_change = 0

            # TV lane count
            tv_lane = qbn.mapping_tv_lane(tv)
            # print("Target vehicle lane number", tv_lane)

            # TV speed

            tvs = qbn.mapping_tv_speed(tv)

            # TV displaying donotovertake sign

            tv_donot = qbn.vehicle_Display_doNot(tv)
            # print("the do not sign is::::", tv_donot)

            ## For getting positions

            pos_x_av, pos_y_av, pos_x_tv, pos_y_tv = position_find.get_position(av, tv)

            position_x_of_av.append(pos_x_av)
            position_y_of_av.append(pos_y_av)
            position_x_of_tv.append(pos_x_tv)
            position_y_of_tv.append(pos_y_tv)


            ## **** End of Primary Checking informtion ****** ###

            ## **** Primary Checking informtion ****** ###


            if(bicycle_lane > 0.0 and "bicycle" in av):

                # ******** FOR RULE 143, 144, 145 ***********#

                print("Then You have to follow Rule 144A and it is under developing.. We did not finish this developement yet")
                print("Sorry we are not considering bicycle issue here")

            elif ("motorbike" in av):

                print("I am not considering for motorbike. Sorry")

            else:

                af = 'F'

                if (av_lane == tv_lane or av_lane == tv_lane - 1):

                    av_behind_tv = tv_ahead_of_av.tv_distance(av, tv)

                    if(tv_donot == 1.0):

                        print("Following Rule 145, 144, 143_l, 141, 140")


                        true_fact_144, false_fact_144, illegal_action_144, pass_144, safety_144, pass_144_safety = qm_144.mapping_144("C:/Users/bhuiyanh/PycharmProjects/Code-Complaince-Checking/atoms/144.txt", "144", av, tv, av_lane,tv_lane, flag_144, primary_144, flag_144_safety, send_trigger_lane_change)

                        flag_144 = pass_144
                        primary_144 = safety_144
                        flag_144_safety = pass_144_safety

                        if (flag_144 == 1):

                            true_fact_145, false_fact_145, illegal_action_145 = qm_145.mapping_145("C:/Users/bhuiyanh/PycharmProjects/Code-Complaince-Checking/atoms/145.txt", "145", av, tv, av_lane,tv_lane, 1, send_trigger_lane_change)

                            true_fact_143, false_fact_143, illegal_action_143 = qm_143_left.mapping_143_left("C:/Users/bhuiyanh/PycharmProjects/Code-Complaince-Checking/atoms/143l.txt", "143l", av, tv, av_lane,tv_lane, 1)

                            true_fact_141, false_fact_141, illegal_action_141 = qm_141.mapping_141("C:/Users/bhuiyanh/PycharmProjects/Code-Complaince-Checking/atoms/141.txt", "141", av, tv, av_lane,tv_lane, 1)

                            #true_fact_140, false_fact_140, illegal_action_140 = qm_140.mapping_140("C:/Users/bhuiyanh/PycharmProjects/Code-Complaince-Checking/atoms/140.txt", "140", av, tv, av_lane,tv_lane, lo, ro, user_require_tv_number, 1)

                            true_fact_140, false_fact_140, illegal_action_140, pass_140_safety = qm_140.mapping_140("C:/Users/bhuiyanh/PycharmProjects/Code-Complaince-Checking/atoms/140.txt", "140", av, tv, av_lane,tv_lane, lo, ro, user_require_tv_number, 1, flag_140_safety)
                            flag_140_safety = pass_140_safety

                        else:
                            true_fact_145, false_fact_145, illegal_action_145 = qm_145.mapping_145("C:/Users/bhuiyanh/PycharmProjects/Code-Complaince-Checking/atoms/145.txt", "145", av, tv, av_lane,tv_lane, 0, send_trigger_lane_change)

                            true_fact_143, false_fact_143, illegal_action_143 = qm_143_left.mapping_143_left("C:/Users/bhuiyanh/PycharmProjects/Code-Complaince-Checking/atoms/143l.txt", "143l", av, tv, av_lane,tv_lane, 0)

                            true_fact_141, false_fact_141, illegal_action_141 = qm_141.mapping_141("C:/Users/bhuiyanh/PycharmProjects/Code-Complaince-Checking/atoms/141.txt", "141", av, tv, av_lane,tv_lane, 0)

                            #true_fact_140, false_fact_140, illegal_action_140 = qm_140.mapping_140("C:/Users/bhuiyanh/PycharmProjects/Code-Complaince-Checking/atoms/140.txt", "140", av, tv, av_lane,tv_lane, lo, ro, user_require_tv_number, 0)

                            true_fact_140, false_fact_140, illegal_action_140, pass_140_safety = qm_140.mapping_140("C:/Users/bhuiyanh/PycharmProjects/Code-Complaince-Checking/atoms/140.txt", "140", av, tv, av_lane,tv_lane, lo, ro, user_require_tv_number, 0, flag_140_safety)
                            flag_140_safety = pass_140_safety


                        overall_true_fact = true_fact_145 + true_fact_144 + true_fact_143 + true_fact_141 + true_fact_140
                        overall_false_fact = false_fact_145 + false_fact_144 + false_fact_143 + false_fact_141 + false_fact_140

                        illegal_action = illegal_action_144 + illegal_action_145 + illegal_action_143 + illegal_action_141 + illegal_action_140


                        final_illegal_action1 = of.overall_mapping_illegal_action(illegal_action)
                        #fully_final_violate_action.append(illegal_action)
                        #print(final_illegal_action)

                        final_true_fact = of.overall_mapping_true(overall_true_fact)
                        final_false_fact = of.overall_mapping_false(overall_false_fact)


                        MyFile = open('true_fact.txt', 'w')
                        for element in final_true_fact:
                            MyFile.write(element)
                            MyFile.write('\n')
                        MyFile.close()

                        os.system('C:/Users/bhuiyanh/PycharmProjects/Code-Complaince-Checking/turnip-cli-20200624 145_144_143l_141_140_rule.txt true_fact.txt > output.txt')

                        file1 = open('C:/Users/bhuiyanh/PycharmProjects/Code-Complaince-Checking/output.txt', 'r')

                        final_result = open("final_output.txt", 'a')

                        for line in file1:
                            if ('[' in line and "[P]driver_Overtake_vehicle" not in line and "[F]driver_Overtake_vehicle" not in line and "[O]" not in line and "[P]driver_DrivePastToTheLeftOf_vehicle" not in line):
                                final_result.write(line)

                        final_result.close()

                        file2 = open('C:/Users/bhuiyanh/PycharmProjects/Code-Complaince-Checking/final_output.txt', 'r')
                        for ab in file2:
                            ab = ab.strip()
                            l1 = ab.split('d')
                            #print(l1)
                            l2 = l1[0].strip("[]")
                            l2 = l2.strip()
                            plot_decision.append(l2)
                        file2.close()
                        file1.close()

                    else:

                        print("Following Rule 145, 144, 141, 140")


                        '''
                        true_fact_144, false_fact_144, illegal_action_144, pass_144, safety_144 = qm_144.mapping_144("C:/Users/bhuiyanh/PycharmProjects/Code-Complaince-Checking/atoms/144.txt", "144", av, tv, av_lane,tv_lane, flag_144, primary_144)
                        flag_144 = pass_144
                        primary_144 = safety_144


                        true_fact_145, false_fact_145, illegal_action_145, pass_145, safety_145 = qm_145.mapping_145("C:/Users/bhuiyanh/PycharmProjects/Code-Complaince-Checking/atoms/145.txt", "145", av, tv, av_lane,tv_lane, flag_145, primary_145)
                        flag_145 = pass_145
                        primary_145 = safety_145

                        true_fact_141, false_fact_141, illegal_action_141, pass_141, safety_141 = qm_141.mapping_141("C:/Users/bhuiyanh/PycharmProjects/Code-Complaince-Checking/atoms/141.txt", "141", av, tv, av_lane,tv_lane, flag_141, primary_141)
                        flag_141 = pass_141
                        primary_141 = safety_141

                        true_fact_140, false_fact_140, illegal_action_140, pass_140, safety_140 = qm_140.mapping_140("C:/Users/bhuiyanh/PycharmProjects/Code-Complaince-Checking/atoms/140.txt", "140", av, tv, av_lane,tv_lane, lo, ro, user_require_tv_number, flag_140, primary_140)

                        flag_140 = pass_140
                        primary_140 = safety_140
                        '''

                        true_fact_144, false_fact_144, illegal_action_144, pass_144, safety_144, pass_144_safety= qm_144.mapping_144("C:/Users/bhuiyanh/PycharmProjects/Code-Complaince-Checking/atoms/144.txt", "144", av, tv, av_lane,tv_lane, flag_144, primary_144,flag_144_safety, send_trigger_lane_change)

                        flag_144 = pass_144
                        primary_144 = safety_144
                        flag_144_safety = pass_144_safety


                        if(flag_144 == 1):

                            true_fact_145, false_fact_145, illegal_action_145= qm_145.mapping_145("C:/Users/bhuiyanh/PycharmProjects/Code-Complaince-Checking/atoms/145.txt", "145", av, tv, av_lane,tv_lane, 1, send_trigger_lane_change)

                            true_fact_141, false_fact_141, illegal_action_141= qm_141.mapping_141("C:/Users/bhuiyanh/PycharmProjects/Code-Complaince-Checking/atoms/141.txt", "141", av, tv, av_lane,tv_lane, 1)

                            #true_fact_140, false_fact_140, illegal_action_140= qm_140.mapping_140("C:/Users/bhuiyanh/PycharmProjects/Code-Complaince-Checking/atoms/140.txt", "140", av, tv, av_lane,tv_lane, lo, ro, user_require_tv_number, 1)

                            true_fact_140, false_fact_140, illegal_action_140, pass_140_safety = qm_140.mapping_140("C:/Users/bhuiyanh/PycharmProjects/Code-Complaince-Checking/atoms/140.txt", "140", av, tv, av_lane,tv_lane, lo, ro, user_require_tv_number, 1, flag_140_safety)
                            flag_140_safety = pass_140_safety

                        else:
                            true_fact_145, false_fact_145, illegal_action_145= qm_145.mapping_145("C:/Users/bhuiyanh/PycharmProjects/Code-Complaince-Checking/atoms/145.txt", "145", av, tv, av_lane,tv_lane, 0, send_trigger_lane_change)

                            true_fact_141, false_fact_141, illegal_action_141= qm_141.mapping_141("C:/Users/bhuiyanh/PycharmProjects/Code-Complaince-Checking/atoms/141.txt", "141", av, tv, av_lane,tv_lane, 0)

                            #true_fact_140, false_fact_140, illegal_action_140= qm_140.mapping_140("C:/Users/bhuiyanh/PycharmProjects/Code-Complaince-Checking/atoms/140.txt", "140", av, tv, av_lane,tv_lane, lo, ro, user_require_tv_number, 0)

                            true_fact_140, false_fact_140, illegal_action_140, pass_140_safety = qm_140.mapping_140("C:/Users/bhuiyanh/PycharmProjects/Code-Complaince-Checking/atoms/140.txt", "140", av, tv, av_lane,tv_lane, lo, ro, user_require_tv_number, 0, flag_140_safety)
                            flag_140_safety = pass_140_safety


                        #print(illegal_action)
                        illegal_action = illegal_action + illegal_action_144 + illegal_action_145 + illegal_action_141 + illegal_action_140
                        #fully_final_violate_action.append(illegal_action)
                        final_illegal_action2 = of.overall_mapping_illegal_action(illegal_action)

                        overall_true_fact = true_fact_145 + true_fact_144 + true_fact_141 + true_fact_140
                        overall_false_fact = false_fact_145 + false_fact_144 + false_fact_141 + false_fact_140

                        final_true_fact = of.overall_mapping_true(overall_true_fact)
                        final_false_fact = of.overall_mapping_false(overall_false_fact)

                        MyFile = open('true_fact.txt', 'w')
                        for element in final_true_fact:
                            MyFile.write(element)
                            MyFile.write('\n')
                        MyFile.close()

                        os.system('C:/Users/bhuiyanh/PycharmProjects/Code-Complaince-Checking/turnip-cli-20200624 145_144_141_140_rule.txt true_fact.txt > output.txt')

                        file1 = open('C:/Users/bhuiyanh/PycharmProjects/Code-Complaince-Checking/output.txt', 'r')

                        final_result = open("final_output.txt", 'a')

                        for line in file1:
                            #print(line)
                            '''
                            if ('[' in line and "[P]driver_Overtake_vehicle" not in line and "[F]driver_Overtake_vehicle" not in line and "[O]" not in line):
                                final_result.write(line)
                                #final_result.write("\n")
                                break
                            '''
                            if ("[P]driver_Overtake_vehicle" in line):
                                #print("yup")
                                final_result.write(line)
                                break
                            elif("[F]driver_Overtake_vehicle" in line):
                                final_result.write(line)
                                break
                            elif("[P]driver_OvertakeToTheLeftOf_vehicle" in line):
                                final_result.write(line)
                                break
                            elif("[F]driver_OvertakeToTheLeftOf_vehicle" in line):
                                final_result.write(line)
                                break

                        final_result.close()

                        file2 = open('C:/Users/bhuiyanh/PycharmProjects/Code-Complaince-Checking/final_output.txt', 'r')
                        for ab in file2:
                            ab = ab.strip()
                            l1 = ab.split('d')
                            l2 = l1[0].strip("[]")
                            l2=l2.strip()
                            plot_decision.append(l2)
                        file2.close()
                        file1.close()

                else:
                    print("This timestamp is not for left overtaking.. Please check the snapshot again")
                    #print("\n")
                    plot_decision.append(af)

            path1 = 'C:/Users/bhuiyanh/PycharmProjects/Code-Complaince-Checking/final_output.txt'

            isExist1 = os.path.exists(path1)

            if (isExist1):
                os.remove("final_output.txt")

        else:
            print("There are no vehicle, so no need to check anything")
            #print("\n")


elif (overtaking_type == "r" or overtaking_type == "R"):

    ro =1

    print("What time range you want to validate")

    start = int(input("Please give the start range"))
    end = int(input("Please give the end range"))

    start_time = time.time()

    plot_decision.clear()
    #timestamp_dict.clear()
    av_lane_number_dict.clear()
    send_trigger_lane_change = 0
    #res = {}

    for timestamp in range(start, end):

        #print("Creating Ontology")

        print("For timestamp", timestamp)
        plot_timestamp.append(timestamp)

        val = timestamp
        locate = val - 2
        print(locate)

        #locate = 2

        ## Behaviour Ontology Functions

        a: behaviour = behaviour()

        what_time = a.create_ontology_behaviour(data1, locate)
        plot_time.append(what_time)

        ## Environment Ontology Functions

        b: environment = environment()

        b.create_ontology_en(data2, locate)

        ### Declaring object for query_management class

        #print("Ontology creation done")
        #print("\n")
        #print("Now rule checking start and determining true facts based on rules")
        #print("\n")

        qbn = query_mapping_lane()
        qm_144 = query_mapping_144()
        qm_145 = query_mapping_145()
        qm_141 = query_mapping_141()
        qm_142 = query_mapping_142()
        qm_140 = query_mapping_140()
        qm_143_right = query_mapping_143_right()
        of = overall_mapping_for_atom()
        tv_ahead_of_av = tv_availability()
        position_find = av_tv_postion()


        atom_path = "C:/Users/bhuiyanh/PycharmProjects/Code-Complaince-Checking/atoms"
        atom_dirs = os.listdir(atom_path)  # Reading all in this directory

        # print("Now checking for what the system have to do compliance checking of traffic rule for vehicle or motorbike")


        if ("vehicle" in av):  # checking for vehicle

            # cache
            true_fact_145.clear()
            false_fact_145.clear()
            true_fact_144.clear()
            false_fact_144.clear()
            true_fact_143.clear()
            false_fact_143.clear()
            true_fact_141.clear()
            false_fact_141.clear()
            true_fact_140.clear()
            false_fact_140.clear()
            overall_true_fact.clear()
            overall_false_fact.clear()
            final_true_fact.clear()
            final_false_fact.clear()

            #print("For Target Vehicle-", i + 1)

            #if(av_behind_tv):

            # Lane Number count
            tn = "totallane"

            total_lane = qbn.mapping_lane(tn)
            # print("Total Lane",total_lane)

            # Bicycle Lane count

            bn = "bicycle"
            bicycle_lane = qbn.mapping_lane(bn)
            # print("Bicycle Lane",bicycle_lane)

            # AV lane number identify

            av_lane = qbn.mapping_av_lane(av)
            # print("AV Lane number",av_lane)

            #timestamp_dict.append(what_time)

            av_lane_number_dict.append(av_lane)
            #print(av_lane_number_dict)
            length = len(av_lane_number_dict)
            #print(length)


            if (locate > 5):

                #print(av_lane_number_dict[length-1])
                #print(av_lane_number_dict[length-2])

                if(av_lane_number_dict and length > 2):

                    if(av_lane_number_dict[length-1] != av_lane_number_dict[length-2]):
                        send_trigger_lane_change = 1
                    else:
                        send_trigger_lane_change = 0

            # TV lane count
            tv_lane = qbn.mapping_tv_lane(tv)
            # print("Target vehicle lane number", tv_lane)

            # TV speed

            tvs = qbn.mapping_tv_speed(tv)

            # TV displaying donotovertake sign

            tv_donot = qbn.vehicle_Display_doNot(tv)

            ## For getting positions

            pos_x_av, pos_y_av, pos_x_tv, pos_y_tv = position_find.get_position(av, tv)

            position_x_of_av.append(pos_x_av)
            position_y_of_av.append(pos_y_av)
            position_x_of_tv.append(pos_x_tv)
            position_y_of_tv.append(pos_y_tv)

            if (bicycle_lane > 0.0 and "bicycle" in av):

                # ******** FOR RULE 143, 144, 145 ***********#

                print("Then You have to follow Rule 144A and it is under developing.. We did not finish this developement yet")
                print("Sorry we are not considering bicycle issue here")

            elif ("motorbike" in av):
                print("I am not considering for motorbike. Sorry")


            else:

                af = 'F'

                if (av_lane == tv_lane or tv_lane == av_lane -1):

                    # av_behind_tv = tv_ahead_of_av.tv_distance(av, tv)

                    if(tv_donot == 1.0):

                        print("Following Rule 145, 144, 143, 142, 140")

                        #print("Yup I am checking do not overtake")

                        overall_true_fact = []
                        overall_false_fact = []

                        true_fact_144, false_fact_144, illegal_action_144, pass_144, safety_144, pass_144_safety = qm_144.mapping_144("C:/Users/bhuiyanh/PycharmProjects/Code-Complaince-Checking/atoms/144.txt", "144", av, tv, av_lane,tv_lane, flag_144, primary_144, flag_144_safety, send_trigger_lane_change)

                        flag_144 = pass_144
                        primary_144 = safety_144
                        flag_144_safety = pass_144_safety

                        if (flag_144 == 1):

                            true_fact_145, false_fact_145, illegal_action_145 = qm_145.mapping_145("C:/Users/bhuiyanh/PycharmProjects/Code-Complaince-Checking/atoms/145.txt", "145", av, tv, av_lane,tv_lane, 1, send_trigger_lane_change)

                            true_fact_143, false_fact_143, illegal_action_143 = qm_143_right.mapping_143_right("C:/Users/bhuiyanh/PycharmProjects/Code-Complaince-Checking/atoms/143r.txt", "143r", av, tv, av_lane,tv_lane, 1)

                            true_fact_142, false_fact_142, illegal_action_142 = qm_142.mapping_142("C:/Users/bhuiyanh/PycharmProjects/Code-Complaince-Checking/atoms/142.txt", "142", av, tv, av_lane,tv_lane, 1)


                            true_fact_140, false_fact_140, illegal_action_140, pass_140_safety = qm_140.mapping_140("C:/Users/bhuiyanh/PycharmProjects/Code-Complaince-Checking/atoms/140.txt", "140", av, tv, av_lane,tv_lane, lo, ro, user_require_tv_number, 1, flag_140_safety)
                            flag_140_safety = pass_140_safety

                        else:
                            true_fact_145, false_fact_145, illegal_action_145 = qm_145.mapping_145("C:/Users/bhuiyanh/PycharmProjects/Code-Complaince-Checking/atoms/145.txt", "145", av, tv, av_lane,tv_lane, 0, send_trigger_lane_change)

                            true_fact_143, false_fact_143, illegal_action_143 = qm_143_right.mapping_143_right("C:/Users/bhuiyanh/PycharmProjects/Code-Complaince-Checking/atoms/143r.txt", "143r", av, tv, av_lane,tv_lane,0)

                            true_fact_142, false_fact_142, illegal_action_142 = qm_142.mapping_142("C:/Users/bhuiyanh/PycharmProjects/Code-Complaince-Checking/atoms/142.txt", "142", av, tv, av_lane,tv_lane, 0)

                            true_fact_140, false_fact_140, illegal_action_140, pass_140_safety = qm_140.mapping_140("C:/Users/bhuiyanh/PycharmProjects/Code-Complaince-Checking/atoms/140.txt", "140", av, tv, av_lane,tv_lane, lo, ro, user_require_tv_number, 0, flag_140_safety)
                            flag_140_safety = pass_140_safety


                        illegal_action = illegal_action_144 + illegal_action_145 + illegal_action_143 + illegal_action_142 + illegal_action_140

                        #final_illegal_action = of.overall_mapping_illegal_action(illegal_action)
                        #fully_final_violate_action.append(illegal_action)
                        final_illegal_action3 = of.overall_mapping_illegal_action(illegal_action)

                        #  Making Overall True facts list

                        overall_true_fact = true_fact_145 + true_fact_144 + true_fact_143 +true_fact_142 + true_fact_140
                        overall_false_fact = false_fact_145 + false_fact_144 + false_fact_143 +false_fact_142 + false_fact_140

                        final_true_fact = of.overall_mapping_true(overall_true_fact)
                        final_false_fact = of.overall_mapping_false(overall_false_fact)

                        #print("\n")
                        #print("Overall True atom for this timestamp are:", final_true_fact)
                        #print("Overall False atom for this timestamp are:", final_false_fact)

                        #print("\n")
                        #print("Turnip reasoner is calling")

                        MyFile = open('true_fact.txt', 'w')
                        for element in final_true_fact:
                            MyFile.write(element)
                            MyFile.write('\n')
                        MyFile.close()

                        os.system('C:/Users/bhuiyanh/PycharmProjects/Code-Complaince-Checking/turnip-cli-20200624 145_144_143r_142_140_rule.txt true_fact.txt > output.txt')

                        file1 = open('C:/Users/bhuiyanh/PycharmProjects/Code-Complaince-Checking/output.txt', 'r')

                        final_result = open("final_output.txt", 'a')



                        for line in file1:
                            
                            '''
                            if ('[' in line and "[P]driver_Overtake_vehicle" not in line and "[F]driver_Overtake_vehicle" not in line and "[O]" not in line and "[P]driver_DrivePastToTheLeftOf_vehicle" not in line):
                                final_result.write(line)
                                # final_result.write("\n")
                                
                            '''

                            if ("[P]driver_Overtake_vehicle" in line):
                                #print("yup")
                                final_result.write(line)
                                break
                            elif("[F]driver_Overtake_vehicle" in line):
                                final_result.write(line)
                                break
                            elif("[P]driver_OvertakeToTheRightOf_vehicle" in line):
                                final_result.write(line)
                                break
                            elif("[F]driver_OvertakeToTheRightOf_vehicle" in line):
                                final_result.write(line)
                                break


                        final_result.close()

                        file2 = open('C:/Users/bhuiyanh/PycharmProjects/Code-Complaince-Checking/final_output.txt', 'r')
                        for ab in file2:
                            ab = ab.strip()
                            l1 = ab.split('d')
                            # print(l1)
                            l2 = l1[0].strip("[]")
                            l2 = l2.strip()
                            plot_decision.append(l2)
                        file2.close()
                        file1.close()

                    else:
                        print("Following Rule 145, 144, 142, 140")

                        # Primary Checking

                        true_fact_144, false_fact_144, illegal_action_144, pass_144, safety_144, pass_144_safety = qm_144.mapping_144("C:/Users/bhuiyanh/PycharmProjects/Code-Complaince-Checking/atoms/144.txt", "144", av, tv, av_lane,tv_lane, flag_144, primary_144, flag_144_safety, send_trigger_lane_change)

                        flag_144 = pass_144
                        primary_144 = safety_144
                        flag_144_safety = pass_144_safety

                        if (flag_144 == 1):

                            true_fact_145, false_fact_145, illegal_action_145 = qm_145.mapping_145("C:/Users/bhuiyanh/PycharmProjects/Code-Complaince-Checking/atoms/145.txt", "145", av, tv, av_lane,tv_lane, 1, send_trigger_lane_change)

                            true_fact_142, false_fact_142, illegal_action_142 = qm_142.mapping_142("C:/Users/bhuiyanh/PycharmProjects/Code-Complaince-Checking/atoms/142.txt", "142", av, tv, av_lane,tv_lane,1)

                            true_fact_140, false_fact_140, illegal_action_140, pass_140_safety = qm_140.mapping_140("C:/Users/bhuiyanh/PycharmProjects/Code-Complaince-Checking/atoms/140.txt", "140", av, tv, av_lane,tv_lane, lo, ro, user_require_tv_number,1, flag_140_safety)
                            flag_140_safety = pass_140_safety

                        else:
                            true_fact_145, false_fact_145, illegal_action_145 = qm_145.mapping_145("C:/Users/bhuiyanh/PycharmProjects/Code-Complaince-Checking/atoms/145.txt", "145", av, tv, av_lane,tv_lane, 0, send_trigger_lane_change)

                            true_fact_142, false_fact_142, illegal_action_142 = qm_142.mapping_142("C:/Users/bhuiyanh/PycharmProjects/Code-Complaince-Checking/atoms/142.txt", "142", av, tv, av_lane,tv_lane,0)

                            true_fact_140, false_fact_140, illegal_action_140, pass_140_safety = qm_140.mapping_140("C:/Users/bhuiyanh/PycharmProjects/Code-Complaince-Checking/atoms/140.txt", "140", av, tv, av_lane,tv_lane, lo, ro, user_require_tv_number,0, flag_140_safety)
                            flag_140_safety = pass_140_safety


                        illegal_action = illegal_action_144 + illegal_action_145 + illegal_action_142 + illegal_action_140

                        #final_illegal_action = of.overall_mapping_illegal_action(illegal_action)
                        #fully_final_violate_action.append(illegal_action)
                        final_illegal_action4 = of.overall_mapping_illegal_action(illegal_action)

                        #  Making Overall True facts list

                        overall_true_fact = true_fact_145 + true_fact_144 + true_fact_142 + true_fact_140
                        overall_false_fact = false_fact_145 + false_fact_144 + false_fact_142 + false_fact_140

                        final_true_fact = of.overall_mapping_true(overall_true_fact)
                        final_false_fact = of.overall_mapping_false(overall_false_fact)


                        #final_true_fact = of.overall_mapping_true(overall_true_fact)
                        #final_false_fact = of.overall_mapping_false(overall_false_fact)

                        MyFile = open('true_fact.txt', 'w')
                        for element in final_true_fact:
                            MyFile.write(element)
                            MyFile.write('\n')
                        MyFile.close()

                        os.system('C:/Users/bhuiyanh/PycharmProjects/Code-Complaince-Checking/turnip-cli-20200624 145_144_142_140_rule.txt true_fact.txt > output.txt')

                        file1 = open('C:/Users/bhuiyanh/PycharmProjects/Code-Complaince-Checking/output.txt', 'r')

                        final_result = open("final_output.txt", 'a')


                        for line in file1:
                            '''
                            if ('[' in line and "[P]driver_Overtake_vehicle" not in line and "[F]driver_Overtake_vehicle" not in line and "[O]" not in line):
                                final_result.write(line)
                                # final_result.write("\n")
                            '''

                            if ("[P]driver_Overtake_vehicle" in line):
                                # print("yup")
                                final_result.write(line)
                                break
                            elif ("[F]driver_Overtake_vehicle" in line):
                                final_result.write(line)
                                break
                            elif ("[P]driver_OvertakeToTheRightOf_vehicle" in line):
                                final_result.write(line)
                                break
                            elif ("[F]driver_OvertakeToTheRightOf_vehicle" in line):
                                final_result.write(line)
                                break


                        final_result.close()

                        file2 = open('C:/Users/bhuiyanh/PycharmProjects/Code-Complaince-Checking/final_output.txt', 'r')
                        for ab in file2:
                            ab = ab.strip()
                            l1 = ab.split('d')
                            l2 = l1[0].strip("[]")
                            l2 = l2.strip()
                            plot_decision.append(l2)
                        file2.close()
                        file1.close()

                else:
                    print("This is not for right overtaking.. please see the snapshot again")
                    plot_decision.append(af)

            path1 = 'C:/Users/bhuiyanh/PycharmProjects/Code-Complaince-Checking/final_output.txt'

            isExist1 = os.path.exists(path1)

            if (isExist1):
                os.remove("final_output.txt")

        else:
            print("There are no vehicle, so no need to check anything")
            #print("\n")

else:
    print("Your input was wrong.... Try again.......")
    # goto

### Final Decision #####


fully_final_illegal_action = final_illegal_action1 + final_illegal_action2 +final_illegal_action3 + final_illegal_action4

if('Target Vehicle intended to turn right' in fully_final_illegal_action and 'Target Vehicle intended to make U-Turn' in fully_final_illegal_action):

    fully_final_illegal_action = [w.replace('Target Vehicle intended to make U-Turn', 'Target Vehicle intended to turn right') for w in fully_final_illegal_action]

    if ('Target Vehicle intended to go right' in fully_final_illegal_action):
        #print("yessssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssss gotttttttttttttttttttttttttttttttttttttttttt")
        fully_final_illegal_action = [w.replace('Target Vehicle intended to go right', 'Target Vehicle intended to turn right') for w in fully_final_illegal_action]

if('Target Vehicle intended to turn right' in fully_final_illegal_action and 'Target Vehicle intended to go right' in fully_final_illegal_action):

        fully_final_illegal_action = [w.replace('Target Vehicle intended to go right', 'Target Vehicle intended to turn right') for w in fully_final_illegal_action]


if('Target Vehicle intended to turn left' in fully_final_illegal_action and 'Target Vehicle intended to make U-Turn' in fully_final_illegal_action):

    fully_final_illegal_action = [w.replace('Target Vehicle intended to make U-Turn', 'Target Vehicle intended to turn left') for w in fully_final_illegal_action]

    if ('Target Vehicle intended to go left' in fully_final_illegal_action):
        #print("yessssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssss gotttttttttttttttttttttttttttttttttttttttttt")
        fully_final_illegal_action = [w.replace('Target Vehicle intended to go left', 'Target Vehicle intended to turn left') for w in fully_final_illegal_action]

if('Target Vehicle intended to turn left' in fully_final_illegal_action and 'Target Vehicle intended to go left' in fully_final_illegal_action):

        fully_final_illegal_action = [w.replace('Target Vehicle intended to go left', 'Target Vehicle intended to turn left') for w in fully_final_illegal_action]


last_fully_final_illegal_action.clear()

for action in fully_final_illegal_action:
    #print(action)
    if action not in last_fully_final_illegal_action:  # not a duplicate
        last_fully_final_illegal_action.append(action)


#if ('F' or 'N' in plot_decision):
if ('F' in plot_decision):
    print("The manouever action is illegal")

    print("\nReason for Illegal manuevers")

    #fully_final_illegal_action = of.overall_mapping_illegal_action(fully_final_illegal_action)
    print(last_fully_final_illegal_action)
    #print(b)


else:
    print("The manouever action is legal")


print("Process complete")

print("\n")

print("--- Execution Time : %s seconds ---" % (time.time() - start_time))


print(plot_timestamp)
print(plot_decision)
################ Sending for plotting #########
for i in range(len(plot_timestamp)):
    print(plot_timestamp[i],"=", plot_decision[i], end = ', ')

#print(plot_decision)
print(len(plot_decision))

b1_col_name = av + " positionx"
c1_col_name = av + " positiony"
d1_col_name = tv + " positionx"
e1_col_name = tv + " positiony"

# plot_timestamp
# position_x_of_av.append
# position_y_of_av.append
# position_x_of_tv.append
# position_y_of_tv.append
# plot_decision

worksheet_data.write('A1', 'Time')
worksheet_data.write('B1', 'Timestamp')
worksheet_data.write('C1', b1_col_name)
worksheet_data.write('D1', c1_col_name)
worksheet_data.write('E1', d1_col_name)
worksheet_data.write('F1', e1_col_name)
worksheet_data.write('G1', 'Result')



row = 1
column = 0

for item in plot_time:
    worksheet_data.write(row, column, item)
    row += 1


row = 1
column = 1

for item in plot_timestamp:
    worksheet_data.write(row, column, item)
    row += 1

row = 1
column = 2

for item in position_x_of_av:
    worksheet_data.write(row, column, item)
    row += 1

row = 1
column = 3

for item in position_y_of_av:
    worksheet_data.write(row, column, item)
    row += 1

row = 1
column = 4

for item in position_x_of_tv:
    worksheet_data.write(row, column, item)
    row += 1

row = 1
column = 5

for item in position_y_of_tv:
    worksheet_data.write(row, column, item)
    row += 1

row = 1
column = 6

for item in plot_decision:
    worksheet_data.write(row, column, item)
    row += 1


workbook.close()


############# Now Calling the plotting ##########
#b = 1
result_plotting(av, tv)



################ Done with plotting #########
