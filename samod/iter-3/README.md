This folder contains the materials produced during the third SAMOD iterations for the constructions of the ontology.

**#3 The interpretative act supporting the US and its properties**

*Scenario*

A stratigraphic unit has different kinds of properties. These are assigned in an interpretative process which is carried out by an agent and is supported by different citations (different things can be the object of this citation). Each interpretation is motivated by a specific criterion such as comparison with other physical objects, diagnostic data, archival sources, general rules. Stratigraphic unit properties can be of different type, such as material, placement, iconography and dimension. 

*Examples*

1. In the final reconstruction, the position of the lost statue of Venus (a US) in the atrium of the domus B is justified by the position of the statue of Venus in the domus C (a physical object)
2. The Eastern Wall of domus B used to be decorated: on the basis of the instructions written by Vitruvius, the layers of decoration might have been composed of plaster.
3. Given the thickness of the Western wall and comparison with other sites, researchers claim that it should be 3.5 m tall. 
4. A diagnostic campaign identified one original layer of decoration in the Western Wall. It should have been decorated in Pompeian first style.


*Competency Questions - Natural Language*

1. Which is the criterion and the cited object in the reconstruction of the location of the Venus in domus B? [Location, Object, Reference] [Atrium of domus B, By comparison, Venus in the Atrium of domus C]
2. Which are the sources and criterion for the reconstruction of the domus B described in this examples? [Reconstruction description, Criterion, Reference objects] [Location of the Venus, comparison, domus C; Material of the decoration of Eastern wall, general rule, Vitruvius; Height of Western wall, general rule; Decoration of the Western wall, diagnostic data]
3. How can we reconstruct the original decoration of the Western wall? [Reconstruction description, Criterion, Reference objects, Style, Iconography][Decoration of the Western wall, diagnostic data, Pompeian 1st style, NA]
4. Which is the hypothesised height of the Western wall of the domus B? [Dimension and unit] [3,5 m]

*Competency Questions - SPARQL Query*

With `PREFIX : <https://w3id.org/cnr-ispc/ontology/branco#>`

1. `SELECT ?locatedObj ?criterion ?citedObj WHERE { ?interpretation :assignsPropertyTo :us-domus-b-atrium-venus . ?interpretation :assigns ?location . ?location a :Placement . ?location :hasSection ?locatedObj . ?interpretation :hasInterpretationCriterion ?criterion OPTIONAL {?interpretation :providesComparisonWith ?citedObj} }`
2. `SELECT DISTINCT ?description ?criterion ?comparedObj ?citedObj WHERE { ?interpretation :assignsPropertyTo ?us . ?us a  :StratigraphicUnit. ?interpretation :hasInterpretationCriterion ?criterion . ?interpretation :hasInterpretationDescription ?description OPTIONAL {?interpretation :providesComparisonWith ?comparedObj}  OPTIONAL {?interpretation :cites ?citedObj}}`
3. `SELECT DISTINCT * WHERE { ?interpretation :assignsPropertyTo :us-domus-b-westwall . ?interpretation :assigns ?decoration . ?decoration a :Decoration . ?interpretation :hasInterpretationCriterion ?criterion . ?interpretation :hasInterpretationDescription ?description . OPTIONAL {?decoration :hasStyle ?style .} OPTIONAL { ?decoration :hasIconography ?icon}}`
4. `SELECT ?dimension ?val ?unit WHERE { :us-domus-b-westwall :hasDimension ?dimension. ?dimension  :hasValue ?val . ?dimension :hasUnit ?unit}`