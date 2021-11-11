#!/usr/bin/python 
# -*-coding:utf-8 -*-
__author__ = '99K'

import rdflib
from rdflib import Graph, Literal, BNode, Namespace, URIRef
from rdflib import RDF, RDFS


g = Graph()
my_namespace = Namespace("http://example.org/")

# initialize a bag
bag = BNode()

# instance URI
Peter_Farrelly = URIRef("http://example.org/Peter_Farrelly")
Viggo_Mortensen = URIRef("http://example.org/Viggo_Mortensen")
Mahershala_Ali = URIRef("http://example.org/Mahershala_Ali")
Linda_Cardellini = URIRef("http://example.org/Linda_Cardellini")
Green_Book = URIRef("http://example.org/Green_Book")
Participant_Media = URIRef("http://example.org/Participant_Media")
Unitied_States = URIRef("http://example.org/Unitied_States")

# concept URI
Person = URIRef("http://example.org/Person")
Director = URIRef("http://example.org/Director")
Producer = URIRef("http://example.org/Producer")
Actor = URIRef("http://example.org/Actor")
Movie = URIRef("http://example.org/Movie")
Org = URIRef("http://example.org/Organization")
Company = URIRef("http://example.org/Company")
Loc = URIRef("http://example.org/Location")
Country = URIRef("http://example.org/Country")


# property URI
directedBy = URIRef("http://example.org/directedBy")
starring = URIRef("http://example.org/starring")
locateAt = URIRef("http://example.org/locateAt")
producedBy = URIRef("http://example.org/producedBy")

# each concept is a RDFS.Class
g.add((Person, RDF.type, RDFS.Class))
g.add((Director, RDF.type, RDFS.Class))
g.add((Producer, RDF.type, RDFS.Class))
g.add((Actor, RDF.type, RDFS.Class))
g.add((Movie, RDF.type, RDFS.Class))
g.add((Org, RDF.type, RDFS.Class))
g.add((Company, RDF.type, RDFS.Class))
g.add((Loc, RDF.type, RDFS.Class))
g.add((Country, RDF.type, RDFS.Class))

# each property is a RDFS.Property
g.add((directedBy, RDF.type, RDF.Property))
g.add((starring, RDF.type, RDF.Property))
g.add((locateAt, RDF.type, RDF.Property))
g.add((producedBy, RDF.type, RDF.Property))

# concept label
g.add((Person, RDFS.label, Literal("Person")))
g.add((Director, RDFS.label, Literal("Director")))
g.add((Producer, RDFS.label, Literal("Producer")))
g.add((Actor, RDFS.label, Literal("Actor")))
g.add((Movie, RDFS.label, Literal("Movie")))
g.add((Org, RDFS.label, Literal("Organization")))
g.add((Company, RDFS.label, Literal("Company")))
g.add((Loc, RDFS.label, Literal("Location")))
g.add((Country, RDFS.label, Literal("Country")))

# instance label
g.add((Peter_Farrelly, RDFS.label, Literal('Peter Farrelly')))
g.add((Viggo_Mortensen, RDFS.label, Literal('Viggo Mortensen')))
g.add((Mahershala_Ali, RDFS.label, Literal('Mahershala Ali')))
g.add((Linda_Cardellini, RDFS.label, Literal('Linda Cardellini')))
g.add((Green_Book, RDFS.label, Literal('Green Book')))
g.add((Participant_Media, RDFS.label, Literal('Participant Media')))
g.add((Unitied_States, RDFS.label, Literal('Unitied States')))

# property label
g.add((directedBy, RDFS.label, Literal("directed by")))
g.add((starring, RDFS.label, Literal("starring")))
g.add((locateAt, RDFS.label, Literal("locate at")))
g.add((producedBy, RDFS.label, Literal("produced by")))

# subClassOf
g.add((Director, RDFS.subClassOf, Person))
g.add((Producer, RDFS.subClassOf, Person))
g.add((Actor, RDFS.subClassOf, Person))
g.add((Company, RDFS.subClassOf, Org))
g.add((Country, RDFS.subClassOf, Loc))

# domain & range
g.add((directedBy, RDFS.domain, Movie))
g.add((directedBy, RDFS.range, Director))
g.add((starring, RDFS.domain, Movie))
g.add((starring, RDFS.range, RDF.Bag))
g.add((locateAt, RDFS.domain, Company))
g.add((locateAt, RDFS.range, Country))
g.add((producedBy, RDFS.domain, Movie))
g.add((producedBy, RDFS.range, Company))

# instanceOf
g.add((Peter_Farrelly, RDF.type, Director))
g.add((Viggo_Mortensen, RDF.type, Actor))
g.add((Mahershala_Ali, RDF.type, Actor))
g.add((Linda_Cardellini, RDF.type, Actor))
# bag is a rdf:Bag
g.add((bag, RDF.type, RDF.Bag))
g.add((Green_Book, RDF.type, Movie))
g.add((Participant_Media, RDF.type, Company))
g.add((Unitied_States, RDF.type, Country))

# property between instances
g.add((Green_Book, directedBy, Peter_Farrelly))
g.add((Green_Book, producedBy, Participant_Media))
g.add((Participant_Media, locateAt, Unitied_States))
g.add((Green_Book, starring, bag))
# edges between bag and three actors
g.add((bag, URIRef(u'http://www.w3.org/1999/02/22-rdf-syntax-ns#_1'), Viggo_Mortensen))
g.add((bag, URIRef(u'http://www.w3.org/1999/02/22-rdf-syntax-ns#_2'), Mahershala_Ali))
g.add((bag, URIRef(u'http://www.w3.org/1999/02/22-rdf-syntax-ns#_3'), Linda_Cardellini))

g.bind("ns", my_namespace)

print("all persons:")
qres = g.query("SELECT * WHERE {{?s a ns:Actor} UNION  {?s a ns:Director} UNION {?s a ns:Producer}}")
#using the fellowing sparql query can not get the result (no reasoning !!!)
#qres = g.query("SELECT * WHERE {?s a ns:Person}")
for item in qres:
	print(item.s)

# g.serialize("result2.ttl", format= "xml")
