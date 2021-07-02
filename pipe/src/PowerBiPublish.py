import os
from bitbucket_pipes_toolkit import Pipe, get_logger

logger = get_logger()


class PowerBiPublishPipe(Pipe):
    def run(self):
        super().run()

        workspace = self.get_variable('WORKSPACE')
        directoryPbix = self.get_variable('DIRECTORY_PBIX')
        username = self.get_variable('USERNAME')
        password = self.get_variable('PASSWORD')
        clientId = self.get_variable('CLIENT_ID')
        clientSecret = self.get_variable('CLIENT_SECRET')
        gateway = self.get_variable('GATEWAY')
        parameter = self.get_variable('PARAMETER')

        parameters = []
        for n in range(len(parameter)):
            parameters.append(parameter[n])

        logger.debug('Workspace: {}'.format(workspace))
        logger.debug('Directory PBIX: {}'.format(directoryPbix))
        logger.debug('Username: {}'.format(username))
        logger.debug('Password: {}'.format(password))
        logger.debug('ClientID: {}'.format(clientId))
        logger.debug('ClienteSecret: {}'.format(clientSecret))
        logger.debug('Gateway: {}'.format(gateway))
        logger.debug('Parameters: {}'.format(parameters))

        # dirs = os.listdir(directoryPbix)
        # print(dirs)

        # logger.error('Executing the Power BI pipe...')
        # logger.info('Executing the Power BI pipe...')
        #
        # print('Hello Pipes')

        self.success(message="Execution with success!")
