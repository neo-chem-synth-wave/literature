# Overview
**Title:**
Automatic Mapping of Atoms across both Simple and Complex Chemical Reactions

**Authors:**
Jaworski, W., Szymkuć, S., Mikulak-Klucznik, B., Piecuch, K., Klucznik, T., Kaźmierowski, M., Rydzewski, J., Gambin, A., and Grzybowski, B.A.

**Publication Date:**
2019/03/29

**Publication Link:**
[ACS JCIM](https://pubs.acs.org/doi/10.1021/acs.jcim.8b00801)


# Abstract
Chemical synthesis planning is a key aspect in many fields of chemistry, especially drug discovery. 
Recent implementations of machine learning and artificial intelligence techniques for retrosynthetic analysis have shown great potential to improve computational methods for synthesis planning. 
Herein, we present a multiscale, data-driven approach for retrosynthetic analysis with deep highway networks (DHN). 
We automatically extracted reaction rules (i.e., ways in which a molecule is produced) from a data set consisting of chemical reactions derived from U.S. patents. 
We performed the retrosynthetic reaction prediction task in two steps: first, we built a DHN model to predict which group of reactions (consisting of chemically similar reaction rules) was employed to produce a molecule. 
Once a reaction group was identified, a DHN trained on the subset of reactions within the identified reaction group, was employed to predict the transformation rule used to produce a molecule. 
To validate our approach, we predicted the first retrosynthetic reaction step for 40 approved drugs using our multiscale model and compared its predictive performance with a conventional model trained on all machine-extracted reaction rules employed as a control. 
Our multiscale approach showed a success rate of 82.9% at generating valid reactants from retrosynthetic reaction predictions. 
Comparatively, the control model trained on all machine-extracted reaction rules yielded a success rate of 58.5% on the validation set of 40 pharmaceutical molecules, indicating a significant statistical improvement with our approach to match known first synthetic reaction of the tested drugs in this study. 
While our multiscale approach was unable to outperform state-of-the-art rule-based systems curated by expert chemists, multiscale classification represents a marked enhancement in retrosynthetic analysis and can be easily adapted for use in a range of artificial intelligence strategies.


# Citation
```
@article{jaworski2019,
    author = "Jaworski, Wojciech and Szymku{\'{c}}, Sara and Mikulak-Klucznik, Barbara and Piecuch, Krzysztof and Klucznik, Tomasz and Ka{\'{z}}mierowski, Micha{\l} and Rydzewski, Jan and Gambin, Anna and Grzybowski, Bartosz A.",
    title = "Automatic mapping of atoms across both simple and complex chemical reactions",
    journal = "Nature Communications",
    year = "2019",
    month = "Mar",
    day = "29",
    volume = "10",
    number = "1",
    pages = "1434",
    issn = "2041-1723",
    doi = "10.1038/s41467-019-09440-2",
    url = "https://doi.org/10.1038/s41467-019-09440-2"
}
```
