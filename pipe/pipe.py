from bitbucket_pipes_toolkit import Pipe, get_logger
from src.PowerBiPublish import PowerBiPublishPipe

logger = get_logger()

schema = {
  'USERNAME': {'type': 'string', 'required': True},
  'PASSWORD': {'type': 'string', 'required': True},
  'CLIENT_ID': {'type': 'string', 'required': True},
  'CLIENT_SECRET': {'type': 'string', 'required': True},
  'WORKSPACE': {'type': 'string', 'required': True},
  'DIRECTORY_PBIX': {'type': 'string', 'required': True},
  'GATEWAY': {'type': 'string', 'required': False, 'default': ''},
  'PERMISSION': {'type': 'list', 'required': False, 'default': ''},
  'PARAMETER': {'type': 'list', 'required': False, 'default': ''},
  'DEBUG': {'type': 'boolean', 'required': False, 'default': False}
}

if __name__ == '__main__':
    pipe = PowerBiPublishPipe(pipe_metadata='/pipe.yml', schema=schema)
    pipe.run()
