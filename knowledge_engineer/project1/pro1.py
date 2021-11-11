#!/usr/bin/python 
# -*-coding:utf-8 -*-
__author__ = '99K'

import rdflib
from rdflib import Graph, Literal, BNode, Namespace, URIRef
from rdflib import RDF, RDFS, XSD, OWL
from rdflib.namespace import SKOS, FOAF
import string

g = Graph()
my_namespace = Namespace("http://example.org/")
prefix = "http://example.org/"


def readEntity(filename):
    res = {}
    with open(filename, encoding='utf-8') as f:
        for line in f:
            line = line.strip('\n')
            res[line] = URIRef(prefix + line.replace(' ', '_').replace('"', '_').replace('\_', '_'))
            # print(line, line.replace(' ', '_'))
            g.add((res[line], RDFS.label, Literal(line)))
    return res


def subClassOf(filename, class_list):
    with open(filename, encoding='utf-8') as f:
        for line in f:
            line = line.strip('\n').split('\t\t')
            g.add((class_list[line[0]], RDFS.subClassOf, class_list[line[1]]))


def instanceOf(filename, instances, classes):
    with open(filename, encoding='utf-8') as f:
        for line in f:
            line = line.strip('\n').split('\t\t')
            g.add((instances[line[0]], RDF.type, classes[line[1]]))
        
def sameAs(filename, instance1, instance2):
    with open(filename, encoding='utf-8') as f:
        for line in f:
            line = line.strip('\n').split('\t\t')
            try:
                g.add((instance1[line[0]], OWL.sameAs, instance2[line[1]]))
            except:
                print(line)
            
            

def domain(filename, properties, classes):
    with open(filename, encoding='utf-8') as f:
        for line in f:
            line = line.strip('\n').split('\t\t')
            g.add((properties[line[0]], RDFS.domain, classes[line[1]]))

def range__(filename, properties, classes):
    dataTypes = {}
    with open(filename, encoding='utf-8') as f:
        for line in f:
            line = line.strip('\n').split('\t\t')
            if line[1] in classes:
                g.add((properties[line[0]], RDFS.range, classes[line[1]]))
            else:
                line1 = line[1].split(':')
                if line1[1] not in dataTypes:
                    dataType = URIRef(prefix+line1[1])
                    g.add((dataType, RDF.type, RDFS.Datatype))
                    g.add((dataType, RDFS.label, Literal(line1[1])))
                    g.add((properties[line[0]], RDFS.range, dataType))
                    dataTypes[line1[1]] = 1

                
def object_triplet(filename, properties, instances):
    with open(filename, encoding='utf-8') as f:
        for line in f:
            line = line.strip('\n').split('\t\t')
            g.add((instances[line[0]], properties[line[1]], instances[line[2]]))

def dataType_triplet(filename, properties, instances):
    with open(filename, encoding='utf-8') as f:
        for line in f:
            line = line.strip('\n').split('\t\t')
            value = line[2].replace(' ', '_').replace('"', '_').replace('\_', '_').replace('\\', '_').replace('|', '_')
            value = value.translate(str.maketrans('', '', string.punctuation)).replace(' ', '_')
            value_resource = URIRef(prefix+value)
            g.add((instances[line[0]], properties[line[1]], value_resource))


if __name__ == '__main__':
    en_instances = readEntity('Data/en_instance.txt')
    fr_instances = readEntity('Data/fr_instance.txt')
    class_list = readEntity('Data/class_list.txt')
    property_list = readEntity('Data/property_list.txt')
    for k in class_list:
        g.add((class_list[k], RDF.type, RDFS.Class))
    for k in property_list:
        g.add((property_list[k], RDF.type, RDF.Property))
    
    subClassOf('Data/subClassOf.txt', class_list)
    instanceOf('Data/en_instanceOf.txt', en_instances, class_list)
    instanceOf('Data/fr_instanceOf.txt', fr_instances, class_list)
    domain('Data/domain.txt', property_list, class_list)
    range__('Data/range.txt', property_list, class_list)
    object_triplet('Data/en_object_triples.txt', property_list, en_instances)
    object_triplet('Data/fr_object_triples.txt', property_list, fr_instances)
    dataType_triplet('Data/en_datatype_triples.txt', property_list, en_instances)
    dataType_triplet('Data/fr_datatype_triples.txt', property_list, fr_instances)


    sameAs('Data/CL_link.txt', en_instances, fr_instances)
    g.bind("ns", my_namespace)
    
    g.serialize("project1.ttl", format="xml")