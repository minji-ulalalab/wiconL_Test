from module_package.wiconClientFunction import WiconClientFunction
import time
from enum import Enum

class WICON_CLIENT_STATE(Enum):
    INIT_SOCKET = 0
    SET_SERVER = 1
    CONNECT_SERVER = 2
    TRANSFER_INIT_MSG = 3
    SEND_DATA_TO_WIMX = 4

class WiconClientThread:
    _wimx_msg = None
    _state = None

    def run_wicon_state(self, queue):

        print("run wicon client thread")

        client_function = WiconClientFunction()

        self._state = WICON_CLIENT_STATE.INIT_SOCKET

        while True:
            if(self._state == WICON_CLIENT_STATE.INIT_SOCKET):
                print("WICON_CLIENT_STATE.INIT_SOCKET")
                ret = client_function.wicon_client_function_init_socket()
                if(ret == 0):
                    self._state = WICON_CLIENT_STATE.SET_SERVER

            elif(self._state == WICON_CLIENT_STATE.SET_SERVER):
                print("WICON_CLIENT_STATE.SET_SERVER")
                server_url = "tcp.wim-x.kr"
                server_port = 50300
                ret_url = client_function.wicon_client_function_set_server(server_url, server_port)

                if(ret_url != -1):
                    ret_con = client_function.wicon_client_function_connect_server(ret_url)
                    if(ret_con != -1):
                        self._state = WICON_CLIENT_STATE.SEND_DATA_TO_WIMX


            elif(self._state == WICON_CLIENT_STATE.SEND_DATA_TO_WIMX):
                print("WICON_CLIENT_STATE.SEND_DATA_TO_WIMX")
                try:
                    ret_send = -1
                    self._wimx_msg = queue.get()
                    print("받기완료")
                    print(self._wimx_msg)
                    ret_send = client_function.wicon_client_function_send_data(self._wimx_msg)
                    if(ret_send == 0):
                        ret_recv = client_function.wicon_client_function_recv_ack()
                        print(ret_recv)
                    time.sleep(0.2)
                except Exception as ex:
                    print(ex)
                    print("메세지안옴")


                

            else:
                pass







