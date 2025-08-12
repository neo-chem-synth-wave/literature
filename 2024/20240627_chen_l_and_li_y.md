# Overview
**Title:**
AutoTemplate: enhancing chemical reaction datasets for machine learning applications in organic chemistry

**Authors:**
Chen, L. and Li, Y.

**Publication Date:**
2024/06/27

**Publication Link:**
[BMC Journal of Cheminformatics](https://jcheminf.biomedcentral.com/articles/10.1186/s13321-024-00869-2)

**Alternative Publication Links:**
[ChemRxiv](https://chemrxiv.org/engage/chemrxiv/article-details/65f4089c66c1381729098d48) |
[PubMed Central](https://pmc.ncbi.nlm.nih.gov/articles/PMC11212196) |
[ResearchGate](https://www.researchgate.net/publication/381795697_AutoTemplate_enhancing_chemical_reaction_datasets_for_machine_learning_applications_in_organic_chemistry)


# Abstract
This paper presents AutoTemplate, an innovative data preprocessing protocol, addressing the crucial need for high-quality chemical reaction datasets in the realm of machine learning applications in organic chemistry.
Recent advances in artificial intelligence have expanded the application of machine learning in chemistry, particularly in yield prediction, retrosynthesis, and reaction condition prediction.
However, the effectiveness of these models hinges on the integrity of chemical reaction datasets, which are often plagued by inconsistencies like missing reactants, incorrect atom mappings, and outright erroneous reactions.
AutoTemplate introduces a two-stage approach to refine these datasets.
The first stage involves extracting meaningful reaction transformation rules and formulating generic reaction templates using a simplified SMARTS representation.
This simplification broadens the applicability of templates across various chemical reactions.
The second stage is template-guided reaction curation, where these templates are systematically applied to validate and correct the reaction data.
This process effectively amends missing reactant information, rectifies atom-mapping errors, and eliminates incorrect data entries.
A standout feature of AutoTemplate is its capability to concurrently identify and correct false chemical reactions.
It operates on the premise that most reactions in datasets are accurate, using these as templates to guide the correction of flawed entries.
The protocol demonstrates its efficacy across a range of chemical reactions, significantly enhancing dataset quality.
This advancement provides a more robust foundation for developing reliable machine learning models in chemistry, thereby improving the accuracy of forward and retrosynthetic predictions.
AutoTemplate marks a significant progression in the preprocessing of chemical reaction datasets, bridging a vital gap and facilitating more precise and efficient machine learning applications in organic synthesis.


# Citation
```
@article{chen2024b,
    author = "Chen, Lung-Yi and Li, Yi-Pei",
    title = "AutoTemplate: enhancing chemical reaction datasets for machine learning applications in organic chemistry",
    journal = "Journal of Cheminformatics",
    year = "2024",
    month = "Jun",
    day = "27",
    volume = "16",
    number = "1",
    pages = "74",
    issn = "1758-2946",
    doi = "10.1186/s13321-024-00869-2",
    url = "https://doi.org/10.1186/s13321-024-00869-2"
}
```
