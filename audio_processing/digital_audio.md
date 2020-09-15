# Digital Audio fundamentals


## Audio sampling

### What is sampling?

Sampling is the process of transforming the analog signal to a digital representation.
This process is done with an Analog-to-digital converter (ADC). This circuit measures
the sound waves and quantizes the amplitude into a fixed size value.


### ADC Types

### Sample rates

Samples per-second. For audio recording the are a set of standard sampling data
rates. 

- 44.1 kHz CD audio
- 48 kHz DVD audio
- 96 kHz studio recording
- 8 kHz, 16kHz thelephony audio

Even when higher sampling rates get a better representation of the sound they
have some disadvantages:

- Require more storage
- Consume more CPU
- Require more Tx bandwidth

### Nyquist-Shannon frequency

The simplest interpretation is that a signal must be sampled at at least twice
the frequency of the highest frequency of interest. This means that the Nyquist
frequency == half of the sample rate.

For example to capture the complete human hearing range (20 kHz) we need to
sample at > 40 kHz. 

Aliasing is problem where a high freq signal being sampled shows the
same samples as a lower frequency signal. To avoid this behaviour a low pass
filter has to be added to the system.



### Decibels explained

- Decibels are relative, then 0 dB means the same volume of the original.
- -Inf means silence
- db SPL: Sound pressure level

For digital audio the dBs are measured relatively to the full scale (FS).
- Then the max value is 0 dB
- Half the amplitude is then -6 dB

To calculate the decibles: `20*log10(signal/reference)`


### Dynamic range in dB

For example a 16 bit value has a dynamic range of 96 dB. This because
The reference used to measure the dynamic range is 1.
96.329 = 20 * log10( (2 ^ 16 -1) / 1 )

For 24 bits the dynamic range is 144 dB. This sampling rate is used to avoid
"clipping". The clipping is the saturation of the max value, which in audio.

The sampling of 32 bit is not made for getting more dynamic range but to allow
easier computation as ther are no natural 24 bit types on regular processors



