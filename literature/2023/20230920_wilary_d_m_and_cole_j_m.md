# Overview
**Title:**
ReactionDataExtractor 2.0: A Deep Learning Approach for Data Extraction From Chemical Reaction Schemes

**Authors:**
Wilary, D.M. and Cole, J.M.

**Publication Date:**
2023/09/20

**Link:**
[ACS Journal of Chemical Information and Modeling](https://pubs.acs.org/doi/10.1021/acs.jcim.3c00422)

**Alternative Links:**
[PubMed Central](https://pmc.ncbi.nlm.nih.gov/articles/PMC10565829) |
[GitHub](https://github.com/dmw51/reactiondataextractor) |
[ReactionDataExtractor](http://www.reactiondataextractor.org)

**Tags:**
reaction-extraction, reaction-data-extractor


# Abstract
Knowledge in the chemical domain is often disseminated graphically via chemical reaction schemes.
The task of describing chemical transformations is greatly simplified by introducing reaction schemes that are composed of chemical diagrams and symbols.
While intuitively understood by any chemist, like most graphical representations, such drawings are not easily understood by machines; this poses a challenge in the context of data extraction.
Currently available tools are limited in their scope of extraction and require manual preprocessing, thus slowing down the speed of data extraction.
We present a new tool, ReactionDataExtractor v2.0, which uses a combination of neural networks and symbolic artificial intelligence to effectively remove this barrier.
We have evaluated our tool on a test set composed of reaction schemes that were taken from open-source journal articles and realized F1 score metrics between 75 and 96%.
These evaluation metrics can be further improved by tuning our object-detection models to a specific chemical subdomain thanks to a data-driven approach that we have adopted with synthetically generated data.
The system architecture of our tool is modular, which allows it to balance speed and accuracy to afford an autonomous, high-throughput solution for image-based chemical data extraction.


# Citation
```
@article {20230920_wilary_d_m_and_cole_j_m,
  author       = { Damian M. Wilary and Jacqueline M. Cole },
  title        = { ReactionDataExtractor 2.0: A Deep Learning Approach for Data Extraction from Chemical Reaction Schemes },
  journal      = { Journal of Chemical Information and Modeling },
  year         = { 2023 },
  note         = { PMID: 37729111 },
  pages        = { 6053-6067 },
  volume       = { 63 },
  number       = { 19 },
  doi          = { 10.1021/acs.jcim.3c00422 },
  url          = { https://doi.org/10.1021/acs.jcim.3c00422 },
  eprint       = { https://doi.org/10.1021/acs.jcim.3c00422 }
}
```
