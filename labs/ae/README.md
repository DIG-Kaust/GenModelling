# AutoEncoders Tutorial

This repository contains code for building a convolutional autoencoder to compress the FossilNET dataset. This can generally be useful for storing and transporting the images, or for speeding up the processing of the images.

![LOGO](https://github.com/SaraAlthubaiti/NER-Project/blob/master/Figure11.png)

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

## Scripts
The repository includes the following files:
- :orange_book:`Linear_AutoEncoders.ipynb`: The code for implementing simple/linear autoencoder.
- :orange_book:`Convolutional_AutoEncoders.ipynb`: The code for implementing convolutional autoencoder.
- :page_facing_up:`dataloader_fossilnet.py`: The code for loading the FossilNET dataset. This file provides a function that can be used to load the dataset into `Linear_AutoEncoders.ipynb` and `Convolutional_AutoEncoders.ipynb` notebooks.
