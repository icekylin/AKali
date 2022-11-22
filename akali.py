from lib.core import sources
from lib.utils.dic_sort import dict_value_sort
from lib.view.terminal import Output

output = Output()

def run_sources():
    # Banner INFO
    banner_start = "Start optimizing the apt source"
    banner_delay = "Detect delay from different sources..."
    banner_modify = "Modify the local source file..."
    banner_end = "Optimizing the apt source success"

    # Sources Module Start
    output.info(banner_start)

    # Detect delay
    output.info(banner_delay)
    l_resp_time = dict_value_sort(sources.run_resp_time())
    for key, value in l_resp_time.items():
        print(f'{value}s - {key}')
    
    # Modify sources.list
    output.info(banner_modify)
    try:
        sources.modify_sources(l_resp_time)
    except FileNotFoundError:
        output.error("\"sources.list\" File Not Found")
    output.info(banner_end)
        
if __name__ == '__main__':
    run_sources()
    print('[EXIT] The program has exited...')