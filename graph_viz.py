#! /usr/bin/env python

import pygraphviz as pgv
A = pgv.AGraph()

network = (
        [0, 1, 2, 3, 4, 5], 
        [
                ((0, 0), 7), 
                ((1, 0), 3), ((1, 1), 36), ((1, 2), 1),  ((1, 3), 4),  ((1, 4), 1),
                ((2, 1), 3), ((2, 2), 31), ((2, 3), 1), 
                ((3, 1), 7), ((3, 2), 3),  ((3, 3), 36), ((3, 4), 1),  ((3, 5), 5),
                ((4, 1), 5), ((4, 2), 2),  ((4, 3), 7),  ((4, 4), 18), ((4, 5), 1), 
                ((5, 5), 66),((5, 3), 5),  ((5, 1), 3),  ((5, 4), 8), 
        ]
)

nodes, edges = network[0], network[1]

for node in nodes:
    A.add_node(str(node))
    tmp_node = A.get_node(str(node))
    if node == 0:
        tmp_node.attr['label'] = 'Myriel, \nNapoleon, \nCountessDeLo,\nGeborand, \nChamptercier, \nCravatte,\nCount, OldMan'
    elif node == 1:
        tmp_node.attr['label'] = 'Perpetue, \nSimplice'
    elif node == 2:
        tmp_node.attr['label'] = 'MlleBaptistine, MmeMagloire, Labarre, \nValjean, Marguerite, MmeDeR, \nIsabeau, Gervais, Scaufflaire, \nWoman1, Toussaint, Fauchelevent, \nMotherInnocent, Gribier, Jondrette, \nMmeBurgon'
    elif node == 3:
        tmp_node.attr['label'] = 'Tholomyes, Listolier, Fameuil, \nBlacheville, Favourite, Dahlia, \nZephine, Fantine, Pontmercy, \nMmePontmercy'
    elif node == 4:
        tmp_node.attr['label'] = 'Bamatabois, Judge, Champmathieu, \nBrevet, Chenildieu, Cochepaille, \nCosette, Woman2, Gillenormand, \nMagnon, MlleGillenormand, MlleVaubois, \nLtGillenormand, Marius, BaronessT'
    else: #node == 6
        tmp_node.attr['label'] = 'Gavroche, Mabeuf, Enjolras, \nCombeferre, Prouvaire, Feuilly, \nCourfeyrac, Bahorel, Bossuet, \nJoly, Grantaire, MotherPlutarch, \nMmeHucheloup, Child1, Child2, \nMmeThenardier, Thenardier, Javert, \nBoulatruelle, Eponine, Anzelma, \nGueulemer, Babet, Claquesous, \nMontparnasse, Brujon'
    

for edge in edges:

    try: # if the edge alerady exists in the other direction, combine weights
        existing_edge = A.get_edge(str(edge[0][1]), str(edge[0][0]))
        existing_label = existing_edge.attr['label']
        existing_edge.attr['label'] = str(int(existing_label) + int(edge[1]))
    except:
        A.add_edge(str(edge[0][0]), str(edge[0][1]), edge[1])
        tmp_edge = A.get_edge(str(edge[0][0]), str(edge[0][1]))
        tmp_edge.attr['label'] = str(edge[1])
        tmp_edge.attr['color'] = "blue"
    

print(A.string())
print("Wrote lesmis.dot")
A.write('lesmis.dot')  # write to simple.dot
B = pgv.AGraph('lesmis.dot')  # create a new graph from file
B.layout()  # layout with default (neato)
B.draw('lesmis.png', prog="circo")  # draw png
print('Wrote lesmis.png')