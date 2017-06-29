# Copyright 2017 NXP
# All rights reserved.
#
# Redistribution and use in source and binary forms, with or without modification,
# are permitted provided that the following conditions are met:
#
# o Redistributions of source code must retain the above copyright notice, this list
#   of conditions and the following disclaimer.
#
# o Redistributions in binary form must reproduce the above copyright notice, this
#   list of conditions and the following disclaimer in the documentation and/or
#   other materials provided with the distribution.
#
# o Neither the name of the copyright holder nor the names of its
#   contributors may be used to endorse or promote products derived from this
#   software without specific prior written permission.
#
# THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS "AS IS" AND
# ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE IMPLIED
# WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE ARE
# DISCLAIMED. IN NO EVENT SHALL THE COPYRIGHT HOLDER OR CONTRIBUTORS BE LIABLE FOR
# ANY DIRECT, INDIRECT, INCIDENTAL, SPECIAL, EXEMPLARY, OR CONSEQUENTIAL DAMAGES
# (INCLUDING, BUT NOT LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR SERVICES;
# LOSS OF USE, DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER CAUSED AND ON
# ANY THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT LIABILITY, OR TORT
# (INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT OF THE USE OF THIS
# SOFTWARE, EVEN IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGE.

#
# Generated by erpcgen 1.4.3 on Mon Jun 19 08:52:04 2017.
#
# AUTOGENERATED - DO NOT EDIT
#

import erpc
from . import common, interface

# Client for MatrixMultiplyService
class MatrixMultiplyServiceService(erpc.server.Service):
    def __init__(self, handler):
        super(MatrixMultiplyServiceService, self).__init__(interface.IMatrixMultiplyService.SERVICE_ID)
        self._handler = handler
        self._methods = {
                interface.IMatrixMultiplyService.ERPCMATRIXMULTIPLY_ID: self._handle_erpcMatrixMultiply,
            }

    def _handle_erpcMatrixMultiply(self, sequence, codec):
        # Create reference objects to pass into handler for out/inout parameters.
        result_matrix = erpc.Reference()

        # Read incoming parameters.
        matrix1 = []
        for _i0 in range(5):
            _v0 = []
            for _i1 in range(5):
                _v1 = codec.read_int32()
                _v0.append(_v1)

            matrix1.append(_v0)

        matrix2 = []
        for _i0 in range(5):
            _v0 = []
            for _i1 in range(5):
                _v1 = codec.read_int32()
                _v0.append(_v1)

            matrix2.append(_v0)

        codec.end_read_message()

        # Invoke user implementation of remote function.
        self._handler.erpcMatrixMultiply(matrix1, matrix2, result_matrix)

        # Prepare codec for reply message.
        codec.reset()

        # Construct reply message.
        codec.start_write_message(erpc.codec.MessageInfo(
            type=erpc.codec.MessageType.kReplyMessage,
            service=interface.IMatrixMultiplyService.SERVICE_ID,
            request=interface.IMatrixMultiplyService.ERPCMATRIXMULTIPLY_ID,
            sequence=sequence))
        if result_matrix.value is None:
            raise ValueError("result_matrix is None")
        for _i0 in result_matrix.value:
            for _i1 in _i0:
                codec.write_int32(_i1)


        codec.end_write_message()


