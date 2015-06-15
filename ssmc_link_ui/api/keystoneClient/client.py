# (c) Copyright 2012-2014 Hewlett Packard Development Company, L.P.
# All Rights Reserved.
#
#    Licensed under the Apache License, Version 2.0 (the "License"); you may
#    not use this file except in compliance with the License. You may obtain
#    a copy of the License at
#
#         http://www.apache.org/licenses/LICENSE-2.0
#
#    Unless required by applicable law or agreed to in writing, software
#    distributed under the License is distributed on an "AS IS" BASIS, WITHOUT
#    WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied. See the
#    License for the specific language governing permissions and limitations
#    under the License.
""" HP3PAR REST Client.

.. module: client
.. moduleauthor: Walter A. Boring IV
.. moduleauthor: Kurt Martin

:Author: Walter A. Boring IV
:Description: This is the 3PAR Client that talks to 3PAR's REST WSAPI Service.
It provides the ability to provision 3PAR volumes, VLUNs, CPGs.  This version
also supports running actions on the 3PAR that use SSH.

This client requires and works with 3PAR InForm 3.1.3 MU1 firmware

"""

try:
    # For Python 3.0 and later
    from urllib.parse import quote
except ImportError:
    # Fall back to Python 2's urllib2
    from urllib2 import quote

import exceptions
import http


class KeystoneClient(object):

    """ The 3PAR REST API Client.

    :param api_url: The url to the WSAPI service on 3PAR
                    ie. http://<3par server>:8080/api/v1
    :type api_url: str

    """


    def __init__(self, api_url):
        self.api_url = api_url
        self.http = http.HTTPJSONRESTClient(self.api_url)
        api_version = None

    def debug_rest(self, flag):
        """This is useful for debugging requests to 3PAR.

        :param flag: set to True to enable debugging
        :type flag: bool

        """
        self.http.set_debug_flag(flag)


    def login(self, username, password, optional=None):
        """This authenticates against the 3PAR wsapi server and creates a
           session.

        :param username: The username
        :type username: str
        :param password: The Password
        :type password: str

        :returns: None

        """
        self.http.authenticateKeystone(username, password, optional)

    def logout(self):
        """This destroys the session and logs out from the 3PAR server.
           The SSH connection to the 3PAR server is also closed.

        :returns: None

        """
        self.http.unauthenticateKeystone()

    def getSessionKey(self):
        return self.http.getSessionKey()

    def getTenantId(self):
        return self.http.getTenantId()

    def getSSMCEndpointForHost(self, host_name):
        return self.http.getSSMCEndpointForHost(host_name)

    def getSSMCEndpointForServiceName(self, service_name):
        return self.http.getSSMCEndpointForServiceName(service_name)

    def getSSMCEndpointForServiceId(self, service_id):
        return self.http.getSSMCEndpointForServiceId(service_id)

    def getSSMCServiceName(self, service_id):
        return self.http.getSSMCServiceName(service_id)

    def getSSMCEndpoints(self):
        return self.http.getSSMCEndpoints()

    def addSSMCEndpoint(self, service_name, endpoint):
        return self.http.addSSMCEndpoint(service_name, endpoint)

    def updateSSMCEndpointUrl(self, service_id, endpoint):
        return self.http.updateSSMCEndpointUrl(service_id, endpoint)

    def deleteSSMCEndpoint(self, service_id):
        return self.http.deleteSSMCEndpoint(service_id)