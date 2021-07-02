import os
import subprocess

docker_image = 'bitbucketpipelines/demo-pipe-python:ci' + os.getenv('BITBUCKET_BUILD_NUMBER', 'local')


def docker_build():
    """
  Build the docker image for tests.
  :return:
  """
    args = [
        'docker',
        'build',
        '-t',
        docker_image,
        '.',
    ]
    subprocess.run(args, check=True)


def setup():
    docker_build()


def test_no_parameters():
    args = [
        'docker',
        'run',
        docker_image,
    ]

    result = subprocess.run(args, check=False, text=True, capture_output=True)
    assert result.returncode == 1
    assert """\x1b[31m✖ Validation errors: \nCLIENT_ID:\n- required field\nCLIENT_SECRET:\n- required field\nDIRECTORY_PBIX:\n- required field\nPASSWORD:\n- required field\nUSERNAME:\n- required field\nWORKSPACE:\n- required field\n\x1b[0m\n""" in result.stdout


def test_success():
    args = [
        'docker',
        'run',
        '-e', 'NAME=hello world',
        docker_image,
    ]

    result = subprocess.run(args, check=False, text=True, capture_output=True)
    assert 'hello world' in result.stdout
    assert result.returncode == 0
