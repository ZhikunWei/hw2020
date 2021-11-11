#!/usr/bin/python 
# -*-coding:utf-8 -*-
__author__ = '99K'

from rdflib import Graph
g = Graph()
g.parse('project1.ttl', format='xml')

qres = g.query("SELECT * WHERE {?s a ns:Star}")
print('Query: SELECT * WHERE {?s a ns:Star}')
for item in qres:
    print('  ', item.s)
    
print()
qres = g.query("SELECT * WHERE {ns:Honesty ?p ?s}")
print('Query: SELECT * WHERE {ns:Honesty ?p ?s}')
for item in qres:
    print('  ',item.p,  item.s)
    
print()
qres = g.query("SELECT * WHERE {ns:Asia a ?s}")
print('Query: SELECT * WHERE {ns:Asia a ?s}')
for item in qres:
    print('  ', item.s)
    
print()
qres = g.query("SELECT * WHERE {ns:Aristotle ns:birthPlace ?s}")
print('Query: SELECT * WHERE {ns:Aristotle ns:birthPlace ?s}')
for item in qres:
    print('  ', item.s)
    
print()
qres = g.query("SELECT * WHERE {ns:Argentine ns:currencyCode ?s}")
print('Query: SELECT * WHERE {ns:Argentine ns:currencyCode ?s}')
for item in qres:
    print('  ', item.s)
