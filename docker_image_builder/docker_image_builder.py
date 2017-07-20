# Copyright (C) 2017 Lukasz Bacik <mail@luka.sh>
#
# This program is free software; you can redistribute it and/or
# modify it under the terms of the GNU General Public License
# as published by the Free Software Foundation; either version 2
# of the License, or (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program; if not, write to the Free Software
# Foundation, Inc., 59 Temple Place - Suite 330, Boston, MA  02111-1307, USA.

import docker

from docker_image_builder import docker_helper
from docker_image_builder import args


def build():
    docker_file = 'Dockerfile'
    docker_sock = 'unix://var/run/docker.sock'

    program_args = args.parse()
    contexts = args.parse_positional_args(program_args.params)

    if len(contexts) < 2:
        print('There should be more than one Dockerfile to merge')
        exit(1)

    client = docker.DockerClient(base_url=docker_sock, timeout=10)

    build_prefix = program_args.images_name_prefix
    builds = docker_helper.build(contexts, build_prefix, docker_file, client)

    if program_args.final_image_name:
        print('*** Adding tag %s to the last build' % (program_args.final_image_name,))
        tag = ''
        if ":" in program_args.final_image_name:
            image, tag = program_args.final_image_name.split(':', 2)
        else:
            image = program_args.final_image_name

        client.api.tag(builds[-1], image, tag)

    if program_args.remove_builds:
        if program_args.final_image_name:
            for i in builds:
                print('*** Removing build %s' % (i,))
                client.api.remove_image(i)
        else:
            print('*** use of "remove-builds" option is only possible in conjunction with "final-image-name" one.')
