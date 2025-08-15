# Overview
**Title:**
Data Transfer Approaches to Improve Seq-to-Seq Retrosynthesis

**Authors:**
Ishiguro, K., Ujihara, K., Sawada, R., Akita, H., and Kotera, M.

**Publication Date:**
2020/10/02

**Publication Link:**
[arXiv](https://arxiv.org/abs/2010.00792)

**Alternative Publication Links:**
[OpenReview](https://openreview.net/forum?id=V6WHleb2nV)


# Abstract
Retrosynthesis is a problem to infer reactant compounds to synthesize a given product compound through chemical reactions. 
Recent studies on retrosynthesis focus on proposing more sophisticated prediction models, but the dataset to feed the models also plays an essential role in achieving the best generalizing models. 
Generally, a dataset that is best suited for a specific task tends to be small. 
In such a case, it is the standard solution to transfer knowledge from a large or clean dataset in the same domain. 
In this paper, we conduct a systematic and intensive examination of data transfer approaches on end-to-end generative models, in application to retrosynthesis. 
Experimental results show that typical data transfer methods can improve test prediction scores of an off-the-shelf Transformer baseline model. 
Especially, the pre-training plus fine-tuning approach boosts the accuracy scores of the baseline, achieving the new state-of-the-art. 
In addition, we conduct a manual inspection for the erroneous prediction results. 
The inspection shows that the pre-training plus fine-tuning models can generate chemically appropriate or sensible proposals in almost all cases.


# Citation
```
@misc {ishiguro2020,
  author       = { Katsuhiko Ishiguro and Kazuya Ujihara and Ryohto Sawada and Hirotaka Akita and Masaaki Kotera },
  title        = { Data Transfer Approaches to Improve Seq-to-Seq Retrosynthesis },
  year         = { 2020 },
  eprint       = { 2010.00792 },
  archiveprefix = { arXiv },
  primaryclass = { cs.LG },
  url          = { https://arxiv.org/abs/2010.00792 }
}
```
