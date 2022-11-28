# EnhancingSpeech

Enhancing voices to improve speech intelligibility, by training a GAN model to learn a mapping from audio input spectrograms to style encoded target speakers inspired by StarGAN.

# Proof of Concept

In order to ensure that the there is a need for this project *EDIT CHANGE THIS*, we tested that the StarGAN-v2 VC model could not clean distorted audio out of the box. The utterances of one of the speakers can be seen below.

<audio ref='orig' src="docs\samples\Proof_of_concept\original.wav"></audio>
<audio ref='dist' src="docs\samples\Proof_of_concept\distorted.wav"></audio>
<audio ref='reco' src="docs\samples\Proof_of_concept\reconstructed.wav"></audio>
