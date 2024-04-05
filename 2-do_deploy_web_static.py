#!/usr/bin/python3
"""Fabric script to distribute an archive to web servers"""

from fabric.api import env, put, run
from os.path import exists
env.hosts = ['54.144.154.101', '52.3.246.209']


def do_deploy(archive_path):
    """Distributes an archive to the web servers"""
    if not exists(archive_path):
        return False

    try:
        archive_name = archive_path.split("/")[-1]
        folder_name = "/data/web_static/releases/{}".format(
            archive_name.split(".")[0])
        put(archive_path, "/tmp/")
        run("sudo mkdir -p {}".format(folder_name))
        run("sudo tar -xzf /tmp/{} -C {}".format(archive_name, folder_name))
        run("sudo rm /tmp/{}".format(archive_name))
        run("sudo mv {}/web_static/* {}".format(folder_name, folder_name))
        run("sudo rm -rf {}/web_static".format(folder_name))
        run("sudo rm -rf /data/web_static/current")
        run("sudo ln -s {} /data/web_static/current".format(folder_name))
        return True
    except Exception as e:
        return False
