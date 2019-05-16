# pix2pix-tensorflow

Based on [pix2pix](https://phillipi.github.io/pix2pix/) by Isola et al.

[Article about this implemention](https://affinelayer.com/pix2pix/)

[Interactive Demo](https://affinelayer.com/pixsrv/)

This repo is forked from [here](https://github.com/affinelayer/pix2pix-tensorflow).

This version contains the original Tensorflow implementation (in 1.x) in addition to
the conversions necessary to get the model into a format that will work for mobile
devices with Firebase (.tflite).

Getting into implementing this has revealed itself to be much more complicated than I
initially thought and will take more time than I had anticipated. I will likely end up
creating my own version of the model in Keras in the future. As of May 2019, I'm putting this
on hold to work on other projects.
