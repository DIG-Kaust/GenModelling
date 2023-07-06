[![Awesome](https://cdn.rawgit.com/sindresorhus/awesome/d7305f38d29fed78fa85652e3a63e154dd8e8829/media/badge.svg)](https://github.com/hee9joon/Awesome-Diffusion-Models) 
[![License: MIT](https://img.shields.io/badge/License-MIT-green.svg)](https://opensource.org/licenses/MIT)
[![Made With Love](https://img.shields.io/badge/Made%20With-Love-red.svg)](https://github.com/chetanraj/awesome-github-badges)

# Diffusion Model Tutorials
![diffusion](https://github.com/Sakhaa-Alsaedi/AI_in_Medicine_KAUST_Academy/assets/42935314/81137981-d242-4fe1-9e0d-4bb9fb288741)


> Created by <br>
> [Sakhaa Alsaedi](https://cemse.kaust.edu.sa/cbrc/people/person/sakhaa-alsaedi)<sup>1</sup> and [Sara Althubaiti](https://cemse.kaust.edu.sa/cs/people/person/sara-althubaiti).<sup>1</sup> <br>
> King Abdullah University of Science and Technology (KAUST)<sup>1</sup>

This repository contains code for building a diffusion model to compress the FossilNET dataset and generate imges. This can generally be useful for high quality samples, or for model diversity.


# Introduction 

Diffusion models are a type of generative model used in machine learning to generate data that is similar to the data on which they are trained . They work by adding noise to the available training data and then gradually reducing the noise until the generated data closely resembles the training data. Diffusion models are a rising class of generative models because of their power-generating ability and tractability . They can also improve upon existing generative models, such as Generative Adversarial Networks (GANs), by being less reliant on adversarial training.

![diffusion](https://github.com/Sakhaa-Alsaedi/CS394D/blob/main/45AD5AED-E217-41B4-89D5-2957621ADFBC.jpeg)



# Building the Diffusion Model steps:
- Step 1: The forward process ==> Noise scheduler
- Step 2: Parameterized backward process ==> NN Model [U-Net (autoencoder)](https://amaarora.github.io/2020/09/13/unet.html)
- step 3: Positional Encoding ==> [timestep encoding](colab.research.google.com/drive/1niCAKS1dJ74_De8Nk_V3_Rx2tpNLadYD#scrollTo=dc8120e5)

## Dataset :shell: (Notebook 1)
We will be using the FossilNET Image dataset that had been collected and curated by [Matt Hall](https://github.com/kwinkunks) and consists of 3000 colour images at 224x224 resolution, split over 10 classes:

- Ammonites
- Bivalues
- Corals
- Dinosaurs
- Echinoderms
- Fishes
- Forams
- Gastropods
- Plants
- Trilobites

# MNIST-Dataset (Notebook 2)
Recognizing the Digits from 0-9 using their pixel values as attributes, using Deep Learning Model to Classify the Digits. The original dataset is in a format that is difficult for beginners to use. This dataset uses the work of Joseph Redmon to provide the MNIST dataset in a CSV format. The mnist_train.csv file contains the 60,000 training examples and labels. The mnist_test.csv contains 10,000 test examples and labels. Each row consists of 785 values: the first value is the label (a number from 0 to 9) and the remaining 784 values are the pixel values (a number from 0 to 255).

The dataset consists of two files:

- Mnist_train.csv
- Mnist_test.csv
- Mnist_train.csv 

## Getting the data
- Utilize the `dataloader_fossilnet.py` script in the notebook 1.
- Use MNIST dataset loader from PyTorch in the notebook 2.

## Dependencies
[Google Colab](https://colab.research.google.com) provides all the necessary dependencies for running the code in this repository. You do not need to install any additional packages.

# Scripts :space_invader:

| Notebook  | Open in Colab| 
| :---:         |     :---:      |  
| [Notebook 1](https://colab.research.google.com/drive/1DDsachehj0bE4_y4sCg70NG9PDvTB4zX?usp=sharing) | [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/drive/1DDsachehj0bE4_y4sCg70NG9PDvTB4zX?usp=sharing)|
| [Notebook 2](https://colab.research.google.com/drive/1Y1Vp-X6FoEf-tw7caNyx3_ageSdlQhu_?usp=sharing)  | [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/drive/1Y1Vp-X6FoEf-tw7caNyx3_ageSdlQhu_?usp=sharing)|

* ▬▬▬▬▬▬ Resources and Materials ▬▬▬▬▬▬

- Github implementation [Denoising Diffusion Pytorch](https://github.com/lucidrains/denoising-diffusion-pytorch)
- Niels Rogge, Kashif Rasul, [Huggingface notebook](https://colab.research.google.com/github/huggingface/notebooks/blob/main/examples/annotated_diffusion.ipynb#scrollTo=3a159023)
- [Diffusion model tutorial 2](https://huggingface.co/blog/annotated-diffusion) by Rogge & Rasul and follows the [paper](https://arxiv.org/abs/2006.11239) by He et al.
- [Awesome Diffusion Models Github]([https://www.youtube.com/watch?v=HoKDTa5jHvg&t=1338s](https://github.com/diff-usion/Awesome-Diffusion-Models))
- [Outlier Diffusion Model Video: Paper Explanation | Math Explained](https://www.youtube.com/watch?v=HoKDTa5jHvg&t=1338s)  
- [Positional Embeddings](colab.research.google.com/drive/1niCAKS1dJ74_De8Nk_V3_Rx2tpNLadYD#scrollTo=dc8120e5)


* ▬▬▬▬▬▬▬ Papers ▬▬▬▬▬▬▬
- Papers on Diffusion models ([Dhariwal, Nichol, 2021], [Ho et al., 2020] ect.)
- [DDPM](https://arxiv.org/pdf/2006.11239.pdf)
- [DDPM Improved](https://arxiv.org/pdf/2105.05233.pdf)
