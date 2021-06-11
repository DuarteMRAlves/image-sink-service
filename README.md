# Image Visualization Service

## Overview

This project offers an ACUMOS asset for web visualization of generic images.
It will display the images at http://localhost:8062, which can be view from
within a browser window.

## Usage

The project can be deployed with docker. 
To execute it run the following commands:

* Deploy the docker container *(The image will be automatically downloaded)*:

```shell
$ docker run --rm -p 8061:8061 -p 8062:8062 sipgisr/image-visualization:latest 
```

* Open the [browser window](http://localhost:8062)

* Test with an image by running the test script 
  *(Requires grpc to be installed, and the grpc generated code for the 
  [service](protos/image_visualization_service.proto))*:
  
```shell
$ python test/test_visualization.py <path_to_image>
```