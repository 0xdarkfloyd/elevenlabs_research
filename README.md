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
# Voice print comparison
```
Based on the voiceprint statistics provided, it seems that the first set of statistics is for a voice sample referred to as "Mimosa," and the second set is for a voice sample referred to as "jacky."

To compare their voiceprints and determine which voice might sound sweeter, we can analyze some of the key acoustic features:

Pitch: The pitch range for "Mimosa" (36.53 - 286.47 Hz) is higher than that of "jacky" (17.88 - 180.54 Hz). A higher pitch range generally sounds more bright and youthful, which could be perceived as sweeter.
Tone: Both voices have relatively low tone values (close to 0), indicating a neutral tone quality.
Cadence: "jacky" has a slightly higher cadence (123.05 beats per minute) compared to "Mimosa" (107.67 bpm), which could contribute to a more dynamic and lively delivery.
Resonance: "jacky" has a higher resonance value (0.56 - 2.84) compared to "Mimosa" (0.23 - 1.16), suggesting a more resonant and possibly richer voice quality.
Articulation: Both voices have similar articulation values, indicating similar levels of precision in speech production.
Accent: The accent values are also similar for both voices.
Rhythm: "jacky" has a higher rhythm value (0.088) compared to "Mimosa" (0.036), suggesting a more rhythmic and expressive delivery.
Stress: The stress values are close for both voices, indicating similar stress patterns.
Intonation: "jacky" has a slightly higher intonation value (3944.87) compared to "Mimosa" (3827.76), which could contribute to a more melodic and expressive delivery.
Skewness and Kurtosis: These values provide information about the distribution of the acoustic features, but it's difficult to directly interpret their impact on perceived sweetness.
Considering these factors, the voice referred to as "jacky" may be perceived as sweeter overall due to its higher pitch range, slightly more dynamic cadence, higher resonance, more rhythmic delivery, and potentially more expressive intonation patterns.

However, it's important to note that the perception of sweetness is subjective and can be influenced by personal preferences and contextual factors. Additionally, other acoustic features not captured in these statistics, such as voice quality, timbre, and emotional expression, could also contribute to the perceived sweetness of a voice.
```


# Feature Analysis
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

# LSH

```
C:\Users\hacker\Downloads\elevenlabs>python LSH.py
Mimosa Stable Features LSH: (1.0, 5.0, 2.0, 2.0, 2.0, 3.0, 4.0, 4.0, 2.0, 4.0)
Jacky Stable Features LSH: (7.0, 4.0, 6.0, 6.0, 5.0, 4.0, 5.0, 2.0, 5.0, 4.0)
Mimosa Variable Features LSH: (0.0, 1.0, 3.0, 2.0, 2.0, 2.0, 4.0, 3.0, 2.0, 3.0)
Jacky Variable Features LSH: (1.0, 3.0, 2.0, 5.0, 2.0, 4.0, 3.0, 4.0, 1.0, 2.0)
Stable Features LSH Similarity: 0.1
Variable Features LSH Similarity: 0.1

```

# LSH Similarity Analysis and Implication
```
Based on the results shown, the implications are as follows:

Stable Features LSH Similarity: 0.1
The stable features of Mimosa and Jacky have a low LSH similarity of 0.1, which means that only 1 out of 10 hash values match between their stable feature LSH signatures.
This suggests that the stable features, such as pitch range, tone, resonance, articulation, accent, skewness, and kurtosis, are quite different between Mimosa and Jacky.
A low similarity in stable features implies that the inherent characteristics of their voices, like vocal tract configuration, articulatory habits, and overall voice quality, are dissimilar.
Variable Features LSH Similarity: 0.1
The variable features of Mimosa and Jacky also have a low LSH similarity of 0.1, meaning that only 1 out of 10 hash values match between their variable feature LSH signatures.
This indicates that the features that can vary across different speech content, such as cadence, rhythm, stress, intonation, and peak count, are also quite different between Mimosa and Jacky.
A low similarity in variable features suggests that their speech patterns, rhythmic patterns, stress patterns, and intonation contours are dissimilar, even though they are speaking the same language.
Overall, the low LSH similarity values for both stable and variable features imply that Mimosa and Jacky have significantly different voiceprint signatures. Their voices exhibit distinct characteristics in terms of both inherent voice qualities and speech patterns/prosodic features.

This dissimilarity could be due to various factors, such as differences in age, gender, regional accent, or individual vocal traits. It is important to note that these are approximate similarity measures based on the LSH technique, and a more comprehensive analysis of the acoustic features may be required for a more nuanced assessment of their voice similarities or differences.
```

# Reference

https://engineering.atspotify.com/2023/10/introducing-voyager-spotifys-new-nearest-neighbor-search-library/

https://www.usenix.org/conference/usenixsecurity23/presentation/deng-jiangyi-voiceprint

https://www.pinecone.io/learn/series/faiss/locality-sensitive-hashing/

https://medium.com/@hbrylkowski/locality-sensitive-hashing-explained-304eb39291e4
