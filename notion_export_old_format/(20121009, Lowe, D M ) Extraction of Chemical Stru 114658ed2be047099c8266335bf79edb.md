# (20121009, Lowe, D.M.) Extraction of Chemical Structures and Reactions from the Literature

Tags: chemical-data

## Publication Overview

| **Title:**  | Extraction of Chemical Structures and Reactions from the Literature |
| --- | --- |
| **Authors:**  | Daniel M. Lowe |
| Publication Date**:**  | 2012/10/09 |
| Publication Links: | [**University of Cambridge Doctoral Thesis**](https://www.repository.cam.ac.uk/handle/1810/244727) |
| Alternative Links: | - |
| Code Links: | - |

## Publication Abstract

<aside>
ℹ️ The ever increasing quantity of chemical literature necessitates the creation of automated techniques for extracting relevant information. This work focuses on two aspects: the conversion of chemical names to computer readable structure representations and the extraction of chemical reactions from text. Chemical names are a common way of communicating chemical structure information. OPSIN (Open Parser for Systematic IUPAC Nomenclature), an open source, freely available algorithm for converting chemical names to structures was developed. OPSIN employs a regular grammar to direct tokenization and parsing leading to the generation of an XML parse tree. Nomenclature operations are applied successively to the tree with many requiring the manipulation of an in-memory connection table representation of the structure under construction. Areas of nomenclature supported are described with attention being drawn to difficulties that may be encountered in name to structure conversion. Results on sets of generated names and names extracted from patents are presented. On generated names, recall of between 96.2% and 99.0% was achieved with a lower bound of 97.9% on precision with all results either being comparable or superior to the tested commercial solutions. On the patent names OPSIN s recall was 2-10% higher than the tested solutions when the patent names were processed as found in the patents. The uses of OPSIN as a web service and as a tool for identifying chemical names in text are shown to demonstrate the direct utility of this algorithm. A software system for extracting chemical reactions from the text of chemical patents was developed. The system relies on the output of ChemicalTagger, a tool for tagging words and identifying phrases of importance in experimental chemistry text. Improvements to this tool required to facilitate this task are documented. The structure of chemical entities are where possible determined using OPSIN in conjunction with a dictionary of name to structure relationships. Extracted reactions are atom mapped to confirm that they are chemically consistent. 424,621 atom mapped reactions were extracted from 65,034 organic chemistry USPTO patents. On a sample of 100 of these extracted reactions chemical entities were identified with 96.4% recall and 88.9% precision. Quantities could be associated with reagents in 98.8% of cases and 64.9% of cases for products whilst the correct role was assigned to chemical entities in 91.8% of cases. Qualitatively the system captured the essence of the reaction in 95% of cases. This system is expected to be useful in the creation of searchable databases of reactions from chemical patents and in facilitating analysis of the properties of large populations of reactions.

</aside>

## Remarks and Comments

<aside>
💬 *Written on **2022/09/11** by **Haris Hasić**.*
****
The doctoral thesis where the United States Patent Office dataset was initially introduced. It contains all that you need to know about how the dataset was originally extracted and curated.

</aside>