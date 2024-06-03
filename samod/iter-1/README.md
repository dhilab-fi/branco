This folder contains the materials produced during the first SAMOD iterations for the constructions of the ontology.

**#1 From the physical object to the reconstruction**

*Scenario*

Every physical object can be digitised in a data object, which may contain different semantic nodes. Moreover, physical objects are not always complete: a reconstruction is therefore necessary. It is a set of propositions about the studied physical objects and is articulated in different  interpretative units. Each interpretative unit can be visualised in a semantic node.

*Examples*

1. The domus A has been digitised in 3D with a photogrammetry campaign. The site has been studied to reconstruct its original aspect.
2. At the end of this reconstruction process, different interpretative units have been identified: IntUnit1, IntUnit2, IntUnit3 and IntUnit4
3. Later, in this 3D model, four semantic nodes have been added to represent the four IntUnits of the reconstruction 

*Competency Questions - Natural Language*

1. When was the domus A digitised? [Event] [Photogrammetry campaign]
2. Which are the 3D models of the domus? [DataObject] [3D Model]
3. How many IntUnits were identified for the domus? [list of IntUnits] [IntUnit1, IntUnit2, IntUnit3, IntUnit4]
4. Are there semantic nodes on the 3D model? If yes, to which IntUnits do they correspond? [Semantic Node (SemN) and IntUnits] [IntUnit1, SemN1; IntUnit2, SemN2; IntUnit3, SemN3; IntUnit4, SemN4]

*Competency Questions - SPARQL Query*

With: `PREFIX : <https://w3id.org/cnr-ispc/ontology/branco#> `

1. `SELECT ?campaign WHERE {?campaign :digitized :domus-a}`
2. `SELECT ?3dmodel WHERE {?campaign :digitized :domus-a. ?campaign :hasCreated ?3dmodel.}`
3. `SELECT ?unit WHERE {?reconstruction :refersTo :domus-a. ?reconstruction :hasComponent ?unit.}`
4. `SELECT ?unit ?semanticNode WHERE {?digitzation :digitized :domus-a. ?digitzation :hasCreated ?3dmodel. ?3dmodel :hasNode ?semanticNode. ?unit :isVisualisedAs ?semanticNode } ORDER BY ?unit`