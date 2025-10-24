# Overview
**Title:**
Exploring BERT for Reaction Yield Prediction: Evaluating the Impact of Tokenization, Molecular Representation, and Pretraining Data Augmentation

**Authors:**
Krzyzanowski, A., Pickett, S.D., and Pogány, P. |
Krzyzanowski, A. et al.

**Publication Date:**
2025/05/01

**Link:**
[ACS Journal of Chemical Information and Modeling](https://pubs.acs.org/doi/10.1021/acs.jcim.5c00359)

**Alternative Links:**
[ChemRxiv](https://chemrxiv.org/engage/chemrxiv/article-details/67adcd81fa469535b9285f22) |
[GitHub](https://github.com/gskcheminformatics/SynthCoder) |
[ResearchGate](https://www.researchgate.net/publication/389133742_Exploring_BERT_for_Reaction_Yield_Prediction_Evaluating_the_Impact_of_Tokenization_Molecular_Representation_and_Pre-training_Data_Augmentation)

**Tags:**
reaction-yield-prediction, synth-coder


# Abstract
Predicting reaction yields in synthetic chemistry remains a significant challenge.
This study systematically evaluates the impact of tokenization, molecular representation, pretraining data, and adversarial training on a BERT-based model for yield prediction of Buchwald-Hartwig and Suzuki-Miyaura coupling reactions using publicly available HTE data sets.
We demonstrate that molecular representation choice (SMILES, DeepSMILES, SELFIES, Morgan fingerprint-based notation, IUPAC names) has minimal impact on model performance, while typically BPE and SentencePiece tokenization outperform other methods.
WordPiece is strongly discouraged for SELFIES and fingerprint-based notation.
Furthermore, pretraining with relatively small data sets (<100 K reactions) achieves comparable performance to larger data sets containing millions of examples.
The use of artificially generated domain-specific pretraining data is proposed.
The artificially generated sets prove to be a good surrogate for the reaction schemes extracted from reaction data sets such as Pistachio or Reaxys.
The best performance was observed for hybrid pretraining sets combining the real and the domain-specific, artificial data.
Finally, we show that a novel adversarial training approach, perturbing input embeddings dynamically, improves model robustness and generalizability for yield and reaction success prediction.
These findings provide valuable insights for developing robust and practical machine learning models for yield prediction in synthetic chemistry.
GSK's BERT training code base is made available to the community with this work.


# Citation
```
@article {20250501_krzyzanowski_a_et_al,
  author       = { Adrian Krzyzanowski and Stephen D. Pickett and Peter Pogány },
  title        = { Exploring BERT for Reaction Yield Prediction: Evaluating the Impact of Tokenization, Molecular Representation, and Pretraining Data Augmentation },
  journal      = { Journal of Chemical Information and Modeling },
  year         = { 2025 },
  note         = { PMID: 40311104 },
  pages        = { 4381-4402 },
  volume       = { 65 },
  number       = { 9 },
  doi          = { 10.1021/acs.jcim.5c00359 },
  url          = { https://doi.org/10.1021/acs.jcim.5c00359 },
  eprint       = { https://doi.org/10.1021/acs.jcim.5c00359 }
}
```
