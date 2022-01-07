import math
from owlready2 import *
from query_check_for_av_b import *
from query_check_for_av_e import *

qb = query_behaviour()
qe = query_environment()


class safety_border_check_for_target_vehicle:

    def safety_check_for_target_vehicle(self,which_tv):

        self.which_tv = which_tv

        onto = get_ontology("C:/Users/bhuiyanh/OneDrive - Queensland University of Technology/Ontology- Protege/av_info_behaviour.owl")
        onto.load()


        ## Modifying query return from ontology ##

        def modify(a):
            answer3 = float(a)
            answer4 = round(answer3, 2)
            return answer4


        sparql = "SELECT ?is_speed WHERE {ab:vehicle ab:is_speed ?is_speed.}"

        answer_tv = qb.query_trigger_for_behaviour(sparql, which_tv)
        answer2_tv = modify(answer_tv[0])
        speed_of_tv = answer2_tv

        #sfaety_border = ((speed_of_tv * 1000 * 2) / 3600)
        #print(sfaety_border)

        tv_reaction_time = 1

        tv_reaction_time_distance = (speed_of_tv * tv_reaction_time) / 3.6

        #return sfaety_border

        return tv_reaction_time_distance




#a = safe_distance_check()

#a.safety()