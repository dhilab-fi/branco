This folder contains the materials produced during the third SAMOD iterations for the constructions of the ontology.

**#3 The interpretative act supporting the US and its properties**

*Scenario*

Each interpretative unit is linked to a physical object, whose qualities are referred to by an interpretative act. Traditional interpretations concern location, dimension, material, technique, authorship, provenance, commision, styles and iconography. For these Iatter two classes, it is possible to recognize single features to assign a style or an iconographic subject (alignable with ICONCLASS) to an artwork. Lastly, any interpretation is justified by interpretative criteria, like direct observation, diagnostic data, general rule, archival sources, or comparison with other objects.

*Examples*

1. The Interpretative Unit IntUnitC1 is related to the decoration of the wall of domus C. In the reconstruction, it is based on the interpretation which claims that it should be 3 metres tall and decorated in Pompeii first style, on the basis of diagnostic data
2. The addition of a - now lost - altarpiece in the Chapel X is described by IntUnitC2. Different interpretations have been made on the iconography: it can be either a  story of Christ stilling the storm on the Sea of Galilee (ICONCLASS: 73C31) or story of Christ walking on the water, 'Navicella' (ICONCLASS: 73C32). 
3. The former interpretation of IntUnitC2 derives from archival sources, whereas the latter one derives from a comparison with the altarpiece in the Chapel Y of the same church.


*Competency Questions - Natural Language*

1. Which is the criterion for the reconstruction of IntUnitC1? [Criterion] [Diagnostic Data]
2. Which is the supposed height for IntUnitC1? [Dimension (value and unit)] [3m]
3. Which are the different interpretations for the reconstruction of the altarpiece in Chapel X? [Interpretative Criterion, Iconography, Comparison (if any)] [Christ stilling the storm on the Sea of Galilee, Archival Sources; Navicella, Comparison with Chapel Y]

*Competency Questions - SPARQL Query*

With `PREFIX : <https://w3id.org/cnr-ispc/ontology/branco#>`

1. `SELECT ?criterion WHERE { :intunit-c1 :cites ?int . ?int :hasInterpretationCriterion ?criterion}`
2. `SELECT ?val ?unit WHERE { :intunit-c1 :cites ?int . ?int :hasInterpretationResult ?dim. ?dim a :Dimension. ?dim :hasValue ?val . ?dim :hasUnit ?unit}`
3. `SELECT ?icon ?criterion ?artwork WHERE { :intunit-c2 :cites ?int . ?int :hasInterpretationResult ?icon . ?int :hasInterpretationCriterion ?criterion OPTIONAL {?int :providesComparisonWith ?artwork}}`