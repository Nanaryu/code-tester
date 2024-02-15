import subprocess as sp


def get_proc_output(test_command: str, in_data: bytes, timeout: float = 5):
    try:
        proc = sp.Popen(test_command, stdin=sp.PIPE, stdout=sp.PIPE, stderr=sp.PIPE)
        try:
            out_data, err = proc.communicate(in_data, timeout=timeout)
        except sp.TimeoutExpired:
            out_data, err = b"", b"TIMED OUT"
            proc.terminate()
    except PermissionError:
        out_data, err = b"", b"CANNOT RUN PROCESS"

    return out_data, err
