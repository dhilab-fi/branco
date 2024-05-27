This folder contains the materials produced during the second SAMOD iterations for the constructions of the ontology.

**#2 From the event to the reconstruction units**

*Scenario*

Physical objects may undergo and be modified by different events: for instance, they can be destroyed. Other types of modifications are production, addition and removal of parts. All these events may be registered by a document and each of them is conceptualised as a unit, which can be in turn interpreted as the result of an event on the physical object. Every unit can either be structural or cladding: the latter covers the former. They can be organised chronologically.

*Examples*

1. The domus B was built in the 2nd century BCE, but in 62 AD the Southern wall collapsed due to an earthquake. The site was eventually destroyed in the eruption of Vesuvius in 79 AD. This event is witnessed by a letter by Pliny the Younger
2. During the earthquake of 62 AD, on the Northern wall of the domus B the previous decoration was destroyed. A new decoration was hence added.


*Competency Questions - Natural Language*

1. Which are the USs associated with the Southern wall of domus B? Organise them chronologically starting with the most recent []
2. Which are the USs associated with the Northern wall domus B (both structural and cladding units)? Organise them chronologically starting with the most recent
3. Which units refer to the earthquake of 62 AD?

*Competency Questions - SPARQL Query*

With `PREFIX rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#>` and `PREFIX : <https://w3id.org/cnr-ispc/ontology/branco#>`

1. `SELECT ?us ?description WHERE {?event ?p :domus-b-southern-wall. ?event a ?event_class. ?event_class rdfs:subClassOf* :Event. ?us :models ?event. ?us :hasChronology ?chron. ?chron :hasChronologicalOrder ?order . ?us :hasUSDescription ?description} ORDER BY ?order`
2. `SELECT ?us ?description WHERE { ?event ?p :domus-b-northern-wall. ?event a ?event_class. ?event_class rdfs:subClassOf* :Event. ?us :models ?event. ?us :hasChronology ?chron. ?chron :hasChronologicalOrder ?order . ?us :hasUSDescription ?description} ORDER BY ?order`
3. `SELECT ?us ?description WHERE { :event-earthquake-62ad :isCauseOf ?event. ?us :models ?event. ?us :hasUSDescription ?description}`