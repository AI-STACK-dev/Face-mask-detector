# Face Mask Detector using live cam

## Live cam을 통한 실내외 Mask Detection

💡팀 구성 : AI developer 4



코로나 19시대에 살고 있는 지금, 일상생활에서 마스크 착용의 중요성은 이미 수차례 강조되었다. 국제 학술지 Lancet의 논문에 따르면 올바르게 마스크를 착용할 경우 감염의 위험을 **85%** 이상 감소시킬 수 있다고 한다. 하지만 우리가 주목해야할 점은 실내에서의 마스크 착용이다. 우리는 실외에서보다 사무실, 작업장, 식당, 카페, 술집 등과 같은 실내에서 마스크를 벗는 일이 많다. 실내에서는 실외에서보다 2m이상 거리 유지가 힘들고 밀폐돼 있는 경우가 많으니 **감염 위험성은 당연히 더 높다.** 또한 마스크를 입에만 걸치거나 턱에만 걸치는 등 마스크를 제대로 쓰지 않는 경우도 많다. 마스크를 제대로 쓰지 않는다면 감염 예방효과가 없기에 제대로 쓰는 것은 굉장히 중요하다.



이런 상황에서 우리는 Face Mask Detector를 고안하였다. 이는 **Livecam**을 기반으로 카페나 식당과 같은 다중이용시설에 들어오는 사람들을 대상으로 마스크 착용여부를 자동으로 탐지한다. 그리하여 마스크를 미착용하거나, 입에만 걸치거나 턱에만 걸치는 등 마스크를 부적절하게 사용한 사람들에게 정확하게 착용할 것을 권고한다. 이는 직원들이 일일이 출입하는 인원을 통제하는 수고를 덜 수 있을 것이다.



### Object

📌 Live cam을 통해 마스크 착용 유무를 Bounding Box와 Class를 **실시간**으로 출력하는 작업 수행

✔️ AI Object Detection Training Part

✔️ Real time Classification developing Part



### Dataset

📌 Using Kaggle Open Dataset

✔️ Total : 853 Image, Class Imbalance

✔️ with mask : without mask : mask weared incorrect = 7 : 4 : 1

✔️ adding mask weared incorrect in Google Image and Personal Image with annotating(.xml)



### Model

📌 Using faster-RCNN

✔️ Fast-RCNN -> faster-RCNN

✔️ROI Pooling -> Class Classification



### Future Work

🔍 얼굴의 정면은 대부분 실시간으로 잘 예측되지만 머리카락을 마스크로 인식하는 경우도 존재 해결

🔍 머리가 길 경우, 검은 색 마스크로 인식되어 Bounding Box가 생기는 문제 해결

🔍 거리에 따라 Accuracy가 달라지는 문제 해결 