This folder contains the materials produced during the first SAMOD iterations for the constructions of the ontology.

**#1 From the physical object to the reconstruction**

*Scenario*

Every physical object can be digitised in a data object, which may contain different semantic nodes. Moreover, physical objects are not always complete: a reconstruction is therefore necessary. It is a set of propositions about the studied physical objects and is articulated in different  stratigraphic units. Each stratigraphic unit can be visualised in a semantic node.

*Examples*

1. The domus A has been digitised in 3D with a photogrammetry campaign. The site has been studied to reconstruct its original aspect.
2. At the end of this reconstruction process, different stratigraphic units have been identified: US1, US2, US3 and US4
3. Later, in this 3D model, four semantic nodes have been added to represent the four USs of the reconstruction 

*Competency Questions - Natural Language*

1. When was the domus A digitised? [Event] [Photogrammetry campaign]
2. Which are the 3D models of the domus? [DataObject] [3D Model]
3. How many USs were identified for the domus? [list of USs] [US1, US2, US3, US4]
4. Are there semantic nodes on the 3D model? If yes, to which US do they correspond? [Semantic Node (SemN) and US] [US1, SemN1; US2, SemN2; US3, SemN3; US4, SemN4]

*Competency Questions - SPARQL Query*

With: `PREFIX : <https://w3id.org/cnr-ispc/ontology/branco#> `

1. `SELECT ?campaign WHERE {?campaign :digitized :domus-a}`
2. `SELECT ?3dmodel WHERE {?campaign :digitized :domus-a. ?campaign :hasCreated ?3dmodel.}`
3. `SELECT ?us WHERE {?reconstruction :refersTo :domus-a. ?reconstruction :hasComponent ?us.}`
4. `SELECT ?us ?semanticNode WHERE {?digitzation :digitized :domus-a. ?digitzation :hasCreated ?3dmodel. ?3dmodel :hasNode ?semanticNode. ?us :isVisualisedAs ?semanticNode } ORDER BY ?us`