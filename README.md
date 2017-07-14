# docker-image-builder

If you have ever suffered from the limitation that you cannot parameterize the value of FROM keyword in Dockerfile 
then this project may turned out somehow interesting for you. However, for the time being, the documentation is limited 
to the only one of use examples of this code.

The main rule is that each next docker_context passed to the docker-image-builder script is build on the previous 
one - despite of what the FROM parameter contains (this value is changed "on the fly" by the script).

##### Please consider:

`build-worker-branch.sh`:

    #!/usr/bin/env bash
    
    DOCKER_RUMMAGER=../rummager-pack-docker
    # you can find rummager-pack-docker here: https://github.com/lbacik/rummager-pack-docker
    
    DOCKER_BUILDER=../docker-builder/docker_image_builder.py
    # DOCKER_BUILDER is THIS project
    
    BRANCH=$1
    
    python3 $DOCKER_BUILDER \
        --images-name-prefix rummager-build-${BRANCH}- \
        --final-image-name rummager:${BRANCH} \
        --remove-builds \
        $DOCKER_RUMMAGER/images/worker \
        $DOCKER_RUMMAGER/images/branch \
            ARG:GIT_URL=https://github.com/lbacik/rummager.git \
            ARG:BRANCH=${BRANCH} \
            ARG:PROJECT_DIR=/project/rummager \
        rummager-worker-config
    

`rummager-worker-config` is a directory looks like this:
    
    └── rummager-worker-config
        ├── Dockerfile
        └── conf
            └── config_local.py


`rummager-worker-config/Dockerfile`:

    FROM base-rummager-image
    
    COPY ./conf/config_local.py /project/rummager
    RUN mkdir /project/rummager/logs
    

`rummager-worker-config/conf/config_local.py`:
    
    import logging
    
    soapurl = 'http://rumsrv.local/soap.php?wsdl'
    soapurl_sender = 'http://rumsrv.local/soap-sender.php?WSDL&readable'
    
    log_dir = 'logs'

    mainloop_delay = 5
    
