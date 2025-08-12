# (20151006, Schneider, N. et al.) Get Your Atoms in Order - An Open-source Implementation of a Novel and Robust Molecular Canonicalization Algorithm

Tags: chemical-data, enhancement

## Publication Overview

| **Title:**  | Get Your Atoms in Order - An Open-source Implementation of a Novel and Robust
Molecular Canonicalization Algorithm |
| --- | --- |
| **Authors:**  | Nadine Schneider, Roger A. Sayle, Gregory A. Landrum |
| Publication Date**:**  | 2015/10/06 |
| Publication Links: | [**ACS JCIM**](https://pubs.acs.org/doi/10.1021/acs.jcim.5b00543) |
| Alternative Links: | - |
| Code Links: | - |

## Publication Abstract

<aside>
ℹ️ Finding a canonical ordering of the atoms in a molecule is a prerequisite for generating a unique representation of the molecule. The canonicalization of a molecule is usually accomplished by applying some sort of graph relaxation algorithm, the most common of which is the Morgan algorithm. There are known issues with that algorithm that lead to noncanonical atom orderings as well as problems when it is applied to large molecules like proteins. Furthermore, each cheminformatics toolkit or software provides its own version of a canonical ordering, most based on unpublished algorithms, which also complicates the generation of a universal unique identifier for molecules. We present an alternative canonicalization approach that uses a standard stable-sorting algorithm instead of a Morgan-like index. Two new invariants that allow canonical ordering of molecules with dependent chirality as well as those with highly symmetrical cyclic graphs have been developed. The new approach proved to be robust and fast when tested on the 1.45 million compounds of the ChEMBL 20 data set in different scenarios like random renumbering of input atoms or SMILES round tripping. Our new algorithm is able to generate a canonical order of the atoms of protein molecules within a few milliseconds. The novel algorithm is implemented in the open-source cheminformatics toolkit RDKit. With this paper, we provide a reference Python implementation of the algorithm that could easily be integrated in any cheminformatics toolkit. This provides a first step toward a common standard for canonical atom ordering to generate a universal unique identifier for molecules other than InChI.

</aside>

<aside>
💬 *Written on **2022/09/20** by **Haris Hasić**.*
****
This publication introduces the standard canonical ordering algorithm used in RDKit today. It is seemingly a niche problem, but it actually represents the foundation of generating unique SMILES representations of chemical compounds. It also serves as a good reminder that the canonical SMILES representation is platform-dependent, and assuming cross-platform uniqueness can result in erroneous outcomes.

</aside>