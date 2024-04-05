#!/usr/bin/python3
# Fabfile to create and distribute an archive to a web server.
import os.path
from datetime import datetime
from fabric.api import env, local, put, run

# Define the list of host IP addresses
env.hosts = ['54.144.154.101', '52.3.246.209']

def do_pack():
    """Create a tar gzipped archive of the directory web_static."""
    # Get the current UTC date and time
    dt = datetime.utcnow()
    # Define the file name with the format 'web_static_<year><month><day><hour><minute><second>.tgz'
    file = "versions/web_static_{}{}{}{}{}{}.tgz".format(dt.year,
                                                         dt.month,
                                                         dt.day,
                                                         dt.hour,
                                                         dt.minute,
                                                         dt.second)
    # Check if the 'versions' directory exists, if not, create it
    if os.path.isdir("versions") is False:
        if local("mkdir -p versions").failed is True:
            return None
    # Create the tar gzipped archive containing 'web_static' directory and 'my_index.html' file
    if local("tar -cvzf {} web_static my_index.html".format(file)).failed is True:
        return None
    return file

def do_deploy(archive_path):
    """Distributes an archive to a web server.

    Args:
        archive_path (str): The path of the archive to distribute.
    Returns:
        If the file doesn't exist at archive_path or an error occurs - False.
        Otherwise - True.
    """
    # Check if the archive file exists
    if os.path.isfile(archive_path) is False:
        return False
    # Extract the file name and name without extension
    file = archive_path.split("/")[-1]
    name = file.split(".")[0]

    # Upload the archive to the remote server's /tmp directory
    if put(archive_path, "/tmp/{}".format(file)).failed is True:
        return False
    # Remove any existing directory with the same name in /data/web_static/releases/
    if run("rm -rf /data/web_static/releases/{}/".format(name)).failed is True:
        return False
    # Create a new directory in /data/web_static/releases/ with the archive name
    if run("mkdir -p /data/web_static/releases/{}/".format(name)).failed is True:
        return False
    # Extract the archive contents to the new directory
    if run("tar -xzf /tmp/{} -C /data/web_static/releases/{}/".format(file, name)).failed is True:
        return False
    # Remove the archive file from /tmp directory
    if run("rm /tmp/{}".format(file)).failed is True:
        return False
    # Move the contents of the extracted directory to the parent directory
    if run("mv /data/web_static/releases/{}/web_static/* /data/web_static/releases/{}/".format(name, name)).failed is True:
        return False
    # Remove the now empty directory
    if run("rm -rf /data/web_static/releases/{}/web_static".format(name)).failed is True:
        return False
    # Delete the symbolic link to the current version
    if run("rm -rf /data/web_static/current").failed is True:
        return False
    # Create a new symbolic link to the new version
    if run("ln -s /data/web_static/releases/{}/ /data/web_static/current".format(name)).failed is True:
        return False
    return True

def deploy():
    """Create and distribute an archive to a web server."""
    # Create an archive
    file = do_pack()
    # If no archive was created, return False
    if file is None:
        return False
    # Deploy the archive
    return do_deploy(file)
