from pocketsphinx import LiveSpeech

speech = LiveSpeech(lm=False, keyphrase='back', kws_threshold=1e-20)
for phrase in speech:
    print(phrase.segments(detailed=True))