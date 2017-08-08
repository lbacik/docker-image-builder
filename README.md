# docker-image-builder

If you have ever suffered from the limitation that you cannot parameterize the value of FROM keyword in Dockerfile 
then this project may turned out somehow interesting for you! Although, for the time being, its functionality is
a little bit... limited - it has already power to do miracles!

The main rule is that each next docker_context passed to the docker-image-builder script is build on the previous 
one - despite of what the FROM parameter contains (this value is changed "on the fly" by the script).

## instalation

You can install the docker-image-builder using pip (version for python3, so pip3 exactly), try:

    $ pip3 install docker-image-builder

The package site at pypi service is at https://pypi.python.org/pypi/docker-image-builder

Please check the:

    $ docker-image-builder --help

for available options.

## examples

...comming soon...
