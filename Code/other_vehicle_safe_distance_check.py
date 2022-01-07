from owlready2 import *
from safe_distance02 import *



class av_after_tv:

    def av_after(self, which_av, which_tv):

        print("Other Vehicle Checking")

        self.which_av = which_av
        self.which_tv = which_tv

        onto = get_ontology(
            "C:/Users/bhuiyanh/OneDrive - Queensland University of Technology/Ontology- Protege/av_info_behaviour.owl")
        onto.load()

        av_behind_tv = tv_ahead_of_av.tv_distance(self.which_av, self.which_tv)

        ## Modifying query return from ontology ##

        def modify(a):
            answer3 = float(a)
            answer4 = round(answer3, 2)
            return answer4

        instance = str(onto.timestamp.instances())
        instance1 = instance.split(".", 1)
        instance2 = instance1[-1].replace("]", "")


        sparql_path = "C:/Users/bhuiyanh/PycharmProjects/Practise19/query/m"
        sparql_dir = os.listdir(sparql_path)  # Reading all in this directory

        for sparql_file in sparql_dir:  ## reading inside of atom folder (c, r_140, r_142... one by one)
            sparql_file.strip()
            sparql_check = os.path.join(sparql_path, sparql_file)
            # print(sparql_check)
            sparql_filename = sparql_file.split("'\'")


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

        av_speed = speed_of_av
        # print("AV speed", av_speed)

        av_distance_calc = (position_x_of_av * position_x_of_av) + (position_y_of_av * position_y_of_av)
        av_distance1 = math.sqrt(av_distance_calc)
        av_distance = av_distance1 - 4.5
        # print("AV distance:", av_distance)

        av_heading = heading_of_av
        # print("AV heading:", av_heading)

        # av_acceleration = abs(acceleration_of_av)
        av_acceleration = acceleration_of_av
        # av_acceleration = 1.60

        # print("AV acceleration:", av_acceleration)

        av_reaction_time = 0.0
        # print("AV reactione time:", av_reaction_time)

        av_reaction_time_distance = (av_speed * av_reaction_time) / 3.6
        av_braking_distance = (av_speed * av_speed) / (2 * 0.7 * 9.8)
        av_stopping_distance = av_reaction_time_distance + av_braking_distance
        # print("AV stopping distance:", av_stopping_distance)

        if (av_stopping_distance == 0.0):
            av_stopping_distance = 1.0

        av_stopping_time = av_speed / (2 * av_stopping_distance)

        tv_speed = speed_of_tv
        # print("tv speed", tv_speed)

        tv_distance_calc = (position_x_of_tv * position_x_of_tv) + (position_y_of_tv * position_y_of_tv)
        tv_distance1 = math.sqrt(tv_distance_calc)
        tv_distance = tv_distance1 - 4.5
        # print("TV distance:", tv_distance)

        tv_heading = heading_of_tv
        # print("tv heading:", tv_heading)

        # tv_acceleration = abs(acceleration_of_tv)
        tv_acceleration = acceleration_of_tv

        # tv_acceleration = 1.93

        # print("tv acceleration:", tv_acceleration)

        tv_reaction_time = 0.0
        # print("tv reactione time:", tv_reaction_time)

        tv_reaction_time_distance = (tv_speed * tv_reaction_time) / 3.6
        tv_braking_distance = (tv_speed * tv_speed) / (2 * 0.7 * 9.8)
        tv_stopping_distance = tv_reaction_time_distance + tv_braking_distance

        if (tv_stopping_distance == 0.0):
            tv_stopping_distance = 1.0
        # print("tv stopping distance:", tv_stopping_distance)

        tv_stopping_time = tv_speed / (2 * tv_stopping_distance)

        tv_velocity_afteremergencybrake_in_raection_time = tv_speed + (-tv_acceleration * 0.3)

        d_rel = tv_distance - av_distance
        # print("Relative Distance:", d_rel)

        reaction_time = 0.3

        if (av_acceleration == 0.0):
            av_acceleration = 1.0
        if (tv_acceleration == 0.0):
            tv_acceleration = 1.0

        av_acceleration1 = - abs(av_acceleration)
        tv_acceleration1 = - abs(tv_acceleration)

        stopping_distance_difference = av_stopping_distance - tv_stopping_distance

        # Obvious collision in freedom -  case -1

        if (av_stopping_distance >= tv_stopping_distance and d_rel < stopping_distance_difference):
            print("case 2")
            #return False
            return -1

        elif (av_stopping_distance < tv_distance):
            print("Case-1")
            safe_distance_1 = - ((av_speed * av_speed) / (2 * (av_acceleration1)))
            print("safe_distance_1:", safe_distance_1)
            #return True
            return safe_distance_1


        elif (tv_distance <= av_stopping_distance and av_stopping_distance < tv_stopping_distance):
            print("Case-3")

            if (tv_distance <= av_stopping_distance and (
                    (tv_acceleration1 > av_acceleration1) and (tv_speed < av_speed) and (
                    av_stopping_time < tv_stopping_time))):

                safe_distance_3 = ((tv_speed - av_speed) * (tv_speed - av_speed)) / (
                        2 * (tv_acceleration1 - av_acceleration1))
                print("safe_distance_3:", safe_distance_3)
                #return True
                return safe_distance_3

            else:
                safe_distance_2 = ((tv_speed * tv_speed) / (2 * tv_acceleration1)) - (
                        (av_speed * av_speed) / (2 * av_acceleration1))
                print("safe_distance_2:", safe_distance_2)
                #return True
                return safe_distance_2

        else:
            print("Could not figure out the safe distance")
            #return True
            return 1