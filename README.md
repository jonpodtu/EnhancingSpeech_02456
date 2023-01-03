# Enhancing Speech

Can StarGANv2-VC be utilized as an intelligent audiofilter for upscaling phone conversations to be less distorted?

# Website

<a href="https://jonpodtu.github.io/EnhancingSpeech_02456/">Github Pages Site</a>

CITES: src/stargan and all its content is copied directly from the original StarGANv2-VC github which can be found <a href="https://github.com/yl4579/StarGANv2-VC">here</a>. In this repo we have added a small number of modifications on many of the files to make it work with our data and goal of reconstructing phone-distorted speech. The most notable contribution being the "models_depthwise_convolutions.py", which is the "models.py" script copied and modified with depthwise seperable convolutions. The script "depthwise_concolution_test.py" is heavily inspired by a script which can be found in <a href="https://www.paepper.com/blog/posts/depthwise-separable-convolutions-in-pytorch/">this blogpost</a> by Marc Päpper.
