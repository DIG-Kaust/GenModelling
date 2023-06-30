# GAN Tutorial for binary porous media generation in 2D

![LOGO](https://github.com/miguelcorralesg/RockGAN2D/blob/main/assets/meme_1png.png)  

> Generative Adversarial Networks tutorial <br>
> Corrales M.<sup>1</sup> <br>
> King Abdullah University of Science and Technology (KAUST)<sup>1</sup>

## Another tutorial on GANs?
Yes, this tutorial provides valuable insights and knowledge gained from my own experiences. It's a concise resource for anyone interested in understanding and applying GANs (especifacilly for a geoscience problem). Let's embark on this exciting adventure together!

This repository aims to provide a tutorial on Generative Adversarial Networks (GANs) for a geoscience problem, specifically focusing on digital rock generation. To simplify the learning approach, we begin with a basic notebook that utilizes the MNIST dataset. In this initial stage, the generator and discriminator networks are constructed using linear layers. This approach allows for a fast understanding of the problem and code execution.

Once we grasp the fundamental concepts, we transition to a specific rock sample dataset while maintaining the same network architectures. This transition highlights the fact that the choice of architecture for training a GAN depends on the specific case at hand. In the subsequent examples, we employ convolutional layers as they prove to be more suitable for working with rock samples.

It is important to note that in this tutorial, we do not utilize metrics to evaluate the quality of the generated results. The nature of our dataset, which is black and white (also different features from natural images), restricts the use of metrics like FID (Fréchet Inception Distance) that rely on access to features from a pre-trained classification model. However, assessing the quality of the results can be accomplished by computing physical characteristics of the rock, such as porosity, surface area, or permeability. These metrics, although not included in this set of tutorials, can provide insights into the quality of the generated samples.

For further exploration and if you're interested in incorporating these metrics, please refer to the following repository: https://github.com/DIG-Kaust/RockGAN.


## Tutorial structure
This repository is organized as follows:

* :open_file_folder: **data**: folder containing data (or instructions on how to retrieve the data).
* :open_file_folder: **notebooks**: set of jupyter notebooks reproducing the experiments for the tutorial.


## Notebooks
The following notebooks are provided:

- :orange_book: ``01_Rock_Samples.ipynb``: notebook performing an illustrative demonstration of the appearance of rock samples and highlights the importance of generating additional digital samples.
- :orange_book: ``02_MNIST_GAN_Tutorial.ipynb``: notebook performing a simple GAN tutorial using the MNIST dataset. Generator and Discriminator are built using linear layers. 
- :orange_book: ``03_RockGAN2D_Beadpack_Tutorial.ipynb``: notebook performing a GAN tutorial using the beadpack dataset where we keep the same architecture and hyperparameters as the previous notebook.
- :orange_book: ``04_RockGAN2D_Beadpack(conv)_Tutorial.ipynb``: notebook performing a GAN tutorial for the beadpack dataset. Here G and D are adapted to use convolutional layers. 
- :orange_book: ``05_RockGAN2D_Berea(conv)_Tutorial.ipynb``: notebook performing a GAN tutorial for the berea dataset. Here G and D are adapted to use convolutional layers. 


## Getting started :space_invader: :robot:
To ensure reproducibility of the results, we suggest using the `environment.yml` file when creating an environment.

Simply run:
```
./install_env.sh
```
It will take some time, if at the end you see the word `Done!` on your terminal you are ready to go.

Remember to always activate the environment by typing:
```
conda activate rockgan2d
```

> **Note** <br>
> All experiments have been carried on a Intel(R) Xeon(R) W-2245 CPU @ 3.90GHz equipped with a single NVIDIA Quadro RTX 4000 GPU. Different 
> environment configurations may be required for different combinations of workstation and GPU.
