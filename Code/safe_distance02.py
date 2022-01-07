import math
from owlready2 import *
from query_check_for_av_b import *
from query_check_for_av_e import *
from tv_availability_check import *
from primary_checking_info import *

qb = query_behaviour()
qe = query_environment()
tv_ahead_of_av = tv_availability()
qbn = query_mapping_lane()

#speed_of_tv = []
#position_x_of_tv = []
#position_y_of_tv = []
#heading_of_tv = []


class safe_distance_check:

    def safety(self, which_av, which_tv):

        self.which_av= which_av
        self.which_tv = which_tv

        onto = get_ontology("C:/Users/bhuiyanh/OneDrive - Queensland University of Technology/Ontology- Protege/av_info_behaviour.owl")
        onto.load()

        av_behind_tv = tv_ahead_of_av.tv_distance(self.which_av, self.which_tv)

        ## Modifying query return from ontology ##

        def modify(a):
            answer3 = float(a)
            answer4 = round(answer3, 2)
            return answer4

        ### End of this block ###

        # This block is reading the text files, like -  C:/Users/bhuiyanh/PycharmProjects/Practise06/query/m/sparql\s_1.txt

        #print("Here firts vehicle is considered as av and others vehicle will be considered as target vehicles")

        #if (av_behind_tv):

        instance = str(onto.timestamp.instances())
        instance1 = instance.split(".", 1)
        instance2 = instance1[-1].replace("]", "")

        # print("Timestamp:", instance2)

        sparql_path = "C:/Users/bhuiyanh/PycharmProjects/Code-Complaince-Checking/query/m"
        sparql_dir = os.listdir(sparql_path)  # Reading all in this directory

        for sparql_file in sparql_dir:  ## reading inside of atom folder (c, r_140, r_142... one by one)
            sparql_file.strip()
            sparql_check = os.path.join(sparql_path, sparql_file)
            # print(sparql_check)
            sparql_filename = sparql_file.split("'\'")
            # print(sparql_filename[-1].strip())

            ####### End of thsi block #########

            ### This block reading one by one file content now ######

            for line in open(sparql_check, "r"):
                # print(line)
                sparql = line.strip()
                # print(sparql)

                answer_av = ""
                answer2_av = ""
                answer_tv = ""
                answer2_tv = ""

                ####### End of this block #########

                if ("is_speed" in sparql):
                    answer_av = qb.query_trigger_for_behaviour(sparql, self.which_av)
                    answer2_av = modify(answer_av[0])
                    speed_of_av = answer2_av

                    answer_tv = qb.query_trigger_for_behaviour(sparql, self.which_tv)
                    answer2_tv = modify(answer_tv[0])
                    speed_of_tv = answer2_tv

                if ("is_positionx" in sparql):
                    answer_av = qb.query_trigger_for_behaviour(sparql, self.which_av)
                    answer2_av = modify(answer_av[0])
                    position_x_of_av = answer2_av

                    answer_tv = qb.query_trigger_for_behaviour(sparql, self.which_tv)
                    answer2_tv = modify(answer_tv[0])
                    # print(answer2_tv)
                    position_x_of_tv = answer2_tv

                if ("is_positiony" in sparql):
                    answer_av = qb.query_trigger_for_behaviour(sparql, self.which_av)
                    answer2_av = modify(answer_av[0])
                    position_y_of_av = answer2_av

                    answer_tv = qb.query_trigger_for_behaviour(sparql, self.which_tv)
                    answer2_tv = modify(answer_tv[0])
                    # print(answer2_tv)
                    position_y_of_tv = answer2_tv

                if ("is_heading" in sparql):
                    answer_av = qb.query_trigger_for_behaviour(sparql, self.which_av)
                    answer2_av = modify(answer_av[0])
                    heading_of_av = answer2_av

                    answer_tv = qb.query_trigger_for_behaviour(sparql, self.which_tv)
                    answer2_tv = modify(answer_tv[0])
                    heading_of_tv = answer2_tv

                if ("is_acceleration" in sparql):
                    answer_av = qb.query_trigger_for_behaviour(sparql, self.which_av)
                    answer2_av = modify(answer_av[0])
                    acceleration_of_av = answer2_av

                    answer_tv = qb.query_trigger_for_behaviour(sparql, self.which_tv)
                    answer2_tv = modify(answer_tv[0])
                    acceleration_of_tv = answer2_tv

        av_speed = ((speed_of_av * 1000) / 3600)
        #print("AV speed", av_speed)

        av_distance_calc = (position_x_of_av * position_x_of_av) + (position_y_of_av * position_y_of_av)
        av_distance1 = math.sqrt(av_distance_calc)
        av_distance = av_distance1 - 4.5
        #print("AV distance:", av_distance)

        av_heading = heading_of_av
        #print("AV heading:", av_heading)

        #av_acceleration = abs(acceleration_of_av)
        av_acceleration = acceleration_of_av
        # av_acceleration = 1.60

        #print("AV acceleration:", av_acceleration)

        av_reaction_time = 0.0
        #print("AV reactione time:", av_reaction_time)

        av_reaction_time_distance = (av_speed * av_reaction_time) / 3.6
        av_braking_distance = (av_speed * av_speed) / (2 * 0.7 * 9.8)
        av_stopping_distance = av_reaction_time_distance + av_braking_distance
        #print("AV stopping distance:", av_stopping_distance)

        if (av_stopping_distance == 0.0):
            av_stopping_distance = 1.0

        av_stopping_time = av_speed / (2 * av_stopping_distance)

        tv_speed = ((speed_of_tv * 1000) / 3600)
        #print("tv speed", tv_speed)

        tv_distance_calc = (position_x_of_tv * position_x_of_tv) + (position_y_of_tv * position_y_of_tv)
        tv_distance1 = math.sqrt(tv_distance_calc)
        tv_distance = tv_distance1 - 4.5
        #print("TV distance:", tv_distance)

        tv_heading = heading_of_tv
        #print("tv heading:", tv_heading)

        #tv_acceleration = abs(acceleration_of_tv)
        tv_acceleration = acceleration_of_tv

        # tv_acceleration = 1.93

        #print("tv acceleration:", tv_acceleration)

        tv_reaction_time = 0.0
        #print("tv reactione time:", tv_reaction_time)

        tv_reaction_time_distance = (tv_speed * tv_reaction_time) / 3.6
        tv_braking_distance = (tv_speed * tv_speed) / (2 * 0.7 * 9.8)
        tv_stopping_distance = tv_reaction_time_distance + tv_braking_distance

        if (tv_stopping_distance == 0.0):
            tv_stopping_distance = 1.0
        #print("tv stopping distance:", tv_stopping_distance)

        tv_stopping_time = tv_speed / (2 * tv_stopping_distance)

        tv_velocity_afteremergencybrake_in_raection_time = tv_speed + (-tv_acceleration * 0.3)

        d_rel = tv_distance - av_distance
        #print("Relative Distance:", d_rel)

        reaction_time = 0.3

        if (av_acceleration == 0.0):
            av_acceleration = 1.0
        if (tv_acceleration == 0.0):
            tv_acceleration = 1.0

        #av_acceleration1 = - av_acceleration
        #tv_acceleration1 = - tv_acceleration

        av_acceleration1 = - abs(av_acceleration)
        tv_acceleration1 = - abs(tv_acceleration)

        stopping_distance_difference = av_stopping_distance - tv_stopping_distance


        safe_av_lane = qbn.mapping_av_lane(self.which_av)
        safe_tv_lane = qbn.mapping_tv_lane(self.which_tv)

        # Obvious collision in freedom -  case -1

        if(safe_av_lane == safe_tv_lane):

            if(tv_speed > 0.0):

                #if (av_stopping_distance >= tv_stopping_distance and d_rel < stopping_distance_difference):
                if (av_stopping_distance >= d_rel + tv_stopping_distance):
                    print("case 2")
                    return False

                elif (av_stopping_distance < tv_distance):
                    print("Case-1")
                    safe_distance_1 = - ((av_speed * av_speed) / (2 * (av_acceleration1)))
                    print("safe_distance_1:", safe_distance_1)
                    #return True
                    if (safe_distance_1 > 0):
                        return True
                    else:
                        return False

                elif (tv_distance <= av_stopping_distance and av_stopping_distance < tv_stopping_distance):
                    print("Case-3")

                    if (tv_distance <= av_stopping_distance and (
                            (tv_acceleration1 > av_acceleration1) and (tv_speed < av_speed) and (
                            av_stopping_time < tv_stopping_time))):

                        safe_distance_3 = ((tv_speed - av_speed) * (tv_speed - av_speed)) / (
                                    2 * (tv_acceleration1 - av_acceleration1))
                        print("safe_distance_3:", safe_distance_3)
                        #return True
                        if (safe_distance_3 > 0):
                            return True
                        else:
                            return False

                    else:
                        safe_distance_2 = ((tv_speed * tv_speed) / (2 * tv_acceleration1)) - (
                                    (av_speed * av_speed) / (2 * av_acceleration1))
                        print("safe_distance_2:", safe_distance_2)
                        #return True
                        if (safe_distance_2 > 0):
                            return True
                        else:
                            return False

                else:
                    print("Could not figure out the safe distance")
                    return True

            else:

                if (av_stopping_distance >= d_rel):
                    print("case 2")
                    #return False

                elif (av_stopping_distance < tv_distance):
                    print("Case-1")
                    safe_distance_1 = - ((av_speed * av_speed) / (2 * (av_acceleration1)))
                    print("safe_distance_1:", safe_distance_1)

                    if(safe_distance_1 > 0):
                        return True
                    else:
                        return False

                elif (tv_distance <= av_stopping_distance and av_stopping_distance < tv_stopping_distance):
                    print("Case-3")

                    if (tv_distance <= av_stopping_distance and (
                            (tv_acceleration1 > av_acceleration1) and (tv_speed < av_speed) and (
                            av_stopping_time < tv_stopping_time))):

                        safe_distance_3 = ((tv_speed - av_speed) * (tv_speed - av_speed)) / (
                                    2 * (tv_acceleration1 - av_acceleration1))
                        print("safe_distance_3:", safe_distance_3)

                        if (safe_distance_3 > 0):
                            return True
                        else:
                            return False

                    else:
                        safe_distance_2 = ((tv_speed * tv_speed) / (2 * tv_acceleration1)) - (
                                    (av_speed * av_speed) / (2 * av_acceleration1))
                        print("safe_distance_2:", safe_distance_2)

                        if (safe_distance_2 > 0):
                            return True
                        else:
                            return False

                else:
                    print("Could not figure out the safe distance")
                    return True

        else:
            return True
        #else:
            #print("Could not figure out the safe distance")
            #return True