# High-Speed Motion Analysis in Badminton via Event Camera
This is a readme of the xprogram project "High-Speed Motion Analysis in Badminton via Event Camera", we mainly adopt the HR-INR, Timelens-XL and CBMNet model to our dataset and compare their performance on our dataset. You may see the code and visual result in the later part.

## Methods Used
In our work, we implemented the code of HR-INR, CBMNet and Timelens-XL. You can see the corresponding code in the repository. The used pretrained model can be found in the later part.

## Datasets Used
We create our own datasets with the equipment from the AI lab, we adopted the APX EVB Gen2 camera in the data collection. The datasets contain various camera stands from close-up, mid-shot to long-shot, and different angles of shooting which may be enough for the badminton scenario evaluation used. The details of shooting can be found in 羽毛球事件相机运动去模糊数据集拍摄脚本.docx. 

What's more, the output of APX EVB Gen2 camera are all binary datatype, which is not suitable for model. So we transformed those data which originally are binary format into required PNG or Npz format, then feed them to 3 model, from TimelensXL, CBMNet, to HR-INR and examine their output. 

## Pretrained Model
The pretrained model of HR-INR corresponds to the parameter setting : epr_encoder_name: swin

Those model can be found in [link]()

## Result
We found out the performance of TimelensXL, CBMNet is not that qualified and have the serious problem of discontinuity which may result from the assumption of linear motion. These two model adopt the optical flow to estimate the motion and suffer from those highly dynamic scenarios or non-linear motion scenarios. 

This situation is much more relieved in the output of HR-INR. Its motion prediction logic leverages the high temporal resolution of event cameras, hierarchical temporal representation, and implicit neural embedding, completely abandoning the traditional optical flow-based "displacement vector calculation" paradigm.
![output of different models](./asset/1.png)

## Intermediate visualization
We can also see this intermediate output from HR-INR for a better understanding of our model.
![The intermediate figure](./asset/6.png)

## Video Supplementary Materials
For a better understanding of our method and its performance, we provide visualizations of the results on various datasets. The following figures demonstrate the output of different approach, and provides the visualizable regional-features graph, holistic-feature graph, etc. For the videos, you can check this [link](https://hkustgz-my.sharepoint.com/:f:/g/personal/hqiang669_connect_hkust-gz_edu_cn/Evc6sNnP3CZJhSBra2MQRvcBWi-LfGeAANHdEVlavnVJUg?e=kld4pS).
