# Overview
**Title:**
Enhancing Diversity in Language based Models for Single-step Retrosynthesis

**Authors:**
Toniato, A., Vaucher, A.C., Schwaller, P., and Laino, T.

**Publication Date:**
2023/02/16

**Publication Link:**
[RSC Digital Discovery](https://pubs.rsc.org/en/content/articlelanding/2023/dd/d2dd00110a)

**Alternative Publication Links:**
[Official GitHub Repository](https://github.com/rxn4chemistry/rxn_cluster_token_prompt)


# Abstract
Over the past four years, several research groups demonstrated the combination of domain-specific language representation with recent NLP architectures to accelerate innovation in a wide range of scientific fields. Chemistry is a great example. 
Among the various chemical challenges addressed with language models, retrosynthesis demonstrates some of the most distinctive successes and limitations. 
Single-step retrosynthesis, the task of identifying reactions able to decompose a complex molecule into simpler structures, can be cast as a translation problem, in which a text-based representation of the target molecule is converted into a sequence of possible precursors. 
A common issue is a lack of diversity in the proposed disconnection strategies. 
The suggested precursors typically fall in the same reaction family, which limits the exploration of the chemical space. 
We present a retrosynthesis Transformer model that increases the diversity of the predictions by prepending a classification token to the language representation of the target molecule. 
At inference, the use of these prompt tokens allows us to steer the model towards different kinds of disconnection strategies. 
We show that the diversity of the predictions improves consistently, which enables recursive synthesis tools to circumvent dead ends and consequently, suggests synthesis pathways for more complex molecules.


# Citation
```
@article {toniato2023,
  author       = { Alessandra Toniato and Alain C. Vaucher and Philippe Schwaller and Teodoro Laino },
  title        = { Enhancing diversity in language based models for single-step retrosynthesis },
  journal      = { Digital Discovery },
  year         = { 2023 },
  pages        = { 489-501 },
  volume       = { 2 },
  issue        = { 2 },
  publisher    = { RSC },
  doi          = { 10.1039/D2DD00110A },
  url          = { http://dx.doi.org/10.1039/D2DD00110A }
}
```
