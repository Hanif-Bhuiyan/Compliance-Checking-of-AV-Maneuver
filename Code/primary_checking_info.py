from owlready2 import *
import os
import math
from query_check_for_av_b import *
from query_check_for_av_e import *


true_atom = []
false_atom = []

qe = query_environment()
qb = query_behaviour()

class query_mapping_lane:

    def mapping_lane(self, bn):
        self.bn = bn

        answer =""
        answer2 = ""

        def modify(a):
            answer3 = float(a)
            answer4 = round(answer3, 1)
            return answer4

        if (self.bn == "totallane"):

            sparql_line = "SELECT ?is_totallane WHERE {ae:time ae:is_totallane ?is_totallane}"

            answer = qe.query_trigger_for_environment(sparql_line)
            answer2 = modify(answer[0])
            return answer2


        if(self.bn == "bicycle"):

            sparql_line= "SELECT ?is_bicycleway WHERE {ae:time ae:is_bicycleway ?is_bicycleway}"

            answer = qe.query_trigger_for_environment(sparql_line)
            answer2 = modify(answer[0])
            return answer2


    def mapping_av_lane(self, av):

        self.av=av
        def modify(a):
            answer3 = float(a)
            answer4 = round(answer3, 1)
            return answer4

        answer = ""
        answer2 = ""

        #print(self.av)
        sparql_line = "SELECT ?is_lanenumber WHERE {ab:vehicle ab:is_lanenumber ?is_lanenumber.}"

        answer = qb.query_trigger_for_behaviour(sparql_line, self.av)
        #print(answer)
        answer2 = modify(answer[0])
        return answer2


    def mapping_tv_lane(self, tv):

        self.tv = tv

        def modify(a):
            answer3 = float(a)
            answer4 = round(answer3, 1)
            return answer4

        answer = ""
        answer2 = ""

        #print(self.tv)
        sparql_line = "SELECT ?is_lanenumber WHERE {ab:vehicle ab:is_lanenumber ?is_lanenumber.}"

        answer = qb.query_trigger_for_behaviour(sparql_line, self.tv)
        answer2 = modify(answer[0])
        return answer2

    def mapping_tv_speed(self, tv):

        self.tv = tv

        def modify(a):
            answer3 = float(a)
            answer4 = round(answer3, 1)
            return answer4

        answer = ""
        answer2 = ""

        # print(self.tv)
        sparql_line = "SELECT ?is_speed WHERE {ab:vehicle ab:is_speed ?is_speed.}"

        answer = qb.query_trigger_for_behaviour(sparql_line, self.tv)
        answer2 = modify(answer[0])
        return answer2

    def vehicle_Display_doNot(self, tv):

        self.tv = tv

        def modify(a):
            answer3 = float(a)
            answer4 = round(answer3, 1)
            return answer4

        answer = ""
        answer2 = ""

        # print(self.tv)
        sparql_line = "SELECT ?is_donotovertakesign WHERE {ab:vehicle ab:is_donotovertakesign ?is_donotovertakesign.}"

        answer = qb.query_trigger_for_behaviour(sparql_line, self.tv)
        answer2 = modify(answer[0])
        return answer2
