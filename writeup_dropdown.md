Reconstruction of Microscopic Particles from CT-Scan

Zachary Ratliff

Initial X-Ray from CT-Scan

The sample that was used for the x-ray was prepared from a larger population of sand obtained from Huntsville, Alabama. Previous samples had been used from the same population for capturing high speed videos of particle impact. A SkyScan microCT was used to capture the preliminary x-ray formats, as seen below. The left figure shows a top-down view of a single image obtained from the scan, while the right figure shows a side profile of the x-ray. Each image represents only one of many unique images obtained from the microCT. Reconstruction was later made possible using complimentary software provided from SkyScan.

The top-down views can be thought of as an x-y plane, with each image being a step in the z-direction. Similarly, it can be said that the side images are views of the x-z plane, with each rotation being a rotation about the z axis. The step size and rotation were defined during the setup of the microCT experiment.

Obtaining Bitmap Images for Reconstruction

After the x-ray files had been obtained from the microCT, the software package DATAVIEWER was used to obtain bitmap images for individual particles. Figures 3, 4 and 5 below show a sample of the x-y, x-z and y-z views of the platform. The red, blue and green lines represent respective x-y, y-z, and x-z planes. The intersection of these three planes meet at the same (x, y, z) coordinate. An adjustable teal perimeter is used to create a bounding three dimensional rectangular prism. This prism sets the upper and lower limits of the x, y and z planes.

From this “bounding box”, the DATAVIEWER software saves x-y plane images, with each image representing a slice of the desired particle in the z direction. These were saved as binary black and white images, with each white pixel representing a point in space occupied by the particle.

In some cases, the bounding box would capture unwanted regions of other particles due to overlap in some areas of the three dimensional plane. When this happened, each z slice of the images was manually edited to remove the unwanted portion of other particles. This had no impact on the desired particle, as it would be impossible for any two particles to have the same (x, y, z) coordinates.

Reconstruction of Particles

3D rendering of the samples were done using an in house python script. When isolated particles were obtained from the DATAVIEWER software, the z sliced images for each particle was saved in a unique directory pertaining to that specific particle. The python script was used to scan through each of these directories, open each z slice, and obtain the x-y coordinates of the white pixels representing a point in space occupied by the particle. The respective (x, y) coordinates for each slice was written to a text file for each z coordinate stack, and once completed the particle could be described by its (x, y, z) coordinates. From these points in space it was a simple task to reconstruct the particles from their coordinates using the python module Mayavi.

A diagram representing the visualization process can be seen in Figure 6 below. The stacks in the top of the figure represent each z coordinate of the particle. In the bottom left it can be seen that each stack has unique (x, y) white particle coordinates. The right image shows how all of these images would look stacked upon one another.

Figure 6: Visualization of a Single Particle
