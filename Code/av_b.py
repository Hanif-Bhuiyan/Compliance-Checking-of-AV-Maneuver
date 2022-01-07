from owlready2 import *

class behaviour:

    def create_ontology_behaviour(self, data, index):

        self.onto = get_ontology("C:/Users/bhuiyanh/OneDrive - Queensland University of Technology/Ontology- Protege/av_info_behaviour.owl").load()
        #C:/Users/bhuiyanh/OneDrive - Queensland University of Technology/Ontology- Protege
        self.data = data
        self.index = index

        with self.onto:
            class drivingbehaviour(Thing):
                pass

            class action(drivingbehaviour):
                pass

            class acceleration(action):
                pass

            class deceleration(action):
                pass

            class speed(action):
                pass

            class heading(action):
                pass

            class directionsignal(drivingbehaviour):
                pass

            class emergencylight(directionsignal):
                pass

            class donotovertakesign(directionsignal):
                pass

            class goingleft(directionsignal):
                pass

            class goingright(directionsignal):
                pass

            class stopsign(directionsignal):
                pass

            class space(drivingbehaviour):
                pass

            class spaceheadway(space):
                pass

            class spacebackway(space):
                pass

            class lanenumber(drivingbehaviour):
                pass

            class gps(drivingbehaviour):
                pass

            class positionx(gps):
                pass

            class positiony(gps):
                pass

        with self.onto:
            class vehicle(Thing):
                pass

        with self.onto:
            class timestamp(Thing):
                pass

        ################
        ## Creating Individuals - I can create ind - thsi are static... so I can do it.. cz it will not change anymore

        acceleration("acc")
        deceleration("dece")
        heading("head")
        speed("spee")
        emergencylight("emerlight")
        donotovertakesign("donotfilters")
        goingleft("goleft")
        goingright("go_right")
        stopsign("sto")
        spacebackway("spaceb")
        spaceheadway("spaceh")
        lanenumber("laneno")
        positionx("posx")
        positiony("posy")

        ######################
        ## Creating object properties
        #####################

        with self.onto:
            class driving(ObjectProperty):
                domain = [timestamp]
                range = [vehicle]

            class has_acceleration(ObjectProperty):
                domain = [vehicle]
                range = [action]

            class has_deceleration(ObjectProperty):
                domain = [vehicle]
                range = [action]

            class has_speed(ObjectProperty):
                domain = [vehicle]
                range = [action]

            class has_heading(ObjectProperty):
                domain = [vehicle]
                range = [action]

            class has_emergencylight(ObjectProperty):
                domain = [vehicle]
                range = [directionsignal]

            class has_donotoveratkesign(ObjectProperty):
                domain = [vehicle]
                range = [directionsignal]

            class has_goingleft(ObjectProperty):
                domain = [vehicle]
                range = [directionsignal]

            class has_goingright(ObjectProperty):
                domain = [vehicle]
                range = [directionsignal]

            class has_stopsign(ObjectProperty):
                domain = [vehicle]
                range = [directionsignal]

            class has_spacebackway(ObjectProperty):
                domain = [vehicle]
                range = [space]

            class has_spaceheadway(ObjectProperty):
                domain = [vehicle]
                range = [space]

            class has_lanenumber(ObjectProperty):
                domain = [vehicle]
                range = [drivingbehaviour]

            class has_positionx(ObjectProperty):
                domain = [vehicle]
                range = [gps]

            class has_positiony(ObjectProperty):
                domain = [vehicle]
                range = [gps]

        ######################
        ## Making Data Property
        ######################

        with self.onto:
            class is_driving(DataProperty):
                domain = [vehicle]
                range = [str]

            class is_acceleration(DataProperty):
                domain = [action]
                range = [str]

            class is_deceleration(DataProperty):
                domain = [action]
                range = [str]

            class is_speed(DataProperty):
                domain = [action]
                range = [str]

            class is_heading(DataProperty):
                domain = [action]
                range = [str]

            class is_emergencylight(DataProperty):
                domain = [directionsignal]
                range = [str]

            class is_donotovertakesign(DataProperty):
                domain = [directionsignal]
                range = [str]

            class is_goingleft(DataProperty):
                domain = [directionsignal]
                range = [str]

            class is_goingright(DataProperty):
                domain = [directionsignal]
                range = [str]

            class is_stopsign(DataProperty):
                domain = [directionsignal]
                range = [str]

            class is_spacebackway(DataProperty):
                domain = [space]
                range = [str]

            class is_spaceheadway(DataProperty):
                domain = [space]
                range = [str]

            class is_lanenumber(DataProperty):
                domain = [drivingbehaviour]
                range = [str]

            class is_positionx(DataProperty):
                domain = [gps]
                range = [str]

            class is_positiony(DataProperty):
                domain = [gps]
                range = [str]

     
        instance_list = []
        instance_list_vehicle = []
        if(list(self.onto.timestamp.instances()) != 0):
            instance_list = list(self.onto.timestamp.instances())
            #print(instance_list)
        # print(instance_list[1])

        if (len(instance_list) != 0):
            for i in range(0, len(instance_list)):
                destroy_entity(instance_list[i])

        if (list(self.onto.vehicle.instances()) != 0):
            instance_list_vehicle = list(self.onto.vehicle.instances())

        if (len(instance_list_vehicle) != 0):
            for i in range(0, len(instance_list_vehicle)):
                destroy_entity(instance_list_vehicle[i])

        time = data.at[index, 'time']
        # print(data.at[locate, 'time'])
        t = str(time)
        print("You are looking for values in" + " " + "time = " + t + " second")

        # timestamp(time)
        timestamp(time)

        # finding how many vehicles -- vehicle instance

        vehicle_list = []
        column_list = data.columns.tolist()

        for i in range(len(column_list)):
            check_word = column_list[i]
            # print(check_word)

            if (len(check_word.split()) > 1):
                # print(check_word.split()[0])

                if (check_word.startswith('v') | check_word.startswith('V')):
                    if (check_word.split()[0] not in vehicle_list):
                        vehicle_list.append(check_word.split()[0])
            else:
                # print(check_word)
                if (check_word.startswith('v') | check_word.startswith('V')):
                    if (check_word not in vehicle_list):
                        vehicle_list.append(check_word)

        vehicle_indi = []

        for i in range(len(vehicle_list)):
            vehicle(vehicle_list[i])

        # Making Relations

        ## Now making time indiviuals by finding how many timeslot in the file

        time_indi = getattr(self.onto, str(time))
        # print(time_indi)

        for i in range(len(vehicle_list)):
            vehicle_indi.append(getattr(self.onto, vehicle_list[i]))
            # print(vehicle_indi)

        ## How many vehicles are driving finding that one and then making relations regarding time of those vehicles.

        for j in range(0, len(vehicle_indi)):
            time_indi.driving.append(vehicle_indi[j])

        ## Now for this individual making relations

        object_list = []
        class_list = []

        object_list = list(self.onto.object_properties())
        class_list = list(self.onto.classes())

        check_class = []
        check_object = []

        for c in range(1, len(class_list)):
            cb = class_list[c]
            cd = str(cb)
            check_class1 = cd.split('.')
            check_class.append(check_class1[-1])
            # print(getattr(onto, class_list[c]))

        for o in range(1, len(object_list)):
            ob = str(object_list[o])
            od = ob.split('.')
            oe = od[-1]
            of = oe.split('_')
            og = of[-1]
            check_object.append(og)

        # print(check_object)
        class_indi = []
        class_indi = []
        obj_indi = []

        # print(acceleration.instances())

        for i in range(0, len(check_object)):
            for j in range(0, len(check_class)):
                if (check_object[i] == check_class[j]):
                    abc_indi1 = getattr(self.onto, check_class[j])
                    abc_indi2 = abc_indi1.instances()
                    class_indi.append(abc_indi2)
                    obj_indi1 = "has_" + check_object[i]
                    obj_indi.append(obj_indi1)

        # print(vehicle_indi)
        # print(obj_indi)
        # print(class_indi)

        for k in range(0, len(vehicle_indi)):
            for i in range(0, len(obj_indi)):
                prop_entity = self.onto[obj_indi[i]]
                prop_entity[vehicle_indi[k]] = class_indi[i]

        # Data properties value input

        # object creation for the behaviour class

        # a = behaviour()

        # for i in range(0,num_rows):
        #    a.ontology(data.loc[i])

        my_data_properties1 = []
        my_data_properties2 = []

        my_dict = {}

        my_dict = data.loc[index]
        # print(my_dict)

        my_data_properties1 = list(self.onto.data_properties())
        # print(my_data_properties1)

        for j in range(0, len(vehicle_indi)):
            for k, v in my_dict.items():
                # print(k)
                vehicle_name1 = str(vehicle_indi[j]).split('.')
                vehicle_name2 = vehicle_name1[-1]

                if (vehicle_name2 in k):

                    for x in range(0, len(my_data_properties1)):
                        prop1 = str(my_data_properties1[x]).split('.')
                        prop2 = prop1[-1]
                        prop3 = prop2.split('_')
                        prop4 = prop3[-1]
                        prop5 = vehicle_name2 + " " + prop4
                        # print(prop5)

                        if (prop5 == k):
                            # print(prop5)
                            # print(k)

                            data_entity = self.onto[prop2]
                            data_entity[vehicle_indi[j]] = [str(v)]

        self.onto.save("C:/Users/bhuiyanh/OneDrive - Queensland University of Technology/Ontology- Protege/av_info_behaviour.owl")

        return t
