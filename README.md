# <div align="center"> Torch RecSys Metrics </div>
<div align="center"> A library of Recommender system metrics for efficient PyTorch applications. </div>

## 🤗 What is TorchRecSysMetrics

안녕하세요! TorchRecSysMetrics는 추천시스템의 대표적인 메트릭들을 Pytorch 기반으로 구현해놓은 라이브러리입니다. 추천시스템을 찾거나 공부하는 학생들에게 도움이 되길 바랍니다. 자유롭게 사용 가능하나, 만약 코드에 잘못된 부분이 있다면 꼭 알려주세요.<br>

Hello! TorchRecSysMetrics is a library that implements representative metrics of the recommendation system based on Pytorch. I hope it will be helpful for students who are looking for a recommendation system or studying. It is freely available, but if there is anything wrong with the code, please let me know.<br>

### 특징
- 추천시스템 연구에 맞춘 표준화된 인터페이스를 지원합니다.
- 모든 메트릭이 Top-K 연산을 지원합니다.
- Batch단위의 Tensor연산을 통한 효율적인 계산이 가능합니다.

### Highlights
- Supports standardized interfaces tailored to recommendation system research.
- All metrics support Top-K operations.
- Efficient calculation is possible through Tensor calculation in Batch units.

## 📥 Installation

## ⌨️ Using TorchRecSysMetrics


## 🗂 Implemented Metric Lists

### Rank Aware Metrics
|Index|Metric　　　　　　　　　　　　　　　　　　　　　　　　　　　　　|Review|Implementation|
|:---:|:----------------------------------------------|:------------:|:------------:|
|1    |MAP (Mean Average Precision)                   |[Link]() |[Link]() |
|2    |MRR (Mean Reciprocal Rank)                     |[Link]() |[Link]() |
|3    |nDCG (normalized Discounted Cumulative Gain)   |[Link]() |[Link]() |
|3    |HR (Hit Rate)                                  |[Link]() |[Link]() |

### Rank Less Metrics
|Index|Metric　　　　　　　　　　　　　　　　　　　　　　　　　　　　　|Review|Implementation|
|:---:|:----------------------------------------------|:------------:|:------------:|
|1    |RMSE (Root Mean Squared Error)                 |[Link]() |[Link]() |
|2    |MAE (Mean Absolute Error)                      |[Link]() |[Link]() |
|3    |AUC (Area Under the ROC-Curve)                 |[Link]() |[Link]() |
|2    |Log Loss                                       |[Link]() |[Link]() |

## 🖋 Citation
If you want to use this Library, please use GitHub's built-in citation option to generate a bibtex or APA-Style citation.



