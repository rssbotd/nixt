# This file is placed in the Public Domiain


"processors"


from concurrent.futures import ProcessPoolExecutor, ThreadPoolExecutor


class ProcessExecutor(ProcessPoolExecutor):

     "Process"

class ThreadExecutor(ThreadPoolExecutor):

     "Thread"


def run(func, *args):
    with ThreadExecutor(6) as exe:
        future = exe.submit(func, *args)
        return future.result()