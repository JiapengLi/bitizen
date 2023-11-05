import ctypes
import random
import os
import sys
import base64
import json
import concurrent.futures
import time
import enum
import websocket
import threading
import platform

dll_name = 'multi_party_sig'
machine = platform.machine()
if machine == 'AMD64' or machine == 'x86_64':
    dll_name = dll_name + '_amd64'
elif machine == 'aarch64' or machine == 'arm64':
    dll_name = dll_name + '_arm64'
else:
    print("not supported", machine)
    os._exit(1)

prefix = {'win32': ''}.get(sys.platform, 'lib')
extension = {'darwin': '.dylib', 'win32': '.dll'}.get(sys.platform, '.so')
dll_name = prefix + dll_name + extension

libmpc = ctypes.cdll.LoadLibrary("/opt/bitizen/" + dll_name)


if len(sys.argv) != 4 and len(sys.argv) != 3:
    print("usage: ", sys.argv[0], "websocket_server keyshare_file")
    print("example: ", sys.argv[0], "keygen ws://127.0.0.1:8000 a")
    print("example: ", sys.argv[0], "sign ws://127.0.0.1:8000 keyshare_a.txt")
    print("example: ", sys.argv[0], "reshare ws://127.0.0.1:8000 keyshare_a.txt")
    print("example: ", sys.argv[0], "reshare ws://127.0.0.1:8000")
    os._exit(1)


action = sys.argv[1]
ws_server = sys.argv[2]

ws_conn = websocket.create_connection(ws_server)

def read_text(file_name: str) -> str:
    """ Read all """
    file = open(file_name, mode='r')
    data = file.read()
    file.close()
    return data


class Protocol(enum.IntEnum):
    CMP = 1
    FrostTaproot = 2


class MPCException(Exception):

    def __init__(self, error_code):
        # Exception.__init__()
        self.error_code = error_code

    def __str__(self):
        return hex(self.error_code)


def test_rv(rv):
    if rv != 0:
        raise MPCException(rv)


