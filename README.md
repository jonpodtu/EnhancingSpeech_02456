# Enhancing Speech

Can StarGANv2-VC be utilized as an intelligent audiofilter for upscaling phone conversations to be less distorted?

# Website

<a href="https://jonpodtu.github.io/EnhancingSpeech_02456/">Github Pages Site</a>

The notebook "Inference.ipynb" can be downloaded and run through Google Colab to obtain the results presented in the report. The notebook has been tested on Google Colab using GPU.

The "run.sh" file has been used when trainig the models on DTU's High Performance Computing servers.

CITES: src/stargan and all its content is copied directly from the original StarGANv2-VC github which can be found <a href="https://github.com/yl4579/StarGANv2-VC">here</a>. In this repo we have added a small number of modifications on many of the files to make it work with our data and goal of reconstructing phone-distorted speech. The most notable contribution being the "models_depthwise_convolutions.py", which is the "models.py" script copied and modified with depthwise seperable convolutions. The script "depthwise_concolution_test.py" added and slightly modified from the original script which can be found in <a href="https://www.paepper.com/blog/posts/depthwise-separable-convolutions-in-pytorch/">this blogpost</a> by Marc Päpper.
