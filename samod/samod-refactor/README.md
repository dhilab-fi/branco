This folder refers to the final refactor of the conceptual model, providing a further alignment and a simplification of the model. 

```
PREFIX : <https://w3id.org/cnr-ispc/ontology/branco#>
PREFIX cito: <http://purl.org/spar/cito/>
PREFIX crm: <http://www.cidoc-crm.org/cidoc-crm/>
PREFIX crmdig: <http://www.ics.forth.gr/isl/CRMdig/>
PREFIX hico: <http://purl.org/emmedi/hico/>
PREFIX rdfs: <http://www.w3.org/2000/01/rdf-schema#>
PREFIX xsd: <http://www.w3.org/2001/XMLSchema#>
```

S2Q1. `SELECT ?unit WHERE {?event ?p :domus-b-southern-wall. ?event a ?event_class. ?event_class rdfs:subClassOf* crm:E5_Event. ?unit :models ?event. ?unit :hasChronologicalOrder ?order} ORDER BY ?order`
S2Q2. `SELECT ?unit WHERE { ?event ?p :domus-b-northern-wall. ?event a ?event_class. ?event_class rdfs:subClassOf* crm:E5_Event. ?unit :models ?event. ?unit :hasChronologicalOrder ?order} ORDER BY ?order`
S2Q3. `SELECT ?unit WHERE { :event-earthquake-62ad crm:P132_spatiotemporally_overlaps_with ?event. ?unit :models ?event.}`