class MultiPartySig:
    @staticmethod
    def PerformRound(ctx_id: int, self_id: str, input: bytes, output: ctypes.c_char_p, out_flag: ctypes.c_int) -> int:
        print("calling PerformRound")
        input_bytes = base64.b64encode(input)

        test_rv(libmpc.PerformRound(ctypes.c_longlong(ctx_id),
                                    self_id.encode('ascii'),
                                    input_bytes,
                                    ctypes.byref(output),
                                    ctypes.byref(out_flag)
                                    ))

        return out_flag.value


    @staticmethod
    def CmpKeygenInit(ctx_id:int, self_id: str, participants, threshold: int):
        print("calling CmpKeygenInit")
        participants = json.dumps(participants)

        test_rv(libmpc.CmpKeygenInit(ctypes.c_longlong(ctx_id),
                                     self_id.encode('ascii'),
                                     participants.encode('ascii'),
                                     threshold
                                     ))


    @staticmethod
    def CmpKeygenResult(ctx_id: int, self_id: str, result_base64: ctypes.c_char_p):
        print("calling CmpKeygenResult")
        test_rv(libmpc.CmpKeygenResult(ctypes.c_longlong(ctx_id),
                                       self_id.encode('ascii'),
                                       ctypes.byref(result_base64)
                                       ))


    @staticmethod
    def CmpSignInit(ctx_id:int, participants, keyshare_base64: str, msg_hash_base64: str):
        print("calling CmpSignInit")
        participants = json.dumps(participants)

        test_rv(libmpc.CmpSignInit(ctypes.c_longlong(ctx_id),
                                   participants.encode('ascii'),
                                   keyshare_base64.encode('ascii'),
                                   msg_hash_base64.encode('ascii')
                                   ))


    @staticmethod
    def CmpSignResult(ctx_id: int, self_id: str, result_base64: ctypes.c_char_p):
        print("calling CmpSignResult")
        test_rv(libmpc.CmpSignResult(ctypes.c_longlong(ctx_id),
                                     self_id.encode('ascii'),
                                     ctypes.byref(result_base64)
                                     ))


    @staticmethod
    def CmpReshareInit(ctx_id:int, self_id: str, detailed_participants, threshold: int, keyshare_base64: str):
        print("calling CmpReshareInit")
        detailed_participants = json.dumps(detailed_participants)

        test_rv(libmpc.CmpReshareInit(ctypes.c_longlong(ctx_id),
                                      self_id.encode('ascii'),
                                      detailed_participants.encode('ascii'),
                                      threshold,
                                      keyshare_base64.encode('ascii')
                                      ))


    @staticmethod
    def CmpReshareResult(ctx_id: int, self_id: str, result_base64: ctypes.c_char_p):
        print("calling CmpReshareResult")
        test_rv(libmpc.CmpReshareResult(ctypes.c_longlong(ctx_id),
                                        self_id.encode('ascii'),
                                        ctypes.byref(result_base64)
                                        ))


    @staticmethod
    def CmpDeriveBip32(keyshareBase64: str, index: int, result_base64: ctypes.c_char_p):
        print("calling CmpDeriveBip32")
        test_rv(libmpc.CmpDeriveBip32(keyshareBase64.encode('ascii'),
                                      index,
                                      ctypes.byref(result_base64)
                                      ))


    @staticmethod
    def FrostTaprootKeygenInit(ctx_id:int, self_id: str, participants, threshold: int):
        print("calling FrostTaprootKeygenInit")
        participants = json.dumps(participants)

        test_rv(libmpc.FrostTaprootKeygenInit(ctypes.c_longlong(ctx_id),
                                              self_id.encode('ascii'),
                                              participants.encode('ascii'),
                                              threshold
                                              ))


    @staticmethod
    def FrostTaprootKeygenResult(ctx_id: int, self_id: str, result_base64: ctypes.c_char_p):
        print("calling FrostTaprootKeygenResult")
        test_rv(libmpc.FrostTaprootKeygenResult(ctypes.c_longlong(ctx_id),
                                                self_id.encode('ascii'),
                                                ctypes.byref(result_base64)
                                                ))


    @staticmethod
    def FrostTaprootSignInit(ctx_id:int, participants, keyshare_base64: str, msg_hash_base64: str):
        print("calling FrostTaprootSignInit")
        participants = json.dumps(participants)

        test_rv(libmpc.FrostTaprootSignInit(ctypes.c_longlong(ctx_id),
                                            participants.encode('ascii'),
                                            keyshare_base64.encode('ascii'),
                                            msg_hash_base64.encode('ascii')
                                            ))

    @staticmethod
    def FrostTaprootSignResult(ctx_id: int, self_id: str, result_base64: ctypes.c_char_p):
        print("calling FrostTaprootSignResult")
        test_rv(libmpc.FrostTaprootSignResult(ctypes.c_longlong(ctx_id),
                                              self_id.encode('ascii'),
                                              ctypes.byref(result_base64)
                                              ))


    @staticmethod
    def FrostTaprootReshareInit(ctx_id:int, self_id: str, detailed_participants, threshold: int, keyshare_base64: str):
        print("calling FrostTaprootReshareInit")
        detailed_participants = json.dumps(detailed_participants)

        test_rv(libmpc.FrostTaprootReshareInit(ctypes.c_longlong(ctx_id),
                                               self_id.encode('ascii'),
                                               detailed_participants.encode('ascii'),
                                               threshold,
                                               keyshare_base64.encode('ascii')
                                               ))


    @staticmethod
    def FrostTaprootReshareResult(ctx_id: int, self_id: str, result_base64: ctypes.c_char_p):
        print("calling FrostTaprootReshareResult")
        test_rv(libmpc.FrostTaprootReshareResult(ctypes.c_longlong(ctx_id),
                                                 self_id.encode('ascii'),
                                                 ctypes.byref(result_base64)
                                                 ))


    @staticmethod
    def FrostTaprootDeriveBip32(keyshare_base64: str, index: int, result_base64: ctypes.c_char_p):
        print("calling FrostTaprootDerive")
        test_rv(libmpc.FrostTaprootDeriveBip32(keyshare_base64.encode('ascii'),
                                               index,
                                               ctypes.byref(result_base64)
                                               ))



