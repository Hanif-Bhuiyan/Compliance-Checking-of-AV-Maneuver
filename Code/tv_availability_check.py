import math
from owlready2 import *
from query_check_for_av_b import *
from query_check_for_av_e import *

qb = query_behaviour()
qe = query_environment()

#speed_of_tv = []
#position_x_of_tv = []
#position_y_of_tv = []
#heading_of_tv = []


class tv_availability:

    def tv_distance(self,which_av, which_tv):

        self.which_av= which_av
        self.which_tv = which_tv

        onto = get_ontology(
            "C:/Users/bhuiyanh/OneDrive - Queensland University of Technology/Ontology- Protege/av_info_behaviour.owl")
        onto.load()


        ## Modifying query return from ontology ##

        def modify(a):
            answer3 = float(a)
            answer4 = round(answer3, 2)
            return answer4

        ### End of this block ###

        # This block is reading the text files, like -  C:/Users/bhuiyanh/PycharmProjects/Practise06/query/m/sparql\s_1.txt

        #print("Here firts vehicle is considered as av and others vehicle will be considered as target vehicles")

        instance = str(onto.timestamp.instances())
        instance1 = instance.split(".", 1)
        instance2 = instance1[-1].replace("]", "")


        #print("Timestamp:", instance2)


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

                if ("is_positionx" in sparql):

                    answer_av = qb.query_trigger_for_behaviour(sparql, self.which_av)
                    answer2_av = modify(answer_av[0])
                    position_x_of_av = answer2_av


                    answer_tv = qb.query_trigger_for_behaviour(sparql, self.which_tv)
                    answer2_tv = modify(answer_tv[0])
                    #print(answer2_tv)
                    position_x_of_tv = answer2_tv


                if ("is_positiony" in sparql):

                    answer_av = qb.query_trigger_for_behaviour(sparql, self.which_av)
                    answer2_av = modify(answer_av[0])
                    position_y_of_av = answer2_av


                    answer_tv = qb.query_trigger_for_behaviour(sparql, self.which_tv)
                    answer2_tv = modify(answer_tv[0])
                    #print(answer2_tv)
                    position_y_of_tv = answer2_tv



        av_distance_calc = (position_x_of_av * position_x_of_av) + (position_y_of_av * position_y_of_av)
        av_distance = math.sqrt(av_distance_calc)
        av_distance = abs(av_distance)

        tv_distance_calc = (position_x_of_tv * position_x_of_tv) + (position_y_of_tv * position_y_of_tv)
        tv_distance = math.sqrt(tv_distance_calc)
        tv_distance = abs(tv_distance)

        #print("The distance between Target Vehicle (TV) and AV is:", tv_distance - av_distance)


        if(tv_distance > av_distance ):
            return True
        else:
            return False


    '''
        if (position_x_of_av > 0):

            if (tv_distance > av_distance):
                return True
            else:
                return False
        else:
            if (tv_distance > av_distance):
                return False
            else:
                return True
    '''
