#wimX에 보내기전 테스트 단계의 testserver
#정보가 제대로 전송 되는지 확인하기 위한 용도-wimX라고 가정하고 테스트
#wimX로 보내기전 확인받을 필요있음(전송이 제대로 되었는지 확인하는 루트)
#tcp소켓통신을 이용해서 wicon(WF-1412)의 정보값을 1초단위로 wimX(현재의 testclient)에게 전송
#모듈화 후

from queue import Queue
from module_package.wiconClientThread import WiconClientThread
from module_package.digital_counter import DigitalCounter
import threading


def main():

    queue = Queue(maxsize=10)
    all_threads = []

    counter_thread = DigitalCounter()
    th = threading.Thread(target=counter_thread.run, args=(queue,))
    th.start()
    all_threads.append(th)


    wicon_client_thread = WiconClientThread()
    th = threading.Thread(target=wicon_client_thread.run_wicon_state, args=(queue,))
    th.start()
    all_threads.append(th)

    for thread in all_threads:
        thread.join()

if __name__=="__main__":
    main()




        