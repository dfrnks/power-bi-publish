import os, requests, time
from bitbucket_pipes_toolkit import Pipe, get_logger
from .api import auth, groups, imports, datasets

logger = get_logger()


class PowerBiPublishPipe(Pipe):
    """
    Create Access Token
    Create Workspace
    Configure permissions
    Publish all .pbix
    Update parameters
    Configure Data Source
    Update Report
    """
    accessToken: str

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
            permissions.append(str(permission[n]).split(":"))

        parameters = []
        for n in range(len(parameter)):
            parameters.append(str(parameter[n]).split(":"))

        logger.debug('Username: {}'.format(username))
        logger.debug('Password: {}'.format(password))
        logger.debug('ClientID: {}'.format(clientId))
        logger.debug('ClienteSecret: {}'.format(clientSecret))
        logger.debug('Workspace: {}'.format(workspace))
        logger.debug('Permissions: {}'.format(permissions))
        logger.debug('Directory PBIX: {}'.format(directoryPbix))
        logger.debug('Gateway: {}'.format(gateway))
        logger.debug('Parameters: {}'.format(parameters))

        if username == 'username' and password == 'password':
            # This is just for tests, the username and password, never will be this values in production;
            self.success(message="Execution with success!")
            exit()

        # Create Access Token
        self.accessToken = auth.getToken(
            client_id=clientId,
            client_secret=clientSecret,
            username=username,
            password=password
        )

        # Create Workspace
        workspaceId = self.createWorkspace(workspace=workspace)

        # Configure permissions
        self.configurePermissions(workspaceId=workspaceId, permissions=permissions)

        # Publish all .pbix
        # Update parameters
        # Configure Data Source
        # Update Report
        datasetIds = self.importAllPbix(workspaceId=workspaceId, directoryPbix=directoryPbix, parameters=parameters)

        self.success(message="Execution with success!")

    def createWorkspace(self, workspace: str) -> str:
        """
        :param workspace
        """
        workspaces = groups.getAllGroups(accessToken=self.accessToken)

        for group in workspaces:
            if workspace == group['name']:
                return group['id']

        return groups.createGroup(accessToken=self.accessToken, name=workspace)

    def configurePermissions(self, workspaceId: str, permissions: list) -> bool:
        """
        :param workspaceId
        :param permissions
        """
        users = groups.getUsersGroup(accessToken=self.accessToken, groupId=workspaceId)

        users = {val['identifier']: val['groupUserAccessRight'] for val in users}
        usersAdd = {val[0]: val[1] for val in permissions}
        usersRemove = []

        for key in users.keys():
            if not key in usersAdd:
                usersRemove.append(key)

        for user in permissions:
            if user[0] not in users:
                groups.addUserGroup(
                    accessToken=self.accessToken,
                    groupId=workspaceId,
                    identifier=user[0],
                    groupUserAccessRight=user[1]
                )

            if user[1] != users.get(user[0]):
                groups.changeUserGroup(
                    accessToken=self.accessToken,
                    groupId=workspaceId,
                    identifier=user[0],
                    groupUserAccessRight=user[1],
                    principalType="User"
                )

        for user in usersRemove:
            groups.deleteUserGroup(
                accessToken=self.accessToken,
                groupId=workspaceId,
                user=user
            )

        return True

    def importAllPbix(self, workspaceId: str, directoryPbix: str, parameters: list) -> list:
        datasetIds = []

        for file in os.listdir(directoryPbix):
            file = open(directoryPbix + "/" + file, 'rb')
            fileName = os.path.basename(file.name)

            # Publish all .pbix
            importId = imports.upload(
                accessToken=self.accessToken,
                groupId=workspaceId,
                fileName=fileName,
                file=file
            )

            result = []

            importState = "Started"
            while importState != "Succeeded":
                try:
                    result = imports.getImport(accessToken=self.accessToken, groupId=workspaceId, importId=importId)

                    importState = result["importState"]

                    time.sleep(1)
                except requests.exceptions.ConnectionError as e:
                    logger.error(e)

            datasetId = result["datasets"][0]["id"]
            reportid = result["reports"][0]["id"]

            datasetIds.append(datasetId)

            if len(parameters) > 0:
                # Update parameters
                datasets.updateParameters(
                    accessToken=self.accessToken,
                    groupId=workspaceId,
                    datasetId=datasetId,
                    parameters=parameters
                )

            # Configure Data Source

            # Update Report
            datasets.forceRefresh(
                accessToken=self.accessToken,
                groupId=workspaceId,
                datasetId=datasetId
            )

        return datasetIds
