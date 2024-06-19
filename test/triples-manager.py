import rdflib
import networkx as nx

def replace_prefixes(iri, graph):
    for prefix, namespace in graph.namespaces():
        if str(iri).startswith(str(namespace)):
            return str(iri).replace(str(namespace), prefix + ":")
    return str(iri)

def replace_prefix_in_g(graph):
    # Replace prefixes in the entire graph
    g_with_prefixes = rdflib.Graph()
    for s, p, o in graph:
        s_prefixed = rdflib.URIRef(replace_prefixes(s, graph))
        p_prefixed = rdflib.URIRef(replace_prefixes(p, graph))
        if isinstance(o, rdflib.URIRef): # avoid replace blank nodes or literals, only URI
            o_prefixed = rdflib.URIRef(replace_prefixes(o, graph))
        else:
            o_prefixed = o
        g_with_prefixes.add((s_prefixed, p_prefixed, o_prefixed))
    return g_with_prefixes

def gephi_converter(graph):
    # Create a NetworkX graph
    G = nx.DiGraph()

    # Extract nodes and edges
    for s, p, o in graph:
        G.add_node(s, label=str(s))
        G.add_node(o, label=str(o))
        G.add_edge(s, o, key=str(p), label=str(p))

    # Export the graph to a GEXF file
    nx.write_gexf(G, "gephi-viz/de-marchi.gexf", prettyprint=True, version="1.2draft")

    print("File graph.gexf has been created.")
    return G

def sparql_query(graph, cq):
    query = "\n".join([prefix, cq])
    for result in graph.query(query):
        #print(type(result))
        for el in result:
            print(el)
        print("\n")
# Create a graph
g = rdflib.Graph()

# Parse the Turtle file
g.parse("de-marchi.ttl", format="ttl")

g = replace_prefix_in_g(g)

# Define the SPARQL query

prefix = """
PREFIX : <http://w3id.org/cnr-ispc/brancacci/example>
PREFIX branco: <https://w3id.org/cnr-ispc/ontology/branco#>

PREFIX crm: <http://www.cidoc-crm.org/cidoc-crm/>
PREFIX crmsci: <http://www.ics.forth.gr/isl/CRMsci/>
PREFIX crmdig: <http://www.ics.forth.gr/isl/CRMdig/>
PREFIX vir: <http://w3id.org/vir#>

PREFIX cito: <http://purl.org/spar/cito/>
PREFIX fabio: <http://purl.org/spar/fabio/>
PREFIX frbr: <http://purl.org/vocab/frbr/core#>
PREFIX hico: <http://purl.org/emmedi/hico/>

PREFIX foaf: <http://xmlns.com/foaf/0.1/>
PREFIX prov: <http://www.w3.org/ns/prov#>
PREFIX xsd: <http://www.w3.org/2001/XMLSchema#>
PREFIX owl: <http://www.w3.org/2002/07/owl#>
PREFIX rdfs: <http://www.w3.org/2000/01/rdf-schema#>

PREFIX viaf: <https://viaf.org/viaf/>
"""

cq1 = """
SELECT ?obj
WHERE {:restoration-1984 crmsci:O2_removed ?obj}
"""

cq2 = """
SELECT ?doc 
WHERE {?attribution crm:P177_assigned_property_of_type branco:iconography . ?attribution cito:citesAsSourceDocument ?doc. }
"""

cq3 = """
SELECT ?icon ?absent_in_doc
WHERE {?attribution crm:P177_assigned_property_of_type branco:iconography . ?attribution cito:extends ?absent_in_doc. ?attribution crm:P141_assigned ?icon .}
"""

cq4 = """
SELECT ?iconology
WHERE {?attribution crm:P177_assigned_property_of_type :iconology . ?attribution crm:P141_assigned ?iconology .}
"""

sparql_query(g, cq2)
#sparql_query(g, "SELECT * WHERE {?s ?p ?o}")