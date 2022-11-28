# Enhancing Speech

Can StarGANv2-VC be utilized as an intelligent audiofilter for upscaling phone conversations to be less distorted?

# Proof of Concept

The StarGANv2-VC model is able to convert speech with an unrecognized input speaker. As such, we tested whether StarGAN-v2 VC model could clean distorted audio out of the box. The utterances of one of the speakers can be heard below.

<table>
  <thead>
    <tr>
      <th style="text-align: center">Original Audio Reading</th>
      <th style="text-align: center">Reading with Distortion</th>
      <th style="text-align: center">StarGANv2-VC Mapping<br>(Distortion → Orignal)</th>
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

As can be heard, the StarGANv2-VC model cannot remove the introduced distortion, when it has not trained on distorted noise.