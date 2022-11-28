# EnhancingSpeech

Enhancing voices to improve speech intelligibility, by training a GAN model to learn a mapping from audio input spectrograms to style encoded target speakers inspired by StarGAN.

# Proof of Concept

In order to ensure that the there is a need for this project *EDIT CHANGE THIS*, we tested that the StarGAN-v2 VC model could not clean distorted audio out of the box. The utterances of one of the speakers can be seen below.

<audio ref='orig' src="https://raw.githubusercontent.com/jonpodtu/EnhancingSpeech_02456/master/docs/samples/original.wav"></audio>
<audio ref='dist' src="https://raw.githubusercontent.com/jonpodtu/EnhancingSpeech_02456/master/docs/samples/distorted.wav"></audio>
<audio ref='reco' src="https://raw.githubusercontent.com/jonpodtu/EnhancingSpeech_02456/master/docs/samples/reconstructed.wav"></audio>
