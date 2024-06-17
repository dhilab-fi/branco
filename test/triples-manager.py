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

def sparql_query(graph, query):
    results = graph.query(query)
    for row in results:
        #print(f"Subject: {row.subject}, Predicate: {row.predicate}, Object: {row.object}")
        print(f"{row.subject}\n{row.predicate}\n{row.object}\n\n")
    return results

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

# Create a graph
g = rdflib.Graph()

# Parse the Turtle file
g.parse("de-marchi.ttl", format="ttl")

g = replace_prefix_in_g(g)

# Define the SPARQL query
query = """
PREFIX ex: <http://example.org/>
SELECT ?subject ?predicate ?object
WHERE {
  ?subject ?predicate ?object .
}
LIMIT 10
"""

sparql_query(g, query)
#gephi_converter(g)