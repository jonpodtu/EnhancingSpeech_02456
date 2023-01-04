# Enhancing Speech
*Can StarGANv2-VC be utilized as an intelligent audiofilter for upscaling phone conversations to be less distorted?*

This repository relates to a Deep Learning university project conducted by 5 students from the Technical University of Denmark. The repository won't be further updated, as the project has reached its deadline.

# Instructions
There are two ways to go about this repository. 

1. **Run inference and review results**. If you wish to use the already trained models that has been used in this project (and uploaded to huggingface), you can simply download the Jupyter notebook `Inference.ipynb` and run it through Google Colab. Her you can run inference on the test/validation set (located in the `Data/valid` folder) and obtain the results presented in the report. The notebook has been tested on Google Colab using GPU.
2. **Train the models from scratch**. As the traning process takes around 16-24 hours on high end GPU's, we havn't provided this through the notebook. However, its possible to train the models by following the below steps:
   1. Clone the repo
   2. Use Python with version 3.7 or above, and pip install the required packages ```pip install SoundFile torchaudio munch parallel_wavegan torch pydub pyyaml click librosa```
   3. Make the phone-distorted filtered audio-files by running `sound_to_phone.py`
   4. (Optional) Make new train/test split. If you don't, you use the one used to gather our results.
   5. Configure the `run.sh` file to your needs and start training. It's set up to run on HPC servers using bsub.

# What else is in the repo?
- Our finding and results can be found in the `docs` folder. We used tensorboard to monitor the train and validation loss.
- The `Data/Poster` folder contains the audio that was played in the poster session. Notice that these also can be found on our <a href="https://jonpodtu.github.io/EnhancingSpeech_02456/">website</a>.
- `src/Configs` contains configs for both models used (Depthwise and non-DW).

# Website
<a href="https://jonpodtu.github.io/EnhancingSpeech_02456/">Github Pages Site</a>

# Cites
`src/stargan` and all its content is copied directly from the original StarGANv2-VC github which can be found <a href="https://github.com/yl4579/StarGANv2-VC">here</a>. This goes for `src/VCTK.ipynb` as well. In this repo we have added a small number of modifications on many of the files to make it work with the modified data and goal of reconstructing phone-distorted speech. The most notable contribution being the "models_depthwise_convolutions.py", which is the "models.py" script copied and modified with depthwise seperable convolutions. The script `depthwise_convolution_test.py` added and slightly modified from the original script which can be found in <a href="https://www.paepper.com/blog/posts/depthwise-separable-convolutions-in-pytorch/">this blogpost</a> by Marc Päpper.

The prepared dataset found in `Data/VCTK/Data` is an already processed collection of speakers provided by StarGANv2-VC through their <a href="https://github.com/yl4579/StarGANv2-VC">repo</a>, and can be downloaded at https://drive.google.com/file/d/1t7QQbu4YC_P1mv9puA_KgSomSFDsSzD6/view. Notice that the train_list.txt and val_list.txt has been changed to follow our setup.