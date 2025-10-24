# Overview
**Title:**
Advancing Retrosynthesis With Retrieval-Augmented Graph Generation

**Authors:**
Qiao, A., Wang, Z., Rao, J., Yang, Y., and Wei, Z. |
Qiao, A. et al.

**Publication Date:**
2025/04/11

**Link:**
[AAAI Conference on Artificial Intelligence](https://ojs.aaai.org/index.php/AAAI/article/view/34203)

**Alternative Links:**
[GitHub](https://github.com/anjie-qiao/RARB)

**Tags:**
single-step-retrosynthesis, template-free, rarb


# Abstract
Diffusion-based molecular graph generative models have achieved significant success in template-free, single-step retrosynthesis prediction.
However, these models typically generate reactants from scratch, often overlooking the fact that the scaffold of a product molecule typically remains unchanged during chemical reactions.
To leverage this useful observation, we introduce a retrieval-augmented molecular graph generation framework.
Our framework comprises three key components: a retrieval component that identifies similar molecules for the given product, an integration component that learns valuable clues from these molecules about which part of the product should remain unchanged, and a base generative model that is prompted by these clues to generate the corresponding reactants.
We explore various design choices for critical and under-explored aspects of this framework and instantiate it as the Retrieval-Augmented RetroBridge (RARB).
RARB demonstrates state-of-the-art performance on standard benchmarks, achieving a 14.8% relative improvement in top-1 accuracy over its base generative model, highlighting the effectiveness of retrieval augmentation.
Additionally, RARB excels in handling out-of-distribution molecules, and its advantages remain significant even with smaller models or fewer denoising steps.
These strengths make RARB highly valuable for real-world retrosynthesis applications, where extrapolation to novel molecules and high-throughput prediction are essential.


# Citation
```
@article {20250411_qiao_a_et_al,
  author       = { Anjie Qiao and Zhen Wang and Jiahua Rao and Yuedong Yang and Zhewei Wei },
  title        = { Advancing Retrosynthesis with Retrieval-Augmented Graph Generation },
  journal      = { Proceedings of the AAAI Conference on Artificial Intelligence },
  year         = { 2025 },
  pages        = { 20004-20013 },
  month        = { Apr },
  volume       = { 39 },
  number       = { 19 },
  url          = { https://ojs.aaai.org/index.php/AAAI/article/view/34203 },
  doi          = { 10.1609/aaai.v39i19.34203 }
}
```
