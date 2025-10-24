# Overview
**Title:**
Highly Parallel Optimisation of Chemical Reactions Through Automation and Machine Intelligence

**Authors:**
Westerlund, A.M., Saigiridharan, L., and Genheden, S. |
Westerlund, A.M. et al.

**Publication Date:**
2025/07/14

**Link:**
[RSC Chemical Science](https://pubs.rsc.org/en/content/articlelanding/2025/sc/d5sc00927h)

**Alternative Links:**
[Elsevier ScienceDirect](https://www.sciencedirect.com/org/science/article/pii/S2041652025011010)

**Tags:**
single-step-retrosynthesis, multi-step-retrosynthesis, template-based, aizynthfinder


# Abstract
Contemporary multistep retrosynthesis tools such as AiZynthFinder, which are frequently used by chemists, generate solved routes for the majority of target molecules, but do not consider the prior knowledge of the chemist, including specific bonds that should disconnect or remain connected throughout the routes.
Such knowledge is for example integral when planning a joint synthesis route for a set of similar molecules where common disconnection sites can be identified across the molecules.
Here, we present a novel strategy in AiZynthFinder for human-guided multistep retrosynthesis via prompting.
This includes a filter for discarding reactions that violate bonds to freeze constraints.
Furthermore, we benchmark four possible strategies for breaking selected bonds in the search for synthetic routes, and show that a combination of a disconnection-aware transformer and a multi-objective search generates routes which satisfy bond constraints for more targets in the PaRoutes dataset compared to the standard search (75.57% vs. 54.80%).
Finally, we apply the strategy on a set of drug molecules to exemplify a real-world scenario.
Our novel approach enables building a short joint synthesis route that satisfies the given bond constraints and covers eight of the ten molecules, demonstrating the added value of incorporating human prior knowledge in synthesis planning.


# Citation
```
@article {20250714b_westerlund_a_m_et_al,
  author       = { Annie M. Westerlund and Lakshidaa Saigiridharan and Samuel Genheden },
  title        = { Human-guided synthesis planning via prompting },
  journal      = { Chem. Sci. },
  year         = { 2025 },
  pages        = { 14655-14667 },
  volume       = { 16 },
  issue        = { 32 },
  publisher    = { The Royal Society of Chemistry },
  doi          = { 10.1039/D5SC00927H },
  url          = { https://dx.doi.org/10.1039/D5SC00927H }
}
```
