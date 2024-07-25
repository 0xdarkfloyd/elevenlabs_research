# elevenlabs_research

https://elevenlabs.io/

It supports voice cloning, text to speech, speech to speech, it supports multilingual.

# Voice Feature Extraction
```
python text2speech.py
```
# Result
```
C:\Users\hacker\Downloads\elevenlabs>python voicefeature.py
pitch: (36.53258, 286.47055)
tone: (0.006881430642110973, 0.10962254489555823)
cadence: (107.666015625, 0.0)
resonance: (0.23388442, 1.1635059)
articulation: (2111.375471239768, 1245.6204469669924)
accent: (1940.907835711859, 625.6070902853011)
rhythm: (0.035560157, 0.023899402)
stress: (22.27156976318561, 12.17001492882612)
intonation: (3827.7638095609095, 2300.3757454273295)
skewness: 0.6346163611970942
kurtosis: 4.095271054585651
peak_count: 111518

C:\Users\hacker\Downloads\elevenlabs>python text2speech.py
Audio stream saved successfully.

C:\Users\hacker\Downloads\elevenlabs>python voicefeature.py
pitch: (17.879423, 180.54068)
tone: (-0.0032661926663031656, 0.11338307019748853)
cadence: (123.046875, 0.0)
resonance: (0.56253284, 2.8386395)
articulation: (2167.783986424077, 1490.7466958581986)
accent: (1963.9484483029048, 650.7770598958132)
rhythm: (0.08746687, 0.05713356)
stress: (23.80613517804654, 12.556464310543193)
intonation: (3944.874079451224, 2445.8176474432753)
skewness: -0.71328553026434
kurtosis: 3.538731521979879
peak_count: 123775

C:\Users\hacker\Downloads\elevenlabs>
```
# Analysis
```
Based on the voiceprint statistics provided, some features are more likely to remain relatively consistent for the same speaker, even when speaking different content in the same language, while other features may vary more significantly.

Features that are likely to be similar:

Pitch range: The overall pitch range (min and max pitch values) is an individual characteristic that tends to be consistent for a given speaker, regardless of the content being spoken.
Tone: The tone quality, reflected in the tone value, is an inherent feature of a speaker's voice and is likely to remain similar across different speech content.
Resonance: The resonance values, which relate to the vocal tract configuration and voice quality, are generally consistent for an individual speaker.
Articulation: The articulation values, which measure the precision of speech production, are influenced by the speaker's articulatory habits and are likely to be similar across different content.
Accent: The accent values, which capture the speaker's regional or linguistic accent, are expected to be consistent for the same speaker and language.
Skewness and Kurtosis: These statistical measures of the distribution of acoustic features are likely to be similar for the same speaker, as they reflect inherent characteristics of the voice.
Features that may vary:

Cadence: The cadence or speech rate can vary depending on the content being spoken, the speaker's emotional state, or the intended delivery style.
Rhythm: The rhythmic patterns can differ based on the linguistic content, such as the syllable structure, stress patterns, and phrasing.
Stress: The stress values, which measure the emphasis on certain syllables or words, can vary based on the specific content being spoken and the speaker's intended emphasis.
Intonation: The intonation patterns, which reflect the melodic contours of speech, can differ based on the content, emotional context, and intended prosody.
Peak Count: The number of peaks in the audio signal can vary depending on the specific content being spoken, as it is influenced by factors like syllable count, pauses, and other speech characteristics.
In summary, features like pitch range, tone, resonance, articulation, accent, skewness, and kurtosis are more likely to remain consistent for the same speaker, even with different speech content in the same language. On the other hand, features like cadence, rhythm, stress, intonation, and peak count may vary more significantly based on the specific content being spoken and the speaker's intended delivery.
```

# Voiceprint
```
Based on the analysis of which features are likely to remain stable across different speech content, and which features may vary, here are the voiceprint signatures for Mimosa and Jacky, separated into these two categories:

Mimosa:
Features likely to be stable across different speech:

Pitch range: (36.53258, 286.47055)
Tone: (0.006881430642110973, 0.10962254489555823)
Resonance: (0.23388442, 1.1635059)
Articulation: (2111.375471239768, 1245.6204469669924)
Accent: (1940.907835711859, 625.6070902853011)
Skewness: 0.6346163611970942
Kurtosis: 4.095271054585651
Features that may vary in different speech:

Cadence: (107.666015625, 0.0)
Rhythm: (0.035560157, 0.023899402)
Stress: (22.27156976318561, 12.17001492882612)
Intonation: (3827.7638095609095, 2300.3757454273295)
Peak Count: 111518
Jacky:
Features likely to be stable across different speech:

Pitch range: (17.879423, 180.54068)
Tone: (-0.0032661926663031656, 0.11338307019748853)
Resonance: (0.56253284, 2.8386395)
Articulation: (2167.783986424077, 1490.7466958581986)
Accent: (1963.9484483029048, 650.7770598958132)
Skewness: -0.71328553026434
Kurtosis: 3.538731521979879
Features that may vary in different speech:

Cadence: (123.046875, 0.0)
Rhythm: (0.08746687, 0.05713356)
Stress: (23.80613517804654, 12.556464310543193)
Intonation: (3944.874079451224, 2445.8176474432753)
Peak Count: 123775
This separation highlights the voiceprint features that are more likely to remain consistent for each speaker, regardless of the specific speech content, and the features that may vary based on the content being spoken.

```
