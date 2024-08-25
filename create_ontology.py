from rdflib import Graph, Literal, RDF, URIRef, Namespace, OWL, RDFS

g = Graph()

ns = Namespace("http://ultimaterules.com#")

# classes
g.add((ns.InBoundsArea, RDF.type, OWL.Class))
g.add((ns.playingField, RDF.type, ns.InBoundsArea))

g.add((ns.OutOfBoundsArea, RDF.type, OWL.Class))
g.add((ns.perimeterLine, RDF.type, ns.OutOfBoundsArea))

g.add((ns.nonPlayer, RDF.type, OWL.Class))
g.add((ns.player, RDF.type, OWL.Class))
g.add((ns.offensivePlayer, RDFS.subClassOf, ns.player))
g.add((ns.defensivePlayer, RDFS.subClassOf, ns.player))

g.add((ns.disc, RDF.type, OWL.Class))

# relationships
g.add((ns.nonPlayer, ns.isAlwaysIn, ns.OutOfBoundsArea))
g.add((ns.defensivePlayer, ns.isAlwaysIn, ns.InBoundsArea))
g.add((ns.offensivePlayer, ns.canBeIn, ns.InBoundsArea))
g.add((ns.offensivePlayer, ns.canBeIn, ns.OutOfBoundsArea))
g.add((ns.perimeterLine, ns.notPartOf, ns.playingField))

g.add((ns.disc, ns.hasStatus, ns.InBoundsArea))
g.add((ns.disc, ns.hasStatus, ns.OutOfBoundsArea))

g.serialize(destination="ontology.ttl")