# EnhancingSpeech

Enhancing voices to improve speech intelligibility, by training a GAN model to learn a mapping from audio input spectrograms to style encoded target speakers inspired by StarGAN.

# Proof of Concept

In order to ensure that the there is a need for this project *EDIT CHANGE THIS*, we tested that the StarGAN-v2 VC model could not clean distorted audio out of the box. The utterances of one of the speakers can be seen below.

Hello


<table>
  <thead>
    <tr>
      <th style="text-align: center"> </th>
      <th style="text-align: center">Sample 1 (p229 → p236)</th>
      <th style="text-align: center">Sample 2 (p231 → p230)</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td style="text-align: center"><audio controls="controls">  <source type="audio/wav" src="https://raw.githubusercontent.com/jonpodtu/EnhancingSpeech_02456/master/docs/samples/original.wav" />&lt;/source&gt; </audio></td>
      <td style="text-align: center"><audio controls="controls">  <source type="audio/wav" src="https://raw.githubusercontent.com/jonpodtu/EnhancingSpeech_02456/master/docs/samples/distorted.wav" />&lt;/source&gt; </audio></td>
      <td style="text-align: center"><audio controls="controls">  <source type="audio/wav" src="https://raw.githubusercontent.com/jonpodtu/EnhancingSpeech_02456/master/docs/samples/reconstructed.wav" />&lt;/source&gt; </audio></td>
    </tr>
  </tbody>
</table>