def handle_output(output: str, ctx_id: int, step: int, bulletin_board):
    msgs = json.loads(output)

    has_broadcast = False
    has_p2p = False
    for msg in msgs:
        from_party = msg["From"]
        to_party = msg["To"]
        is_broadcast = msg["Broadcast"]
        round_number = msg["RoundNumber"]
        if is_broadcast:
            has_broadcast = True
        else:
            has_p2p = True
        key = '{ctx_id}-{round_number}-{is_broadcast}-{from_party}-{to_party}'.format(
            ctx_id=ctx_id, round_number=round_number, is_broadcast=is_broadcast, from_party=from_party, to_party=to_party)
        # print("set key", key)
        bulletin_board[key] = msg
        # Send message via websocket
        data = {"key": key,
                "value": msg,
                }
        ws_conn.send(json.dumps(data))
    return has_broadcast, has_p2p


def get_next_input(ctx_id: int, self_id: str, participants, step: int, has_broadcast: bool, has_p2p: bool, bulletin_board) -> bytes:
    outputs = []
    if has_broadcast:
        for participant in participants:
            if participant == self_id:
                continue  # skip self
            key = '{ctx_id}-{round_number}-{is_broadcast}-{from_party}-{to_party}'.format(
                ctx_id=ctx_id, round_number=step, is_broadcast=True, from_party=participant, to_party="")
            data = poll_data(key, bulletin_board)
            outputs.append(data)
    if has_p2p:
        for participant in participants:
            if participant == self_id:
                continue  # skip self
            key = '{ctx_id}-{round_number}-{is_broadcast}-{from_party}-{to_party}'.format(
                ctx_id=ctx_id, round_number=step, is_broadcast=False, from_party=participant, to_party=self_id)
            data = poll_data(key, bulletin_board)
            outputs.append(data)
    json_str = json.dumps(outputs)
    json_bytes = json_str.encode('ascii')
    return json_bytes


def poll_data(key: str, bulletin_board):
    max_retry = 300
    for i in range(max_retry):
        if key in bulletin_board:
            return bulletin_board[key]
        else:
            # print("waiting for ", key)
            time.sleep(0.2)
    raise ValueError("No data found for key " + key)


def keygen(prot: Protocol, ctx_id: int, self_id: str, participants, threshold: int, bulletin_board) -> str:
    # Init
    if prot == Protocol.CMP:
        MultiPartySig.CmpKeygenInit(ctx_id, self_id, participants, threshold)
    elif prot == Protocol.FrostTaproot:
        MultiPartySig.FrostTaprootKeygenInit(ctx_id, self_id, participants, threshold)
    else:
        raise ValueError("Unknown protocol")

    out_flag = ctypes.c_int()
    step = 1
    input_bytes = b'[]' # An empty json array
    output_base64 = ctypes.c_char_p()
    while True:
        # print('self_id = {}, step = {}'.format(self_id, step))

        # Run Step
        start_time = time.time()
        MultiPartySig.PerformRound(ctx_id, self_id, input_bytes, output_base64, out_flag)
        print("--- step %i TIME %s seconds ---" % (step, time.time() - start_time))

        output = base64.b64decode(output_base64.value)
        output_str = output.decode('ascii')

        if out_flag.value == 1:  # Finished
            break

        has_broadcast, has_p2p = handle_output(output_str, ctx_id, step, bulletin_board)

        step = step + 1
        next_input = get_next_input(ctx_id, self_id, participants, step, has_broadcast, has_p2p, bulletin_board)
        input_bytes = next_input

    # Get Result
    result_base64 = ctypes.c_char_p()
    if prot == Protocol.CMP:
        MultiPartySig.CmpKeygenResult(ctx_id, self_id, result_base64)
    elif prot == Protocol.FrostTaproot:
        MultiPartySig.FrostTaprootKeygenResult(ctx_id, self_id, result_base64)
    else:
        raise ValueError("Unknown protocol")
    return result_base64.value.decode('ascii')


