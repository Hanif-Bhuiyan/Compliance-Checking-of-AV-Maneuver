import pandas as pd
from owlready2 import *

class environment:


    def create_ontology_en(self, data, index):

        self.onto = get_ontology("C:/Users/bhuiyanh/OneDrive - Queensland University of Technology/Ontology- Protege/av_info_environment.owl").load()

        with self.onto:

            class environment(Thing):
                pass

            class roadspeed(environment):
                pass

            class totallane(environment):
                pass

            class roadsign(environment):
                pass

            class nofiltersign(roadsign):
                pass

            class endsign(roadsign):
                pass

            class roadconnection(environment):
                pass

            class intersection(roadconnection):
                pass

            class crossingwithouttrafficsign(roadconnection):
                pass

            class crossingwithtrafficsign(roadconnection):
                pass

            class railcrossing(roadconnection):
                pass

            class roundabout(roadconnection):
                pass

            class pedestriancrossing(roadconnection):
                pass

            class roadmarking(environment):
                pass

            class brokencenterline(roadmarking):
                pass

            class continouscenterline(roadmarking):
                pass

            class givewayline(roadmarking):
                pass

            class stopline(roadmarking):
                pass

            class specialzone(environment):
                pass

            class schoolzone(specialzone):
                pass

            class hospitalzone(specialzone):
                pass

            class universityzone(specialzone):
                pass

            class roadmaintanance(specialzone):
                pass

            class sharedzone(specialzone):
                pass

            class lane(environment):
                pass

            class markedlane(lane):
                pass

            class nonmarkedlane(lane):
                pass

            class roadtype(environment):
                pass

            class busway(roadtype):
                pass

            class bicycleway(roadtype):
                pass

            class freeway(roadtype):
                pass

            class highway(roadtype):
                pass

            class motorway(roadtype):
                pass

            class localstreet(roadtype):
                pass

            class twowayroad(roadtype):
                pass

            class weathercondition(environment):
                pass

            class foggyweather(weathercondition):
                pass

            class heavyrain(weathercondition):
                pass

            class notenoughlight(weathercondition):
                pass

        with self.onto:
            class timestamp(Thing):
                pass

        ################
        ## Creating Individuals - I can create ind - thsi are static... so I can do it.. cz it will not change anymore

        roadspeed("roads")
        nofiltersign("nofilters")
        endsign("ends")
        intersection("intersec")
        crossingwithouttrafficsign("croswithoutts")
        crossingwithtrafficsign("crosswithts")
        railcrossing("railc")
        roundabout("rounda")
        pedestriancrossing("pedestrians")
        roadmarking("roadmark")
        brokencenterline("brokencenterl")
        continouscenterline("continouscenterl")
        givewayline("givewayl")
        stopline("stopl")
        schoolzone("schoolz")
        hospitalzone("hospitalz")
        universityzone("universityz")
        roadmaintanance("roadmain")
        sharedzone("sharedz")
        totallane("totall")
        markedlane("markedl")
        nonmarkedlane("nonmarkedl")
        busway("busw")
        bicycleway("bicyclew")
        freeway("freew")
        highway("highw")
        motorway("motorw")
        localstreet("locals")
        twowayroad("twoway")
        foggyweather("foggyw")
        heavyrain("heavyr")
        notenoughlight("notenoughl")


        ######################
        ## Creating object properties
        #####################

        with self.onto:

            class has_roadspeed(ObjectProperty):
                domain = [environment]

            class has_totallane(ObjectProperty):
                domain = [environment]

            class has_nofiltersign(ObjectProperty):
                domain = [roadsign]

            class has_endsign(ObjectProperty):
                domain = [roadsign]

            class has_intersection(ObjectProperty):
                domain = [roadconnection]

            class has_crossingwithouttrafficsign(ObjectProperty):
                domain = [roadconnection]

            class has_has_crossingwithtrafficsign(ObjectProperty):
                domain = [roadconnection]

            class has_railcrossing(ObjectProperty):
                domain = [roadconnection]

            class has_roundabout(ObjectProperty):
                domain = [roadconnection]

            class has_pedestriancrossing(ObjectProperty):
                domain = [roadconnection]

            class has_brokencenterline(ObjectProperty):
                domain = [roadmarking]

            class has_continouscenterline(ObjectProperty):
                domain = [roadmarking]

            class has_givewayline(ObjectProperty):
                domain = [roadmarking]

            class has_stopline(ObjectProperty):
                domain = [roadmarking]

            class has_schoolzone(ObjectProperty):
                domain = [specialzone]

            class has_hospitalzone(ObjectProperty):
                domain = [specialzone]

            class has_universityzone(ObjectProperty):
                domain = [specialzone]

            class has_roadmaintanance(ObjectProperty):
                domain = [specialzone]

            class has_sharedzone(ObjectProperty):
                domain = [specialzone]

            class has_markedlane(ObjectProperty):
                domain = [lane]

            class has_nonmarkedlane(ObjectProperty):
                domain = [lane]

            class has_busway(ObjectProperty):
                domain = [roadtype]

            class has_bicyleway(ObjectProperty):
                domain = [roadtype]

            class has_freeway(ObjectProperty):
                domain = [roadtype]

            class has_highway(ObjectProperty):
                domain = [roadtype]

            class has_motorway(ObjectProperty):
                domain = [roadtype]

            class has_localstreet(ObjectProperty):
                domain = [roadtype]

            class has_twowayroad(ObjectProperty):
                domain = [roadtype]

            class has_foggyweather(ObjectProperty):
                domain = [weathercondition]

            class has_heavyrain(ObjectProperty):
                domain = [weathercondition]

            class has_notenoughlight(ObjectProperty):
                domain = [weathercondition]

        ######################
        ## Creating data properties
        #####################

        with self.onto:
            class is_roadspeed(DataProperty):
                domain = [environment]
                range = [str]

            class is_totallane(DataProperty):
                domain = [environment]
                range = [str]

            class is_nofiltersign(DataProperty):
                domain = [roadsign]
                range = [str]

            class is_endsign(DataProperty):
                domain = [roadsign]
                range = [str]

            class is_intersection(DataProperty):
                domain = [roadconnection]
                range = [str]

            class is_crossingwithouttrafficsign(DataProperty):
                domain = [roadconnection]
                range = [str]

            class is_crossingwithtrafficsign(DataProperty):
                domain = [roadconnection]
                range = [str]

            class is_railcrossing(DataProperty):
                domain = [roadconnection]
                range = [str]

            class is_roundabout(DataProperty):
                domain = [roadconnection]
                range = [str]

            class is_pedestriancrossing(DataProperty):
                domain = [roadconnection]
                range = [str]

            class is_brokencenterline(DataProperty):
                domain = [roadmarking]
                range = [str]

            class is_continouscenterline(DataProperty):
                domain = [roadmarking]
                range = [str]

            class is_givewayline(DataProperty):
                domain = [roadmarking]
                range = [str]

            class is_stopline(DataProperty):
                domain = [roadmarking]
                range = [str]

            class is_schoolzone(DataProperty):
                domain = [specialzone]
                range = [str]

            class is_hospitalzone(DataProperty):
                domain = [specialzone]
                range = [str]

            class is_universityzone(DataProperty):
                domain = [specialzone]
                range = [str]

            class is_roadmaintanance(DataProperty):
                domain = [specialzone]
                range = [str]

            class is_sharedzone(DataProperty):
                domain = [specialzone]
                range = [str]

            class is_markedlane(DataProperty):
                domain = [lane]
                range = [str]

            class is_nonmarkedlane(DataProperty):
                domain = [lane]
                range = [str]

            class is_busway(DataProperty):
                domain = [roadtype]
                range = [str]

            class is_bicycleway(DataProperty):
                domain = [roadtype]
                range = [str]

            class is_freeway(DataProperty):
                domain = [roadtype]
                range = [str]

            class is_highway(DataProperty):
                domain = [roadtype]
                range = [str]

            class is_motorway(DataProperty):
                domain = [roadtype]
                range = [str]

            class is_localstreet(DataProperty):
                domain = [roadtype]
                range = [str]

            class is_twowayroad(DataProperty):
                domain = [roadtype]
                range = [str]

            class is_foggyweather(DataProperty):
                domain = [weathercondition]
                range = [str]

            class is_heavyrain(DataProperty):
                domain = [weathercondition]
                range = [str]

            class is_notenoughlight(DataProperty):
                domain = [weathercondition]
                range = [str]



        ######################
        ### Creating Time individual based on user input ###
        ######################

        self.data = data
        self.index = index

        instance_list = []
        instance_list = list(self.onto.timestamp.instances())
        # print(instance_list)

        if (len(instance_list) != 0):
            for i in range(0, len(instance_list)):
                #print(instance_list[i])
                destroy_entity(instance_list[i])

        time = self.data.at[self.index, 'time']
        # t = str(time)
        # print("You are looking for values in" + " " + "time = " + t + " second")

        self.onto.timestamp(time)
        # print("Hello Buddy")

        ######################
        ### Making Relations ###
        ######################

        ## No relation is for environment

        ######################
        ## Data properties value input
        ### Data Input from Excel file ###
        ######################

        my_data_properties1 = []
        my_data_properties2 = []

        my_dict = {}

        my_dict = self.data.loc[index]
        # print(my_dict)

        my_data_properties1 = list(self.onto.data_properties())
        # print(my_data_properties1)

        time_indi = getattr(self.onto, str(time))
        #print(time_indi)

        # for j in range(0, len(time_indi)):
        for k, v in my_dict.items():
            for x in range(0, len(my_data_properties1)):
                prop1 = str(my_data_properties1[x]).split('.')
                prop2 = prop1[-1]
                prop3 = prop2.split('_')
                prop4 = prop3[-1]

                if (prop4 == k):
                    # print(prop2)
                    data_entity = self.onto[prop2]
                    data_entity[time_indi] = [str(v)]

        self.onto.save("C:/Users/bhuiyanh/OneDrive - Queensland University of Technology/Ontology- Protege/av_info_environment.owl")










