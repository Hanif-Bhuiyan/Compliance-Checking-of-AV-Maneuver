from owlready2 import *


class query_environment:

    def query_trigger_for_environment(self, query):

        owlready2.JAVA_EXE = "C:\\Program Files\\Java\\jdk1.8.0_221\\bin\\java.exe"

        onto = get_ontology(
            "C:/Users/bhuiyanh/OneDrive - Queensland University of Technology/Ontology- Protege/av_info_environment.owl")
        onto.load()

        onto_name = str(onto.base_iri)

        ### Start --- Function for removing outer list ###
        output = []

        def reemovNestings(l):
            for i in l:
                if type(i) == list:
                    reemovNestings(i)
                else:
                    output.append(i)

        ### End --- Function for removing outer list ###

        ### Start ---Function for finding URL in a string #####

        def Find(string):
            regex = r"(?i)\b((?:https?://|www\d{0,3}[.]|[a-z0-9.\-]+[.][a-z]{2,4}/)(?:[^\s()<>]+|\(([^\s()<>]+|(\([^\s()<>]+\)))*\))+(?:\(([^\s()<>]+|(\([^\s()<>]+\)))*\)|[^\s`!()\[\]{};:'\".,<>?«»“”‘’]))"
            url = re.findall(regex, string)
            return [x[0] for x in url]

        ### End ---Function for finding URL in a string #####

        ## list to string convert ##

        def listToString(s):
                # initialize an empty string
            str1 = " "

                # return string
            return (str1.join(s))

        ## End llist to string convert ##

        self.query = query

        instance = str(onto.timestamp.instances())
        instance1 = instance.split(".", 1)
        instance2 = instance1[-1].replace("]", "")

        c = self.query.replace('ae:', onto_name)
        c = c.replace('time', instance2)

        f = []
        f = Find(c)

        for i in range(0, len(f)):
            checking_string = "<" + f[i] + ">"
            #print(checking_string)
            c = c.replace(f[i], checking_string)

        # print(c)

        #sync_reasoner()

        graph = default_world.as_rdflib_graph()

        r = list(graph.query_owlready(c))

        '''
        query_result1 = reemovNestings(r)

        query_result2 = listToString(query_result1)

        return query_result2
        
        '''

        reemovNestings(r)

        return output
        # print(output)

        # print(r)
