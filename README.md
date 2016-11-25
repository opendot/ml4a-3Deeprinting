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

```
  facet normal -0.17081 -0.988312 0.0561681
    outer loop
      vertex -30.7425 -26.6532 9.91734
    endloop
  endfacet
  facet narmal 0.0603022 -0.763323 -0.617013
    outer loop
      vertex -1.50774 37.4165 54.4858
      vertex -30.065 -26.9583 7.9822
      vertex -37.6077 -4.31576 67.6813
      vertex -33.8138 -9.28438 22.0912
    endloop
  endfacet
  facet normal 0.624037 0.64761 0.43890
    outer loop
      vertex 15.7994 -37.9519 73.2936
      vertex 17.5564 -37.7542 77.3769
      vertex 15.0306 -40.7614 62.6957
      vertex 24.8122 39.7458 52.8605
      vertex 40.2831 18.9427 72.5635
      vertex 38.6411 17.7964 67.497
      vertex 36.6483 20.4316 57.9928
    endloop
  endfacet
```

