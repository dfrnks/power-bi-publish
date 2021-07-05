import os
from bitbucket_pipes_toolkit import Pipe, get_logger

logger = get_logger()


class PowerBiPublishPipe(Pipe):
    """
    Create token
    Create Workspace
    Configure permissions
    Publish all .pbix
    Update parameters
    Configure Gateway
    Configure Data Source
    Update Report
    """
    def run(self):
        super().run()

        username = self.get_variable('USERNAME')
        password = self.get_variable('PASSWORD')
        clientId = self.get_variable('CLIENT_ID')
        clientSecret = self.get_variable('CLIENT_SECRET')
        workspace = self.get_variable('WORKSPACE')
        permission = self.get_variable('PERMISSION')
        directoryPbix = self.get_variable('DIRECTORY_PBIX')
        gateway = self.get_variable('GATEWAY')
        parameter = self.get_variable('PARAMETER')

        permissions = []
        for n in range(len(permission)):
            permissions.append(permission[n])

        parameters = []
        for n in range(len(parameter)):
            parameters.append(parameter[n])

        logger.debug('Username: {}'.format(username))
        logger.debug('Password: {}'.format(password))
        logger.debug('ClientID: {}'.format(clientId))
        logger.debug('ClienteSecret: {}'.format(clientSecret))
        logger.debug('Workspace: {}'.format(workspace))
        logger.debug('Permissions: {}'.format(permissions))
        logger.debug('Directory PBIX: {}'.format(directoryPbix))
        logger.debug('Gateway: {}'.format(gateway))
        logger.debug('Parameters: {}'.format(parameters))

        # dirs = os.listdir(directoryPbix)
        # print(dirs)

        # logger.error('Executing the Power BI pipe...')
        # logger.info('Executing the Power BI pipe...')
        #
        # print('Hello Pipes')

        self.success(message="Execution with success!")
