# Enhancing Speech

Can StarGANv2-VC be utilized as an intelligent audiofilter for upscaling phone conversations to be less distorted?

# Proof of Concept

The StarGANv2-VC model is able to convert speech with an unrecognized input speaker. As such, we tested whether StarGAN-v2 VC model could clean distorted audio out of the box. The utterances of one of the speakers can be heard below.

<table>
  <thead>
    <tr>
      <th style="text-align: center">Original Audio Recording</th>
      <th style="text-align: center">Recoding with Distortion</th>
      <th style="text-align: center">StarGANv2-VC Mapping<br>(Distortion → Orignal)</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td style="text-align: center"><audio controls="controls">  <source type="audio/wav" src="https://raw.githubusercontent.com/jonpodtu/EnhancingSpeech_02456/master/docs\samples\VanillaModel_NoPhoneTrain\original.wav" />&lt;/source&gt; </audio></td>
      <td style="text-align: center"><audio controls="controls">  <source type="audio/wav" src="https://raw.githubusercontent.com/jonpodtu/EnhancingSpeech_02456/master/docs/samples/VanillaModel_NoPhoneTrain\distorted.wav" />&lt;/source&gt; </audio></td>
      <td style="text-align: center"><audio controls="controls">  <source type="audio/wav" src="https://raw.githubusercontent.com/jonpodtu/EnhancingSpeech_02456/master/docs/samples/VanillaModel_NoPhoneTrain\reconstructed.wav" />&lt;/source&gt; </audio></td>
    </tr>
  </tbody>
</table>

As can be heard, the StarGANv2-VC model cannot remove the introduced distortion, when it has not trained on distorted noise.

# Training on Noisy Data

We added constructed, noisy versions of the data the model trained on

<table>
  <thead>
    <tr>
      <th style="text-align: center">Original Audio Recording</th>
      <th style="text-align: center">Recoding with Distortion</th>
      <th style="text-align: center">StarGANv2-VC Mapping<br>(Distortion → Orignal)</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td style="text-align: center"><audio controls="controls">  <source type="audio/wav" src="https://raw.githubusercontent.com/jonpodtu/EnhancingSpeech_02456/master/docs\samples\VanillaModel_PhoneData\p228.wav" />&lt;/source&gt; </audio></td>
      <td style="text-align: center"><audio controls="controls">  <source type="audio/wav" src="https://raw.githubusercontent.com/jonpodtu/EnhancingSpeech_02456/master/docs/samples/VanillaModel_PhoneData\p228_phone.wav" />&lt;/source&gt; </audio></td>
      <td style="text-align: center"><audio controls="controls">  <source type="audio/wav" src="https://raw.githubusercontent.com/jonpodtu/EnhancingSpeech_02456/master/docs/samples/VanillaModel_PhoneData\p228_phone_to_p228.wav" />&lt;/source&gt; </audio></td>
    </tr>
  </tbody>
</table>