#!/usr/bin/python 
# -*-coding:utf-8 -*-
__author__ = '99K'

from rdflib import URIRef, BNode, Literal, Namespace
from rdflib import Graph
from rdflib.namespace import RDF, FOAF, RDFS

g = Graph()
my_namespace = Namespace("http://example.org/")

# instance
KnowledgeEngineering = URIRef("http://example.org/KnowledgeEngineering")
JuanziLi = URIRef("http://example.org/JuanziLi")

# concept
Course = URIRef("http://example.org/Course")
AcademicStaffMember = URIRef("http://example.org/AcademicStaffMember")
StaffMember = URIRef("http://example.org/StaffMember")
AssociateProfessor = URIRef("http://example.org/AssociateProfessor")
Professor = URIRef("http://example.org/Professor")
AssistantProfessor = URIRef("http://example.org/AssistantProfessor")
ID = URIRef("http://example.org/ID")
phone = URIRef("http://example.org/phone")

# property
isToughtBy = URIRef("http://example.org/isToughtBy")
involves = URIRef("http://example.org/involves")

# each concept is a RDFS.Class
g.add((Course, RDF.type, RDFS.Class))
g.add((AcademicStaffMember, RDF.type, RDFS.Class))
g.add((StaffMember, RDF.type, RDFS.Class))
g.add((Professor, RDF.type, RDFS.Class))
g.add((AssistantProfessor, RDF.type, RDFS.Class))
g.add((ID, RDF.type, RDFS.Class))
g.add((phone, RDF.type, RDFS.Class))


# each property is a RDF.Property
g.add((isToughtBy, RDF.type, RDF.Property))
g.add((involves, RDF.type, RDF.Property))

# label
g.add((KnowledgeEngineering, RDFS.label, Literal("Knowledge Engineering")))
g.add((JuanziLi, RDFS.label, Literal("Juanzi Li")))
g.add((Course, RDFS.label, Literal("Course")))
g.add((AcademicStaffMember, RDFS.label, Literal("Academic Staff Member")))
g.add((StaffMember, RDFS.label, Literal("Staff Member")))
g.add((Professor, RDFS.label, Literal("Professor")))
g.add((AssistantProfessor, RDFS.label, Literal("Assistant Professor")))
g.add((isToughtBy, RDFS.label, Literal("is Tought By")))
g.add((involves, RDFS.label, Literal("involves")))

# subclass
g.add((AssociateProfessor, RDFS.subClassOf, AcademicStaffMember))
g.add((Professor, RDFS.subClassOf, AcademicStaffMember))
g.add((AssistantProfessor, RDFS.subClassOf, AcademicStaffMember))
g.add((AcademicStaffMember, RDFS.subClassOf, StaffMember))
# subProperty
g.add((isToughtBy, RDFS.subPropertyOf, involves))

# domain and range
g.add((isToughtBy, RDFS.domain, Course))
g.add((isToughtBy, RDFS.range, AcademicStaffMember))
g.add((involves, RDFS.domain, Course))
g.add((involves, RDFS.range, AcademicStaffMember))
g.add((ID, RDFS.domain, StaffMember))
g.add((ID, RDFS.range, RDFS.Literal))
g.add((phone, RDFS.domain, StaffMember))
g.add((phone, RDFS.range, RDFS.Literal))

# instance of
g.add((KnowledgeEngineering, RDF.type, Course))
g.add((JuanziLi, RDF.type, Professor))

# property between instances
g.add((KnowledgeEngineering, isToughtBy, JuanziLi))

g.bind("ns", my_namespace)

g.serialize("hw2_staff_member.ttl", format="xml")
