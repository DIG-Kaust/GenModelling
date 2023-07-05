# Diffusion Models Tutorials

This repository contains code for building a convolutional autoencoder to compress the FossilNET dataset. This can generally be useful for storing and transporting the images, or for speeding up the processing of the images.

#introduction 

Diffusion models are a type of generative model used in machine learning to generate data that is similar to the data on which they are trained . They work by adding noise to the available training data and then gradually reducing the noise until the generated data closely resembles the training data. Diffusion models are a rising class of generative models because of their power-generating ability and tractability . They can also improve upon existing generative models, such as Generative Adversarial Networks (GANs), by being less reliant on adversarial training.

![diffusion](https://github.com/Sakhaa-Alsaedi/AI_in_Medicine_KAUST_Academy/assets/42935314/81137981-d242-4fe1-9e0d-4bb9fb288741)

# Building the Diffusion Model
## Step 1: The forward process = Noise scheduler
We first need to build the inputs for our model, which are more and more noisy images. Instead of doing this sequentially, we can use the closed form provided in the papers to calculate the image for any of the timesteps individually.

**Key Takeaways**:
- The noise-levels/variances can be pre-computed
- There are different types of variance schedules
- We can sample each timestep image independently (Sums of Gaussians is also Gaussian)
- No model is needed in this forward step

## Step 2: The backward process = U-Net
For a great introduction to UNets, have a look at this post: https://amaarora.github.io/2020/09/13/unet.html.

**Key Takeaways**:
- We use a simple form of a UNet for to predict the noise in the image
- The input is a noisy image, the ouput the noise in the image
- Because the parameters are shared accross time, we need to tell the network in which timestep we are
- The Timestep is encoded by the transformer Sinusoidal Embedding
- We output one single value (mean), because the variance is fixed


## Step 3: The loss
**Key Takeaways**:
- After some maths we end up with a very simple loss function
- There are other possible choices like L2 loss ect.


## Dataset :shell:
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

## Getting the data
Utilize the `dataloader_fossilnet.py` script in the `Linear_AutoEncoders.ipynb` and `Convolutional_AutoEncoders.ipynb` notebooks.

## Dependencies
[Google Colab](https://colab.research.google.com) provides all the necessary dependencies for running the code in this repository. You do not need to install any additional packages.

## Scripts ::

| Notebook  | Colabes| 
| :---:         |     :---:      |  
| Notebook 1 | [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)]([https://colab.research.google.com/github/username/repo/blob/master/notebook.ipynb][([https://colab.research.google.com/drive/1DDsachehj0bE4_y4sCg70NG9PDvTB4zX](https://github.com/DIG-Kaust/GenModelling/blob/main/labs/diffusion/Sakhaa_diffusion_model.ipynb))])  |
| Notebook 2  | [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)]([https://colab.research.google.com/github/username/repo/blob/master/notebook.ipynb]([https://colab.research.google.com/drive/1DDsachehj0bE4_y4sCg70NG9PDvTB4zX](https://colab.research.google.com/drive/1Y1Vp-X6FoEf-tw7caNyx3_ageSdlQhu_#scrollTo=5153024b))) |

**Sources and Materials:**

- Github implementation [Denoising Diffusion Pytorch](https://github.com/lucidrains/denoising-diffusion-pytorch)
- Niels Rogge, Kashif Rasul, [Huggingface notebook](https://colab.research.google.com/github/huggingface/notebooks/blob/main/examples/annotated_diffusion.ipynb#scrollTo=3a159023)
- Papers on Diffusion models ([Dhariwal, Nichol, 2021], [Ho et al., 2020] ect.)

[Sakhaa Alsaedi](https://cemse.kaust.edu.sa/cbrc/people/person/sakhaa-alsaedi) and Sara Althubaiti
