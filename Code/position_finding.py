import math
from owlready2 import *

import xlsxwriter

from query_check_for_av_b import *
from query_check_for_av_e import *

qb = query_behaviour()
qe = query_environment()


# speed_of_tv = []
#position_x_of_av = []
#position_y_of_av = []
#position_x_of_tv = []
#position_y_of_tv = []
# heading_of_tv = []


class av_tv_postion:

    def get_position(self, which_av, which_tv):
        self.which_av = which_av
        self.which_tv = which_tv

        onto = get_ontology(
            "C:/Users/bhuiyanh/OneDrive - Queensland University of Technology/Ontology- Protege/av_info_behaviour.owl")
        onto.load()

        def modify(a):
            answer3 = float(a)
            answer4 = round(answer3, 2)
            return answer4

        answer_av_x_1 = ""
        answer_av_x =""
        answer_av_y_1=""
        answer_av_y=""

        answer_tv_x_1 = ""
        answer_tv_x = ""
        answer_tv_y_1 = ""
        answer_tv_y=""

        sparql_x = "SELECT ?is_positionx WHERE {ab:vehicle ab:is_positionx ?is_positionx.}"
        sparql_y = "SELECT ?is_positiony WHERE {ab:vehicle ab:is_positiony ?is_positiony.}"

        answer_av_x_1 = qb.query_trigger_for_behaviour(sparql_x, self.which_av)
        answer_av_x = modify(answer_av_x_1[0])
        #position_x_of_av.append(answer_av_x)


        answer_av_y_1 = qb.query_trigger_for_behaviour(sparql_y, self.which_av)
        answer_av_y = modify(answer_av_y_1[0])
        #position_y_of_av.append(answer_av_y)

        answer_tv_x_1 = qb.query_trigger_for_behaviour(sparql_x, self.which_tv)
        answer_tv_x = modify(answer_tv_x_1[0])
        #position_x_of_tv.append(answer_tv_x)

        answer_tv_y_1 = qb.query_trigger_for_behaviour(sparql_y, self.which_tv)
        answer_tv_y = modify(answer_tv_y_1[0])
        #position_y_of_tv.append(answer_tv_y)

        return answer_av_x, answer_av_y, answer_tv_x, answer_tv_y



# a = safe_distance_check()

# a.safety()
