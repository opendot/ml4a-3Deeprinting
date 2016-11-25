# 3Deeprinting

STL 3D models generator based on Recurrent Neurla Network

For more details see [The Unreasonable Effectiveness of Recurrent Neural Networks](http://karpathy.github.io/2015/05/21/rnn-effectiveness/) blog post.

## Goals

The generator is fed by a dataset of STL models translated in ASCII, or RAW
format using [Python STL](http://python-stl.readthedocs.io/en/latest/) library.

## Main steps

- [collect](collect/) data scraping of STL format models / about 1000 3D models (keyword: Bottles);
- [filter](filter/) and convert scraped STL into ASCII or RAW with the `stlfilter` library;
- [generate](generate/) models, after training the generarive model.

## The journey

![alt text](img/1.png)
![alt text](img/2.png)
![alt text](img/3.png)