def sign(prot: Protocol, ctx_id: int, self_id: str, participants, keyshare_base64: str, msg_hash_base64: str, bulletin_board) -> str:
    # Init
    if prot == Protocol.CMP:
        MultiPartySig.CmpSignInit(ctx_id, participants, keyshare_base64, msg_hash_base64)
    elif prot == Protocol.FrostTaproot:
        MultiPartySig.FrostTaprootSignInit(ctx_id, participants, keyshare_base64, msg_hash_base64)
    else:
        raise ValueError("Unknown protocol")

    out_flag = ctypes.c_int()
    step = 1
    input_bytes = b'[]' # An empty json array
    output_base64 = ctypes.c_char_p()
    while True:
        # print('self_id = {}, step = {}'.format(self_id, step))

        # Run Step
        start_time = time.time()
        MultiPartySig.PerformRound(ctx_id, self_id, input_bytes, output_base64, out_flag)
        print("--- step %i TIME %s seconds ---" % (step, time.time() - start_time))

        output = base64.b64decode(output_base64.value)
        output_str = output.decode('ascii')

        if out_flag.value == 1:  # Finished
            break

        has_broadcast, has_p2p = handle_output(output_str, ctx_id, step, bulletin_board)

        step = step + 1
        next_input = get_next_input(ctx_id, self_id, participants, step, has_broadcast, has_p2p, bulletin_board)
        input_bytes = next_input

    # Get Result
    result_base64 = ctypes.c_char_p()
    if prot == Protocol.CMP:
        MultiPartySig.CmpSignResult(ctx_id, self_id, result_base64)
    elif prot == Protocol.FrostTaproot:
        MultiPartySig.FrostTaprootSignResult(ctx_id, self_id, result_base64)
    else:
        raise ValueError("Unknown protocol")
    return result_base64.value.decode('ascii')


def reshare(prot: Protocol, ctx_id: int, self_id: str, detailed_participants, threshold: int, keyshare_base64: str, bulletin_board) -> str:
    # Init
    if prot == Protocol.CMP:
        MultiPartySig.CmpReshareInit(ctx_id, self_id, detailed_participants, threshold, keyshare_base64)
    elif prot == Protocol.FrostTaproot:
        MultiPartySig.FrostTaprootReshareInit(ctx_id, self_id, detailed_participants, threshold, keyshare_base64)
    else:
        raise ValueError("Unknown protocol")

    participants = [p["PartyID"] for p in detailed_participants]

    out_flag = ctypes.c_int()
    step = 1
    input_bytes = b'[]' # An empty json array
    output_base64 = ctypes.c_char_p()
    while True:
        # print('self_id = {}, step = {}'.format(self_id, step))

        # Run Step
        start_time = time.time()
        MultiPartySig.PerformRound(ctx_id, self_id, input_bytes, output_base64, out_flag)
        print("--- step %i TIME %s seconds ---" % (step, time.time() - start_time))

        output = base64.b64decode(output_base64.value)
        output_str = output.decode('ascii')

        if out_flag.value == 1:  # Finished
            break

        has_broadcast, has_p2p = handle_output(output_str, ctx_id, step, bulletin_board)

        step = step + 1
        next_input = get_next_input(ctx_id, self_id, participants, step, has_broadcast, has_p2p, bulletin_board)
        input_bytes = next_input

    # Get Result
    result_base64 = ctypes.c_char_p()
    if prot == Protocol.CMP:
        MultiPartySig.CmpReshareResult(ctx_id, self_id, result_base64)
    elif prot == Protocol.FrostTaproot:
        MultiPartySig.FrostTaprootReshareResult(ctx_id, self_id, result_base64)
    else:
        raise ValueError("Unknown protocol")
    return result_base64.value.decode('ascii')


