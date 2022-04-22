#소켓 설정, 보내는 기능, 받는 기능 이에따른 확인
import socket
import time


class WiconClientFunction:

    _wicon_socket = 0

    def wicon_client_function_init_socket(self):
        try:
            ret = -1
            self._wicon_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)#AF_INEF -> IP4v, SOCK_STREAM -> TCP
            self._wicon_socket.settimeout(0.5)
            ret = 0

        except Exception as ex:
            print(ex)
            ret = -1
            pass

        finally:
            return ret    

    def wicon_client_function_set_server(self, server_url, server_port):
        try:
            ret = -1
            url_ip = socket.gethostbyname(server_url)
            url = (url_ip, server_port)
            ret = url
        except Exception as ex:
            print("서버세팅오류")
            print(ex)
            ret = -1

        finally:
            return ret
        
    def wicon_client_function_connect_server(self, url):
        try:
            ret = -1
            self._wicon_socket.connect(url)
            ret = 0
            print("connect OK")

        except Exception as ex:
            print(ex)
            print("no connect")
            ret = -1

        finally:
            return ret

    def wicon_client_function_recv_ack(self):
            try:
                ret = -1
                ack = self._wicon_socket.recv(1024)
                print("%s" %(ack))
                ret = 0
            except:
                print("no ack")
                ret = -1
                
            finally:
                return ret

    def wicon_client_function_send_data(self, msg):#1회이후 끊어짐
            try:
                ret = -1
                self._wicon_socket.send(msg.encode('utf-8'))
                print("%s" %(msg))
                ret = 0
               
            except Exception as ex:
                print("못보냄")
                print(ex)
                ret = -1

            finally:
                return ret