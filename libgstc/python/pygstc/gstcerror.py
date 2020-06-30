# GStreamer Daemon - gst-launch on steroids
# Python client library abstracting gstd interprocess communication

# Copyright (c) 2015-2020 RidgeRun, LLC (http://www.ridgerun.com)

# Redistribution and use in source and binary forms, with or without
# modification, are permitted provided that the following conditions
# are met:

# 1. Redistributions of source code must retain the above copyright
# notice, this list of conditions and the following disclaimer.

# 2. Redistributions in binary form must reproduce the above
# copyright notice, this list of conditions and the following
# disclaimer in the documentation and/or other materials provided
# with the distribution.

# THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS
# "AS IS" AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT
# LIMITED TO, THE IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS
# FOR A PARTICULAR PURPOSE ARE DISCLAIMED. IN NO EVENT SHALL THE
# COPYRIGHT HOLDER OR CONTRIBUTORS BE LIABLE FOR ANY DIRECT,
# INDIRECT, INCIDENTAL, SPECIAL, EXEMPLARY, OR CONSEQUENTIAL DAMAGES
# (INCLUDING, BUT NOT LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR
# SERVICES; LOSS OF USE, DATA, OR PROFITS; OR BUSINESS INTERRUPTION)
# HOWEVER CAUSED AND ON ANY THEORY OF LIABILITY, WHETHER IN CONTRACT,
# STRICT LIABILITY, OR TORT (INCLUDING NEGLIGENCE OR OTHERWISE)
# ARISING IN ANY WAY OUT OF THE USE OF THIS SOFTWARE, EVEN IF ADVISED
# OF THE POSSIBILITY OF SUCH DAMAGE.

from enum import Enum

"""
GstClient - GstClientError Class
Main GstClientError Class for the GstClient
It groups together all the GstClient Errors
"""


class GstClientError(Exception):

    def __init__(self, description, code):
        """
        Raised when GstClient fails

        Parameters
        ----------
        Attributes:
            description -- GstClient error description message
        """
        self.description = description
        self.code = code


"""
GstClient - GstdError Class
Raised when Gstd IPC fails
"""


class GstdError(GstClientError):

    def __init__(self, description, code):
        """
        Initialize new GstdError

        Parameters
        ----------
        Attributes:
            description : GstdError description message
            code : Error code
        """
        super().__init__(description, code)


"""
GstClient - GstcError Class
Raised when the GstClient fails internally
"""


class GstcError(GstClientError):

    def __init__(self, description, code):
        """
        Initialize new GstcError

        Parameters
        ----------
        Attributes:
            description : GstcError description message
            code : Error code
        """
        super().__init__(description, code)


"""
GstClient - GstcErrorCode Class
Representation for error codes
"""


class GstcErrorCode(Enum):
    GSTC_OK = 0
    GSTC_NULL_ARGUMENT = -1
    GSTC_UNREACHABLE = -2
    GSTC_TIMEOUT = -3
    GSTC_OOM = -4
    GSTC_TYPE_ERROR = -5
    GSTC_MALFORMED = -6
    GSTC_NOT_FOUND = -7
    GSTC_SEND_ERROR = -8
    GSTC_RECV_ERROR = -9
    GSTC_SOCKET_ERROR = -10
    GSTC_THREAD_ERROR = -11
    GSTC_BUS_TIMEOUT = -12
    GSTC_SOCKET_TIMEOUT = -13