def init_websocket_client(bulletin_board):
    while True:
        res = ws_conn.recv()
        # print('websocket msg = {}'.format(res))
        ws_msg = json.loads(res)
        bulletin_board[ws_msg['key']] = ws_msg['value']


def test_keygen(prot: Protocol, participant_id: str, participants, threshold: int, bulletin_board) -> str:
    ctx_id = 101234567890

    print("KEYGEN START")
    start_time = time.time()
    result = keygen(prot, ctx_id, participant_id, participants, threshold, bulletin_board)
    print("KEYGEN END", result)
    print("--- KEYGEN TIME %s seconds ---" % (time.time() - start_time))
    return result


def test_sign(prot: Protocol, participant_id: str, keyshare_for_sign: str, bulletin_board):
    msg_hash_base64 = "aGVsbG8gd29ybGQ="
    ctx_id = 201234567890

    print("SIGN START")
    start_time = time.time()
    result = sign(prot, ctx_id, participant_id, ["a", "b"], keyshare_for_sign, msg_hash_base64, bulletin_board)
    print("SIGN END", result)
    print("--- SIGN TIME %s seconds ---" % (time.time() - start_time))


def test_reshare(prot: Protocol, participant_id: str, threshold: int, old_keyshare: str, bulletin_board) -> str:
    ctx_id = 301234567890
    detailed_participants = [{"PartyID":"a", "OldPartyID":"a"}, {"PartyID":"b", "OldPartyID":"b"}, {"PartyID":"c","OldPartyID":""}]

    print("RESHARE START")
    start_time = time.time()
    result = reshare(prot, ctx_id, participant_id, detailed_participants, threshold, old_keyshare, bulletin_board)
    print("RESHARE END", result)
    print("--- RESHARE TIME %s seconds ---" % (time.time() - start_time))
    return result


if __name__ == "__main__":
    bulletin_board = {}

    t1 = threading.Thread(target=init_websocket_client, args=(bulletin_board,))
    t1.start()

    time.sleep(20)

    if action.startswith("cmp_"):
        prot = Protocol.CMP
    elif action.startswith("frost_"):
        prot = Protocol.FrostTaproot
    else:
        print("invalid action", action)
        os._exit(1)

    if action == "cmp_keygen" or action == "frost_keygen":
        participant_id = sys.argv[3]
        participants = ["a", "b"]
        threshold = 1
        keyshare = test_keygen(prot, participant_id, participants, threshold, bulletin_board)
    elif action == "cmp_sign" or action == "frost_sign":
        key_share_file = sys.argv[3]
        keyshare_for_sign = read_text(key_share_file)
        if "_a.txt" in key_share_file:
            participant_id = "a"
        elif "_b.txt" in key_share_file:
            participant_id = "b"
        else:
            print("invalid keyshare file name")
            os._exit(1)
        print("participant_id", participant_id)
        test_sign(prot, participant_id, keyshare_for_sign, bulletin_board)
    elif action == "cmp_reshare" or action == "frost_reshare":
        if len(sys.argv) == 4:
            key_share_file = sys.argv[3]
            old_keyshare = read_text(key_share_file)
            if "_a.txt" in key_share_file:
                participant_id = "a"
            elif "_b.txt" in key_share_file:
                participant_id = "b"
            else:
                print("invalid keyshare file name")
                os._exit(1)
        else:
            old_keyshare = ''
            participant_id = 'c'
        threshold = 1
        keyshare = test_reshare(prot, participant_id, threshold, old_keyshare, bulletin_board)
    else:
        print("invalid action", action)
    os._exit(0)

