# paganda

This repository contains how to build an end-to-end system to produce more data by Generative Adverserial Network to produce more data 
to test game theory

PAGANDA follows a k-folder idea, which means that we need to have K GANs running parallely and generate new traning data based on each GAN's quality. In this case, we achieve adaptation during the training phase.

## GAN
We use WGAN-GP to genenrate new data.
After each certain iterations, we need to save the model because we need to continue training from a certain status.


## Data forwarding
After we generated new data with GAN, we firstly need to evaluate the quality of each GAN.  
