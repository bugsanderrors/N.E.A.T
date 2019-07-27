# N.E.S.T
Neural Engine Style Transfer

-------------------------------------------------------------------------------------------------------------------
It's my college project.


Neural Style Transfer (NST) is one of the most fun techniques in deep learning. It merges two images, namely, a "content" image (C) and a 
"style" image (S), to create a "generated" image (G). The generated image G combines the "content" of the image C with the "style" of 
image S.

Neural Style Transfer (NST) uses a previously trained convolutional network, and builds on top of that. The idea of using a network
trained on a different task and applying it to a new task is called transfer learning. We will use the VGG network, specifically, VGG-19,
a 19-layer version of the VGG network. This model has already been trained on the very large ImageNet database, and thus has learned to 
recognize a variety of low-level features (at the earlier layers) and high-level features (at the deeper layers).

