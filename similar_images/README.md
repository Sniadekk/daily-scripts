This is a CLI tool to check for a similar images in given directory. It takes all the images from the directory script is run in and compare it with input image. Photos that are similar enough are moved into similar_images directory.
### Usage

```sh
$ python similar_images.py image min_sim
image - image that we want to compare with others in current directory
min_sim - minimum similarity of the compared images to be moved to similar_images directory. The bigger value is the more accurate and demanding script will be.
```
