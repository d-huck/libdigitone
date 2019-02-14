# libdigitone

This library is intended to interface with the Elektron Digitone and convert the sysex dumps into meaningful data.
More information on the structure can be found in the attached [Jupyter Notebook](https://gitlab.com/dhuck/libdigitone/blob/production/doc/libdigitone.ipynb).

## What it is

This is a simple python library that can analyze patch data from the Digitone's SysEx dumps. It can also analyze the live state from the Digitone with a simple sysex request. I've attempted to be as verbose in the in-line documentation as possible so people can translate to other languages as needed. The only known issue at this point is the LFO Depth output tends to be off by 0.01 when it is negative.

## What it is not

This library is not yet 100% guaranteed to work. I've been able to successfully display the correct values for all parameters in my test code, but have not had the time to fully test the library. Isolating and testing the individual bytes is an extremely tedious process but I'm confident enough that the library is giving useful data back.

This library cannot (yet) decode Pattern data and other SysEx messages from the Digitone. It cannot yet encode the SysEx data to be returned to the Digitone.

### Legal and Acknowledgments

The only relation to Elektron here is the fact that I purchased some of their gear and loved it enough to make a project
like this. I do not work and do not plan to work for Elektron anytime. This library is and will
remain a labor of love.

I would like to acknowledge the great work done over at [libanalogrytm](https://github.com/bsp2/libanalogrytm), which
has given me a giant leg up on this endeavor. Also, the fine people who answered when I asked the preliminary
[questions about this project](https://www.elektronauts.com/t/decoding-the-digitone-sysex/62731). I would have become
frustrated and given up long ago without the people in that thread who pointed me in the right direction.
